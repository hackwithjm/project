import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(event):
    current_text = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "=":
        evaluate_expression()
    else:
        entry.insert(tk.END, button_text)

# Create the main window
window = tk.Tk()
window.title("Unique Calculator")

# Create an entry field for input
entry = tk.Entry(window, font=("Arial", 18))
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operators
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button_text in button_texts:
    button = tk.Button(window, text=button_text, font=("Arial", 18), padx=20, pady=20)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

window.mainloop()
