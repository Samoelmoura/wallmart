import pickle as pkl
import pandas as pd

class Preprocessing(object):
    def __init__(self):
        self.map_isholiday = pkl.load(open('features/map_isholiday.pkl', 'rb'))
        self.map_type = pkl.load(open('features/map_type.pkl', 'rb'))
        self.pp_temperature = pkl.load(open('features/pp_temperature.pkl', 'rb'))
        self.pp_cpi = pkl.load(open('features/pp_cpi.pkl', 'rb'))
        self.pp_fuel_price = pkl.load(open('features/pp_fuel_price.pkl', 'rb'))
        self.pp_unemployment = pkl.load(open('features/pp_unemployment.pkl', 'rb'))
        self.pp_size = pkl.load(open('features/pp_size.pkl', 'rb'))


    def data_description(self, df_raw):
        df = df_raw.copy()
        # DATA_DESCRIPTION
        # changing datatypes
        df['isholiday'] = df['isholiday'].astype(int)
        df['type'] = df['type'].apply(lambda x: 0 if x == 'A' else (1 if x == 'B' else 2))
        return df


    def data_preparation(self, df):
        # DATA_PREPARATION
        df['isholiday'] = df['isholiday'].map(self.map_isholiday)
        df['type'] = df['type'].map(self.map_type)
        df['temperature'] = self.pp_temperature.transform(df[['temperature']].values)
        df['fuel_price'] = self.pp_fuel_price.transform(df[['fuel_price']].values)
        df['cpi'] = self.pp_cpi.transform(df[['cpi']].values)
        df['unemployment'] = self.pp_unemployment.transform(df[['unemployment']].values)
        df['size'] = self.pp_size.transform(df[['size']].values)
        return df