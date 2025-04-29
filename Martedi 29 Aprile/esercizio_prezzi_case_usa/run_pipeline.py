import os
import sys
import time

# Import dei moduli custom
from cleaner import HousePriceCleaner
from predict import HousePricePredictor

def run_pipeline():
    """Esegue l'intera pipeline: pulizia dati -> predizione"""
    BASE_DIR = 'Martedi 29 Aprile/esercizio_prezzi_case_usa'
    CLEANED_FILE = 'kc_house_data_cleaned.csv'
    
    print("=" * 50)
    print("FASE 1: PULIZIA DEI DATI")
    print("=" * 50)
    
    # Esegui il cleaner
    cleaner = HousePriceCleaner(
        base_dir=BASE_DIR,
        input_file='kc_house_data.csv',
        output_file=CLEANED_FILE
    )
    cleaner.run()
    
    print("\nPulizia dati completata!")
    print(f"File pulito salvato in: {os.path.join(BASE_DIR, CLEANED_FILE)}")
    
    # Breve pausa per separare visivamente le due fasi
    time.sleep(1)
    
    print("\n" + "=" * 50)
    print("FASE 2: PREDIZIONE DEI PREZZI")
    print("=" * 50)
    
    # Esegui il predittore
    predictor = HousePricePredictor(
        base_dir=BASE_DIR,
        input_file=CLEANED_FILE
    )
    predictor.run()
    
    print("\nPipeline completata con successo!")

if __name__ == "__main__":
    try:
        run_pipeline()
    except Exception as e:
        print(f"Errore durante l'esecuzione della pipeline: {str(e)}")
        sys.exit(1)