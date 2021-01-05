#Model
import torchvision
import torchvision.transforms as transforms
import torch
import cv2
import numpy as np

def load_backbone():
    model = torchvision.models.detection.retinanet_resnet50_fpn(pretrained=True)
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    
    # load the model onto the computation device
    model.eval().to(device)
    
    return model

def create_model():
    pass

def load_model():
    pass

def retinanet_train():
    pass

