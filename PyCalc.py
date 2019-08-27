import tkinter as tk

expression = ""


def press(num):
    global expression
    expression += str(num)
    equation.set(expression)


def equal_press():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Calculator")
    # each button is 160px
    window.geometry("480x800")
    window.resizable(False, False)
    equation = tk.StringVar()
    main_frame = tk.Frame(window)
    num_frame = tk.Frame(main_frame)
    input_entry = tk.Entry(main_frame, textvariable=equation)
    equation.set("Do some maths")
    num1 = tk.Button(num_frame, text="1", height=7, width=14, command=lambda: press(1))
    num2 = tk.Button(num_frame, text="2", height=7, width=14, command=lambda: press(2))
    num3 = tk.Button(num_frame, text="3", height=7, width=14, command=lambda: press(3))
    num4 = tk.Button(num_frame, text="4", height=7, width=14, command=lambda: press(4))
    num5 = tk.Button(num_frame, text="5", height=7, width=14, command=lambda: press(5))
    num6 = tk.Button(num_frame, text="6", height=7, width=14, command=lambda: press(6))
    num7 = tk.Button(num_frame, text="7", height=7, width=14, command=lambda: press(7))
    num8 = tk.Button(num_frame, text="8", height=7, width=14, command=lambda: press(8))
    num9 = tk.Button(num_frame, text="9", height=7, width=14, command=lambda: press(9))
    num0 = tk.Button(num_frame, text="0", height=7, width=14, command=lambda: press(0))
    clrbtn = tk.Button(num_frame, text="clear", height=7, width=14, command=lambda: clear())
    addbtn = tk.Button(num_frame, text="+", height=7, width=14, command=lambda: press("+"))
    subbtn = tk.Button(num_frame, text="-", height=7, width=14, command=lambda: press("-"))
    multbtn = tk.Button(num_frame, text="*", height=7, width=14, command=lambda: press("*"))
    divbtn = tk.Button(num_frame, text="/", height=7, width=14, command=lambda: press("/"))
    equalbtn = tk.Button(num_frame, text="=", height=7, width=14, command=lambda: equal_press())
    floatbtn = tk.Button(num_frame, text=".", height=7, width=14, command=lambda: press("."))
    leftparbtn = tk.Button(num_frame, text="(", height=7, width=14, command=lambda: press("("))
    rightparbtn = tk.Button(num_frame, text=")", height=7, width=14, command=lambda: press(")"))

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
    floatbtn.grid(column=1, row=4)
    leftparbtn.grid(column=0, row=4)
    rightparbtn.grid(column=2, row=4)
    window.mainloop()
