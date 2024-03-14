from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=350,height=300)
font_1= ("Bold",20,"italic")
font_2= ("Bold",20)
font_3= ("bold",20)

height_text = Label(text="Enter your height(cm):", fg="white",font=font_1)
height_text.config(pady=8)
height_text.pack()

height_entry = Entry()
height_entry.pack()

weight_text = Label(text="Enter your weight:", fg="white",font=font_1)
weight_text.config(pady=8)
weight_text.pack()

weight_entry = Entry()
weight_entry.pack()

def click_button():
    Heigh = (height_entry.get())
    weight = (weight_entry.get())
    try:
        if weight == "" or Heigh == "":
            empty_label = Label(text="Please enter your height and weight",font=font_3)
            empty_label.pack()
        else:
            BMI = float(weight) / (float(Heigh)/100)**2
            BMI = int(BMI * 100) / 100
            if 0< BMI < 18.5:
                text= "Underweight" #230
            elif 18<= BMI <25:
                text= "Normal weight"  #169
            elif 25<= BMI <30:
                text= "Overweight"#216
            elif 30<= BMI:
                text= "Obese" #162
            elif BMI <= 0:
                text="entered the wrong number."
            calculated_BMI_label = Label(text=f"Your BMI is {BMI} You are {text}",font=font_3)
            calculated_BMI_label.config(pady=10)
            calculated_BMI_label.pack()
    except ValueError:
        calculated_ValueError = Label(text="please enter a correct value!!..",font=font_3)
        calculated_ValueError.config(pady=10)
        calculated_ValueError.pack()





calculate_button = Button(text="Calculate",command=click_button)
calculate_button.pack()

def how_much_pixel():
    calculate_button.update()
    x = calculate_button.winfo_height()
    y = calculate_button.winfo_width()
    print(y)

window.mainloop()