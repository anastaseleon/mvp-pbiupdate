import tkinter as tk
from tkinter import ttk
import gui.home_page as home_page
import gui.categorization_page as categorization_page
import gui.summary_page as summary_page
import gui.ishikawa_guide as ishikawa_guide
import gui.upload as upload

def create_gui(root):
    """Sets up the main GUI elements and navigation."""
    global main_frame
    main_frame = ttk.Frame(root)
    main_frame.pack(expand=True, padx=20, pady=20)

    # Navigation frame
    nav_frame = ttk.Frame(root)
    nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

    # Navigation buttons
    ttk.Button(nav_frame, text="Home", command=lambda: home_page.show_home_page(main_frame)).pack(pady=5)
    ttk.Button(nav_frame, text="Upload", command=lambda: upload.show_upload_page(main_frame)).pack(pady=5)
    ttk.Button(nav_frame, text="Ishikawa Guide", command=lambda: ishikawa_guide.show_guide_page(main_frame)).pack(pady=5)

    # Show the Ishikawa guide initially
    ishikawa_guide.show_guide_page(main_frame)

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    root.title("Ishikawa Analyzer")
    root.geometry("900x800")
    create_gui(root)
    root.mainloop()