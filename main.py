import tkinter as tk

window = tk.Tk()
window.title("kek")
h = 500
w = 400


window.geometry(f"{h}x{w}+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

window.mainloop()