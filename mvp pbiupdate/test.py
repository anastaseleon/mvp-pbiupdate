import os
import sqlite3
import pandas as pd
import subprocess

path="./template.pbit"
def open_power_bi(pbix_path):
    try:
        subprocess.run(["pbixrefresher.exe", "--pbix", pbix_path, "--refresh"], check=True)
        print("Power BI report refreshed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error refreshing Power BI: {e}")