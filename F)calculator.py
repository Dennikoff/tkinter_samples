import tkinter as tk

window = tk.Tk()
window.title("kek")


window.geometry(f"500x400+500+300")
window.resizable(False, False)


window.columnconfigure(0, 30)


window.mainloop()