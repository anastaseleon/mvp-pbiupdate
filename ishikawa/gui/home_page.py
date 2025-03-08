# -*- coding: utf-8 -*-
from tkinter import ttk
from . import categorization_page
import styles  # Import the styles module

def show_home_page(main_frame):
    """Displays the initial home page."""
    for widget in main_frame.winfo_children():
        widget.destroy()
    # Create a frame for the home page content
    home_frame = ttk.Frame(main_frame, style="Black.TFrame")
    home_frame.pack(expand=True)

    # Title label
    ttk.Label(home_frame, text="Générateur de Diagramme d'Ishikawa", font=("Times New Roman", 30), style="Black.TLabel").pack(pady=10)

    # Description label
    description_label = ttk.Label(home_frame, text="Cet outil vous aide à créer des diagrammes d'Ishikawa pour l'analyse des causes profondes.",
                                    wraplength=500, style="Black.TLabel", font=("Times New Roman", 20))
    description_label.pack(pady=10)

    # Button to start the process
    start_button = ttk.Button(home_frame, text="Démarrer l'Analyse",
                                command=lambda: categorization_page.show_categorization_page(main_frame), style="Black.TButton")
    start_button.pack(pady=20)