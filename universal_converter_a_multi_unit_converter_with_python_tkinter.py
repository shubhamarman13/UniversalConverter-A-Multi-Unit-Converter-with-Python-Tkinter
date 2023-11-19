from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("733x566")
root.title("calculator")


# defining 12 function for multiple window
#first function
def Celsius_Fahrenheit():
    root1=Tk()
    root1.geometry("1000x1166")
    root1.title("Celsius_Fahrenheit")
    # var1=()
    #var1=DoubleVar()
    label1=Label(root1,text='Temperture in Celcius =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root1,text='Temperture in Fahrenheit =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root1,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root1,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        # x=messagebox.showinfo("box",str(var1.get()+2))
        v=entry1.get()
        z=float(v)*1.8 + 32
        print(v)
        #label3.config(text=''+str(z)+ '°F')
        label3['text']=str(z)+ '°F'
        # x=messagebox.showinfo(var1.get())

    button1=Button(root1,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root1.mainloop()




#2nd function
def Fahrenheit_Celsius():
    root2=Tk()
    root2.geometry("1000x1166")
    root2.title("Celsius-Fahrenheit")
    label1=Label(root2,text='Temperture in Fahrenheit =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root2,text='Temperture in Celcius =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root2,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root2,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=((float(v)-32)*0.5555)
        print(v)
        
        label3['text']=str(z)+ '°c'
        

    button1=Button(root2,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root2.mainloop()
#3



def Celsius_kelvin():
    root3=Tk()
    root3.geometry("1000x1100")
    root3.title("Celsius_kelvin")
    label1=Label(root3,text='Temperture in Celsius =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root3,text='Temperture in Kelvin =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root3,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root3,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)+273.15)
        print(v)
        
        label3['text']=str(z)+ ' k'
        

    button1=Button(root3,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root3.mainloop()
    
  #4
  
  
def kelvin_Fahrenheit():
    root4=Tk()
    root4.geometry("1000x1166")
    root4.title("kelvin_Fahrenheit")
    label1=Label(root4,text='Temperture in Kelvin =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root4,text='Temperture in Fahrenheit =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root4,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root4,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(1.8*(float(v)-273)+32)
        print(v)
        
        label3['text']=str(z)+ ' F'
        

    button1=Button(root4,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    
    
    root4.mainloop()  
#5



def Meter_Kilometer():
    root5=Tk()
    root5.geometry("1000x1166")
    root5.title("Meter_Kilometer")
    
    label1=Label(root5,text='Distance in Meter =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root5,text='Distance in KM  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root5,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root5,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)/1000)
        print(v)
        
        label3['text']=str(z)+ ' Kilometer'
        

    button1=Button(root5,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root5.mainloop()    
#6



def Kilometer_Meter():
    root6=Tk()
    root6.geometry("1033x1166")
    root6.title("Kilometer_Meter")
    label1=Label(root6,text='Distance in KM =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root6,text='Distance in Meter  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root6,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root6,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)*1000)
        print(v)
        
        label3['text']=str(z)+ ' Meter'
        

    button1=Button(root6,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root6.mainloop()
    #7
    
    
    
def Mile_Yard():
    root7=Tk()
    root7.geometry("1033x1166")
    root7.title("Mile_Yard")
    label1=Label(root7,text='Distance in Mile =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root7,text='Distance in Yard  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root7,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root7,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)*1760)
        print(v)
        
        label3['text']=str(z)+ ' yard'
        

    button1=Button(root7,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root7.mainloop()
    #8
    
    
    
    
def Yard_Mile():
    root8=Tk()
    root8.geometry("1033x1166")
    root8.title("Yard_Mile")
    label1=Label(root8,text='Distance in Yard =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root8,text='Distance in Mile  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root8,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root8,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)/1760)
        print(v)
        
        label3['text']=str(z)+ ' Mile'
        

    button1=Button(root8,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root8.mainloop()
    #9
    
    
    
    
def Tonne_Kilogram():
    root9=Tk()
    root9.geometry("1033x1116")
    root9.title("Tonne_Kilogram")
    label1=Label(root9,text='Weight in tonne =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root9,text='Weight in Kilogram  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root9,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root9,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)*1000)
        print(v)
        
        label3['text']=str(z)+ ' Kilogram'
        

    button1=Button(root9,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root9.mainloop()
    #10
    
    
    
    
def Kilogram_Tonne():
    root10=Tk()
    root10.geometry("1033x1166")
    root10.title("Kilogram_Tonne")
    label1=Label(root10,text='Weight in Kilogram =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root10,text='Weight in Tonne  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root10,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root10,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)/1000)
        print(v)
        
        label3['text']=str(z)+ ' Tonne'
        

    button1=Button(root10,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root10.mainloop()
    #11
    
    
    
    
    
def Pound_Kilogram():
    root11=Tk()
    root11.geometry("1033x1166")
    root11.title("Pound_Kilogram")
    label1=Label(root11,text='Weight in Pound =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root11,text='Weight in Kilogram  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root11,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root11,font=('Arial',25))
    label3.place(x=600,y=300)
    

    def click1():
        
        v=entry1.get()
        z=(float(v)*0.453592)
        print(v)
        
        label3['text']=str(z)+ ' kilogram'
        

    button1=Button(root11,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root11.mainloop()
    #12
    
    
    
    
    
def Kilogram_Ounce():
    root12=Tk()
    root12.geometry("1033x1166")
    root12.title("Kilogram_Ounce")
    label1=Label(root12,text='Weight in Kilogram =',font=('Arial',25))
    label1.place(x=200,y=200)
    label2=Label(root12,text='Weight in Ounce  =',font=('Arial',25))
    label2.place(x=200,y=300)
    entry1=Entry(root12,font=('Arial',25))
    entry1.place(x=600,y=200)
    label3=Label(root12,font=('Arial',25))
    label3.place(x=600,y=300)
    
 
    def click1():
        
        v=entry1.get()
        z=(float(v)*35.274)
        print(v)
        
        label3['text']=str(z)+ ' Ounce'
        

    button1=Button(root12,text='Convert',font=('Arial',25),command=click1)
    button1.place(x=600,y=400)
    root12.mainloop()
    
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
# the end of the code