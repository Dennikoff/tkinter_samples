import tkinter as tk

window = tk.Tk()
window.title("kek")


def button_click():
    label1['text'] = password_entry.get()



def entry_delete():
    entry.delete(0, tk.END)


window.geometry(f"500x400+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

a = tk.StringVar()

entry = tk.Entry()
entry.grid(column=1, row=0)
password_entry = tk.Entry(show='*')
password_entry.grid(column=2, row=0)

label = tk.Label(text='Имя')
label.grid(column=0, row=0, sticky='w')

label1 = tk.Label(text='')
label1.grid(column=1, row=2, sticky='')

button = tk.Button(window, text='get', command=button_click)
button.grid(column=1, row=1)

tk.Button(window, text='del', command=entry_delete).grid(column=2, row=1)

window.grid_columnconfigure(0, minsize=50)
window.grid_columnconfigure(2, minsize=150)

window.mainloop()
