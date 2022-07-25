import tkinter as tk

window = tk.Tk()
window.title("kek")


window.geometry(f"500x400+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

label_1 = tk.Label(window,
                   text="Hello,\nworld\na lot of letters",
                   bg="red",
                   fg="white",
                   font=('Arial', 20, 'bold'),
                   padx=0,
                   pady=0,
                   width=10,
                   height=10,
                   anchor='nw',
                   relief=tk.RAISED,
                   bd=5,
                   justify=tk.RIGHT
                   )
label_1.pack()

window.mainloop()