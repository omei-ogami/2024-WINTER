import requests
import pandas as pd
import os
import torch
import numpy as np
import tqdm
from PIL import Image
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
from torchvision import io

data = pd.read_csv('data/CNN.csv')

# Download images
def download_image_from_url(row):
    id = row['BookId']
    url = row['Image']
    save_path = f"images/{id}.jpg"
    if os.path.exists(save_path):
        return
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Download Succesfully ID: {id}")
        check_image(save_path)
    except Exception as e:
        print(f"Download Failed ID: {id}")

# check images
def check_image(save_path):
    try:
        img = Image.open(save_path)
        img.verify()  
        print("Success")
    except Exception as e:
        print(f"Failed: {e}")

data.apply(download_image_from_url, axis=1)

'''
for file_name in os.listdir("images/"):
    # Check if file is a numpy file and delete it
    if file_name.endswith('.npy'):
        file_path = os.path.join("images/", file_name)
        os.remove(file_path)  
        print(f"Deleted: {file_path}")
'''

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Save images as numpy arrays
def save_image_as_numpy(row):
    id = row['BookId']
    save_path = f"images/{id}.jpg"
    img = Image.open(save_path).convert("RGB")  # 强制转换为 RGB 格式
    img = transform(img)  # 应用 transform
    np.save(f"processed_images/{id}.npy", img.numpy())  # 保存为 .npy 文件

# 假设 data 是包含书籍信息的 DataFrame
for i, row in tqdm.tqdm(data.iterrows(), total=len(data)):
    save_image_as_numpy(row)

# save batches of images
'''
dataset = datasets.ImageFolder(root='processed_images/')
loader = DataLoader(dataset, batch_size=32, shuffle=True)
for i, (images, labels) in enumerate(loader):
    batch_path = f"processed_images/batch_{i}.pt"
    torch.save((images, labels), batch_path)
    print(f"Saved batch {i} to {batch_path}")
'''
