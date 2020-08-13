import torch.nn as nn
import torch

# hyper parameters
in_dim = 10
n_hidden_1 = 20
n_hidden_2 = 30
out_dim = 5


class Net(nn.Module):
    def __init__(self, in_dim, n_hidden_1, n_hidden_2, out_dim):
        super().__init__()

        self.model = nn.Sequential(
            nn.Linear(in_dim, n_hidden_1),
            nn.ReLU(True),
            nn.Linear(n_hidden_1, n_hidden_2),
            nn.ReLU(True),
            # 最后一层不需要添加激活函数
            nn.Linear(n_hidden_2, out_dim)
        )

    def forward(self, x):
        x = self.model(x)
        return x


if __name__ == '__main__':
    x = torch.linspace(1, 10, 10)
    print(x)
    net = Net(10, 1000, 2000, 1)
    output = net(x)
    print(output)