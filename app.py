from flask import Flask, jsonify
from tensorflow.keras.models import load_model

import numpy as np

model = load_model('crash_model.h5')

app = Flask(__name__)



@app.route("/")
def welcome():
    return (
        f"/api/v1.0/model/010101010101010101"
    )


@app.route("/api/v1.0/model/<input_array>", methods=['GET'])
def crash_model(input_array):

    data = [int(char) for char in input_array]
    data = np.reshape(data, (1, -1))
    predictions = model.predict(data)

    return jsonify({'predictions': predictions.tolist()})



if __name__ == "__main__":
    app.run(debug=True)


