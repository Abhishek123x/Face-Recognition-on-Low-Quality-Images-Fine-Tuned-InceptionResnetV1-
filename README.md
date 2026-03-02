# Face Recognition on Low-Quality Images (Fine-Tuned InceptionResnetV1)

## Project Overview

This project implements a complete face recognition pipeline designed to
improve performance on low-quality images. The objective was to build a
face recognition system that performs reliably under degraded conditions
such as blur, compression artifacts, and lighting variations.

A pre-trained InceptionResnetV1 model (VGGFace2 weights) was used as the
backbone for extracting 512-dimensional face embeddings. The model was
first evaluated as a baseline and later fine-tuned using identity
classification to improve discrimination performance.

Strict train-test separation was maintained throughout the project to
ensure no data leakage.

------------------------------------------------------------------------

## Key Features

-   Pre-trained InceptionResnetV1 (VGGFace2)
-   512-D face embeddings
-   Cosine similarity for verification
-   Baseline vs Fine-tuned performance comparison
-   ROC & Precision-Recall evaluation
-   Fine-tuning using CrossEntropyLoss + Adam optimizer
-   Streamlit deployment for real-time inference

------------------------------------------------------------------------

## Performance

Baseline AUC: \~0.72\
Fine-Tuned AUC: \~0.88

Fine-tuning significantly improved the model's ability to distinguish
between same-person and different-person pairs under low-quality
conditions.

------------------------------------------------------------------------

## Tech Stack

-   Python
-   PyTorch
-   torchvision
-   NumPy
-   scikit-learn
-   Matplotlib
-   Streamlit
-   facenet-pytorch

------------------------------------------------------------------------

## Project Structure

AI_Intern.ipynb\
app.py\
best_model.pth\
requirements.txt\
README.md

------------------------------------------------------------------------

## How It Works

1.  Load pre-trained InceptionResnetV1\
2.  Extract 512-D embeddings\
3.  Normalize embeddings\
4.  Compute cosine similarity\
5.  Fine-tune using identity classification\
6.  Evaluate using ROC & PR curves\
7.  Deploy via Streamlit UI

------------------------------------------------------------------------

## Running the Streamlit App

streamlit run app.py

------------------------------------------------------------------------

## Data Leakage Prevention

Training and evaluation datasets were strictly separated. No evaluation
images were used during fine-tuning.

------------------------------------------------------------------------

## Note

This project was developed as part of an AI Internship evaluation task.
