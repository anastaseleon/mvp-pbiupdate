import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend
from. import summary_page
from. import home_page  # Import home_page

def show_categorization_page(main_frame, file_path=None):
    """Displays the categorization page."""
    if not file_path:
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if not file_path:
            return

    try:
        df_columns = backend.get_csv_columns(file_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return

    for widget in main_frame.winfo_children():
        widget.destroy()

    ttk.Label(main_frame, text="Map columns to Ishikawa categories:").pack(pady=10)

    column_mappings = {}
    for col in df_columns:
        frame = ttk.Frame(main_frame)
        frame.pack(pady=5)
        ttk.Label(frame, text=col, width=20, anchor="w").pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES, width=25)
        combo.pack(side=tk.RIGHT)
        combo.current(0)
        column_mappings[col] = combo

    # Target column selection
    target_frame = ttk.Frame(main_frame)
    target_frame.pack(pady=5)
    ttk.Label(target_frame, text="Target Column:", width=20, anchor="w").pack(side=tk.LEFT)
    target_combo = ttk.Combobox(target_frame, values=df_columns, width=25)
    target_combo.pack(side=tk.RIGHT)
    if df_columns:
        target_combo.current(0)

    # Button frame for Back and Next buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.pack(pady=10, fill='x', expand=False)

    # Back button (goes back to home page)
    back_button = ttk.Button(button_frame, text="Back", command=lambda: home_page.show_home_page(main_frame))  # Call home_page.show_home_page
    back_button.pack(side=tk.LEFT, padx=5)

    # Next button
    next_button = ttk.Button(button_frame, text="Next", command=lambda: summary_page.save_and_show_summary(main_frame, file_path, column_mappings, target_combo))
    next_button.pack(side=tk.RIGHT, padx=5)