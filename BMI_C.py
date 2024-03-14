from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=350,height=300)
font_1= ("Bold",20,"italic")
font_2= ("Bold",20)
font_3= ("bold",25)


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
    Heigh = int(height_entry.get())
    weight = int(weight_entry.get())
    BMI = weight / ((Heigh/100)*(Heigh/100))
    if 0< BMI < 18.5:
        text= "Underweight" #230
        He=230
    elif 18<= BMI <25:
        text= "Normal"  #169
        He=169
    elif 25<= BMI <30:
        text= "Overweight"#216
        He=216
    elif 30<= BMI:
        text= "Obese" #162
        He=162
    elif BMI <= 0:
        text="entered the wrong number."
    calculated_BMI_label = Label(text=f"you are {text}",font=font_3)
    calculated_BMI_label.config(pady=10)
    calculated_BMI_label.place(x= 175-He/2,y= 190)
    def how_much_pixel_2():
        calculated_BMI_label.update()
        print(calculated_BMI_label.winfo_width())
calculate_button = Button(text="Calculate",command=click_button)
calculate_button.place(x= 129,y= 150)

def how_much_pixel():
    calculate_button.update()
    x = calculate_button.winfo_height()
    y = calculate_button.winfo_width()
    print(y)

window.mainloop()