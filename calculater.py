from tkinter import *

root = Tk()


def enter(button):
    button.config(bg="light blue", fg="black")


def leave(button):
    button.config(bg="white", fg="black")


def add_char(char):
    current = ent.get()
    x.set(current + char)


def clear():
    x.set("")


def calc():
    e = ent.get()
    e = e.replace(" ", "")
    if "+" in e:
        result = e.split("+")

        respon = sum(float(num) for num in result)
        x.set(str(respon))
    elif "-" in e:
        result = e.split("-")
        reply = float(result[0]) * 2 - sum(float(num) for num in result)
        x.set(str(reply))
    elif "/" in e:
        result = e.split("/")

        reply = float(result[0]) / float(result[1])
        x.set(str(reply))
    elif "*" in e:
        numbers = e.split("*")
        reply = float(numbers[0]) * float(numbers[1])
        x.set(str(reply))
    elif "^" in e:
        numbers = e.split("^")
        number1 = int(numbers[0])
        number2 = int(numbers[1])
        reply = 1
        for i in range(number2):
            reply *= number1
        x.set(str(reply))
    elif "!" in e:
        numbers = e.split("!")
        reply = 1
        for i in range(int(numbers[1]), 0, -1):
            reply *= i
        x.set(str(reply))
    elif "sqrt" in e:
        numbers = e.split("sqrt")
        reply = 1
        for i in range(0, 2):
            reply *= float(numbers[1])
        x.set(str(reply))
    elif "rad" in e:
        numbers = e.split("rad")
        reply = float(numbers[1]) ** 0.5
        x.set(str(reply))


x = StringVar()
ent = Entry(root, textvariable=x, width=11, bd=10, bg="lightblue", font=("Arial", 24))
ent.grid(row=0, column=0, columnspan=4)

button1 = Button(root, text="1", padx=20, pady=20, command=lambda: add_char("1"))
button1.bind("<Enter>", lambda e: enter(button1))
button1.bind("<Leave>", lambda e: leave(button1))

button1.grid(row=1, column=0)

button2 = Button(root, text="2", pady=20, padx=20, command=lambda: add_char("2"))
button2.bind("<Enter>", lambda e: enter(button2))
button2.bind("<Leave>", lambda e: leave(button2))
button2.grid(row=1, column=1)

button3 = Button(root, text="3", padx=20, pady=20, command=lambda: add_char("3"))
button3.bind("<Enter>", lambda e: enter(button3))
button3.bind("<Leave>", lambda e: leave(button3))
button3.grid(row=1, column=2)

taqsim = Button(root, text="/", pady=20, padx=20, command=lambda: add_char("/"))
taqsim.bind("<Enter>", lambda e: enter(taqsim))
taqsim.bind("<Leave>", lambda e: leave(taqsim))
taqsim.grid(row=1, column=3)

button4 = Button(root, text="4", pady=20, padx=20, command=lambda: add_char("4"))
button4.bind("<Enter>", lambda e: enter(button4))
button4.bind("<Leave>", lambda e: leave(button4))
button4.grid(row=2, column=0)

button5 = Button(text="5", pady=20, padx=20, command=lambda: add_char("5"))
button5.bind("<Enter>", lambda e: enter(button5))
button5.bind("<Leave>", lambda e: leave(button5))
button5.grid(row=2, column=1)

button6 = Button(text="6", padx=20, pady=20, command=lambda: add_char("6"))
button6.grid(row=2, column=2)
button6.bind("<Enter>", lambda e: enter(button6))
button6.bind("<Leave>", lambda e: leave(button6))

button_multiply = Button(text="*", pady=20, padx=20, command=lambda: add_char("*"))
button_multiply.grid(row=2, column=3)
button_multiply.bind("<Enter>", lambda e: enter(button_multiply))
button_multiply.bind("<Leave>", lambda e: leave(button_multiply))

button7 = Button(text="7", padx=20, pady=20, command=lambda: add_char("7"))
button7.grid(row=3, column=0)
button7.bind("<Enter>", lambda e: enter(button7))
button7.bind("<Leave>", lambda e: leave(button7))

button8 = Button(text="8", pady=20, padx=20, command=lambda: add_char("8"))
button8.bind("<Enter>", lambda e: enter(button8))
button8.bind("<Leave>", lambda e: leave(button8))
button8.grid(row=3, column=1)

button9 = Button(text="9", padx=20, pady=20, command=lambda: add_char("9"))
button9.grid(row=3, column=2)
button9.bind("<Enter>", lambda e: enter(button9))
button9.bind("<Leave>", lambda e: leave(button9))

plus = Button(text="+", pady=20, padx=20, command=lambda: add_char("+"))
plus.grid(row=3, column=3)
plus.bind("<Enter>", lambda e: enter(plus))
plus.bind("<Leave>", lambda e: leave(plus))

mosavi = Button(text="=", padx=20, pady=20, command=calc)
mosavi.grid(row=4, column=3)
mosavi.bind("<Enter>", lambda e: enter(mosavi))
mosavi.bind("<Leave>", lambda e: leave(mosavi))

pow = Button(text="^", pady=20, padx=20, command=lambda: add_char("^"))
pow.grid(row=4, column=2)
pow.bind("<Enter>", lambda e: enter(pow))
pow.bind("<Leave>", lambda e: leave(pow))

fact = Button(text="!", padx=20, pady=20, command=lambda: add_char("!"))
fact.grid(row=0, column=4)
fact.bind("<Enter>", lambda e: enter(fact))
fact.bind("<Leave>", lambda e: leave(fact))

radical = Button(text="rad", pady=20, padx=20, command=lambda: add_char("rad"))
radical.grid(row=4, column=0)
radical.bind("<Enter>", lambda e: enter(radical))
radical.bind("<Leave>", lambda e: leave(radical))

clear_button = Button(text="C", padx=20, pady=20, command=clear)
clear_button.grid(row=1, column=4)
clear_button.bind("<Enter>", lambda e: enter(clear_button))
clear_button.bind("<Leave>", lambda e: leave(clear_button))

menha = Button(text="-", pady=20, padx=20, command=lambda: add_char("-"))
menha.grid(row=2, column=4)
menha.bind("<Enter>", lambda e: enter(menha))
menha.bind("<Leave>", lambda e: leave(menha))

dot_button = Button(text=".", padx=20, pady=20, command=lambda: add_char("."))
dot_button.grid(row=3, column=4)
dot_button.bind("<Enter>", lambda e: enter(dot_button))
dot_button.bind("<Leave>", lambda e: leave(dot_button))

sqrt = Button(text="sqrt", padx=20, pady=20, command=lambda: add_char("sqrt"))
sqrt.grid(row=4, column=4)
sqrt.bind("<Enter>", lambda e: enter(sqrt))
sqrt.bind("<Leave>", lambda e: leave(sqrt))

button0 = Button(text="0", pady=20, padx=20, command=lambda: add_char("0"))
button0.grid(row=4, column=1)
button0.bind("<Enter>", lambda e: enter(button0))
button0.bind("<Leave>", lambda e: leave(button0))
mainloop()
