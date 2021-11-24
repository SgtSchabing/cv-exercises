import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module):
    def __init__(self):
        # START TODO #################
        # see model description in exercise pdf
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        #self.relu1 = F.relu()
        #self.pool1 = F.max_pool2d(2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        #self.relu2 = F.relu()
        #self.pool2 = F.max_pool2d(2)
        #self.vectorize =
        self.linear1 = nn.Linear(400, 120)
        self.linear2 = nn.Linear(120, 84)
        self.linear3 = nn.Linear(84, 10)

        # END TODO #################

    def forward(self, x):
        # START TODO #################
        # see model description in exercise pdf
        #print(x.shape)
        x = self.conv1(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        #print(x.shape)
        x = x.view(10, 400)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        x = F.relu(x)
        x = self.linear3(x)
        #print(x.shape)
        return x
        # END TODO #################
