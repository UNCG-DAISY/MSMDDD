# Image Classifiers
In our research, we compared several image classifiers. A group of them was to classify images as Real or Spam (Binary Classification), and the second was annotate the real images based on what's happening within them.

## Binary Classifier
Our best model was a pretrained Inception-V3 model that was retrained on our data. The model is available [here](https://github.com/tensorflow/models/tree/master/research/inception), check the *How to Fine-Tune a Pre-Trained Model on a New Task* Section.

## Multi-Label Classifier (Annotator)
As before, Inception-V3 was our best model in this part. We used a slightly modified version to be able to predict multiple labels per image. The code is available [here](https://github.com/BartyzalRadek/Multi-label-Inception-net).


## Image Downloader
To make things easier on is, we created an image downloading script that takes a bunch of tweets, their url links, their image classes; and try to download the image inside it's appropriate path.
