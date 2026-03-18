import tkinter as tk
window = tk.Tk()
window.title("Simple Caculator")
input = tk.Entry(window, width=20, borderwidth=5, font=("Arial",20))
input.grid(row=0, column=0, columnspan=3)
pos = 0
number1 = []
number2 = []

#Creating the "1" button
def button_1_click():
    global pos
    input.insert(pos, "1")
    pos += 1
    if "+" in number1:
        number2.append("1")
    elif "-" in number1:
        number2.append("1")
    elif "*" in number1:
        number2.append("1")
    elif "/" in number1:
        number2.append("1")
    else:
        number1.append("1")
button_1 = tk.Button(window, text="1", padx=50, pady=15, command=button_1_click)
button_1.grid(row=3, column=0)

#Creating the "2" button
def button_2_click():
    global pos
    input.insert(pos, "2")
    pos += 1
    if "+" in number1:
        number2.append("2")
    elif "-" in number1:
        number2.append("2")
    elif "*" in number1:
        number2.append("2")
    elif "/" in number1:
        number2.append("2")
    else:
        number1.append("2")
button_2 = tk.Button(window, text="2", padx=50, pady=15, command=button_2_click)
button_2.grid(row=3, column=1)

#Creating the "3" button
def button_3_click():
    global pos
    input.insert(pos, "3")
    pos += 1
    if "+" in number1:
        number2.append("3")
    elif "-" in number1:
        number2.append("3")
    elif "*" in number1:
        number2.append("3")
    elif "/" in number1:
        number2.append("3")
    else:
        number1.append("3")
button_3 = tk.Button(window, text="3", padx=49, pady=15, command=button_3_click)
button_3.grid(row=3, column=2)

#Creating the "4" button
def button_4_click():
    global pos
    input.insert(pos, "4")
    pos += 1
    if "+" in number1:
        number2.append("4")
    elif "-" in number1:
        number2.append("4")
    elif "*" in number1:
        number2.append("4")
    elif "/" in number1:
        number2.append("4")
    else:
        number1.append("4")
button_4 = tk.Button(window, text="4", padx=50, pady=15, command=button_4_click)
button_4.grid(row=2, column=0)

#Creating the "5" button
def button_5_click():
    global pos
    input.insert(pos, "5")
    pos += 1
    if "+" in number1:
        number2.append("5")
    elif "-" in number1:
        number2.append("5")
    elif "*" in number1:
        number2.append("5")
    elif "/" in number1:
        number2.append("5")
    else:
        number1.append("5")
button_5 = tk.Button(window, text="5", padx=50, pady=15, command=button_5_click)
button_5.grid(row=2, column=1)

#Creating the "6" button
def button_6_click():
    global pos
    input.insert(pos, "6")
    pos += 1
    if "+" in number1:
        number2.append("6")
    elif "-" in number1:
        number2.append("6")
    elif "*" in number1:
        number2.append("6")
    elif "/" in number1:
        number2.append("6")
    else:
        number1.append("6")
button_6 = tk.Button(window, text="6", padx=49, pady=15, command=button_6_click)
button_6.grid(row=2, column=2)

#Creating the "7" button
def button_7_click():
    global pos
    input.insert(pos, "7")
    pos += 1
    if "+" in number1:
        number2.append("7")
    elif "-" in number1:
        number2.append("7")
    elif "*" in number1:
        number2.append("7")
    elif "/" in number1:
        number2.append("7")
    else:
        number1.append("7")
button_7 = tk.Button(window, text="7", padx=50, pady=15, command=button_7_click)
button_7.grid(row=1, column=0)

#Creating the "8" button
def button_8_click():
    global pos
    input.insert(pos, "8")
    pos += 1
    if "+" in number1:
        number2.append("8")
    elif "-" in number1:
        number2.append("8")
    elif "*" in number1:
        number2.append("8")
    elif "/" in number1:
        number2.append("8")
    else:
        number1.append("8")
button_8 = tk.Button(window, text="8", padx=50, pady=15, command=button_8_click)
button_8.grid(row=1, column=1)

#Creating the "9" button
def button_9_click():
    global pos
    input.insert(pos, "9")
    pos += 1
    if "+" in number1:
        number2.append("9")
    elif "-" in number1:
        number2.append("9")
    elif "*" in number1:
        number2.append("9")
    elif "/" in number1:
        number2.append("9")
    else:
        number1.append("9")
button_9 = tk.Button(window, text="9", padx=49, pady=15, command=button_9_click)
button_9.grid(row=1, column=2)

#Creating the "0" button
def button_0_click():
    global pos
    input.insert(pos, "0")
    pos += 1
    if "+" in number1:
        number2.append("0")
    elif "-" in number1:
        number2.append("0")
    elif "*" in number1:
        number2.append("0")
    elif "/" in number1:
        number2.append("0")
    else:
        number1.append("0")
button_9 = tk.Button(window, text="0", padx=50, pady=15, command=button_0_click)
button_9.grid(row=4, column=0)

#Creating the "+" button
def button_plus_click():
    global pos
    input.insert(pos, "+")
    pos += 1
    number1.append("+")
button_plus = tk.Button(window, text="+", padx=49, pady=15, command=button_plus_click)
button_plus.grid(row=5, column=0)

#Creating the "-" button
def button_minus_click():
    global pos
    input.insert(pos, "-")
    pos += 1
    number1.append("-")
button_minus = tk.Button(window, text="-", padx=51, pady=15, command=button_minus_click)
button_minus.grid(row=6, column=0)

#Creating the "*" button
def button_multi_click():
    global pos
    input.insert(pos, "*")
    pos += 1
    number1.append("*")
button_multi = tk.Button(window, text="*", padx=51, pady=15, command=button_multi_click)
button_multi.grid(row=6, column=1)

#Creating the "/" button
def button_div_click():
    global pos
    input.insert(pos, "/")
    pos += 1
    number1.append("/")
button_div = tk.Button(window, text="/", padx=50, pady=15, command=button_div_click)
button_div.grid(row=6, column=2)

#Creating the "=" button
def button_equal_click():
    if "+" in number1:
        number1.remove("+")
        number1_1 = ''.join(number1)
        number1_1 = int(number1_1)
        number2_2 = ''.join(number2)
        number2_2 = int(number2_2)
        result = number1_1 + number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "-" in number1:
        number1.remove("-")
        number1_1 = ''.join(number1)
        number1_1 = int(number1_1)
        number2_2 = ''.join(number2)
        number2_2 = int(number2_2)
        result = number1_1 - number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "*" in number1:
        number1.remove("*")
        number1_1 = ''.join(number1)
        number1_1 = int(number1_1)
        number2_2 = ''.join(number2)
        number2_2 = int(number2_2)
        result = number1_1 * number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    elif "/" in number1:
        number1.remove("/")
        number1_1 = ''.join(number1)
        number1_1 = int(number1_1)
        number2_2 = ''.join(number2)
        number2_2 = int(number2_2)
        result = number1_1 / number2_2
        input.delete(0,pos)
        label = tk.Label(window, text = result, width=21, borderwidth=5, font=("Arial",20), bg = "Grey")
        label.grid(row=0, column=0, columnspan=3)
    def button_clear_click():
        label.destroy()
        number1.clear()
        number2.clear()
    button_clear = tk.Button(window, text="Clear", padx=97, pady=15, command=button_clear_click)
    button_clear.grid(row=4, column=1, columnspan=2)
button_equal = tk.Button(window, text="=", padx=107, pady=15, command=button_equal_click)
button_equal.grid(row=5, column=1, columnspan=2)

#Creating the "Clear" button
def button_clear_click():
    input.delete(0,pos)
button_clear = tk.Button(window, text="Clear", padx=97, pady=15, command=button_clear_click)
button_clear.grid(row=4, column=1, columnspan=2)

window.mainloop()