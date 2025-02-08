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
    df_columns = backend.get_csv_columns(file_path)

    window2 = tk.Toplevel(root)
    window2.title("Map Columns to Ishikawa Categories")

    for col in df_columns:
        frame = tk.Frame(window2)
        frame.pack()
        label = tk.Label(frame, text=col)
        label.pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES)
        combo.pack(side=tk.RIGHT)
        combo.set(backend.CATEGORIES[0])

    def save_mapping():
        mappings = {}
        for frame in window2.winfo_children():
            if isinstance(frame, tk.Frame):
                label = frame.winfo_children()[0]
                combo = frame.winfo_children()[1]
                mappings[label.cget("text")] = combo.get()

        try:
            summary_path = backend.process_data(file_path, mappings)
            messagebox.showinfo("Processing Complete", f"Summary saved at: {summary_path}")
            backend.open_power_bi(summary_path, POWER_BI_TEMPLATE)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn_save = tk.Button(window2, text="Save and Process", command=save_mapping)
    btn_save.pack()


def show_db_path():
    window3 = tk.Toplevel(root)
    window3.title("Database Path")
    db_label = tk.Label(window3, text=f"Database Path: {backend.DB_PATH}")
    db_label.pack()
    # Add a close button if you want
    close_button = tk.Button(window3, text="Close", command=window3.destroy)
    close_button.pack()



# Main Application Setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ishikawa Analyzer")
    btn_upload = tk.Button(root, text="Upload Data", command=open_file)
    btn_upload.pack()

    btn_db_path = tk.Button(root, text="Show Database Path", command=show_db_path) # button to show db path
    btn_db_path.pack()

    root.mainloop()