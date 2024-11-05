# video_to_labeled_images_based_on_YOLO8
Aiming to build a pipeline that processes a video to images based on their labels, which could be used to generate datasets. The annotations are generated based on YOLO8. 
## Structure
image_cutting.py: cut images based on YOLO labels 

main.py: where you use this pipeline

movefile.py: move each image to the right folder (based on the label id)

video_processing.py: transform the video to images


yolo.py: use the YOLO8 model to obtain annotations

## Usage
1. In my case, the label I need is 2, you should personalize your own label.
2. make sure all the paths are what you need
3. download the YOLO8 model([pretrained model](https://docs.ultralytics.com/tasks/detect/)), or train it by yourself, **notes that the YOLOs are trained on Coco dataset so there're some labels they can not detect**

