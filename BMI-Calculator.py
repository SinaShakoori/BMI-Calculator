from tkinter import *
from tkinter import ttk
def calc():
    try:
        w=float(WW1.get())
        h=float(HH1.get())
        bmi=w/((h/100)**2)
        
        if bmi < 18 :
                show.config(text=f"Your BMI IS: {bmi : .2f}\n\n Your Must Eat more!" , bg="yellow")
        elif 18 <= bmi < 25 :
                show.config(text=f"Your BMI IS: {bmi : .2f}\n\n Your lifestyle is Perfect!", bg="Green")
        elif 25 <= bmi < 30 :
                show.config(text=f"Your BMI IS: {bmi : .2f}\n\n You have overweight!" , bg= "orange")
        elif 30 <= bmi :
                show.config(text=f"Your BMI IS: {bmi : .2f}\n\n Your Are Fat!" , bg= "red")

    except ValueError:
           show.config(text=f"Please enter correct Values!" , bg= "red")
    




window=Tk()
window.title("BMI")
window.geometry("500x600")
window.resizable(0,0)


W1=Label(window,text="Please inter your weight (Kg): ",font=("Arial",22),bg="darkblue",fg="white")
W1.place(x=50,y=20,width=400)
WW1=Entry(window, font=("Arial",22),bg="lightblue")
WW1.place(x=50,y=70, width=400,height=65)

H1=Label(window,text="Please inter your height (Cm): ",font=("Arial",22),bg="darkblue",fg="white")
H1.place(x=50,y=150,width=400)
HH1=Entry(window, font=("Arial",22), bg="lightblue")
HH1.place(x=50,y=200,width=400,height=65)


en=ttk.Button(window, text="Calc",command=calc)
en.place(x=50,y=480,width=400,height=50)

show=Label(window,text="",font=("Arial",22))
show.place(x=15,y=280,width=470,height=165)


window.mainloop()