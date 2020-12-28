import torch
import numpy as np


device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        #1 x 28 x 28
        self.conv1 = torch.nn.Conv2d(in_channels= 1, out_channels= 32, kernel_size= (3, 3),  padding = 1)
        self.bn1 = torch.nn.BatchNorm2d(32)
        self.pool1 = torch.nn.MaxPool2d(kernel_size= (2, 2)) #out 16 x (14 x 14)

        self.conv2 = torch.nn.Conv2d(in_channels= 32, out_channels= 64, kernel_size= (3, 3),  padding = 1)
        self.bn2 = torch.nn.BatchNorm2d(64)
        self.pool2 = torch.nn.MaxPool2d(kernel_size= (2, 2)) #out 32 x (7 x 7)

        self.conv3 = torch.nn.Conv2d(in_channels= 64, out_channels= 16, kernel_size= (2, 2))
        self.bn3 = torch.nn.BatchNorm2d(16)
        self.pool3 = torch.nn.MaxPool2d(kernel_size= (2, 2)) #out 16 x (3 x 3)

        self.conv4 = torch.nn.Conv2d(in_channels= 16, out_channels= 10, kernel_size= (3, 3))
        #out 10 x (1 x 1)

        self.Flatten = torch.nn.Flatten()
        
        
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = torch.relu(x)
        x = self.pool1(x)

        x = self.conv2(x)
        x = self.bn2(x)
        x = torch.relu(x)
        x = self.pool2(x)

        x = self.conv3(x)
        x = self.bn3(x)
        x = torch.relu(x)
        x = self.pool3(x)

        x = self.conv4(x)
        
        x = self.Flatten(x)

        return x
        

model = Net()
model.load_state_dict(torch.load("mymodel"))
model.to(device)

def predict(image):
    imTensor = torch.tensor(np.array(image.resize(size=(28, 28)))[ None,None, :,:, 3], dtype=torch.float).to(device)
    x= torch.nn.Softmax(dim= 1)(model(imTensor))
    return x.detach().cpu().numpy()[0].tolist()