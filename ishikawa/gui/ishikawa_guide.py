import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk  # Import for image handling
from . import home_page

def show_guide_page(main_frame):
    """Displays the Ishikawa guide pages."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create the guide pages (example with 5 pages)
    guide_pages = [
        {
            "text": """
        ## Ishikawa (Fishbone) Diagram Guide - Page 1

        The Ishikawa diagram, also known as the fishbone diagram or cause-and-effect diagram, is a visual tool used to identify and organize the potential causes of a problem.
        """,
        "image": "imagepage1.png"  # Path to the image for this page
        },
        {
            "text":"""
        ## Ishikawa (Fishbone) Diagram Guide - Page 2

        ### Steps:

        1. **Identify the problem:** Clearly define the problem you want to analyze.
        2. **Identify the major categories:** Determine the main categories of causes (e.g., Materials, Methods, Machines, Manpower, Environment, Measurement).
        """,
        "image": "imagepage1.png"  # Path to the image for this page
        },
        {
            "text":
        """
        ## Ishikawa (Fishbone) Diagram Guide - Page 3

        3. **Brainstorm potential causes:** For each category, brainstorm possible causes that could contribute to the problem.
        4. **Analyze and prioritize:** Discuss and analyze the causes to identify the most likely root causes.
        ""","image": "imagepage1.png"  # Path to the image for this page
        },
        {
            "text":"""
        ## Ishikawa (Fishbone) Diagram Guide - Page 4

        5. **Take action:** Develop action plans to address the root causes.
        ""","image": "imagepage1.png"  # Path to the image for this page
        },
        {
            "text":"""
        ## Ishikawa (Fishbone) Diagram Guide - Page 5

        ### Example:

        **Problem:** High defect rate in manufacturing.

        **Categories:**
        * Materials
        * Methods
        * Machines
        * Manpower
        * Environment

        **Potential Causes:**
        * **Materials:** Poor quality raw materials, inconsistent supplier quality.
        * **Methods:** Inadequate training, outdated procedures.
        * **Machines:** Equipment malfunction, lack of maintenance.
        * **Manpower:** Operator error, lack of experience.
        * **Environment:** Temperature fluctuations, poor lighting.
        ""","image": "imagepage1.png"  # Path to the image for this page
        }
    ]

    current_page_num = 0

    def show_guide_page(page_num):
        nonlocal current_page_num
        current_page_num = page_num
        for widget in main_frame.winfo_children():
            widget.destroy()

        page_data = guide_pages[page_num]

        # Text Label
        text_label = ttk.Label(main_frame, text=page_data["text"], justify="left")
        text_label.pack(pady=10, fill=tk.X) # Fill horizontally

        # Image Label (if an image is specified)
        if page_data.get("image"):  # Use get to handle missing images gracefully
            try:
                image = Image.open(page_data["image"])
                # Resize the image if necessary
                image = image.resize((400, 300), Image.LANCZOS) #Example size
                photo = ImageTk.PhotoImage(image)
                image_label = ttk.Label(main_frame, image=photo)
                image_label.image = photo  # Keep a reference to prevent garbage collection
                image_label.pack(pady=5)
            except FileNotFoundError:
                print(f"Error: Image file not found: {page_data['image']}")
                error_label = ttk.Label(main_frame, text=f"Image not found: {page_data['image']}", foreground="red")
                error_label.pack()
            except Exception as e:
                print(f"Error loading image: {e}")
                error_label = ttk.Label(main_frame, text=f"Error loading image", foreground="red")
                error_label.pack()

        # Button frame for navigation
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10, fill='x', expand=False)

        if page_num > 0:
            ttk.Button(button_frame, text="Previous", command=lambda: show_guide_page(page_num - 1)).pack(side=tk.LEFT, padx=5)
        if page_num < len(guide_pages) - 1:
            ttk.Button(button_frame, text="Next", command=lambda: show_guide_page(page_num + 1)).pack(side=tk.RIGHT, padx=5)
        else:
            ttk.Button(button_frame, text="Home", command=lambda: home_page.show_home_page(main_frame)).pack(side=tk.RIGHT, padx=5)

    # Show the first guide page initially
    show_guide_page(0)