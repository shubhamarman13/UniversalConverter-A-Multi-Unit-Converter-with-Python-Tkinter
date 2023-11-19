from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("733x566")
root.title("calculator")

# defining 12 function for multiple window
def Celsius_Fahrenheit():
    root1=Tk()
    root1.geometry("733x566")
    root1.title("Celsius_Fahrenheit")
    # var1=()
    var1=DoubleVar()
    label1=Label(root1,text='Temperture in Celcius =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root1,text='Temperture in Fahrenheit =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root1,font=('Arial',25),textvariable=var1)
    entry1.place(x=600,y=200)
    label3=Label(root1,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        # x=messagebox.showinfo("box",str(var1.get()+2))
        label3.config(text=''+str(var1.get()*1.8 + 32)+ '°F')
        # x=messagebox.showinfo(var1.get())

    button1=Button(root1,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=920,y=200)
    root1.mainloop()


def Fahrenheit_Celsius():
    root2=Tk()
    root2.geometry("733x566")
    root2.title("Fahrenheit-Celsius")
    root2.mainloop()
#3
def Celsius_kelvin():
    root3=Tk()
    root3.geometry("733x566")
    root3.title("Celsius_kelvin")
    root3.mainloop()
    
  #4
def kelvin_Fahrenheit():
    root4=Tk()
    root4.geometry("733x566")
    root4.title("kelvin_Fahrenheit")
    root4.mainloop()  
#5
def Meter_Kilometer():
    root5=Tk()
    root5.geometry("733x566")
    root5.title("Meter_Kilometer")
    root5.mainloop()    
    #6
def Kilometer_Meter():
    root6=Tk()
    root6.geometry("733x566")
    root6.title("Kilometer_Meter")
    root6.mainloop()
    #7
def Mile_Yard():
    root7=Tk()
    root7.geometry("733x566")
    root7.title("Mile_Yard")
    root7.mainloop()
    #8
def Yard_Mile():
    root8=Tk()
    root8.geometry("733x566")
    root8.title("Yard_Mile")
    root8.mainloop()
    #9
def Tonne_Kilogram():
    root9=Tk()
    root9.geometry("733x566")
    root9.title("Tonne_Kilogram")
    root9.mainloop()
    #10
def Kilogram_Tonne():
    root10=Tk()
    root10.geometry("733x566")
    root10.title("Kilogram_Tonne")
    root10.mainloop()
    #11
def Pound_Kilogram():
    root11=Tk()
    root11.geometry("733x566")
    root11.title("Pound_Kilogram")
    root11.mainloop()
    #12
def Kilogram_Ounce():
    root13=Tk()
    root13.geometry("733x566")
    root13.title("Kilogram_Ounce")
    root13.mainloop()
    
mainmenubar= Menu(root)
m1=Menu(mainmenubar,tearoff=0)


mainmenubar.add_cascade(label="Temperature",menu=m1)
m1.add_command(label="Celsius-Fahrenheit", command=Celsius_Fahrenheit)
m1.add_command(label="Fahrenheit-Celsius", command=Fahrenheit_Celsius)
m1.add_separator()
m1.add_command(label="Celsius-kelvin", command=Celsius_kelvin)
m1.add_command(label="kelvin-Fahrenheit ", command=kelvin_Fahrenheit)
root.config(menu=mainmenubar)


# adding another sub menu in main menubar 
m2=Menu(mainmenubar,tearoff=0)
mainmenubar.add_cascade(label="Distance",menu=m2)

m2.add_command(label="Meter - Kilometer",command=Meter_Kilometer)
m2.add_command(label="Kilometer-Meter",command=Kilometer_Meter)
m2.add_separator()
m2.add_command(label="Mile-Yard",command=Mile_Yard)
m2.add_command(label="Yard -Mile",command=Yard_Mile)
root.config(menu=mainmenubar)

#adding another sub menu in tha main menubar

m3=Menu(mainmenubar,tearoff=0)
mainmenubar.add_cascade(label="Weight",menu=m3)

m3.add_command(label="Tonne- Kilogram",command=Tonne_Kilogram)
m3.add_command(label="Kilogram-Tonne",command=Kilogram_Tonne)
m3.add_separator()
m3.add_command(label="Pound-Kilogram",command=Pound_Kilogram)
m3.add_command(label="Kilogram-Ounce",command=Kilogram_Ounce)
root.config(menu=mainmenubar)

root.mainloop()