import torch

a = torch.Tensor([[1,2],[3,4]])
print(a)


y = torch.sum(a**2) # 1 + 4 + 9 + 16

print(y)

