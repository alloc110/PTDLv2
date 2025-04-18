import sys
import torch
import torch.nn as nn
import torch.optim

device = 'cuda' if torch.cuda.is_available else "cpu"
class LSTM_MODEL (nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(LSTM_MODEL, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
        self.device = 'cuda' if torch.cuda.is_available else "cpu"

    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(self.device)
        out,_ = self.lstm(x, (h0, c0))

        out = self.fc(out[:, -1, :])
        return out.squeeze()

    # def init_hidden(self,  device):
    #     h0 = torch.zeros(self.num_layers, self.hidden_size).to(device)
    #     c0 = torch.zeros(self.num_layers, self.hidden_size).to(device)
    #     return h0, c0
