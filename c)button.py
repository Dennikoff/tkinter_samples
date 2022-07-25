import tkinter as tk


count = 0
flag = False


def counter():
    global count
    count +=1
    button3['text'] = f"Cчётчик {count}"

def print_click():
    global flag
    flag = not flag
    print('CLick')
    button3['state'] = tk.NORMAL if flag else tk.DISABLED


def add_label():
    label = tk.Label(window, text="new")
    label.pack()


window = tk.Tk()
window.title("kek")


window.geometry(f"500x400+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

button1 = tk.Button(window,
                   text='Click me',
                    command=print_click
                   )

button2 = tk.Button(window,
                   text='Add label',
                    command=add_label
                   )

button3 = tk.Button(window,
                    text=f'Счётчик {count}',
                    command=counter,
                    state=tk.NORMAL if flag else tk.DISABLED)

button1.pack()
button2.pack()
button3.pack()

window.mainloop()