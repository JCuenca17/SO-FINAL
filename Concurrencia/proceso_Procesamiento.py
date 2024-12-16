import pandas as pd
import numpy as np
import time
import random

def generate_sample_data(rows=1000):
    """
    Generar datos de muestra para procesamiento
    """
    return pd.DataFrame({
        'age': np.random.randint(18, 80, rows),
        'income': np.random.normal(50000, 15000, rows),
        'education_years': np.random.normal(14, 3, rows),
        'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], rows)
    })

def process_data(df):
    """
    Realizar análisis de datos
    """
    print("--- Iniciando Procesamiento de Datos ---")
    
    # Estadísticas descriptivas
    print("\nEstadísticas Descriptivas:")
    print(df.describe())
    
    # Análisis por ciudad
    print("\nPromedios por Ciudad:")
    city_analysis = df.groupby('city').agg({
        'age': 'mean',
        'income': ['mean', 'median'],
        'education_years': 'mean'
    })
    print(city_analysis)
    
    # Categorización de ingresos
    def categorize_income(income):
        if income < 30000: return 'Bajo'
        elif income < 60000: return 'Medio'
        else: return 'Alto'
    
    df['income_category'] = df['income'].apply(categorize_income)
    
    # Distribución de categorías de ingresos
    print("\nDistribución de Categorías de Ingresos:")
    print(df['income_category'].value_counts(normalize=True))
    
    # Correlaciones
    print("\nCorrelaciones:")
    print(df[['age', 'income', 'education_years']].corr())
    
    # Guardar resultados
    df.to_csv('processed_data.csv', index=False)
    print("\nDatos procesados guardados en 'processed_data.csv'")

def main():
    # Simular tiempo de procesamiento
    time.sleep(random.uniform(2, 5))
    
    # Generar y procesar datos
    data = generate_sample_data()
    process_data(data)

if __name__ == '__main__':
    main()