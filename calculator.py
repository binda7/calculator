import tkinter as tk
from keyboard import add_hotkey

calculation = ""


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


app = tk.Tk()
app.geometry("300x325")
app.title("Calculator")
text_result = tk.Text(app, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

buton_7 = tk.Button(app, text='7', command=lambda: add_to_calculation(
    7), width=5, font=("Arial", 14))
buton_7.grid(row=2, column=1)
buton_8 = tk.Button(app, text='8', command=lambda: add_to_calculation(
    8), width=5, font=("Arial", 14))
buton_8.grid(row=2, column=2)
buton_9 = tk.Button(app, text='9', command=lambda: add_to_calculation(
    9), width=5, font=("Arial", 14))
buton_9.grid(row=2, column=3)
buton_4 = tk.Button(app, text='4', command=lambda: add_to_calculation(
    4), width=5, font=("Arial", 14))
buton_4.grid(row=3, column=1)
buton_5 = tk.Button(app, text='5', command=lambda: add_to_calculation(
    5), width=5, font=("Arial", 14))
buton_5.grid(row=3, column=2)
buton_6 = tk.Button(app, text='6', command=lambda: add_to_calculation(
    6), width=5, font=("Arial", 14))
buton_6.grid(row=3, column=3)
buton_1 = tk.Button(app, text='1', command=lambda: add_to_calculation(
    1), width=5, font=("Arial", 14))
buton_1.grid(row=4, column=1)
buton_2 = tk.Button(app, text='2', command=lambda: add_to_calculation(
    2), width=5, font=("Arial", 14))
buton_2.grid(row=4, column=2)
buton_3 = tk.Button(app, text='3', command=lambda: add_to_calculation(
    3), width=5, font=("Arial", 14))
buton_3.grid(row=4, column=3)
buton_0 = tk.Button(app, text='0', command=lambda: add_to_calculation(
    0), width=5, font=("Arial", 14))
buton_0.grid(row=5, column=1)
buton_plus = tk.Button(
    app, text='+', command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
buton_plus.grid(row=3, column=4)
buton_minus = tk.Button(
    app, text='-', command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
buton_minus.grid(row=4, column=4)
buton_mul = tk.Button(
    app, text='*', command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
buton_mul.grid(row=5, column=4)
buton_div = tk.Button(
    app, text='/', command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
buton_div.grid(row=6, column=4)
buton_open = tk.Button(app, text='(', command=lambda: add_to_calculation(
    "("), width=5, font=("Arial", 14))
buton_open.grid(row=5, column=2)
buton_close = tk.Button(app, text=')', command=lambda: add_to_calculation(
    ")"), width=5, font=("Arial", 14))
buton_close.grid(row=5, column=3)
buton_power = tk.Button(app, text='x^y', command=lambda: add_to_calculation(
    "**"), width=5, font=("Arial", 14))
buton_power.grid(row=6, column=1)
buton_mod = tk.Button(app, text='Mod', command=lambda: add_to_calculation(
    "%"), width=5, font=("Arial", 14))
buton_mod.grid(row=6, column=2)
buton_divcal = tk.Button(app, text='//', command=lambda: add_to_calculation(
    "//"), width=5, font=("Arial", 14))
buton_divcal.grid(row=6, column=3)
buton_equals = tk.Button(
    app, text='=', command=evaluate_calculation, width=11, font=("Arial", 14))
buton_equals.grid(row=7, column=1, columnspan=4)
buton_clear = tk.Button(app, text='C', command=clear_field,
                        width=5, font=("Arial", 14))
buton_clear.grid(row=2, column=4, columnspan=2)

add_hotkey('+', buton_plus.invoke)
add_hotkey('shift+6', buton_power.invoke)
add_hotkey('-', buton_minus.invoke)
add_hotkey('*', buton_mul.invoke)
add_hotkey('/', buton_div.invoke)
add_hotkey('shift+5', buton_mod.invoke)
add_hotkey('1', buton_1.invoke)
add_hotkey('2', buton_2.invoke)
add_hotkey('3', buton_3.invoke)
add_hotkey('4', buton_4.invoke)
add_hotkey('5', buton_5.invoke)
add_hotkey('6', buton_6.invoke)
add_hotkey('7', buton_7.invoke)
add_hotkey('8', buton_8.invoke)
add_hotkey('9', buton_9.invoke)
add_hotkey('enter', buton_equals.invoke)
add_hotkey('backspace', buton_clear.invoke)

app.mainloop()
