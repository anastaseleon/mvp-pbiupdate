import tkinter as tk
from tkinter import ttk

# Import the necessary modules from the gui package
import gui.home_page as home_page
import gui.categorization_page as categorization_page
import gui.summary_page as summary_page

def create_gui(root):
    """Sets up the main GUI elements and navigation."""
    global main_frame  # Make main_frame accessible globally
    main_frame = ttk.Frame(root)
    main_frame.pack(expand=True, padx=20, pady=20)

    # Navigation frame
    nav_frame = ttk.Frame(root)
    nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

    # Navigation buttons
    ttk.Button(nav_frame, text="Home", command=lambda: home_page.show_home_page(main_frame)).pack(pady=5)
    ttk.Button(nav_frame, text="Categorization", command=lambda: categorization_page.show_categorization_page(main_frame)).pack(pady=5)

    # Show the home page initially
    home_page.show_home_page(main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ishikawa Analyzer")
    root.geometry("800x500")
    create_gui(root)
    root.mainloop()