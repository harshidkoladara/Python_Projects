import torch
from torchvision.models import ResNet
from torchvision.models.resnet import BasicBlock
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from PIL import Image
import numpy as np

class EXCV10TestImageFolder(datasets.ImageFolder):
    def _getitem_(self, index):
        img_path = self.imgs[index][0]
        img = Image.open(img_path).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img

def test_cnn(model, test_loader):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    model.eval()
    predicted_labels = []
    correct = 0
    total = 0

    with torch.no_grad():
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
            predicted_labels.extend(predicted.cpu().numpy())

    accuracy = 100 * correct / total
    return np.array(predicted_labels), accuracy

if __name__ == '__main__':
    image_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    test_data = EXCV10TestImageFolder(r'C:/Users/Admin/Documents/ECMM_pract/data/EXCV10/val', transform=image_transform)
    test_loader = DataLoader(test_data, batch_size=64, shuffle=False, num_workers=4, pin_memory=True)

    model = ResNet(block=BasicBlock, layers=[2, 2, 2, 2]) 

    num_classes = 10  
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    predicted_labels, accuracy = test_cnn(model, test_loader)

    print("Predicted labels:", predicted_labels)
    print("Classification accuracy:", accuracy)
