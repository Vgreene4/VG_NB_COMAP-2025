import numpy as np
from sklearn.model_selection import train_test_split
import torch
from torch import nn
import torch.nn.functional as F
from abc import ABC, abstractmethod
import torch.utils.data as data
import csv
import matplotlib.pyplot as plt


SEED = 42
batch_size = 32
learning_rate = 0.000005
num_epochs = 2000
print_epochs = 50
record_epochs = 10


raw_data = np.load("TrainingData/predict_medals_data.npz")
x_data = raw_data['x_data'][:,1:]
y_data = raw_data['y_data'][:,1:]

split_data = train_test_split(x_data, y_data, test_size=0.2, random_state=SEED)
x_train = torch.from_numpy(split_data[0]).float()
x_test = torch.from_numpy(split_data[1]).float()
y_train = torch.from_numpy(split_data[2]).float()
y_test = torch.from_numpy(split_data[3]).float()


train_dataset = data.TensorDataset(x_train, y_train)
train_loader = data.DataLoader(train_dataset, batch_size=batch_size)
test_dataset = data.TensorDataset(x_test, y_test)
test_loader = data.DataLoader(test_dataset, batch_size=batch_size)

class Metric(ABC):
    @abstractmethod
    def __call__(
        self, 
        values_predict: torch.Tensor,
        values_true: torch.Tensor
    ) -> torch.Tensor:
        pass

    @property
    @abstractmethod
    def greater_is_better(self) -> bool:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass




class MSE(Metric):
    def __call__(
        self,
        values_predict: torch.Tensor,
        values_true: torch.Tensor,
    ) -> torch.Tensor:
        
        predict = values_predict.squeeze()
        error_off = predict - values_true
        MSE_off = (torch.square(error_off)).to(torch.float32).mean()

        g_predict = predict[:,0]
        s_predict = predict[:,1]
        b_predict = predict[:,2]
        t_predict = predict[:,3]
        t_alt_predict = g_predict + s_predict + b_predict
        tot_off = (torch.abs(t_alt_predict - t_predict)).to(torch.float32).mean()

        error = MSE_off + tot_off

        return (torch.square(error)).to(torch.float32).mean()

    greater_is_better = False
    name = "mean squared error"



class dnn(nn.Module):
    def __init__(self):
        super(dnn, self).__init__()
        self.fc1 = nn.Linear(7, 256)  
        self.fc2 = nn.Linear(256, 256)
        self.fc3 = nn.Linear(256, 4)
        self.drop = nn.Dropout(p=0.5)

    def forward(self, input):
        f1 = F.relu(self.fc1(input))
        d1 = self.drop(f1)
        f2 = F.relu(self.fc2(d1))
        d2 = self.drop(f2)
        output = self.fc3(d2)
        return output


model = dnn()

criterion = MSE()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)


# training loop



train_loss_list = []
test_loss_list = []


for epoch in range(num_epochs):
    for i, (inputs, targets) in enumerate(train_loader):
        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # Print progress (optional)
    if (epoch+1) % record_epochs == 0:
        test_loss = criterion(model(x_test), y_test)
        train_loss_list.append(loss.item())
        test_loss_list.append(test_loss.item())

        if (epoch+1) % print_epochs == 0:
            print(epoch)
            print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}, Test error: {test_loss.item():.4f}')


times = [print_epochs*x+1 for x in range(len(train_loss_list))]
print(times)




with open('train_loss_list', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(train_loss_list)
with open('test_loss_list', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(test_loss_list)



print('training done')
print(f'final test error: {criterion(model(x_test), y_test).item():.4f}')
torch.save(model, 'model1')
print("saved model")

plt.plot(times, train_loss_list, label='Train loss')
plt.plot(times, test_loss_list, label='Test loss')
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.legend()
plt.savefig('Error graph.png')
plt.show()