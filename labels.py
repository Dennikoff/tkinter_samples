import tkinter as tk

window = tk.Tk()
window.title("kek")


window.geometry(f"{h}x{w}+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

label_1 = tk.Label(window, text="Hello",
                   bg="red")
label_1.pack()

window.mainloop()