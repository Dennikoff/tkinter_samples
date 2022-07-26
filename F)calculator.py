import tkinter as tk


def create_button(text, col, row):
    button = tk.Button(text=text)
    button.grid(column=col, row=row, sticky='nswe')
    return button


window = tk.Tk()
window.title("kek")



window.geometry(f"320x400+500+300")
window.resizable(False, False)

button_0 = create_button('0', 1, 4)
button_1 = create_button('1', 0, 3)
button_2 = create_button('2', 1, 3)
button_3 = create_button('3', 2, 3)
button_4 = create_button('4', 0, 2)
button_5 = create_button('5', 1, 2)
button_6 = create_button('6', 2, 2)
button_7 = create_button('7', 0, 1)
button_8 = create_button('8', 1, 1)
button_9 = create_button('9', 2, 1)




window.grid_columnconfigure(0, minsize=80)
window.grid_columnconfigure(1, minsize=80)
window.grid_columnconfigure(2, minsize=80)
window.grid_columnconfigure(3, minsize=80)
window.grid_rowconfigure(0, minsize=80)
window.grid_rowconfigure(1, minsize=80)
window.grid_rowconfigure(2, minsize=80)
window.grid_rowconfigure(3, minsize=80)
window.grid_rowconfigure(4, minsize=80)



window.mainloop()