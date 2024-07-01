from flask import Flask, render_template, request
# Flask: A web framework for creating web applications in Python.
# render_template: A function to render HTML templates.
# request: A function to handle HTTP requests.
import pickle
import numpy as np
# pickle: A module to serialize and deserialize Python objects (used here to load the pre-trained model and vectorizer).
# numpy: A library for numerical operations in Python.
model = pickle.load(open('spamclassifier_MnB.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
# model: The pre-trained machine learning model for spam classification,
#  loaded from a file named 'spamclassifier_MnB.pkl'.
# vectorizer: The vectorizer used to transform text data into numerical format,
# loaded from a file named 'vectorizer.pkl'.
# 'r': This indicates that the file is being opened for reading.
# 'b': This indicates that the file is being opened in binary mode.
app = Flask(__name__)
# app: An instance of the Flask class, which is the main object for your web application.
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
# @app.route('/'): Decorator to define the URL route for the home page (root URL).
# methods=['GET', 'POST']: The home route can handle both GET and POST requests.
# home(): Function to handle requests to the home route, rendering the 'index.html' template.
# The render_template function in Flask is used to render an HTML template and
# return it as a response to the client. This function allows you to dynamically
# generate HTML pages using templates
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            messg = str(request.form['mesg'])
            transformed = vectorizer.transform([messg])
            transformed_data = transformed.toarray()
            pred = model.predict(transformed_data)
            output = str(pred[0])
            return render_template('result.html',prediction=f"{output}")
    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")
# @app.route('/predict', methods=['POST']): Decorator to define the URL route for the prediction functionality. It only handles POST requests.
# predict(): Function to handle prediction requests.
# if request.method == 'POST': Checks if the request method is POST.
# messg = str(request.form['mesg']): Retrieves the message text from the form data.
# transformed = vectorizer.transform([messg]): Transforms the message text 
# into a numerical format using the vectorizer.
# transformed_data = transformed.toarray(): Converts the transformed data to an array format.
# pred = model.predict(transformed_data): Uses the model to predict whether the message is spam or ham.
# output = str(pred[0]): Converts the prediction result to a string.
# return render_template('result.html',prediction=f"{output}"): Renders the 
# 'result.html' template with the prediction result.
# except Exception as e: Handles any exceptions that occur during the prediction process.
# return render_template('result.html', prediction=f"Error: {str(e)}"):
# Renders the 'result.html' template with the error message if an exception occurs.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

# if __name__ == "__main__":: Ensures the Flask application runs only if the 
# script is executed directly (not imported as a module).
# app.run(host="0.0.0.0", port=8080, debug=True): Starts the Flask web server.
# host="0.0.0.0": Makes the server accessible externally.
# port=8080: Specifies the port number.
# debug=True: Enables debug mode, which provides detailed error 
# messages and auto-reloads the server on code changes.