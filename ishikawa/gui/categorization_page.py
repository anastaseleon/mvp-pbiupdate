import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import backend
from . import summary_page
from . import home_page
import styles  # Import the styles module

def show_categorization_page(main_frame, file_path=None):
    """Displays the categorization page."""
    if not file_path:
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers CSV", "*.csv")])
        if not file_path:
            return

    try:
        df_columns = backend.get_csv_columns(file_path)
    except Exception as e:
        messagebox.showerror("Erreur", str(e))
        return

    for widget in main_frame.winfo_children():
        widget.destroy()

    ttk.Label(main_frame, text="Associer les colonnes aux catégories d'Ishikawa et sélectionner les mesures:", style="Black.TLabel", font=("Times New Roman", 30)).pack(pady=10)

    column_mappings = {}
    measures = {}
    categorical_handling = {} #added
    for col in df_columns:
        frame = ttk.Frame(main_frame, style="Black.TFrame")
        frame.pack(pady=5)
        ttk.Label(frame, text=col, width=20, anchor="w", style="Black.TLabel", font=("Times New Roman", 20)).pack(side=tk.LEFT)
        combo = ttk.Combobox(frame, values=backend.CATEGORIES, width=20)
        combo.pack(side=tk.LEFT, padx=(0, 10))
        combo.current(0)
        column_mappings[col] = combo

        measure_combo = ttk.Combobox(frame, values=backend.MEASURES, width=15)
        measure_combo.pack(side=tk.LEFT)
        measure_combo.current(0)
        measures[col] = measure_combo

        # Categorical handling combobox
        cat_handling_combo = ttk.Combobox(frame, values=["One-Hot", "Label", "Target", "Frequency", "None"], width=15) #added none option
        cat_handling_combo.pack(side=tk.LEFT)
        cat_handling_combo.current(0)  # Default to One-Hot encoding
        categorical_handling[col] = cat_handling_combo

    target_frame = ttk.Frame(main_frame, style="Black.TFrame")
    target_frame.pack(pady=5)
    ttk.Label(target_frame, text="Colonne Cible:", width=20, anchor="w", style="Black.TLabel").pack(side=tk.LEFT)
    target_combo = ttk.Combobox(target_frame, values=df_columns, width=25)
    target_combo.pack(side=tk.RIGHT)
    if df_columns:
        target_combo.current(0)

    button_frame = ttk.Frame(main_frame, style="Black.TFrame")
    button_frame.pack(pady=10, fill='x', expand=False)
    back_button = ttk.Button(button_frame, text="Retour", command=lambda: home_page.show_home_page(main_frame), style="Black.TButton")
    back_button.pack(side=tk.LEFT, padx=5)
    next_button = ttk.Button(button_frame, text="Suivant", command=lambda: summary_page.save_and_show_summary(main_frame, file_path, column_mappings, target_combo, measures, categorical_handling), style="Black.TButton") #modified
    next_button.pack(side=tk.RIGHT, padx=5)