Spam Detection Web Application
Overview

This web application, built using Flask, detects spam messages using a Naive Bayes classification model. The application uses a pre-trained Naive Bayes model and a vectorizer to classify messages as either spam or ham (not spam).
Features

    Message Input: Users can input a message to be classified as spam or ham.
    Spam Detection: The application uses a pre-trained Naive Bayes model to classify the input message as spam or ham.
    Result Display: The application displays the classification result, indicating whether the message is spam or ham.

Technical Details

    Model: The application uses a pre-trained Naive Bayes model (spamclassifier_MnB.pkl) to classify messages. The model was trained on a dataset of labeled spam and ham messages.
    Vectorizer: The application uses a pre-trained vectorizer (vectorizer.pkl) to transform text data into numerical format. The vectorizer was trained on the same dataset as the Naive Bayes model.
    Flask: The application is built using Flask, a Python web framework.
    HTML Templates: The application uses HTML templates (index.html and result.html) to render the user interface.

Dataset

The Naive Bayes model was trained on a dataset of labeled spam and ham messages, consisting of:

    Spam messages: 1000 messages labeled as spam
    Ham messages: 1000 messages labeled as ham

The dataset was preprocessed to remove stop words, punctuation, and special characters. The text data was then transformed into numerical format using the vectorizer.
How to Run

    Install the required dependencies by running:

    bash

pip install -r requirements.txt

Run the application by executing:

bash

    python app.py

    Open a web browser and navigate to http://0.0.0.0:8080/.
    Input a message to be classified as spam or ham.
    Click the "Submit" button to see the classification result.

Troubleshooting

    If you encounter any errors, check the console output for error messages.
    Ensure that the spamclassifier_MnB.pkl and vectorizer.pkl files are in the same directory as the app.py file.
