from tkinter import ttk

def configure_styles():
    """Configures the styles for the application."""
    style = ttk.Style()
    style.theme_use('clam')

    # Configure styles for different widgets
    style.configure("Black.TFrame", background="#1e1e1e")
    style.configure("Black.TLabel", background="#1e1e1e", foreground="white")
    style.configure("Black.TButton", background="black", foreground="white")

    # Additional styles for a modern look
    style.configure("Modern.TButton",
                    background="#2196F3",  # Blue background
                    foreground="white",
                    font=("Arial", 12),
                    borderwidth=0,  # Remove default border
                    relief="flat",  # Flat button appearance
                    padding=10)

    style.map("Modern.TButton",
              background=[('active', '#1976D2')],  # Darker blue on hover
              foreground=[('active', 'white')])

    style.configure("Modern.TLabel",
                    background="black",
                    foreground="white",
                    font=("Arial", 14),
                    padding=10)

    style.configure("Modern.TEntry",
                    fieldbackground="#f0f0f0",  # Light gray background for entry fields
                    foreground="black",
                    font=("Arial", 12),
                    borderwidth=1,
                    relief="solid")

    style.configure("Modern.TCombobox",
                    fieldbackground="#f0f0f0",  # Light gray background for comboboxes
                    foreground="black",
                    font=("Arial", 12),
                    arrowsize=20)  # Larger arrow size

    # Add more styles for other widgets as needed