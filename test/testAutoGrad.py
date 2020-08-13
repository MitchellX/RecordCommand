import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)

y = x+2
print(y)

z = y* y* 3
out = z.mean()
print(z, out)
print(out)

print('------------')

out.backward()
print(x.grad)   # Print gradients d(out)/dx

print('############')
# x = torch.tensor((20.5556, 285.4648, -1303.7313), dtype=torch.float, requires_grad=True)

x = torch.randn(3, requires_grad=True)

y = x * 2
while y.data.norm() < 1000:
    y = y * 2

print(x)
print(y)
# y = y.mean()

v = torch.tensor([1, 1, 1], dtype=torch.float)
y.backward(v)
print('----')
print(x.grad)