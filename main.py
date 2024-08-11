import cv2

# Set up the model
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
myModel = cv2.dnn_DetectionModel(net)   
myModel.setInputParams(size=(320,320), scale=1/255)

# load class names
classes = []
with  open("dnn_model/classes.txt", "r") as f:
    for class_name in f.readlines():
        class_name = class_name.replace("\n", "")
        classes.append(class_name.strip()) 

# Set up the camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    # Get the frames from the camera
    ret, frame = cap.read()

    # Detect the objects
    (class_ids, score, bboxes) = myModel.detect(frame)
    for class_id, score, bbox in zip(class_ids, score, bboxes):
        x, y, w, h = bbox
        cv2.putText(frame, classes[class_id], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        
    # Show the camera
    cv2.imshow('Frame', frame)
    cv2.waitKey(1)
