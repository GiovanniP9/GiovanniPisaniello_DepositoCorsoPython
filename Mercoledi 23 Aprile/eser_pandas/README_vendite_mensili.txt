
# Programma di Analisi Vendite Mensili

Questo programma è progettato per simulare e analizzare le vendite di un ristorante o negozio in un mese. Utilizzando i dati generati casualmente, è possibile esplorare le vendite per prodotto e città, creare tabelle pivot, calcolare vendite globali per prodotto, e salvare i risultati in diversi formati (CSV, JSON, Excel).

## Funzionalità principali

### 1. **Genera Dati**
   - Crea un DataFrame con dati casuali, simulando vendite giornaliere per un mese (31 giorni).
   - I dati includono:
     - **Data**: Data della vendita (31 giorni tra il 1 gennaio 2025 e il 31 gennaio 2025).
     - **Città**: La città in cui sono state effettuate le vendite (Roma, Milano, Napoli).
     - **Prodotto**: Tipo di prodotto venduto (Pizza, Pasta, Gelato).
     - **Vendite**: Numero di vendite per ogni giorno.

### 2. **Crea Tabella Pivot**
   - Crea una tabella pivot che calcola le vendite medie per prodotto per ogni città.
   - La tabella pivot aiuta a visualizzare le performance di vendita per ciascun prodotto nelle diverse città.

### 3. **Calcola Vendite Globali**
   - Calcola il totale delle vendite per ciascun prodotto (Pizza, Pasta, Gelato) durante il mese.
   - Le vendite vengono sommate per ogni prodotto e presentate in una tabella.

### 4. **Salva i File**
   - I dati possono essere salvati in vari formati:
     - **CSV**: Salva i dati originali, la tabella pivot e le vendite globali in file CSV separati.
     - **JSON**: Salva i dati in formato JSON (con un record per ogni riga).
     - **Excel**: Salva i dati in un file Excel con più fogli: uno per i dati originali, uno per la tabella pivot, e uno per le vendite globali.

### 5. **Stampa Tutti i Dati**
   - Stampa i dati generati, la tabella pivot e le vendite globali per il controllo visivo.

## Come usare il programma

1. **Esegui il programma**:
   - Avvia il programma nel tuo ambiente Python. Verrà presentato un menu interattivo per scegliere l'azione desiderata.

2. **Scegli l'opzione dal menu**:
   - Puoi generare i dati, creare una tabella pivot, calcolare le vendite globali, salvare i file in vari formati o stampare i dati a schermo.

3. **Salvataggio dei file**:
   - Quando scegli di salvare i dati, puoi selezionare il formato tra **CSV**, **JSON**, o **Excel**. Il programma genererà i file nel formato scelto e li salverà nella stessa cartella in cui è stato eseguito il programma.

## Requisiti

- **Python 3.x** (Testato con Python 3.8)
- **Pandas**: per la gestione dei dati.
- **NumPy**: per operazioni numeriche.

Puoi installare le librerie necessarie utilizzando `pip`:
```bash
pip install pandas numpy
```

## Esempio di utilizzo

1. Avvia il programma con il comando:
   ```bash
   python programma_vendite.py
   ```
2. Seleziona l'opzione desiderata dal menu:
   - **Genera Dati**: Crea i dati casuali.
   - **Crea Tabella Pivot**: Visualizza la tabella pivot.
   - **Calcola Vendite Globali**: Visualizza il totale delle vendite per ogni prodotto.
   - **Salva i File**: Salva i risultati in formato CSV, JSON o Excel.
   - **Stampa Tutti i Dati**: Stampa i dati generati, la tabella pivot e le vendite globali.

## Contributi

I contributi al programma sono benvenuti. Puoi fare una pull request per aggiungere nuove funzionalità o miglioramenti.
