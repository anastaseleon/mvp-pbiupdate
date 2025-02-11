import os
import sqlite3
import pandas as pd
import subprocess

# Constants
DB_PATH = "ishikawa_data.db"
CATEGORIES = ["Materials", "Methods", "Machines", "Manpower", "Environment", "Measurement", "Target"]

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS ishikawa_mapping (
                    column_name TEXT PRIMARY KEY,
                    category TEXT)''')
    conn.commit()
    conn.close()

def get_csv_columns(file_path):
    try:
        df = pd.read_csv(file_path)
        return list(df.columns)
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def process_data(file_path, mappings, target_column):
    try:
        df = pd.read_csv(file_path)

        summaries = {}  # Dictionary to store summaries for each column

        for col in df.columns:
            if col!= target_column:  # Exclude the target column from summarization
                summary = df[col].agg(['count', 'sum', 'mean']).to_dict()  # Calculate summary statistics
                summaries[col] = summary  # Store the summary

        # Now, map each column to its Ishikawa category and include in final summary
        final_summary = []
        for col, summary_data in summaries.items():
            ishikawa_category = mappings.get(col)
            if ishikawa_category is None:
                print(f"Warning: Column '{col}' not found in mappings. Skipping.")
                continue  # Skip if no mapping

            summary_data['Column'] = col  # Include the column name in the summary
            summary_data['Ishikawa'] = ishikawa_category  # Add the Ishikawa category

            final_summary.append(summary_data)  # Add to the final list of summaries

        final_summary_df = pd.DataFrame(final_summary)  # Create a DataFrame from the list
        summary_path = "summary.csv"
        final_summary_df.to_csv(summary_path, index=False)
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