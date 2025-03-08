# -*- coding: utf-8 -*-
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
            "title": "Comprendre l'analyse des causes profondes (RCA)",
            "text": """
                L'analyse des causes profondes (RCA) est une approche systématique pour identifier les causes sous-jacentes des problèmes ou des événements.
                Au lieu de simplement traiter les symptômes, l'RCA approfondit pour comprendre pourquoi le problème est survenu et l'empêcher de se reproduire.

                Principaux avantages :

                - Empêche les problèmes récurrents.
                - Améliore les capacités de résolution de problèmes.
                - Améliore la prise de décision.
                - Augmente l'efficacité et la productivité.
                - Réduit les coûts associés aux problèmes récurrents.

                Notre outil Ishikawa vous aidera  à categoriser et quantifier les causes profondes des problèmes que vous rencontrez,
                que ce soit dans la fabrication, la prestation de services ou tout autre domaine.
                """
        },
        {
            "title": "Le diagramme d'Ishikawa dans l'RCA",
            "text": """
                Le diagramme d'Ishikawa, également connu sous le nom de diagramme en arêtes de poisson ou diagramme de cause à effet, est un outil visuel pour le brainstorming
                et l'organisation des causes potentielles d'un problème.

                Avantages de l'utilisation du diagramme d'Ishikawa :

                - Fournit une représentation visuelle claire des relations de cause à effet.
                - Aide à identifier les causes profondes en explorant différentes catégories de causes potentielles.
                - Facilite la participation et le brainstorming de l'équipe.

                Notre outil fournit un template Power BI pour la representation du diagrammes d'Ishikawa, vous permettant de suivre facilement les causes et les catégories.
                """
        },
        {
            "title": "Étapes de l'RCA avec le diagramme d'Ishikawa",
            "text": """
                Étapes impliquées dans l'utilisation du diagramme d'Ishikawa pour l'RCA :

                1. Définir le problème : Énoncez clairement le problème et son impact.
                2. Identifier les catégories principales : Déterminez les principales catégories de causes potentielles (par exemple, les 6M ou les catégories spécifiques au domaine du problème).
                3. Brainstorming des causes potentielles : Pour chaque catégorie, réfléchissez aux causes possibles qui pourraient contribuer au problème.
                4. Analyser et hiérRCAhiser : Discutez et analysez les causes pour identifier les causes profondes les plus probables.
                5. Élaborer des solutions : Générez des solutions potentielles pour traiter les causes profondes.
                6. Mettre en œuvre et surveiller : Mettez en œuvre les solutions choisies et suivez leur efficacité.

                Notre outil vous guide à travers chaque étape du processus RCA, en fournissant des invites et des modèles pour vous aider à définir le problème,
                catégoriser les causes et élaborer des solutions.
                """
        },
        {
            "title": "Étapes pour faire l'RCA avec notre outil",
            "text": """
                1. Définir le problème : Articulez clairement le problème que vous essayez de résoudre et identifiez la variable cible.
                2. Catégoriser : Utilisez l'outil pour classer les causes potentielles dans les catégories pertinentes (par exemple, les 6M).
                3. Choisir des mesures pertinentes : Sélectionnez les mesures appropriées pour évaluer l'impact de chaque catégorie et cause potentielle sur la variable cible.
                4. Surveiller avec Power BI : Intégrez la sortie de l'outil avec Power BI pour visualiser et surveiller les relations entre les causes et la variable cible.
                5. Analyser et améliorer : Observez comment les changements dans les variables indépendantes affectent la variable cible, identifiez les causes profondes et élaborez des solutions.
                """
        },
        {
            "title": "Conseils pour une RCA efficace avec le diagramme d'Ishikawa",
            "text": """
                Conseils pour utiliser efficacement le diagramme d'Ishikawa :

                - Impliquer une équipe interfonctionnelle pour obtenir des perspectives diverses.
                - Utiliser des données et des preuves pour étayer l'analyse.
                - Ne vous arrêtez pas à la première cause identifiée ; continuez à demander « pourquoi » pour arriver à la cause profonde.
                - Envisager d'utiliser d'autres outils RCA en conjonction avec le diagramme d'Ishikawa (par exemple, les 5 pourquoi, l'analyse de Pareto).

                Notre outil vous permet de collaborer avec les membres de l'équipe, de joindre des données et des preuves à votre diagramme et d'exporter votre analyse pour l'utiliser dans d'autres outils RCA.
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
            ttk.Button(button_frame, text="Précédent", command=lambda: show_guide_page(page_num - 1), style="Black.TButton").pack(side=tk.LEFT, padx=5)
        if page_num < len(guide_pages) - 1:
            ttk.Button(button_frame, text="Suivant", command=lambda: show_guide_page(page_num + 1), style="Black.TButton").pack(side=tk.RIGHT, padx=5)
        else:
            ttk.Button(button_frame, text="Accueil", command=lambda: home_page.show_home_page(main_frame), style="Black.TButton").pack(side=tk.RIGHT, padx=5)

    # Show the first guide page initially
    show_guide_page(0)