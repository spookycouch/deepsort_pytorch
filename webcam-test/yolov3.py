import cv2
import numpy as np

class YOLOv3():
    def __init__(self, labels_path, config_path, weights_path, confidence = 0.5, nms = 0.3):
        # yolo params
        self.confidence = confidence
        self.nms = nms

        # net setup
        self.labels = open(labels_path).read().strip().split("\n")
        self.net = cv2.dnn.readNetFromDarknet(config_path, weights_path)

        # yolo layers
        layers = self.net.getLayerNames()
        self.yolo_layers = []
        for x in self.net.getUnconnectedOutLayers():
            layer_index = x[0] - 1
            self.yolo_layers.append(layers[layer_index])
    
    def detectObjects(self, frame):
        # get frame dims
        (frame_height, frame_width) = frame.shape[:2]

        # preprocess image and get output of yolo layers thru DNN
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416,416), swapRB=True, crop=False)
        self.net.setInput(blob)
        yolo_outputs = self.net.forward(self.yolo_layers)

        # array setup
        boxes = []
        confidences = []
        class_ids = []

        # loop over detections
        for output in yolo_outputs:
            for detection in output:
                predictions = detection[5:]
                class_id = np.argmax(predictions)
                confidence = predictions[class_id]
                # if the detection meets the confidence threshold
                if confidence > self.confidence:
                    # get bounding box
                    centre_x = detection[0] * frame_width
                    centre_y = detection[1] * frame_height
                    w = int(detection[2] * frame_width)
                    h = int(detection[3] * frame_height)
                    x = int(centre_x - (w/2))
                    y = int(centre_y - (h/2))
                    # update boxes, confidences and classIDs with detection
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # apply NMS
        kept_indices = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence, self.nms)
        detected_objects = []

        # for any kept indices after NMS
        if len(kept_indices) > 0:
            for i in kept_indices.flatten():
                # append label, box, confidence
                x1 = boxes[i][0]
                y1 = boxes[i][1]
                x2 = boxes[i][0] + boxes[i][2]
                y2 = boxes[i][1] + boxes[i][3]
                detected_objects.append((self.labels[class_ids[i]], [x1, y1, x2, y2, confidences[i]]))
        
        return detected_objects