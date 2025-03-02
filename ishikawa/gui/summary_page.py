import tkinter as tk
from tkinter import messagebox, ttk
import backend
import pyperclip
from. import categorization_page
import styles  # Import the styles module

# Constants
POWER_BI_TEMPLATE = "template.pbit"

def save_and_show_summary(main_frame, file_path, column_mappings, target_combo, measures):
    """Processes the data and displays the summary page."""
    mappings = {col: combo.get() for col, combo in column_mappings.items()}
    target_column = target_combo.get()
    selected_measures = {col: combo.get() for col, combo in measures.items()}

    try:
        message = backend.process_data(file_path, mappings, target_column, selected_measures)

        # Clear the main frame
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Summary page content
        ttk.Label(main_frame, text=message, style="Black.TLabel").pack(pady=10)
        csv_label_text = f"Summary File: {backend.SUMMARY_CSV}"
        ttk.Label(main_frame, text=csv_label_text, wraplength=700, style="Black.TLabel").pack()
        ttk.Button(main_frame, text="Copy Path", command=lambda: pyperclip.copy(backend.SUMMARY_CSV), style="Black.TButton").pack(pady=10)
        ttk.Button(main_frame, text="Open Power BI", command=lambda: backend.open_power_bi(POWER_BI_TEMPLATE), style="Black.TButton").pack()

        # Button frame for Back and Finish buttons
        button_frame = ttk.Frame(main_frame, style="Black.TFrame")
        button_frame.pack(pady=10, fill='x', expand=False)

        # Back button (goes back to categorization)
        back_button = ttk.Button(button_frame, text="Back", command=lambda: categorization_page.show_categorization_page(main_frame, file_path), style="Black.TButton")
        back_button.pack(side=tk.LEFT, padx=5)

        # Finish button (closes the GUI)
        finish_button = ttk.Button(button_frame, text="Finish", command=main_frame.winfo_toplevel().destroy, style="Black.TButton")
        finish_button.pack(side=tk.RIGHT, padx=5)

    except Exception as e:
        messagebox.showerror("Error", str(e))