import tkinter as tk
from tkinter import ttk

def show_guide_page(main_frame):
    """Displays the Ishikawa guide pages."""
    # Clear the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create the guide pages (example with two pages)
    guide_pages = [
        """
        ## Ishikawa (Fishbone) Diagram Guide

        The Ishikawa diagram, also known as the fishbone diagram or cause-and-effect diagram, is a visual tool used to identify and organize the potential causes of a problem.

        ### Steps:

        1. **Identify the problem:** Clearly define the problem you want to analyze.
        2. **Identify the major categories:** Determine the main categories of causes (e.g., Materials, Methods, Machines, Manpower, Environment, Measurement).
        3. **Brainstorm potential causes:** For each category, brainstorm possible causes that could contribute to the problem.
        4. **Analyze and prioritize:** Discuss and analyze the causes to identify the most likely root causes.
        5. **Take action:** Develop action plans to address the root causes.
        """,
        """
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
        """
    ]

    # Function to switch between guide pages
    def show_guide_page(page_num):
        for widget in main_frame.winfo_children():
            widget.destroy()
        ttk.Label(main_frame, text=guide_pages[page_num], justify="left").pack(pady=10)

        # Button frame for navigation
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=10, fill='x', expand=False)

        if page_num > 0:
            ttk.Button(button_frame, text="Previous", command=lambda: show_guide_page(page_num - 1)).pack(side=tk.LEFT, padx=5)
        if page_num < len(guide_pages) - 1:
            ttk.Button(button_frame, text="Next", command=lambda: show_guide_page(page_num + 1)).pack(side=tk.RIGHT, padx=5)

    # Show the first guide page initially
    show_guide_page(0)