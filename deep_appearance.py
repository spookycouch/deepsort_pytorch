import os

import torch
import torchvision.transforms as transforms

from fullbodynet.full_body_net import FullBodyNet


class DeepAppearance:
    def __init__(self):
        # use GPU if avail
        if torch.cuda.is_available():
            self.device = 'cuda'
        else:
            self.device = 'cpu'
        
        net = FullBodyNet()
        net.load_state_dict(torch.load(os.path.dirname(os.path.abspath(__file__)) + '/mars_triplet_500.pth'))
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