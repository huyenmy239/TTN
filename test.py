import tkinter as tk
from customtkinter import *

class EditableTable:
    def __init__(self, root, rows, columns):
        self.root = root
        self.rows = rows
        self.columns = columns
        self.table = []

        # Create table structure
        for i in range(rows):
            row = []
            for j in range(columns):
                cell = CTkEntry(root, width=10, font=('Arial', 12))
                cell.grid(row=i, column=j, sticky="nsew")
                row.append(cell)
            self.table.append(row)

        # Configure grid weights to make cells expandable
        for i in range(rows):
            root.grid_rowconfigure(i, weight=1)
        for j in range(columns):
            root.grid_columnconfigure(j, weight=1)

    def get(self):
        """
        Retrieve the data from the table.
        """
        data = []
        for i in range(self.rows):
            row_data = []
            for j in range(self.columns):
                value = self.table[i][j].get()
                row_data.append(value)
            data.append(row_data)
        return data

    def set(self, data):
        """
        Set the data into the table.
        :param data: A list of lists containing the data.
        """
        for i in range(self.rows):
            for j in range(self.columns):
                self.table[i][j].delete(0, tk.END)  # Clear previous value
                self.table[i][j].insert(0, data[i][j])

# Create a tkinter window
root = tk.Tk()
root.title("Editable Table")

# Define table dimensions
rows = 5
columns = 3

# Create an editable table
table = EditableTable(root, rows, columns)

# Example: Set some initial data
initial_data = [
    ["A1", "B1", "C1"],
    ["A2", "B2", "C2"],
    ["A3", "B3", "C3"],
    ["A4", "B4", "C4"],
    ["A5", "B5", "C5"]
]
table.set(initial_data)

# Example: Function to retrieve data from the table
def get_data():
    data = table.get()
    print("Table data:")
    for row in data:
        print(row)

# Example: Button to retrieve data
btn_get_data = tk.Button(root, text="Get Data", command=get_data)
btn_get_data.grid(row=rows+1, columnspan=columns)

root.mainloop()
