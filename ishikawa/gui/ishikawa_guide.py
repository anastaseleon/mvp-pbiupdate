import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from . import home_page

def show_guide_page(main_frame):
    """Displays the Ishikawa guide pages."""
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Create the guide pages (example with 5 pages)
    guide_pages = [
        {
            "title": "Ishikawa (Fishbone) Diagram - Introduction",
            "text": """
            The Ishikawa diagram, also known as the fishbone diagram or cause-and-effect diagram, is a visual tool used to identify and organize the potential causes of a problem.

            Key benefits:

            - Provides a visual representation of the problem and its potential causes.
            - Helps to identify root causes rather than just symptoms.
            - Facilitates brainstorming and encourages team participation.
            - Can be used in various settings, from manufacturing to service industries.
            """
        },
        {
            "title": "Ishikawa Diagram and the DMAIC Framework",
            "text": """
            The DMAIC framework (Define, Measure, Analyze, Improve, Control) is a structured problem-solving approach often used in Six Sigma projects.
           It can be effectively integrated with the Ishikawa diagram to provide a comprehensive approach to problem-solving.

            How DMAIC complements the Ishikawa diagram:

            - Define: Clearly define the problem and project scope.
            - Measure: Collect data and establish metrics to track progress.
            - Analyze: Use the Ishikawa diagram to brainstorm and analyze potential causes.
            - Improve: Develop and implement solutions to address root causes.
            - Control: Monitor results, sustain improvements, and standardize processes.
            """,
            "image": "imagepage2.png"
        },
        {
            "title": "Ishikawa (Fishbone) Diagram - Define Phase",
            "text": """
            In the Define phase, you clearly articulate the problem you're trying to solve. This involves:

            - Problem Statement: Create a concise and specific problem statement.
            - Project Scope: Define the boundaries of your analysis.
            - Goals: Establish clear and measurable goals for the project.
            - Team: Identify the team members who will be involved in the analysis and improvement efforts.
            """
        },
        {
            "title": "Ishikawa (Fishbone) Diagram - Measure Phase",
            "text": """
            The Measure phase focuses on gathering data related to the problem. This includes:

            - Data Collection: Collect both quantitative and qualitative data.
            - Metrics: Develop key performance indicators (KPIs) to track progress.
            - Measurement System Analysis: Ensure the accuracy and reliability of your measurement system.
            """
        },
        {
            "title": "Ishikawa (Fishbone) Diagram - Analyze Phase",
            "text": """
            In the Analyze phase, you use the Ishikawa diagram to brainstorm and analyze potential causes:

            - Brainstorming: Generate a comprehensive list of potential causes.
            - Categorization: Group the causes into the 6M categories (or other relevant categories).
            - Prioritization: Identify the most likely root causes using data analysis and statistical tools.
            """
        },
        {
            "title": "Ishikawa (Fishbone) Diagram - Improve Phase",
            "text": """
            The Improve phase involves developing and implementing solutions to address the root causes:

            - Solution Generation: Brainstorm potential solutions.
            - Evaluation: Evaluate the potential solutions based on feasibility and effectiveness.
            - Implementation: Implement the chosen solutions, starting with pilot tests if possible.
            """
        },
        {
            "title": "Ishikawa (Fishbone) Diagram - Control Phase",
            "text": """
            The Control phase focuses on sustaining the improvements and preventing the problem from recurring:

            - Monitoring: Track the effectiveness of the solutions using KPIs.
            - Standardization: Update procedures and documentation to reflect the improved processes.
            - Control Mechanisms: Implement controls to ensure the improvements are maintained.
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

        # Title Label (formatted differently)
        title_label = ttk.Label(main_frame, text=page_data["title"], justify="center", style="Black.TLabel", font=("Arial", 18, "bold"))
        title_label.pack(pady=10)

        # Text Label
        text_label = ttk.Label(main_frame, text=page_data["text"], justify="left", style="Black.TLabel",font=("Arial", 15))
        text_label.pack(pady=10, fill=tk.X)

        # Image Label (if an image is specified)
        if page_data.get("image"):
            try:
                image = Image.open(page_data["image"])
                image = image.resize((400, 300), Image.LANCZOS)
                photo = ImageTk.PhotoImage(image)
                image_label = ttk.Label(main_frame, image=photo, style="Black.TLabel")
                image_label.image = photo
                image_label.pack(pady=5)
            except FileNotFoundError:
                print(f"Error: Image file not found: {page_data['image']}")
                error_label = ttk.Label(main_frame, text=f"Image not found: {page_data['image']}", foreground="red",
                                       style="Black.TLabel")
                error_label.pack()
            except Exception as e:
                print(f"Error loading image: {e}")
                error_label = ttk.Label(main_frame, text=f"Error loading image", foreground="red", style="Black.TLabel")
                error_label.pack()

        # Button frame for navigation
        button_frame = ttk.Frame(main_frame, style="Black.TFrame")
        button_frame.pack(pady=10, fill='x', expand=False, side=tk.BOTTOM)  # Pack at the bottom

        if page_num > 0:
            ttk.Button(button_frame, text="Previous", command=lambda: show_guide_page(page_num - 1),
                       style="Black.TButton").pack(side=tk.LEFT, padx=5)
        if page_num < len(guide_pages) - 1:
            ttk.Button(button_frame, text="Next", command=lambda: show_guide_page(page_num + 1),
                       style="Black.TButton").pack(side=tk.RIGHT, padx=5)
        else:
            ttk.Button(button_frame, text="Home", command=lambda: home_page.show_home_page(main_frame),
                       style="Black.TButton").pack(side=tk.RIGHT, padx=5)

    # Show the first guide page initially
    show_guide_page(0)