import pickle
from flask import Flask, render_template, request


IRIS_TYPES = {
	0: 'setosa',
	1: 'versicolor',
	2: 'virginica'
}

model = pickle.load(open(f"model.sav", 'rb'))

app = Flask(__name__)

@app.route('/')
def iris_index():
    return render_template('index.html')


@app.route('/predict/', methods=['POST'])
def results():
    if request.method == 'POST':

        sepal_length = request.form['inputSepalLength']
        sepal_width = request.form['inputSepalWidth']
        petal_length = request.form['inputPetalLength']
        petal_width = request.form['inputPetalWidth']

        data = [[sepal_length, sepal_width, petal_length, petal_width]]
        pred = model.predict(data)[0]
        flower_name = IRIS_TYPES[pred]

        return render_template('prediction.html', iris_type=flower_name)




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000 ,
        debug=True
    )