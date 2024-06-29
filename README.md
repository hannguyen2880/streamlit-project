# Simple Streamlit Project

## Introduction

Welcome to my first Streamlit Project, a suite of 3 simple applications developed using Python. This project demonstrates the versatility and capability of Streamlit in deploying interactive web applications. The applications included in this project are:

1. **Word Correction**: A spelling correction tool that utilizes the Levenshtein distance algorithm to find and correct misspelled words by suggesting the closest match from a pre-defined dictionary.
2. **Object Detection**: An application that uses a Deep Neural Network (DNN) model from the OpenCV library to detect and highlight objects in images.
3. **A simple Chatbot**: A simple yet effective chatbot built using HugChat, designed to provide interactive conversations and assist users with various queries.

## How to Intall
1. **Clone the repository:**
   ```sh
    git clone https://github.com/hannguyen2880/streamlit-project.git
    cd streamlit-project
    ```
2. **(Optional) Create and activate a virtual environment**:
   
   For macOS and Linux:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    For Windows:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```
3. **Intall the required dependencies:**
   ```sh
    pip install -r requirements.txt
    ```
## Running the Application

Once everything is ready, you can launch the application by running one of the following commands based on the application you want to start:

1. **Correct Word**:
    ```sh
    streamlit run src/levelshtein_distance.py
    ```

2. **Object Detection**:
    ```sh
    streamlit run src/object-detection.py
    ```

3. **Chatbot**:
    ```sh
    streamlit run src/chatbot.py
    ```