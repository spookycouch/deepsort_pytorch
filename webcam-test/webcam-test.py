import sys
sys.path.append('../')

import cv2
import numpy as np

from yolov3 import YOLOv3
from deepsort import DeepSort


LABELS_PATH  = './YOLOv3/classes.txt'
CONFIG_PATH  = './YOLOv3/yolov3.cfg'
WEIGHTS_PATH = './YOLOv3/yolov3.weights'


def show_detections(frame, detections):
    for detection in track_bbs_ids:
        x1, y1, x2, y2, id = [int(i) for i in detection]
        cv2.rectangle(frame, (x1,y1), (x2,y2), (0,255,0), 2)
        cv2.putText(frame, 'id: {}'.format(id), (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow('deepsort', frame)
    cv2.waitKey(1)


deepsort = DeepSort(max_age=30)
yolo = YOLOv3(labels_path=LABELS_PATH, config_path=CONFIG_PATH, weights_path=WEIGHTS_PATH, confidence=0.3)

cap = cv2.VideoCapture(0)

while 1:
    grabbed, frame = cap.read()
    detections = yolo.detectObjects(frame)

    # deep appearance was designed to work on humans but
    # this allows all yolov3 detections to be tracked for fun
    detections = [obj[1] for obj in detections]
    
    # detections = [obj[1] for obj in detections if obj[0] == 'person']
    detections = np.array(detections)
    
    track_bbs_ids = deepsort.update(frame, detections[:,:4])
    show_detections(frame, track_bbs_ids)