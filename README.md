# E-KYC Implementation using Computer Vision

## Project Overview
This project implements an E-KYC (Electronic Know Your Customer) process using computer vision techniques. The application extracts information from PAN card images, validates it against an existing database, and stores the data. The project leverages OpenCV for image processing, EasyOCR for text extraction, and MySQL for database management. The application is deployed using Streamlit, providing a user-friendly interface for the E-KYC process.

## Features
- **Image Processing**: Utilized OpenCV for Gaussian blur and adaptive thresholding to preprocess document images.
- **Text Extraction**: Employed EasyOCR to extract text from PAN card images.
- **Data Validation and Storage**: Created a MySQL database to store the extracted identity data and validate it against existing records.
- **Application Deployment**: Deployed the E-KYC application using Streamlit to provide an interactive interface.

## Files in the Repository
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **=4.8.0**: File related to the project's dependencies or configuration.
- **app.py**: The main application script for deploying the E-KYC interface using Streamlit.
- **config.yaml**: Configuration file for managing settings and parameters.
- **db_operations.py**: Script for database operations, including data insertion and validation.
- **ekyc.drawio**: Diagram representing the E-KYC process flow.
- **face_verification.py**: Script for verifying the face on the document against an existing database.
- **mysqldb_operations.py**: Script for MySQL database operations.
- **ocr.drawio**: Diagram representing the OCR process.
- **ocr_engine.py**: Script for running the OCR process using EasyOCR.
- **old_app.py**: An older version of the application script.
- **postprocess.py**: Script for post-processing the extracted data.
- **preprocess.py**: Script for preprocessing the document images using OpenCV.
- **Query.sql**: SQL queries for setting up and managing the MySQL database.
- **README.md**: Documentation file describing the project.
- **requirements.txt**: List of Python dependencies required to run the project.
- **requirements_deepface.txt**: Additional dependencies for face verification using DeepFace.
- **test.ipynb**: Jupyter notebook for testing and prototyping code.
- **utils.py**: Utility functions used across the project.

## Getting Started
### Prerequisites
- **Python 3.x**: Required to run the scripts.
- **MySQL**: Required to manage the database operations.
- **Streamlit**: Required to deploy the application.
- **OpenCV**: Required for image preprocessing.
- **EasyOCR**: Required for text extraction from images.
- **DeepFace**: Required for face verification.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/e-kyc-implementation.git
