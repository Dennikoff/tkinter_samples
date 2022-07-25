import tkinter as tk

window = tk.Tk()
window.title("kek")


window.geometry(f"500x400+500+300")
window.resizable(True, True)
window.minsize(300, 400)
window.maxsize(800, 900)

button1 = tk.Button(window, text="button 1")
button2 = tk.Button(window, text="button 2")
button3 = tk.Button(window, text="button 3")
button4 = tk.Button(window, text="button 4 lol kek")
button5 = tk.Button(window, text="button 5")
button6 = tk.Button(window, text="button 6")
button7 = tk.Button(window, text="button 7")
button8 = tk.Button(window, text="button 8")
button9 = tk.Button(window, text="button 9")
button10 = tk.Button(window, text="button 10")

button1.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0, sticky="we")
button4.grid(row=1, column=1)
button5.grid(row=2, column=0)
button6.grid(row=2, column=1, sticky="w")
button7.grid(row=3, column=0)
button8.grid(row=3, column=1, sticky="e")
button9.grid(row=4, column=0, columnspan=2, sticky="we")
button10.grid(row=0, column=2, rowspan=5, sticky="nsew")

window.grid_columnconfigure(0, minsize=200)
window.grid_columnconfigure(2, minsize=150)

window.mainloop()