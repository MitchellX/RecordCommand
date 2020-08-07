from torchgpipe import GPipe
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import os
from torchgpipe import GPipe
from typing import cast

os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"   # OMP error ->put these two lines
PATH = './cifar_net.pth'    # save model in this path

class View(nn.Module):
    def __init__(self):
        super(View, self).__init__()

    def forward(self, x):
        return x.view(x.size()[0], -1)



transform = transforms.Compose([transforms.ToTensor(),
                               transforms.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5))])

trainset = torchvision.datasets.CIFAR10(root='./data', train=True, download=False, transform=transform)
# print(trainset)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=0)
# If running on Windows and you get a BrokenPipeError, try setting
# the num_worker of torch.utils.data.DataLoader() to 0.

testset = torchvision.datasets.CIFAR10(root='./data', train=False, download=False, transform=transform)
# print(trainset)
testloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=0)

classes = ('plane', 'car', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck')


# 输出图像的函数


def imshow(img):
    img = img / 2 + 0.5     # unnormalize
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    '''
    np.transpose(npimg,(1,2,0))，将npimg的数据格式由（channels,imagesize,imagesize）->（imagesize,imagesize,channels）,
    进行格式的转换后方可进行显示。 (1, 2, 0)分别代表位置
    '''
    plt.show()


# 随机获取训练图片
dataiter = iter(trainloader)
images, labels = dataiter.next()

# 显示图片
# imshow(torchvision.utils.make_grid(images))
# 打印图片标签
print(' '.join('%5s' % classes[labels[j]] for j in range(4)))

print("let's begin to define the model!")


# Define a Convolutional Neural Network
model = nn.Sequential(
         nn.Conv2d(3, 6, 5),
         nn.ReLU(inplace=True),
         nn.MaxPool2d(2, 2),
         nn.Conv2d(6, 16, 5),
         nn.ReLU(inplace=True),
         nn.MaxPool2d(2, 2),
         View(),
         nn.Linear(16*5*5, 120),
         nn.ReLU(inplace=True),
         nn.Linear(120, 84),
         nn.ReLU(inplace=True),
         nn.Linear(84, 10)
        )

# init
net = GPipe(model, balance=[6, 6], chunks=2)
print(len(net))
print('this is the end of defining model')



# Define a Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

# Train the network
for epoch in range(2):  # loop over the dataset multiple times
    running_loss = 0.0
    for i, data in enumerate(trainloader, start=0):
        # print(i, data)
        # get the inputs; data is a list of [inputs, labels]
        inputs, labels = data
        optimizer.zero_grad()
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        inputs = inputs.to(device)

        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.item()
        if i % 2000 == 1999:    # print every 2000 mini-batch
            print('[%d, %5d] loss: %.3f' %
                  (epoch+1, i+1, running_loss/2000))
            running_loss = 0.0
print("Finished Training")

torch.save(net.state_dict(), PATH)



# Test the network on the test data
dataiter = iter(testloader)
images, labels = dataiter.next()

# print images
# imshow(torchvision.utils.make_grid(images))
print('GroundTrue:', ' '.join('%5s' % classes[labels[j]] for j in range(4)))


net.load_state_dict(torch.load(PATH))

outputs = net(images)
# to get highest energy for a class
_location, predicted = torch.max(outputs, 1)    # 1 means row maxing
print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                              for j in range(4)))

# calculate the accuracy over whole dataset
correct = 0
total = 0
# we don't need to calculate the gradient inference
with torch.no_grad():
    for data in testloader:
        images, labels = data
        outputs = net(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    print('Accuracy of the network on the 10000 test images: %d %%' % (
            100 * correct / total))





