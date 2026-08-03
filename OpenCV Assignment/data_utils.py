# data_utils.py

from torchvision import datasets
from PIL import Image

class EXCV10TestImageFolder(datasets.ImageFolder):
    def __init__(self, *args, **kwargs):
        super(EXCV10TestImageFolder, self).__init__(*args, **kwargs)

    def __getitem__(self, index):
        img_path = self.imgs[index][0]
        img = Image.open(img_path).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img
