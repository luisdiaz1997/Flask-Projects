import torch
import numpy as np
from torchvision import models

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


model = models.resnet34(pretrained=True)
model.conv1 = torch.nn.Conv2d(in_channels= 1, out_channels= 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)
model.fc = torch.nn.Linear(model.fc.in_features, 10)
model.eval()

model.load_state_dict(torch.load("mymodel", map_location=device))
model.to(device)

def predict(image):
    imTensor = torch.tensor((1/255)*np.array(image.resize(size=(28, 28)))[ None,None, :,:, 3], dtype=torch.float).to(device)
    x= torch.nn.Softmax(dim= 1)(model(imTensor))
    return x.detach().cpu().numpy()[0].tolist()
