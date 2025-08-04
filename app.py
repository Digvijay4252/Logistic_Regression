from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and encoder
model = joblib.load('model.pkl')
label_encoder = joblib.load('label_encoder.pkl')
pass_map_rev = {v: k for k, v in zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_))}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            hours = float(request.form['hours_studied'])
            attendance = float(request.form['attendance'])
            assignments = float(request.form['assignments_completed'])
            sleep = float(request.form['sleep_hours'])

            pred = model.predict([[hours, attendance, assignments, sleep]])[0]
            prediction = pass_map_rev.get(pred, "Unknown")
        except:
            prediction = "Invalid input."

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
