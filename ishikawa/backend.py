import os
import pandas as pd
import subprocess

# Constants
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SUMMARY_CSV = os.path.join(SCRIPT_DIR, "ishikawa_summary.csv")
CATEGORIES = ["Materials", "Methods", "Machines", "Manpower", "Environment", "Measurement", "Ignore", "Target"]
MEASURES = ['count', 'sum', 'mean']

def get_csv_columns(file_path):
    """Extracts column names from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        return list(df.columns)
    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def process_data(file_path, mappings, target_column, measures):
    """Processes the data, calculates correlations, and saves the summary to a CSV file."""
    try:
        df = pd.read_csv(file_path)


        summaries =[]
        for col, measure in measures.items():
            if col!= target_column and measure in MEASURES:
                value = df[col].agg([measure]).to_dict()[measure]
                ishikawa_category = mappings.get(col, "Unknown")

                # Calculate correlation with target column (if numeric)
                if pd.api.types.is_numeric_dtype(df[col]):
                    correlation = df[col].corr(df[target_column])
                else:
                    correlation = None

                # Add the selected measure and correlation to the summary
                summaries.append({
                    "Column": col,
                    "Ishikawa": ishikawa_category,
                    "Value": value,
                    "Measure": measure,
                    "Correlation to target": correlation  # Add correlation as a separate column
                })

        # Add the target column summary
        target_summary = df[target_column].agg(['count', 'sum', 'mean']).to_dict()
        summaries.append({
            "Column": target_column,
            "Ishikawa": "Target",
            "Value": target_summary["mean"],
            "Measure": "mean",
            "Correlation to target": 1.0  # Correlation with itself is 1
        })

        summary_df = pd.DataFrame(summaries)
        summary_df.to_csv(SUMMARY_CSV, index=False)

        return f"Summary saved to {SUMMARY_CSV}"

    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")
def open_power_bi(template_path):
    """Opens Power BI template without blocking the Tkinter app."""
    try:
        if os.name == "nt":
            subprocess.Popen(["start", "", template_path], shell=True)
        else:
            subprocess.Popen(["open", template_path])
    except Exception as e:
        print(f"Error opening Power BI: {e}")