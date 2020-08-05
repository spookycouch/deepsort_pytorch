import numpy as np

import torch
import torchvision
import torchvision.transforms as transforms

from PIL import Image

from full_body_net.full_body_net import FullBodyNet
from sort import Sort



class DeepAppearance:
    def __init__(self):
        # use GPU if avail
        if torch.cuda.is_available():
            self.device = 'cuda'
        else:
            self.device = 'cpu'
        
        net = FullBodyNet()
        net.load_state_dict(torch.load('./mars_triplet_500.pth'))
        net.to(self.device)
        net.eval()
        self.net = net

    # transform for nets trained on imagenet
    def imagenet_transform(self):
        return transforms.Compose([
            transforms.Resize((299, 299)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

    def predict_embeddings(self, detections, batch_size=8):
        # transform
        transform = self.imagenet_transform()
        detections = [transform(i) for i in detections]

        # separate detections into batches
        batches = []
        index = -1

        for i, detection in enumerate(detections):
            if i % batch_size == 0:
                batches.append([])
                index += 1
            
            batches[index].append(detection)

        # get embeddings
        embeddings_out = []

        with torch.no_grad():
            for batch in batches:
                batch = torch.stack(batch).to(self.device)
                embeddings = self.net(batch).cpu().numpy()

                for embedding in embeddings:
                    embeddings_out.append(embedding)
            
        return embeddings_out



class DeepSort():
    """
    wrapper class for Sort using deep appearance above
    """
    def __init__(self, max_age=30, min_hits=3):
        self.deep_appearance = DeepAppearance()
        self.sort = Sort(max_age, min_hits)
    
    def update(self, frame, dets):
        frame = np.flip(frame, axis=2)
        H,W,C = frame.shape
        images = []

        for detection in dets:
            x1 = max(int(detection[0]), 0)
            y1 = max(int(detection[1]), 0)
            x2 = min(int(detection[2]), W)
            y2 = min(int(detection[3]), H)
            image = frame[y1:y2, x1:x2, :]
            image = Image.fromarray(image)
            images.append(image)
        
        if len(images) > 0:
            embs = self.deep_appearance.predict_embeddings(images)
        else:
            embs = []
        
        return self.sort.update(dets, embs)