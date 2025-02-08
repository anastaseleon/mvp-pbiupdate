import os
import sqlite3
import pandas as pd
import subprocess

# Constants
DB_PATH = "ishikawa_data.db"
CATEGORIES = ["Materials", "Methods", "Machines", "Manpower", "Environment", "Measurement"]

# Database Functions
def initialize_db(): # Keep database initialization in backend
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ishikawa_mapping (
                    column_name TEXT PRIMARY KEY,
                    category TEXT)''')
    conn.commit()
    conn.close()

# Data Processing Functions
def get_csv_columns(file_path):
    try:
        df = pd.read_csv(file_path)
        return list(df.columns)
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:  # Handle CSV parsing errors
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def process_data(file_path, mappings):
    try:
        df = pd.read_csv(file_path)
        df['Ishikawa'] = df.columns.map(mappings.get)

        if df['Ishikawa'].isnull().any(): # Check if any value is null
            raise ValueError("Some columns are not mapped to an Ishikawa category.")

        summary = df.groupby('Ishikawa').agg(['count', 'sum', 'mean']).reset_index()
        summary.columns = ["_".join(col).strip() for col in summary.columns.values]
        summary_path = "summary.csv"
        summary.to_csv(summary_path, index=False)
        return summary_path
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def open_power_bi(summary_path, pbix_file):
    if os.path.exists(pbix_file):
        try:
            subprocess.run(["powerbi", pbix_file, summary_path], shell=True, check=True)
        except subprocess.CalledProcessError as e:
            raise Exception(f"Error opening Power BI: {e}")
        except FileNotFoundError:
            raise FileNotFoundError("Power BI executable not found. Is Power BI installed?")
    else:
        raise FileNotFoundError(f"Power BI template not found at: {pbix_file}")

# Initialize the database when the backend is imported
initialize_db()
