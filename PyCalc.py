import tkinter as tk


expression = ""


window = tk.Tk()
window.title("Simple Calculator")
# each button is 160px
window.geometry("480x640")
window.resizable(False, False)
main_frame = tk.Frame(window)
num_frame = tk.Frame(main_frame)
input_entry = tk.Entry(main_frame, state="disabled", textvariable="StringVar")
num1 = tk.Button(num_frame, text="1", height=7, width=14)
num2 = tk.Button(num_frame, text="2", height=7, width=14)
num3 = tk.Button(num_frame, text="3", height=7, width=14)
num4 = tk.Button(num_frame, text="4", height=7, width=14)
num5 = tk.Button(num_frame, text="5", height=7, width=14)
num6 = tk.Button(num_frame, text="6", height=7, width=14)
num7 = tk.Button(num_frame, text="7", height=7, width=14)
num8 = tk.Button(num_frame, text="8", height=7, width=14)
num9 = tk.Button(num_frame, text="9", height=7, width=14)
num0 = tk.Button(num_frame, text="0", height=7, width=14)
clrbtn = tk.Button(num_frame, text="clear", height=7, width=14)
addbtn = tk.Button(num_frame, text="+", height=7, width=14)
subbtn = tk.Button(num_frame, text="-", height=7, width=14)
multbtn = tk.Button(num_frame, text="*", height=7, width=14)
divbtn = tk.Button(num_frame, text="/", height=7, width=14)
equalbtn = tk.Button(num_frame, text="=", height=7, width=14)
floatbtn = tk.Button(num_frame, text=".", height=7, width=14)


main_frame.place(relx=0.05, rely=0.05, relheight=0.9, relwidth=0.9)
num_frame.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)
input_entry.place(relx=0, rely=0, relheight=0.2, relwidth=1)
num1.grid(column=0, row=0)
num2.grid(column=1, row=0)
num3.grid(column=2, row=0)
num4.grid(column=0, row=1)
num5.grid(column=1, row=1)
num6.grid(column=2, row=1)
num7.grid(column=0, row=2)
num8.grid(column=1, row=2)
num9.grid(column=2, row=2)
num0.grid(column=1, row=3)
clrbtn.grid(column=3, row=0)
addbtn.grid(column=3, row=1)
subbtn.grid(column=3, row=2)
multbtn.grid(column=0, row=3)
divbtn.grid(column=2, row=3)
equalbtn.grid(column=3, row=3)
floatbtn.grid()
window.mainloop()
