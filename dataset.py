import cv2
import torch
import os
import glob
from torch.utils.data import Dataset
import torchvision.transforms as transforms
import random
import numpy as np



class ISBI_Loader(Dataset):

    def __init__(self, data_path):
        # 初始化函数，读取所有data_path下的图片
        self.data_path = data_path
        self.imgs_path = glob.glob(os.path.join(data_path, '*.tif'))
        # transform = transforms.Compose([transforms.ToTensor(),
        #                                 transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])

    def __getitem__(self, index):
        # 根据index读取图片
        image_path = self.imgs_path[index]
        # 读取训练图片和标签图片
        image = cv2.imread(image_path)
        print(type(image))
        print(np.shape(image))

        # 将数据转为单通道的图片
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # 多加一个列1，因为输入数据的格式是：通道数*长*宽
        image = image.reshape(1, image.shape[0], image.shape[1])

        print(type(image))
        return image

    def __len__(self):
        # 返回训练集大小
        return len(self.imgs_path)


if __name__ == "__main__":
    isbi_dataset = ISBI_Loader("E:/satellite/")
    print("数据个数：", len(isbi_dataset))
    train_loader = torch.utils.data.DataLoader(dataset=isbi_dataset,
                                               batch_size=1,
                                               shuffle=False)
    print("----test----")
    for image in train_loader:
        print("----------")
        print(image.shape)
        print(type(image))


