# A Convoluted Neural Network (CNN) Model for Image Recognition Deployed in Streamlit.


## Table of Contents


- [Introduction](#Introduction)
- [Dataset Link](#Dataset-Links)
- [Data Dictionary](#Data-Dictionary)
- [Analytical Summary](#Analytical-Summary)


---

## Introduction

This repo contains the products of our General Assembley group hackthon project to create an image recognition convoluted neural network model to detect the presence, or lack there of, a hotdog in an image file. 

Image recognition refers to the ability of a model to accurately identify a target within an image. Image recognition is utilized in a number of different industries from identifying possible faults in a manufacturing line to determining if an individual possesses anatomical abnormalities in healthcare([*source*](https://www.mathworks.com/discovery/image-recognition-matlab.html#:~:text=Image%20recognition%20is%20the%20process,medical%20imaging%2C%20and%20security%20surveillance.)). Image recognition is also used in artificial Intelligence (AI) programs to identify individuals based on facial features or create new faces modeled after previously identified features. The applications of image recognition are vast and the cornerstone for many emerging technologies([*source*](https://www.comidor.com/knowledge-base/machine-learning/image-recognition-use-cases/)).  

Feel free to upload an image to the [app](https://saskinosie-image-recognition-streamlit-app-hotdog-ddxcvn.streamlit.app/) and try and stump the model!!!

## Dataset Link

* [*Original Kaggle Data Set*](https://www.kaggle.com/datasets/yashvrdnjain/hotdognothotdog)

## Analytical Summary

The CNN model for the hot dog data set did not perform as well as the EfficientNetB0 transfer learning model we tested in distinguishing whether or not a hot dog was present in an image. This stands to reason as the EfficientNetB0 model is trained in a much larger data set than the Kaggle data set used here. However, teh CNN model did perform relatively well and can be used as a starting point for developing a better model with more training data. Ultimately, the EfficientNetB0 model was used in the Streamlit app.
