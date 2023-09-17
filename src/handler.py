from flask import Flask, request
import pandas as pd
import os
import pickle as pkl
from preprocessing import Preprocessing

app = Flask(__name__)
@app.route('/predict', methods=['POST'])

def wallmart_predict():
    data = request.get_json()
    if data:
        df_raw = pd.DataFrame(data, columns=data[0].keys())
        preprocessing = Preprocessing()
        df = preprocessing.data_description(df_raw.drop(['store', 'date', 'weekly_sales'], axis=1))
        df = preprocessing.data_preparation(df)
        model = pkl.load(open('models/model.pkl', 'rb'))
        predicts = model.predict(df)
        df_raw['predicts'] = predicts
        pp_weekly_sales = pkl.load(open('features/pp_weekly_sales.pkl', 'rb'))
        df_raw['predicts'] = pp_weekly_sales.inverse_transform(df_raw[['predicts']].values)
        return df_raw.to_json(orient='records')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)
