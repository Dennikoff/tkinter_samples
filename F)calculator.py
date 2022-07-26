import tkinter as tk


operation = ''
first_val = 0



def button0():
    entry.insert(tk.END, '0')


def button1():
    entry.insert(tk.END, '1')


def button2():
    entry.insert(tk.END, '2')


def button3():
    entry.insert(tk.END, '3')


def button4():
    entry.insert(tk.END, '4')


def button5():
    entry.insert(tk.END, '5')


def button6():
    entry.insert(tk.END, '6')


def button7():
    entry.insert(tk.END, '7')


def button8():
    entry.insert(tk.END, '8')


def button9():
    entry.insert(tk.END, '9')


def buttonplus():
    global operation
    global first_val
    operation = '+'
    first_val = entry.get()
    buttondel()



def buttonminus():
    global operation
    global first_val
    operation = '-'
    first_val = entry.get()
    buttondel()


def buttonmul():
    global operation
    global first_val
    operation = '*'
    first_val = entry.get()
    buttondel()


def buttondiv():
    global operation
    global first_val
    operation = '/'
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


def create_button(text, col, row):
    button = tk.Button(text=text)
    button.grid(column=col, row=row, sticky='nswe')
    return button


window = tk.Tk()
window.title("kek")

window.geometry(f"320x400+500+300")
window.resizable(False, False)

button_0 = create_button('0', 1, 4)
button_0['command'] = button0

button_1 = create_button('1', 0, 3)
button_1['command'] = button1

button_2 = create_button('2', 1, 3)
button_2['command'] = button2

button_3 = create_button('3', 2, 3)
button_3['command'] = button3

button_4 = create_button('4', 0, 2)
button_4['command'] = button4

button_5 = create_button('5', 1, 2)
button_5['command'] = button5

button_6 = create_button('6', 2, 2)
button_6['command'] = button6

button_7 = create_button('7', 0, 1)
button_7['command'] = button7

button_8 = create_button('8', 1, 1)
button_8['command'] = button8

button_9 = create_button('9', 2, 1)
button_9['command'] = button9

button_plus = create_button('+', 3, 1)
button_plus['command'] = buttonplus

button_minus = create_button('-', 3, 2)
button_minus['command'] = buttonminus

button_mul = create_button('*', 3, 3)
button_mul['command'] = buttonmul

button_div = create_button('/', 3, 4)
button_div['command'] = buttondiv

button_equal = create_button('=', 2, 4)
button_equal['command'] = buttonequal

button_del = create_button('C', 0, 4)
button_del['command'] = buttondel


entry = tk.Entry(font=('Areal', 20, 'bold'))
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
