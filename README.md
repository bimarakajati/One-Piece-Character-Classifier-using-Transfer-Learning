# One Piece Character Classifier Using Transfer Learning

![One Piece Character Classifier](output/photo_2024-09-19_22-26-23.jpg)
This project aims to classify characters from the anime One Piece using transfer learning. The dataset used for this project is sourced from Kaggle and contains 18 classes of characters from the anime. The dataset is split into 80% for training and 20% for testing.

## 💡 Project Overview

- **Base Model**: MobileNet
- **Dataset**: [Kaggle](https://www.kaggle.com/datasets/ibrahimserouis99/one-piece-image-classifier) (18 classes of One Piece characters)
- **Data Split**: 80% training, 20% testing
- **Model Accuracy**: Achieved 96% accuracy on the validation dataset

## 🏗️ Model Architecture

The MobileNet model is used as the base model, with additional layers added to enhance its performance. The model is trained using the training dataset and evaluated on the validation dataset.

## 🧑🏻‍💻 Model Deployment

The trained model is saved in multiple formats for deployment:
- [**TensorFlow Lite**](tflite)
- [**TensorFlow.js**](tfjs_model)
- [**SavedModel**](saved_model) for TensorFlow Serving

These formats allow the model to be deployed in web or mobile applications, making it versatile for various use cases.

## ✍ Usage

The model can be used to classify characters from the anime One Piece with high accuracy, making it a valuable tool for fans and developers working on related projects.

## 🤔 How to Inference with Pretrained Models

This document provides a step-by-step guide on how to use a pretrained model to perform inference on a new image.

### Step 1: Install the required packages

To run this notebook, you will need to install the required packages. You can install them using the following command:

```bash
pip install -r requirements.txt
```

### Step 2: Load the pretrained model with docker and tensorflow serving

You can load the pretrained model using the following command:

```bash
sudo docker run -d --name tf_serving_predict \
  -v /repository_path/saved_model:/models/predict \
  -p 8501:8501 \
  -e MODEL_NAME=predict \
  tensorflow/serving:latest
```

### Step 3: Perform inference on a new image

You can now perform inference on a new image using the inference notebook provided in this repository.

### Step 4: Stop the docker container

After you are done with the inference, you can stop the docker container using the following command:

```bash
sudo docker stop tf_serving_predict
sudo docker rm tf_serving_predict
```