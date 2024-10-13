import pandas as pd

def load_data(file_path):
    """Load CSV data from the provided path."""
    return pd.read_csv(file_path)

def calculate_health_metrics(data):
    """Calculate key metrics for the dashboard."""
    total_cases = data['Cases'].sum()
    total_vaccinated = data[data['Vaccination Status'] == 'Vaccinated'].shape[0]
    hospital_occupancy = data['Occupancy Rate'].mean()
    return {
        'total_cases': total_cases,
        'total_vaccinated': total_vaccinated,
        'hospital_occupancy': round(hospital_occupancy, 2)
    }
