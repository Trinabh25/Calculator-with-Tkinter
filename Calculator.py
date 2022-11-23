from tkinter import *


expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def clr():
    global expression
    expression = ""
    equation.set(expression)

def ans():
    try: 
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("Error")
        expression = ""




if __name__ == "__main__":
    window = Tk()
    window.title("Calculator")

    window.geometry("300x150")

    equation = StringVar()

    input = Entry(window, textvariable=equation).grid(column=1, row=0)

    one = Button(window,text = " 1", fg = "black", bg="red", height=1, width=7, command=lambda: press(1)).grid(column=0, row=2)
    two = Button(window,text = " 2", fg = "black", bg="red", height=1, width=7, command=lambda: press(2)).grid(column=1, row=2)
    three = Button(window,text = " 3", fg = "black", bg="red", height=1, width=7, command=lambda: press(3)).grid(column=2, row=2)
    four = Button(window,text = " 4", fg = "black", bg="red", height=1, width=7, command=lambda: press(4)).grid(column=0, row=3)
    five = Button(window,text = " 5", fg = "black", bg="red", height=1, width=7, command=lambda: press(5)).grid(column=1, row=3)
    six = Button(window,text = " 6", fg = "black", bg="red", height=1, width=7, command=lambda: press(6)).grid(column=2, row=3)
    seven = Button(window,text = " 7", fg = "black", bg="red", height=1, width=7, command=lambda: press(7)).grid(column=0, row=4)
    eight = Button(window,text = " 8", fg = "black", bg="red", height=1, width=7, command=lambda: press(8)).grid(column=1, row=4)
    nine = Button(window,text = " 9", fg = "black", bg="red", height=1, width=7, command=lambda: press(9)).grid(column=2, row=4)
    zero = Button(window,text = " 0", fg = "black", bg="red", height=1, width=7, command=lambda: press(0)).grid(column=0, row=5)

    add = Button(window,text = " +", fg = "black", bg="green", height=1, width=7, command=lambda: press("+")).grid(column=4, row=1)
    sub = Button(window,text = " -", fg = "black", bg="green", height=1, width=7, command=lambda: press("-")).grid(column=4, row=2)
    mult = Button(window,text = " *", fg = "black", bg="green", height=1, width=7, command=lambda: press("*")).grid(column=4, row=3)
    divid = Button(window,text = " /", fg = "black", bg="green", height=1, width=7, command=lambda: press("/")).grid(column=4, row=4)
    dec = Button(window,text = " .", fg = "black", bg="green", height=1, width=7, command=lambda: press(".")).grid(column=4, row=5)
    clear = Button(window,text = " C", fg = "black", bg="green", height=1, width=7, command=clr).grid(column=2, row=5)
    equal = Button(window,text = " =", fg = "black", bg="green", height=1, width=7, command=ans).grid(column=1, row=5)



    window.mainloop()