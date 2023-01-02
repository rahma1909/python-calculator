#calculator app
from errno import ENODEV
from pickletools import read_unicodestringnl
from re import A
from tkinter import*
root=Tk()
root.title("simple calc")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)


#e.insert(0,'enter your email')
#def myclick():
 #   hello="welcome to\t"+e.get()
  #  mylabel=Label(root,text=hello,fg="white",bg="black")
  
   # mylabel.pack()
def add_button(number):
      current=e.get()
      e.delete(0,END)
      e.insert(0,str(current)+str(number))
      


def clear_button():
      e.delete(0,END)
      
def add1_button():
      first_num=e.get()
      global f_num
      global math
      math="addition"
      f_num=int(first_num)
      e.delete(0,END)
def mult_button():
      first_num=e.get()
      global f_num
      global math
      math="mult"
      f_num=int(first_num)
      e.delete(0,END)

def divide_button():
      first_num=e.get()
      global f_num
      global math
      math="division"
      f_num=int(first_num)
      e.delete(0,END)

def sub_button():
      first_num=e.get()
      global f_num
      global math
      math="sub"
      f_num=int(first_num)
      e.delete(0,END)
      
def equal_button():
      second_num=e.get()
      e.delete(0,END)
      if math=="addition":
        e.insert(0,f_num+int(second_num))
      if math=="sub":
            e.insert(0,f_num-int(second_num))
      if math=="mult":
            e.insert(0,f_num*int(second_num))
      if math=="division":
            e.insert(0,f_num/int(second_num))      
            
  #.insert(0,number)
      

#define buttons
button1=Button(root,text="1",pady=20,padx=90,command=lambda:add_button(1))
button2=Button(root,text="2",pady=20,padx=90,command=lambda:add_button(2))
button3=Button(root,text="3",pady=20,padx=90,command=lambda:add_button(3))
button4=Button(root,text="4",pady=20,padx=90,command=lambda:add_button(4))
button5=Button(root,text="5",pady=20,padx=90,command=lambda:add_button(5))
button6=Button(root,text="6",pady=20,padx=90,command=lambda:add_button(6))
button7=Button(root,text="7",pady=20,padx=90,command=lambda:add_button(7))
button8=Button(root,text="8",pady=20,padx=90,command=lambda:add_button(8))
button9=Button(root,text="9",pady=20,padx=90,command=lambda:add_button(9))
button10=Button(root,text="0",pady=20,padx=90,command=lambda:add_button(0))

buttonequl=Button(root,text="=",pady=20,padx=90,command=lambda:equal_button())
buttonclear=Button(root,text="clear",pady=20,padx=90,command=clear_button)
buttonpluse=Button(root,text="+",pady=20,padx=90,command=add1_button)

buttondivide=Button(root,text="/",pady=20,padx=90,command=divide_button)
buttonmultiply=Button(root,text="*",pady=20,padx=90,command=mult_button)
buttonsub=Button(root,text="-",pady=20,padx=90,command=sub_button)

#put buttons on the screen
button1.grid(row=3,column=0)  
button2.grid(row=3,column=1)  
button3.grid(row=3,column=2)  
button4.grid(row=2,column=0)  
button5.grid(row=2,column=1)  
button6.grid(row=2,column=2)  
button7.grid(row=1,column=0)  
button8.grid(row=1,column=1)  
button9.grid(row=1,column=2) 

button10.grid(row=1,column=2) 
buttonequl.grid(row=5,column=0)
buttonclear.grid(row=5,column=1)
buttonpluse.grid(row=5,column=2)

buttondivide.grid(row=6,column=0)
buttonmultiply.grid(row=6,column=1)
buttonsub.grid(row=6,column=2)
##mybutton=Button(root,text="enter your email",command=myclick,pady=50,padx=50)
 
##mybutton=Button(root,text="enter your email",command=myclick,pady=50,padx=50)
##mybutton=Button(root,text="enter your email",command=myclick,pady=50,padx=50)
##mybutton=Button(root,text="enter your email",command=myclick,pady=50,padx=50)
#my#button.pack()

root.mainloop()
