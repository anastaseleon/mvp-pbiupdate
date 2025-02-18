import tkinter as tk
from tkinter import ttk
from. import categorization_page

def show_home_page(main_frame):
    """Displays the initial home page."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create a frame for the home page content
    home_frame = ttk.Frame(main_frame)
    home_frame.pack(expand=True)

    # Title label
    ttk.Label(home_frame, text="Ishikawa Diagram Generator", font=("Arial", 24)).pack(pady=20)

    # Description label
    description_label = ttk.Label(home_frame, text="This tool helps you create Ishikawa diagrams for root cause analysis.", wraplength=500)
    description_label.pack(pady=10)

    # Button to start the process
    start_button = ttk.Button(home_frame, text="Start Analysis", command=lambda: categorization_page.show_categorization_page(main_frame))
    start_button.pack(pady=20)