import numpy as np
import torch
from torchvision.models import ResNet
from torchvision.models.resnet import BasicBlock
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from PIL import Image
from prac5 import test_cnn

class EXCV10TestImageFolder(datasets.ImageFolder):
    def _getitem_(self, index):
        img_path = self.imgs[index][0]
        img = Image.open(img_path).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img

def compute_confusion_matrix(true, predictions):
    unique_labels = np.unique(np.concatenate((true, predictions)))
    num_labels = len(unique_labels)
    confusion_matrix = np.zeros((num_labels, num_labels), dtype=int)

    label_to_index = {label: i for i, label in enumerate(unique_labels)}

    for true_label, pred_label in zip(true, predictions):
        true_index = label_to_index[true_label]
        pred_index = label_to_index[pred_label]
        confusion_matrix[true_index][pred_index] += 1

    return confusion_matrix

if __name__ == '__main__':
    image_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    test_data = EXCV10TestImageFolder(r'C:/Users/Admin/Documents/ECMM_pract/data/EXCV10/val', transform=image_transform)
    test_loader = DataLoader(test_data, batch_size=64, shuffle=False, num_workers=0, pin_memory=True)

    model = ResNet(block=BasicBlock, layers=[2, 2, 2, 2])
    num_classes = 10
    model.fc = torch.nn.Linear(model.fc.in_features, num_classes)

    predicted_labels, _ = test_cnn(model, test_loader)

    print("Predicted labels:", predicted_labels)

    true_labels = test_data.targets
    confusion_matrix = compute_confusion_matrix(true_labels, predicted_labels)
    print("Confusion Matrix:")
    print(confusion_matrix)
