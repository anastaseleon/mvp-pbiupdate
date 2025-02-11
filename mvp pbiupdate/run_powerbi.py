import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend

# Constants
POWER_BI_TEMPLATE = "template.pbix"

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if file_path:
        open_categorization_window(file_path)

def open_categorization_window(file_path):
    try:
        df_columns = backend.get_csv_columns(file_path)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return  # Exit if getting columns fails

    window2 = tk.Toplevel(root)
    window2.title("Map Columns to Ishikawa Categories")

    column_frames = {}  # Store frames for easy access

    for col in df_columns:
        frame = tk.Frame(window2)
        frame.pack()
        label = tk.Label(frame, text=col)
        label.pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES)
        combo.pack(side=tk.RIGHT)
        combo.current(0)  # Set the default value to the first item in the list
        column_frames[col] = frame

    target_frame = tk.Frame(window2)
    target_frame.pack()
    target_label = tk.Label(target_frame, text="Target Column:")
    target_label.pack(side=tk.LEFT)
    target_combo = ttk.Combobox(target_frame, values=df_columns)
    target_combo.pack(side=tk.RIGHT)
    if df_columns:
        target_combo.current(0)  # Set the default value to the first item in the list

    btn_save = tk.Button(window2, text="Save and Process", command=lambda: save_mapping(file_path, column_frames, target_combo))
    btn_save.pack()

def save_mapping(file_path, column_frames, target_combo):
    mappings = {}
    for col, frame in column_frames.items():
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Combobox):
                mappings[col] = widget.get()
                break  # Exit the inner loop once the combobox is found

    try:
        target_column = target_combo.get()
        summary_path = backend.process_data(file_path, mappings, target_column)
        messagebox.showinfo("Processing Complete", f"Summary saved at: {summary_path}")
        backend.open_power_bi(summary_path, POWER_BI_TEMPLATE)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def show_db_path():
    window3 = tk.Toplevel(root)
    window3.title("Database Path")
    db_label = tk.Label(window3, text=f"Database Path: {backend.DB_PATH}")
    db_label.pack()
    close_button = tk.Button(window3, text="Close", command=window3.destroy)
    close_button.pack()

# Main Application Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ishikawa Analyzer")
    btn_upload = tk.Button(root, text="Upload Data", command=open_file)
    btn_upload.pack()

    btn_db_path = tk.Button(root, text="Show Database Path", command=show_db_path)
    btn_db_path.pack()

    root.mainloop()