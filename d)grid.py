import tkinter as tk

window = tk.Tk()
window.title("kek")


window.geometry(f"500x400+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)


window.mainloop()