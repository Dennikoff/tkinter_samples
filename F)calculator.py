import tkinter as tk

operation = ''
first_val = 0


def add_digit(digit):
    entry.insert(tk.END, digit)

def add_operation(oper):
    global operation
    global first_val
    operation = oper
    first_val = entry.get()
    buttondel()



def buttonequal():
    global operation
    global first_val
    second_val = entry.get()
    entry.delete(0, tk.END)
    match operation:
        case '+':
            entry.insert(0, str(int(float(first_val) + float(second_val))))
        case '-':
            entry.insert(0, str(int(float(first_val) - float(second_val))))
        case '*':
            entry.insert(0, str(int(float(first_val) * float(second_val))))
        case '/':
            entry.insert(0, str(float(first_val) / float(second_val)))


def buttondel():
    entry.delete(0, tk.END)


def create_digit_button(text, col, row):
    button = tk.Button(text=text,relief=tk.RAISED, bd='5', command=lambda: add_digit(text))
    button.grid(column=col, row=row, sticky='nswe')
    return button

def create_operation_button(text, col, row):
    button = tk.Button(text=text,relief=tk.RAISED, bd='5', command=lambda: add_operation(text))
    button.grid(column=col, row=row, sticky='nswe')
    return button


window = tk.Tk()
window.title("Калькулятор")

window['bg'] = '#33ffe6'

window.geometry(f"320x370+500+300")
window.resizable(False, False)

button_0 = create_digit_button('0', 1, 4)

button_0['bd'] = 5

button_1 = create_digit_button('1', 0, 3)

button_2 = create_digit_button('2', 1, 3)

button_3 = create_digit_button('3', 2, 3)

button_4 = create_digit_button('4', 0, 2)

button_5 = create_digit_button('5', 1, 2)

button_6 = create_digit_button('6', 2, 2)

button_7 = create_digit_button('7', 0, 1)

button_8 = create_digit_button('8', 1, 1)

button_9 = create_digit_button('9', 2, 1)

button_plus = create_operation_button('+', 3, 1)

button_minus = create_operation_button('-', 3, 2)

button_mul = create_operation_button('*', 3, 3)

button_div = create_operation_button('/', 3, 4)

button_equal = create_operation_button('=', 2, 4)
button_equal['command'] = buttonequal

button_del = create_operation_button('C', 0, 4)
button_del['command'] = buttondel

entry = tk.Entry(font=('Areal', 20, 'bold'), justify=tk.RIGHT)
entry.grid(column=0, row=0, columnspan=4, sticky='nwes')

window.grid_columnconfigure(0, minsize=80)
window.grid_columnconfigure(1, minsize=80)
window.grid_columnconfigure(2, minsize=80)
window.grid_columnconfigure(3, minsize=80)
window.grid_rowconfigure(0, minsize=50)
window.grid_rowconfigure(1, minsize=80)
window.grid_rowconfigure(2, minsize=80)
window.grid_rowconfigure(3, minsize=80)
window.grid_rowconfigure(4, minsize=80)

window.mainloop()
