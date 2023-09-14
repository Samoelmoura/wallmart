from flask import Flask, request
import pandas as pd
import os
import pickle as pkl

app = Flask(__name__)
@app.route('/predict', methods=['POST'])

def wallmart_predict():
    data = request.get_json()
    if data:
        df = pd.DataFrame(data, columns=data[0].keys())
        model = pkl.load(open('models/model.pkl', 'rb'))
        predicts = model.predict(df)
        df['predicts'] = predicts
        return df.to_json(orient='records')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
