import numpy as np
from PIL import Image

from sort import Sort
from deep_appearance import DeepAppearance

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