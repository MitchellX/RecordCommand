import torch
import cv2
import numpy as np

path = "E:/satellite/satellite1.tif"
image = cv2.imread(path)
image = np.transpose(image, (2, 0, 1))
data = torch.from_numpy(image).cuda()   # H*W*C

corpus_size = 1
train_data = data.unsqueeze(0).repeat(corpus_size, 1, 1, 1)
print(type(train_data))
print(train_data)
print("print size of train_data: ")
print(train_data.size())

train_target = torch.zeros(corpus_size, 1)
print(train_target)
print(train_target.size())
dataset = torch.utils.data.TensorDataset(train_data, train_target)
train_dataloader = torch.utils.data.DataLoader(dataset, batch_size=16)