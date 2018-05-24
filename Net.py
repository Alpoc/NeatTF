import torch.nn as nn
import torch.nn.functional as F


class Net(nn.Module):
    def __init__(self, input_nodes, hidden_layers, output_nodes):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(input_nodes, hidden_layers[0])
        for layer, num_nodes in enumerate(hidden_layers[1:]):
            name = "fc" + str(layer)
            self.name = nn.linear(hidden_layers[layer - 1], num_nodes)
            if layer == len(hidden_layers):
                self.name = nn.linear(num_nodes, output_nodes)

    def __str__(self):
        print(Net)
