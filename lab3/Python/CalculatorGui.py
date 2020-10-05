from tkinter import *



root = Tk()
root.title("Calculator")
root.configure(background = "white")
root.geometry("400x400")

resultBox = Entry(root,width=45,borderwidth=5,justify = RIGHT)
resultBox.grid(row=0, column = 0 , columnspan=4,padx=10,pady=10,ipady=10)



def button_Click(number):
    # i converted these into a string so that they 
    # dont add each other until user clicks result.
    currentNum = resultBox.get()
    resultBox.delete(0,END)
    resultBox.insert(0,str(currentNum) + str(number))  

#Function that clears the text box when user presses C
def button_Clear():
     resultBox.delete(0,END)

#Work in Progress
#def button_point(dot):   
#    resultBox.insert(END, int(dot))  


def button_Add():
    global number   
    global operator
    operator = "+"
    first_Number = resultBox.get() 
    number = int(first_Number)
    resultBox.delete(0,END)


def button_Substract():
    global number   
    global operator
    operator = "-"
    first_Number = resultBox.get() 
    number = int(first_Number)
    resultBox.delete(0,END)

def button_Multiply():
    global number   
    global operator
    operator = "*"
    first_Number = resultBox.get() 
    number = int(first_Number)
    resultBox.delete(0,END)

def button_Divide():
    global number   
    global operator
    operator = "/"
    first_Number = resultBox.get() 
    number = int(first_Number)
    resultBox.delete(0,END)
  

def button_Equal():
    second_Number = resultBox.get()
    resultBox.delete(0,END)
    if operator == "+":
        resultBox.insert(0,number + int(second_Number))
   
    elif operator == "-":
         resultBox.insert(0,number - int(second_Number))
    
    elif operator == "*":
         resultBox.insert(0,number * int(second_Number))

    elif operator == "/":
         resultBox.insert(0,number / int(second_Number))




#Number buttons 
button_0 = Button(root,text="0",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(0))
button_1 = Button(root,text="1",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(1))
button_2 = Button(root,text="2",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(2))
button_3 = Button(root,text="3",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(3))
button_4 = Button(root,text="4",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(4))
button_5 = Button(root,text="5",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(5))
button_6 = Button(root,text="6",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(6))
button_7 = Button(root,text="7",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(7))
button_8 = Button(root,text="8",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(8))
button_9 = Button(root,text="9",padx=40,pady=20,bg="gainsboro", command = lambda: button_Click(9))

#Operations buttons 
button_percentage = Button(root,text="%",padx=40,pady=20,bg="gray49")
button_left_parenthesis = Button(root,text="(",padx=40,pady=20,bg="gray49")
button_right_parenthesis = Button(root,text=")",padx=40,pady=20,bg="gray49")
button_clear = Button(root,text="C",padx=40,pady=20,bg="gray49" ,command = button_Clear)
button_add = Button(root,text="+",padx=40,pady=20,bg="gray49", command = button_Add)
button_substract = Button(root,text="-",padx=40,pady=20,bg="gray49", command = button_Substract)
button_multiply = Button(root,text="×",padx=40,pady=20,bg="gray49", command = button_Multiply)
button_divide = Button(root,text="÷",padx=40,pady=20,bg="gray49",command = button_Divide)

button_dot = Button(root,text=". ",padx=40,pady=20,bg="gray85")
button_equal = Button(root,text="=",padx=40,pady=20,bg="dodger blue",fg="white",command=button_Equal)


#Button placement
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)

button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)

button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)

button_0.grid(row=5,column=0)

button_add.grid(row=5,column=4)
button_substract.grid(row=4,column=4)
button_multiply.grid(row=3,column=4)

button_divide.grid(row=2,column=4)
button_dot.grid(row=5,column=1)
button_equal.grid(row=5,column=2)

button_percentage.grid(row=1,column=0)
button_left_parenthesis.grid(row=1,column=1)
button_right_parenthesis.grid(row=1,column=2)
button_clear.grid(row=1,column=4)







root.mainloop()

