import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from . import home_page

def show_guide_page(main_frame):
    """Displays the Ishikawa guide pages."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create the guide pages
    guide_pages = [
        {
            "title": "Understanding Root Cause Analysis (RCA)",
            "text": """
            Root Cause Analysis (RCA) is a systematic approach to identifying the underlying causes of problems or events. 
            Instead of just addressing the symptoms, RCA delves deeper to understand why the issue occurred and prevent it from happening again.

            Key benefits:

            - Prevents recurring problems.
            - Improves problem-solving abilities.
            - Enhances decision-making.
            - Increases efficiency and productivity.
            - Reduces costs associated with recurring issues.

            Our Ishikawa tool will help you systematically investigate and document the root causes of problems you encounter, 
            whether in manufacturing, service delivery, or any other area.
            """
        },
        {
            "title": "The Ishikawa Diagram in RCA",
            "text": """
            The Ishikawa diagram, also known as the fishbone diagram or cause-and-effect diagram, is a visual tool for brainstorming 
            and organizing potential causes of a problem.

            Benefits of using the Ishikawa diagram:

            - Provides a clear visual representation of cause-and-effect relationships.
            - Helps identify root causes by exploring different categories of potential causes.
            - Facilitates team participation and brainstorming.

            Our tool provides a digital canvas for creating Ishikawa diagrams, allowing you to easily add, edit, and organize causes and categories.
            """
        },
        {
            "title": "Steps in RCA with the Ishikawa Diagram",
            "text": """
            Steps involved in using the Ishikawa diagram for RCA:

            1. **Define the Problem:** Clearly state the problem and its impact.
            2. **Identify Major Categories:** Determine the main categories of potential causes (e.g., 6Ms, or categories specific to the problem domain).
            3. **Brainstorm Potential Causes:** For each category, brainstorm possible causes that could contribute to the problem.
            4. **Analyze and Prioritize:** Discuss and analyze the causes to identify the most likely root causes.
            5. **Develop Solutions:** Generate potential solutions to address the root causes.
            6. **Implement and Monitor:** Put the chosen solutions into action and track their effectiveness.

            Our tool guides you through each step of the RCA process, providing prompts and templates to help you define the problem, 
            categorize causes, and develop solutions.
            """
        },
        {
            "title": "Steps to do RCA with our tool",
            "text": """
            1. **Define the problem:** Clearly articulate the problem you're trying to solve and identify the target variable.
            2. **Categorize:** Use the tool to categorize potential causes into relevant categories (e.g., the 6Ms).
            3. **Choose relevant metrics:** Select appropriate metrics to measure the impact of each category and potential cause on the target variable.
            4. **Monitor using Power BI:** Integrate the tool's output with Power BI to visualize and monitor the relationships between causes and the target variable.
            5. **Analyze and improve:** Observe how changes in the independent variables affect the target variable, identify root causes, and develop solutions.
            """
        },
        {
            "title": "Tips for Effective RCA with the Ishikawa Diagram",
            "text": """
            Tips for using the Ishikawa diagram effectively:

            - Involve a cross-functional team to get diverse perspectives.
            - Use data and evidence to support the analysis.
            - Don't stop at the first identified cause; keep asking "why" to get to the root cause.
            - Consider using other RCA tools in conjunction with the Ishikawa diagram (e.g., 5 Whys, Pareto analysis).

            Our tool allows you to collaborate with team members, attach data and evidence to your diagram, and export your analysis for use in other RCA tools.
            """
        }
    ]

    current_page_num = 0

    def show_guide_page(page_num):
        nonlocal current_page_num
        current_page_num = page_num
        for widget in main_frame.winfo_children():
            widget.destroy()

        page_data = guide_pages[page_num]

        # Title Label
        title_label = ttk.Label(main_frame, text=page_data["title"], justify="center", style="Black.TLabel", font=("Arial", 30, "bold"))
        title_label.pack(pady=10)

        # Text Label
        text_label = ttk.Label(main_frame, text=page_data["text"], justify="left", style="Black.TLabel", font=("Arial", 20))
        text_label.pack(pady=10, fill=tk.X)

        # Button frame for navigation
        button_frame = ttk.Frame(main_frame, style="Black.TFrame")
        button_frame.pack(pady=10, fill='x', expand=False, side=tk.BOTTOM)

        if page_num > 0:
            ttk.Button(button_frame, text="Previous", command=lambda: show_guide_page(page_num - 1), style="Black.TButton").pack(side=tk.LEFT, padx=5)
        if page_num < len(guide_pages) - 1:
            ttk.Button(button_frame, text="Next", command=lambda: show_guide_page(page_num + 1), style="Black.TButton").pack(side=tk.RIGHT, padx=5)
        else:
            ttk.Button(button_frame, text="Home", command=lambda: home_page.show_home_page(main_frame), style="Black.TButton").pack(side=tk.RIGHT, padx=5)

    # Show the first guide page initially
    show_guide_page(0)