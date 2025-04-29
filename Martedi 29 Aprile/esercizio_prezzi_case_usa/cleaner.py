import os
import pandas as pd
import numpy as np


class HousePriceCleaner:
    def __init__(self, base_dir: str, input_file: str, output_file: str):
        self.base_dir = base_dir
        self.input_file = input_file
        self.output_file = output_file
        self.df: pd.DataFrame = pd.DataFrame()

    def load_data(self):
        path = os.path.join(self.base_dir, self.input_file)
        self.df = pd.read_csv(path)

    def clean_data(self):
        # data → datetime
        self.df['date'] = pd.to_datetime(self.df['date'], errors='coerce')
        self.df.drop(columns=['id'], inplace=True)

        # rimuovi duplicati e NaN
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(inplace=True)
        
        # colonna binaria 'renovated'
        self.df['renovated'] = self.df['yr_renovated'].apply(lambda x: 1 if x > 0 else 0)
        self.df.drop(columns=['yr_renovated'], inplace=True)
    
    

    def save_data(self):
        out_path = os.path.join(self.base_dir, self.output_file)
        self.df.to_csv(out_path, index=False)

    def run(self):
        self.load_data()
        self.clean_data()
        self.save_data()


if __name__ == '__main__':
    BASE_DIR = 'Martedi 29 Aprile/esercizio_prezzi_case_usa'
    cleaner = HousePriceCleaner(
        base_dir=BASE_DIR,
        input_file='kc_house_data.csv',
        output_file='kc_house_data_cleaned.csv'
    )
    cleaner.run()
