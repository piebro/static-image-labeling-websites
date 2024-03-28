# Static Image Labeling Websites

Static and simple websites for labeling images for computer vision applications.

1. [Website](https://piebro.github.io/static-image-labeling-websites/object-detection-labeling.html) for labeling bounding boxes for one object class with 0 or 1 objects per image.
2. [Website](https://piebro.github.io/static-image-labeling-websites/classification-labeling.html) for labeling image for classification. Use `python classification_txt_to_folder.py <path-dataset-folder>` to save the images in folder according to the annotations. In the dataset folder should be oroginal images in a `classification_raw` folder and the `classification-annotations.txt` file.

These annotation workflows are very opinionated and optimized for specific labeling tasks I have used.
If your requirements differ from these, you can just fork and modify the code.
If you think your modifications could also be useful to others and you want to share them, feel free to open a pull request.

I also recommend trying zero-shot labeling to pre-annotate images and then only correct the generated labels.

1. [Zero-Shot Object Detection](https://huggingface.co/models?pipeline_tag=zero-shot-object-detection&sort=trending)
2. [Zero-Shot Image Classification Model](https://huggingface.co/models?pipeline_tag=zero-shot-image-classification&sort=trending)
