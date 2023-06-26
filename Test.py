import tkinter as tk
from tkinter import filedialog
import pandas as pd
import openpyxl
from tabulate import tabulate

root = tk.Tk()
root.withdraw()

print("Select Dataset in CSV Or Excel Format")
path2urExcel = filedialog.askopenfilename(title="Select the desired excel file")

try:
    data = pd.read_csv(path2urExcel)
except:
    try:
        sheet_name = str(input("Enter sheet name:  \n"))
        data = pd.read_excel(open(path2urExcel, 'rb'), sheet_name=sheet_name)
    except:
        print("Invalid format")

print(tabulate(data, headers = 'keys', tablefmt = 'psql'))

