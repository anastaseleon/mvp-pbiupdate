import tkinter as tk
from tkinter import ttk
import styles
import gui.home_page as home_page
import gui.categorization_page as categorization_page
import gui.summary_page as summary_page
import gui.ishikawa_guide as ishikawa_guide
import gui.upload as upload

def create_gui(root):
    """Sets up the main GUI elements and navigation."""
    global main_frame
    main_frame = ttk.Frame(root, style="Black.TFrame")
    main_frame.pack(expand=True, padx=20, pady=20)

    # Navigation frame
    nav_frame = ttk.Frame(root, style="Black.TFrame")
    nav_frame.pack(side="top", fill=tk.X, padx=5)  # Pack at the top and fill horizontally

    # Navigation buttons
    ttk.Button(nav_frame, text="Home", command=lambda: home_page.show_home_page(main_frame), style="Black.TButton").pack(side=tk.LEFT, padx=5)
    ttk.Button(nav_frame, text="Ishikawa Guide", command=lambda: ishikawa_guide.show_guide_page(main_frame), style="Black.TButton").pack(side=tk.LEFT, padx=5)

    # Show the Ishikawa guide initially
    ishikawa_guide.show_guide_page(main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ishikawa Analyzer")
    root.geometry("1800x1200")
    root.configure(bg="#1e1e1e")
    styles.configure_styles()
    create_gui(root)
    root.mainloop()