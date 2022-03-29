from tkinter import*

from tkinter import ttk

from PIL import ImageTk,Image

root=Tk()

root.configure(bg="aqua")

root.geometry("900x500")

 

burger_image=ImageTk.PhotoImage(Image.open("burger1.png"))

burger_label=Label(root)

burger_label['image']=burger_image

burger_label.place(relx=0.7,rely=0.5,anchor=CENTER)

 

title_L=Label(root,text="MCdonalds",font=("times",40,"bold"),fg="orange",bg="aqua")

title_L.place(relx=0.12,rely=0.1,anchor=CENTER)

 

Dish_L=Label(root,text="Choose Dish",font=("times",15),bg="aqua")

Dish_L.place(relx=0.06,rely=0.2,anchor=CENTER)

 

Dish=["Burger","Ice_Cream"]

Dish_dropdown=ttk.Combobox(root,state="readonly",values=Dish)

Dish_dropdown.place(relx=0.25,rely=0.2,anchor=CENTER)

 

 

addons_L=Label(root,text="Choose Addons",font=("times",15),bg="aqua")

addons_L.place(relx=0.08,rely=0.5,anchor=CENTER)

 

Addons=[]

Addons_dropdown=ttk.Combobox(root,state="readonly",values=Addons)

Addons_dropdown.place(relx=0.25,rely=0.5,anchor=CENTER)

 

final_amount_L=Label(root,font=("times",15),bg="aqua",fg="red")

final_amount_L.place(relx=0.2,rely=0.75,anchor=CENTER)

 

class parent():

  def __init__(self):

   print("Parent class")

  def menu(dish):

     if (dish=="Burger"):
      print("You can add the following toppings: Cheese | Jalapeno")
      addons=["Cheese","Jalapeno"]
      Addons_dropdown['values']=addons
     elif (dish=="Ice_Cream"):
      print("You can add the following flavour: Chocolate | Caramel")
      addons=["Chocolate","Caramel"]
      Addons_dropdown['values']=addons
     else:
      print("Give Valid Dish :")

  def final_amount(dish,addons):

        if (dish=="Burger" and addons== "Cheese"):

           final_amount_L['text']="The Total amount will be 250 USD"

        elif(dish=="Burger" and addons== "Jalapeno"):

           final_amount_L['text']="The Total amount will be 350 USD"

        elif(dish=="Ice_Cream" and addons== "Chocolate"):

           final_amount_L['text']="The Total amount will be 350 USD"

        elif(dish=="Ice_Cream" and addons== "Caramel"):

           final_amount_L['text']="The Total amount will be 450 USD"

class child1(parent):
    def __init__(self,dish):
        self.dish = dish
       
    def  get_menu(self):
        dish=Dish_dropdown.get()
        parent.menu(dish)
       
class child2(parent):
    def __init__(self,dish,addons):
        self.dish = dish
        self.addons = addons
       
    def get_final_amount(self):
        dish=Dish_dropdown.get()
        addons=Addons_dropdown.get()
        parent.final_amount(dish,addons)

child1_object =child1(Dish_dropdown.get())
child1_object.get_menu()
child2_object = child2(Addons_dropdown.get(),Dish_dropdown.get())
child2_object.get_final_amount()

 

btn_dish=Button(root,text="Choose Dish",bg="blue",command=child1_object.get_menu)

btn_dish.place(relx=0.06,rely=0.3,anchor=CENTER)

 

btn_addons=Button(root,text="Choose Addons",bg="blue",command=child2_object.get_final_amount)

btn_addons.place(relx=0.4,rely=0.6,anchor=CENTER)

 

root.mainloop()

