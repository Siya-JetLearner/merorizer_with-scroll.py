import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("ComboBox Example") 
root.geometry("300x200")


#Label
label = tk.Label(root, text="Choose a Course:") 
label.pack(pady=10)



# Combobox
courses = ["Python", "Java", "C++", "Data Science"]
combo = ttk.Combobox (root, values=courses) 
combo.pack()

# Set default text
combo.set("Select Course")

# Function to display selected option
def show_selection():
    print("Selected:", combo.get())


# Button
button = tk.Button(root, text="Submit", command=show_selection) 
button.pack(pady=10)



root.mainloop()