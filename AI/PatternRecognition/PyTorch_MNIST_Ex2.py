## Implementing a Neural Network for Handwritten Character Recognition Using the MNIST Dataset

import torch
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.MNIST(root=".", train=True, download=True, transform=ToTensor())

test_data = datasets.MNIST(root=".", train=False, download=True, transform=ToTensor())

count_train = len(training_data)
count_test = len(test_data)
##--------------------------------------------------------------------
## plot a random image from training data
fig1 = plt.figure(figsize=(8, 8))
sample_idx = torch.randint(len(training_data), size=(1,)).item()
img, label = training_data[sample_idx]
plt.title(label)
plt.axis("off")
plt.imshow(img.squeeze(), cmap="gray")
    
## plot n*n random images from training data in a grid
n = 3
fig2 = plt.figure(figsize=(8, 8))
cols, rows = n, n

for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(count_train, size=(1,)).item()
    img, label = training_data[sample_idx]
    ax2 = fig2.add_subplot(rows, cols, i)
    ax2.title.set_text(label)
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()
##--------------------------------------------------------------------
## use the DataLoader to iterate over the dataset in mini-batches

from torch.utils.data import DataLoader

loaded_train = DataLoader(training_data, batch_size=64, shuffle=True)
loaded_test = DataLoader(test_data, batch_size=64, shuffle=True)

##--------------------------------------------------------------------
## Build Neural Networks
from torch import nn

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.flatten = nn.Flatten()
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
##--------------------------------------------------------------------  
##  instantiates  model:  
model = NeuralNetwork()
print(model)
##--------------------------------------------------------------------  
## Define Cross-entropy is a common loss function
loss_function = nn.CrossEntropyLoss()
##--------------------------------------------------------------------  
## set an optimization algorithm
learning_rate = 0.001
optimizer = torch.optim.SGD(model.parameters(), learning_rate)
##-------------------------------------------------------------------- 
## Training the Neural Network
## looping through the data one batch at a time, using the optimizer to adjust the model, and computing the prediction and the loss
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        pred = model(X)
        train_loss = loss_fn(pred, y)

        optimizer.zero_grad()
        train_loss.backward()
        optimizer.step()

        if batch:
            train_loss, current = train_loss.item(), batch * len(X)
            print(f"Training loss: {train_loss:>7f}  [{current:>5d}/{size:>5d}]")
##--------------------------------------------------------------------  
## test function, which computes the accuracy and the loss
def test(dataloader, model, loss_fn):
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()    
     
    test_loss /= num_batches
    correct /= size
    return test_loss, correct

##--------------------------------------------------------------------  
## run the model 
epochs = 4
for t in range(epochs): ## set number of epochs
    train(loaded_train, model, loss_function, optimizer)
    test_loss, correct = test(loaded_test, model, loss_function)    
    print('\n Finished Epoch: ' , (t+1))    
    print ("--------------------------------------------")

##--------------------------------------------------------------------  
accuracy = correct*100
print('Number of training images = ' , count_train)
print('Number of testing images = ' , count_test)
print('Training data classes')
print(training_data.classes) #classes inside the data:
print("Accuracy = %.2f %%" %(accuracy))
print("Average loss = %.2f" %(test_loss))
##--------------------------------------------------------------------  
