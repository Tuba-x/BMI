from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=200)

label_w = Label(text="Enter Your Weight(kg)", pady=5)
label_w.pack()

entry_w = Entry(width=10)
entry_w.pack()


label_h = Label(text="Enter Your Height(cm)", pady=5)
label_h.pack()

entry_h = Entry(width=10)
entry_h.pack()


def click_button():
    if entry_w.get() == "" or entry_h.get() == "":
        label_result.config(text="Enter both weight and height!")
    else:
        try:
            w = int(entry_w.get())
            h = int(entry_h.get())
            bmi = round(w/((h/100)**2), 1)

            if bmi < 18.5:
                label_result.config(text=f"Your bmi is {bmi}. You are underweight")
            elif 18.5 <= bmi < 25:
                label_result.config(text=f"Your bmi is {bmi}. You are normal")
            elif 25 <= bmi < 30:
                label_result.config(text=f"Your bmi is {bmi}. You are overweight")
            else:
                label_result.config(text=f"Your bmi is {bmi}. You are obese")

        except ValueError:
            label_result.config(text="Enter a valid number")


button = Button(text="Calculate", width=10, height=1, command=click_button)
button.pack(pady=10)


label_result = Label()
label_result.pack()

window.mainloop()
