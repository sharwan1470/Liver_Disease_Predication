from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = os.path.join(os.path.dirname(__file__), 'templates', 'liver_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('liver.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        features = [
            int(request.form['Age']),
            int(request.form['Gender']),
            float(request.form['Total_Bilirubin']),
            float(request.form['Direct_Bilirubin']),
            float(request.form['Alkaline_Phosphotase']),
            float(request.form['Alamine_Aminotransferase']),
            float(request.form['Aspartate_Aminotransferase']),
            float(request.form['Total_Protiens']),
            float(request.form['Albumin']),
            float(request.form['Albumin_and_Globulin_Ratio'])
        ]

        # Prepare the input array
        input_features = np.array([features])

        # Make prediction
        prediction = model.predict(input_features)[0]

        # Interpret the result
        result = "The person is likely to have liver disease." if prediction == 1 else "The person is unlikely to have liver disease."

        return render_template('Result.html', prediction_text=result)
    
    except Exception as e:
        error_message = f"Error occurred: {str(e)}"
        return render_template('liver.html', error=error_message)

if __name__ == "__main__":
    app.run(debug=True)