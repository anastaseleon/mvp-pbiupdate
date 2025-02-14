import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend
import pyperclip  # For clipboard functionality

# Constants
POWER_BI_TEMPLATE = "template.pbit"

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        try:
            df_columns = backend.get_csv_columns(file_path)
            show_categorization_page(file_path, df_columns)
        except Exception as e:
            messagebox.showerror("Error", str(e))

def show_categorization_page(file_path, df_columns):
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Categorization page content
    instructions_label = tk.Label(main_frame, text="Map columns to Ishikawa categories:")
    instructions_label.pack(pady=10)

    column_frames = {}
    for col in df_columns:
        frame = tk.Frame(main_frame)
        frame.pack(pady=5)
        label = tk.Label(frame, text=col, width=20, anchor="w")
        label.pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES, width=25)
        combo.pack(side=tk.RIGHT)
        combo.current(0)
        column_frames[col] = frame

    target_frame = tk.Frame(main_frame)
    target_frame.pack(pady=5)
    target_label = tk.Label(target_frame, text="Target Column:", width=20, anchor="w")
    target_label.pack(side=tk.LEFT)
    target_combo = ttk.Combobox(target_frame, values=df_columns, width=25)
    target_combo.pack(side=tk.RIGHT)
    if df_columns:
        target_combo.current(0)

    next_button = tk.Button(main_frame, text="Next", command=lambda: save_and_show_summary(file_path, column_frames, target_combo))
    next_button.pack(pady=10)

def save_and_show_summary(file_path, column_frames, target_combo):
    mappings = {}
    for col, frame in column_frames.items():
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Combobox):
                mappings[col] = widget.get()
                break

    try:
        target_column = target_combo.get()
        message = backend.process_data(file_path, mappings, target_column)

        # Clear the main frame
        for widget in main_frame.winfo_children():
            widget.destroy()

        # Summary page content
        summary_label = tk.Label(main_frame, text=message)
        summary_label.pack(pady=10)

        db_path_label = tk.Label(main_frame, text=f"Database Path: {backend.DB_PATH}")
        db_path_label.pack()

        # Copy button for the database path
        copy_button = tk.Button(main_frame, text="Copy Path", command=lambda: pyperclip.copy(backend.DB_PATH))
        copy_button.pack(pady=10)

        open_pbi_button = tk.Button(main_frame, text="Open Power BI", command=lambda: backend.open_power_bi(POWER_BI_TEMPLATE))
        open_pbi_button.pack()

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
    title_label = tk.Label(main_frame, text="Ishikawa Diagram Generator", font=("Arial", 16))
    title_label.pack(pady=(0, 10))

    instructions_label = tk.Label(main_frame, text="Upload your CSV data to map columns to Ishikawa categories.")
    instructions_label.pack(pady=(0, 20))

    btn_upload = tk.Button(main_frame, text="Upload Data", command=open_file)
    btn_upload.pack()

    root.mainloop()