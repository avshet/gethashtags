# gethashtags

A web interface which generates hashtag for the given input images, widely useful for social media platforms for tagging.

### APIs Used

- [Google Vision API](https://cloud.google.com/vision/docs/quickstart) - Google Cloud’s Vision API offers powerful pre-trained machine learning models through REST and RPC APIs.

### Getting Started

- Establish a Vision API project and vision key.
  - Sign-in to Google Cloud Platform Console and create a new project
  - Enable the Vision API.
  - Authenticate API requests and download the keyFile.json.
  - Set GOOGLE_APPLICATION_CREDENTIALS with keyFile.json.
  - Install the Google Client Vision API client library.
- Write [Python code to query the Vision API](https://codelabs.developers.google.com/codelabs/cloud-vision-api-python#2).
  - Import google.cloud.vision
  - Use inbuilt methods label-detection and label-annotations
- [Build web app using Flask and html](https://www.youtube.com/watch?v=rFPzo1VnPXU)
  - processing an image using a python script by uploading the image from HTML form and executing the python script.
#### Note - Keyfile.json should be downloaded and should be stored in the repository

https://user-images.githubusercontent.com/71021069/217905579-eb08ce2d-6ff1-4dbe-97e9-5a45448cd708.mp4

The Vision API can detect and extract information about entities in an image, across a broad group of categories.

Labels can identify general objects, locations, activities, animal species, products, and more. If you need targeted custom labels, [Cloud AutoML Vision](https://cloud.google.com/vision/automl/docs) allows you to train a custom machine learning model to classify images.

Labels are returned in English only. The Cloud Translation API can translate English labels into any of a number of other languages
