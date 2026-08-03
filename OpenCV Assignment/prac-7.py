import os
import glob
import numpy as np
from PIL import Image
import cv2
from torch.utils.data import Dataset

class MaskedFaceTestDataset(Dataset):
    def __init__(self, root, transform=None):
        super(MaskedFaceTestDataset, self).__init__()
        self.imgs = sorted(glob.glob(os.path.join(root, '*.png')))
        self.transform = transform

    def __getitem__(self, index):
        img_path = self.imgs[index]
        img = Image.open(img_path).convert("RGB")
        if self.transform is not None:
            img = self.transform(img)
        return img

    def __len__(self):
        return len(self.imgs)

def detect_faces(img):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    img_cv = np.array(img)
    
    gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    classes = []
    for (x, y, w, h) in faces:
        if w > 100:
            classes.append('with_mask')
        else:
            classes.append('without_mask')

    return faces, classes

def count_masks(dataset):
    num_with_mask = 0
    num_without_mask = 0
    num_mask_incorrect = 0
    total_images = len(dataset)
    mape_scores = []

    for i in range(total_images):
        img = dataset[i]
        faces, classes = detect_faces(img)
        
        num_with_mask += classes.count('with_mask')
        num_without_mask += classes.count('without_mask')
        num_mask_incorrect += classes.count('mask_worn_incorrect')

        true_counts = np.array([
            classes.count('with_mask'),
            classes.count('without_mask'),
            classes.count('mask_worn_incorrect')
        ])
        predicted_counts = np.array([num_with_mask, num_without_mask, num_mask_incorrect])
        mape = np.mean(np.abs((true_counts - predicted_counts) / np.maximum(true_counts, 1))) * 100
        mape_scores.append(mape)

    total_mape = np.mean(mape_scores)

    return np.array([[num_with_mask, num_without_mask, num_mask_incorrect]]), total_mape

dataset_path = r'C:\Users\Admin\Documents\ECMM_pract\data\MaskedFace\train'
dataset = MaskedFaceTestDataset(dataset_path)
counts, mape = count_masks(dataset)
print("Counts:", counts)
print("MAPE:", mape)
