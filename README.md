# video_to_labeled_images_based_on_YOLO8
Aiming to build a pipeline that processes a video to images based on their labels, which could be used to generate datasets. The annotations are generated based on YOLO8. 
## Structure
3.image_cutting.py: cut images based on YOLO labels 

~~main.py: where you use this pipeline~~(on building)

[optional]movefile.py: move each image to the right folder (based on the label id)

requirements.txt: all the packages you need

1.video_processing.py: transform the video to images


2.yolo.py: use the YOLO8 model to obtain annotations

## Usage
1. In my case, the label I need is 2, you should personalize your own label.
2. Make sure all the paths are what you need
3. Download the YOLO8 model([pretrained model](https://docs.ultralytics.com/tasks/detect/)), or train it by yourself, **notes that the YOLOs are trained on Coco dataset so there're some labels they can not detect**
4. I choose to save one image every five frames, you should personalize it based on your video.
5. the order of this pipeline is showed before the file name in **Structure** section, I'm planning to build the main.py to make it convenient, we'll see.
