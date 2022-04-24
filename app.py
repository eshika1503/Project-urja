# -*- coding: utf-8 -*-

import numpy as np
import os
import pickle
import joblib

from flask import Flask, request, render_template 

# Create application
app = Flask(__name__,static_url_path='', static_folder='script',template_folder='templates')


# Load ML model
# model = joblib.load('model.pkl')
model = pickle.load(open('model.pkl', 'rb')) 
# fullpath = os.path.join( 'model.pkl')
# model = joblib.load(fullpath)


# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Heart_Disease_Classifier')
def mlmodel():
    return render_template('Heart_Disease_Classifier.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('Heart_Disease_Classifier.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('Heart_Disease_Classifier.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()
    
    