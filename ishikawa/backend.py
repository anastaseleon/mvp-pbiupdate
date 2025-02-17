import os
import pandas as pd
import subprocess

# Constants
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # Get script directory
SUMMARY_CSV = os.path.join(SCRIPT_DIR, "ishikawa_summary.csv")  # Summary CSV path
CATEGORIES = ["Materials", "Methods", "Machines", "Manpower", "Environment", "Measurement", "Target"]  # Include "Target"

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

def process_data(file_path, mappings, target_column):
    """Processes the data, calculates correlations, and saves the summary to a CSV file."""
    try:
        df = pd.read_csv(file_path)

        summaries = []
        for col in df.columns:
            if col!= target_column:  # Exclude target column from correlation calculation
                summary = df[col].agg(['count', 'sum', 'mean']).to_dict()
                ishikawa_category = mappings.get(col, "Unknown")  # Default to "Unknown" if no mapping

                # Calculate correlation with target column (if numeric)
                if pd.api.types.is_numeric_dtype(df[col]):
                    correlation = df[col].corr(df[target_column])
                else:
                    correlation = None  # Cannot calculate correlation for non-numeric columns

                summaries.append({
                    "Column": col,
                    "Ishikawa": ishikawa_category,
                    "Count": summary["count"],
                    "Sum": summary["sum"],
                    "Mean": summary["mean"],
                    "Correlation": correlation  # Add correlation to the summary
                })

        # Add the target column summary
        target_summary = df[target_column].agg(['count', 'sum', 'mean']).to_dict()
        summaries.append({
            "Column": target_column,
            "Ishikawa": "Target",
            "Count": target_summary["count"],
            "Sum": target_summary["sum"],
            "Mean": target_summary["mean"],
            "Correlation": 1.0  # Correlation with itself is 1
        })

        # Convert list to DataFrame and save as CSV
        summary_df = pd.DataFrame(summaries)
        summary_df.to_csv(SUMMARY_CSV, index=False)

        return f"Summary saved to {SUMMARY_CSV}"  # Return a success message

    except FileNotFoundError:
        raise FileNotFoundError("CSV file not found.")
    except pd.errors.ParserError:
        raise ValueError("Error parsing CSV file. Check format.")
    except Exception as e:
        raise Exception(f"An unexpected error occurred: {e}")

def open_power_bi(template_path):
    """Opens Power BI template without blocking the Tkinter app."""
    try:
        # Use 'start' (Windows) or 'open' (Mac) for non-blocking execution
        if os.name == "nt":  # Windows
            subprocess.Popen(["start", "", template_path], shell=True)
        else:  # macOS/Linux
            subprocess.Popen(["open", template_path])

    except Exception as e:
        print(f"Error opening Power BI: {e}")