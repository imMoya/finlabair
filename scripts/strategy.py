import pandas as pd
from datetime import datetime, timedelta
import random

def random_strategy(ini_date: datetime, fin_date: datetime, n_events: int):
    # DJIA tickers
    dj_tickers = pd.read_csv('../data/dow_jones_constituents.csv')
    dj_tickers = dj_tickers['Symbol'].tolist()

    def random_date(ini_date, fin_date):
        while True:
            # Generar una fecha aleatoria entre start_date y end_date
            delta = fin_date - ini_date
            random_days = random.randint(0, delta.days)
            random_week_day = ini_date + timedelta(days=random_days)

            # Verificar si la fecha es de lunes a viernes
            if random_week_day.weekday() < 5:  # 0 = lunes, 4 = viernes
                return random_week_day


    # Crear un diccionario vacío
    transactions_list = {
        'symbol': [],
        'date': [],
        'quantity': [],
        'transaction_type': []
    }

    # Generar transacciones aleatorias
    for _ in range(n_events):
        # Elegir un símbolo aleatorio
        symbol = random.choice(dj_tickers)

        # Elegir una fecha aleatoria entre las fechas dadas
        date = random_date(ini_date, fin_date)

        # Generar una cantidad aleatoria entre 1 y 100
        quantity = random.randint(1, 100)

        # Elegir un tipo de transacción aleatorio
        transaction_type = random.choice(['buy', 'sell'])

        # Añadir los valores al diccionario
        transactions_list['symbol'].append(symbol)
        transactions_list['date'].append(date)
        transactions_list['quantity'].append(quantity)
        transactions_list['transaction_type'].append(transaction_type)

    #Mostrar el diccionario resultante
    # for i in range(10):
    #     print(f"Transaction {i + 1}:")
    #     print(f"  Symbol: {transactions_list['symbol'][i]}")
    #     print(f"  Date: {transactions_list['date'][i]}-{transactions_list['date'][i].weekday()}")
    #     print(f"  Quantity: {transactions_list['quantity'][i]}")
    #     print(f"  Transaction Type: {transactions_list['transaction_type'][i]}")
    #     print()

    return transactions_list