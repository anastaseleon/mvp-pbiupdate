import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend
import pyperclip  # For clipboard functionality

# Constants
POWER_BI_TEMPLATE = "template.pbit"

def open_file():
    """Opens a file dialog for CSV selection and proceeds to categorization."""
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df_columns = backend.get_csv_columns(file_path)
            show_categorization_page(file_path, df_columns)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def show_categorization_page(file_path, df_columns):
    """Displays the categorization page where users map columns to Ishikawa categories."""
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Categorization page content
    tk.Label(main_frame, text="Map columns to Ishikawa categories:").pack(pady=10)

    column_mappings = {}
    for col in df_columns:
        frame = tk.Frame(main_frame)
        frame.pack(pady=5)
        tk.Label(frame, text=col, width=20, anchor="w").pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES, width=25)
        combo.pack(side=tk.RIGHT)
        combo.current(0)
        column_mappings[col] = combo

    # Target column selection
    target_frame = tk.Frame(main_frame)
    target_frame.pack(pady=5)
    tk.Label(target_frame, text="Target Column:", width=20, anchor="w").pack(side=tk.LEFT)
    target_combo = ttk.Combobox(target_frame, values=df_columns, width=25)
    target_combo.pack(side=tk.RIGHT)
    if df_columns:
        target_combo.current(0)

    # Next button
    tk.Button(main_frame, text="Next", command=lambda: save_and_show_summary(file_path, column_mappings, target_combo)).pack(pady=10)

def save_and_show_summary(file_path, column_mappings, target_combo):
    """Processes the data and displays the summary page."""
    mappings = {col: combo.get() for col, combo in column_mappings.items()}
    target_column = target_combo.get()

    try:
        message = backend.process_data(file_path, mappings, target_column)

        # Clear the main frame
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Summary page content
        tk.Label(main_frame, text=message).pack(pady=10)

        # Show the path of the summary CSV file
        csv_label_text = f"Summary File: {backend.SUMMARY_CSV}"
        tk.Label(main_frame, text=csv_label_text, wraplength=500).pack()

        # Copy button for the CSV file path
        tk.Button(main_frame, text="Copy Path", command=lambda: pyperclip.copy(backend.SUMMARY_CSV)).pack(pady=10)

        # Open Power BI button
        tk.Button(main_frame, text="Open Power BI", command=lambda: backend.open_power_bi(POWER_BI_TEMPLATE)).pack()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main Application Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ishikawa Analyzer")
    root.geometry("600x400")

    # Main frame to hold the content
    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, padx=20, pady=20)

    # Initial page content
    tk.Label(main_frame, text="Ishikawa Diagram Generator", font=("Arial", 16)).pack(pady=(0, 10))
    tk.Label(main_frame, text="Upload your CSV data to map columns to Ishikawa categories.").pack(pady=(0, 20))

    tk.Button(main_frame, text="Upload Data", command=open_file).pack()

    root.mainloop()
