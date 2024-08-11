
# Object Detection using YOLOv4-Tiny with OpenCV

This project demonstrates how to use the YOLOv4-Tiny model with OpenCV for real-time object detection through a webcam. The model detects various objects in the video stream and displays bounding boxes and labels around them.

## Prerequisites

Before you begin, ensure you have met the following requirements:

1. Python 3.x installed.
2. Install the required libraries using the following command:
   ```bash
   pip install opencv-python opencv-python-headless
   ```
3. Download the YOLOv4-Tiny model files:
   - [yolov4-tiny.weights](https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights)
   - [yolov4-tiny.cfg](https://github.com/AlexeyAB/darknet/blob/master/cfg/yolov4-tiny.cfg)

4. Download the `classes.txt` file that contains the class names.

## Usage

To run the object detection script, use the following command:

```bash
python main.py
```

## Files

- `object_detection.py`: The main script to run the object detection.
- `dnn_model/yolov4-tiny.weights`: The weights file for YOLOv4-Tiny.
- `dnn_model/yolov4-tiny.cfg`: The configuration file for YOLOv4-Tiny.
- `dnn_model/classes.txt`: Text file containing the names of the object classes.

## How It Works

1. The script loads the YOLOv4-Tiny model using OpenCV's DNN module.
2. It reads class names from the `classes.txt` file.
3. It captures video from the default webcam (ID 0).
4. The model detects objects in each frame, and the script draws bounding boxes and labels around detected objects.

## Notes

- Ensure the `yolov4-tiny.weights`, `yolov4-tiny.cfg`, and `classes.txt` files are placed in the `dnn_model` directory.
- Modify the webcam settings or object detection parameters as needed.

## License

This project is licensed under the MIT License.
