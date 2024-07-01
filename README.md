Spam Detection Web Application

## Overview

This web application, built using Flask, detects spam messages using a Naive Bayes classification model. The application uses a pre-trained Naive Bayes model and a vectorizer to classify messages as either spam or ham (not spam).

## Features

- **Message Input**: Users can input a message to be classified as spam or ham.
- **Spam Detection**: The application uses a pre-trained Naive Bayes model to classify the input message as spam or ham.
- **Result Display**: The application displays the classification result, indicating whether the message is spam or ham.

## Technical Details

- **Model**: The application uses a pre-trained Naive Bayes model (`spamclassifier_MnB.pkl`) to classify messages. The model was trained on a dataset of labeled spam and ham messages.
- **Vectorizer**: The application uses a pre-trained vectorizer (`vectorizer.pkl`) to transform text data into numerical format. The vectorizer was trained on the same dataset as the Naive Bayes model.
- **Flask**: The application is built using Flask, a Python web framework.
- **HTML Templates**: The application uses HTML templates (`index.html` and `result.html`) to render the user interface.

## Dataset

The Naive Bayes model was trained on a dataset of labeled spam and ham messages, consisting of:

- **Spam messages**: 1000 messages labeled as spam
- **Ham messages**: 1000 messages labeled as ham

The dataset was preprocessed to remove stop words, punctuation, and special characters. The text data was then transformed into numerical format using the vectorizer.

## How to Run

1. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application**:
   ```bash
   python app.py
   ```
3. **Open a web browser and navigate to [http://0.0.0.0:8080/](http://0.0.0.0:8080/)**.
4. **Input a message** to be classified as spam or ham.
5. **Click the "Submit" button** to see the classification result.

## Troubleshooting

- **Check for errors**: If you encounter any errors, check the console output for error messages.
- **File location**: Ensure that the `spamclassifier_MnB.pkl` and `vectorizer.pkl` files are in the same directory as the `app.py` file.

## Code Explanation

```python
from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('spamclassifier_MnB.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            messg = str(request.form['mesg'])
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template('result.html', prediction=f"{output}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
```

### Explanation of Key Components

- **Flask**: A web framework for creating web applications in Python.
- **render_template**: A function to render HTML templates.
- **request**: A function to handle HTTP requests.
- **pickle**: A module to serialize and deserialize Python objects (used here to load the pre-trained model and vectorizer).
- **numpy**: A library for numerical operations in Python.
- **model**: The pre-trained machine learning model for spam classification, loaded from a file named `spamclassifier_MnB.pkl`.
- **vectorizer**: The vectorizer used to transform text data into numerical format, loaded from a file named `vectorizer.pkl`.

### Application Routes

- **Home Route** (`@app.route('/', methods=['GET', 'POST'])`):
  - Renders the `index.html` template, allowing users to input a message.
  
- **Prediction Route** (`@app.route('/predict', methods=['POST'])`):
  - Handles POST requests to classify the input message.
  - Transforms the input message using the vectorizer and predicts whether it is spam or ham using the model.
  - Renders the `result.html` template with the prediction result.

### Running the Application

- The application runs on host `0.0.0.0` and port `8080`, making it accessible externally.
- Debug mode is enabled for detailed error messages and auto-reloading on code changes.

---

This README file provides an overview of the Spam Detection Web Application, including its features, technical details, dataset information, and instructions for running and troubleshooting the application.
