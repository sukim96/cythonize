import torch
import torchvision

from torchvision.models import resnet18


class Engine:
    def __init__(self, device='cuda'):
        self.device = device
        self.model = resnet18().to(self.device).eval()
        self.model.requires_grad_(False)

    def forward(self, x):
        return self.model(x)
