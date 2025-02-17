from tkinter import ttk
from. import categorization_page  # Import from the same directory

def show_home_page(main_frame):
    """Displays the initial home page."""
    for widget in main_frame.winfo_children():
        widget.destroy()
    ttk.Label(main_frame, text="Ishikawa Diagram Generator", font=("Arial", 16)).pack(pady=(0, 10))
    ttk.Label(main_frame, text="Upload your CSV data to map columns to Ishikawa categories.").pack(pady=(0, 20))
    ttk.Button(main_frame, text="Upload Data", command=lambda: categorization_page.show_categorization_page(main_frame)).pack()