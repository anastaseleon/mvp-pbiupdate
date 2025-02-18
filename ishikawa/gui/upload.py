import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend
from. import categorization_page

def show_upload_page(main_frame):
    """Displays the upload page."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Upload page content
    ttk.Label(main_frame, text="Upload your CSV data file.").pack(pady=10)

    def upload_file():
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                df_columns = backend.get_csv_columns(file_path)
                categorization_page.show_categorization_page(main_frame, file_path, df_columns)
            except Exception as e:
                messagebox.showerror("Error", str(e))

    ttk.Button(main_frame, text="Upload Data", command=upload_file).pack()