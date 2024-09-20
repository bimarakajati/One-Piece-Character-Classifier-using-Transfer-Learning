# 🍖 One Piece Character Classifier Using Transfer Learning

This project implements a character classifier for the popular anime One Piece using transfer learning techniques. The classifier can identify 18 different characters from the series with high accuracy, making it a valuable tool for fans and developers working on One Piece related projects.

## 💡 Key Features

- Utilizes MobileNet as the base model with additional custom layers
- Trained on a dataset of 18 One Piece character classes from [Kaggle](https://www.kaggle.com/datasets/ibrahimserouis99/one-piece-image-classifier)
- Achieves 96% accuracy on the validation dataset
- Deployed in multiple formats for versatile use:
  - [**TensorFlow Lite**](tflite)
  - [**TensorFlow.js**](tfjs_model)
  - [**SavedModel**](saved_model) for TensorFlow Serving

## 🏗️ Technical Details

- **Data Split:** 80% training, 20% testing
- **Model Architecture:** MobileNet base with custom layers
- **Inference Methods:** Web interface via Streamlit and API endpoints via TensorFlow Serving

## ✍ Usage

The model can be easily integrated into various applications, including:
- Fan websites and apps
- Character recognition tools
- Content moderation for One Piece-related platforms

## 🧑🏻‍💻 Deployment Using Streamlit Web App

![One Piece Character Classifier](output/-2147483648_-212620.jpg)
- Available online at: https://onepiececlassifier.streamlit.app/
- Can be run locally using: `streamlit run app.py`

## 🧑🏻‍💻 Deployment Using TensorFlow Serving with Docker

![One Piece Character Classifier](output/photo_2024-09-19_22-26-23.jpg)

### Step 1: Install the Required Packages

To run this notebook, you will need to install the required packages. You can install them using the following command:

```bash
pip install -r requirements.txt
```

### Step 2: Run the TensorFlow Serving Docker Container

You can run the TensorFlow Serving Docker container using the following command:

```bash
sudo docker run -d --name tf_serving_predict \
  -v /repository_path/saved_model:/models/predict \
  -p 8501:8501 \
  -e MODEL_NAME=predict \
  tensorflow/serving:latest
```

### Step 3: Perform Inference on a New Image

You can now perform inference on a new image using the [inference notebook](inference.ipynb) provided in this repository or by sending a POST request to the TensorFlow Serving API endpoint. The API endpoint for the TensorFlow Serving is:

```
http://localhost:8501/v1/models/predict:predict
```

### Step 4: Stop the Docker Container

After you are done with the inference, you can stop the docker container using the following command:

```bash
sudo docker stop tf_serving_predict
sudo docker rm tf_serving_predict
```