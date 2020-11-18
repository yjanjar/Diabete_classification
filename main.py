import pickle
import numpy as np
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model


TEST_RESULTS = {
	0: 'negative',
	1: 'postive'
}

model = load_model("models/best_model.hdf5")

app = Flask(__name__)

@app.route('/')
def iris_index():
    return render_template('home.html')


@app.route('/predict/', methods=['POST'])
def results():
    if request.method == 'POST':

        pregnancies = float(request.form['inputPregnancies'])
        glucose = float(request.form['inputGlucose'])
        bloodpressure = float(request.form['inputBloodPressure'])
        skinthinchness = float(request.form['inputSkinThickness'])
        insuline = float(request.form['inputInsuline'])
        bmi = float(request.form['inputBMI'])
        dpf = float(request.form['inputDiabetesPredigreeFunction'])
        age = float(request.form['inputAge'])

        data = [[pregnancies, glucose, bloodpressure, skinthinchness,
         insuline, bmi, dpf, age]]
        #data = np.array(data).astype(np.float)
        #print(type(data), data.shape)
        pred = np.argmax(model.predict(data))
        result = TEST_RESULTS[pred]

        return render_template('predict.html', result=result)




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000 ,
        debug=True
    )