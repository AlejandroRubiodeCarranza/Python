# -*- coding: utf-8 -*-
"""
Create a program that has:
-Window
-Fixed size
-A menu
-Different screens
-Add product form
-Save data frequently
-Show data listed on the home screen
-Option to exit the program
"""


from tkinter import *
from tkinter import ttk


# Define Window
ventana=Tk()

ventana.minsize(500,500)

ventana.title("Project Tkinter")

ventana.resizable(0,0)


# Important variables

products=[]

name_data=StringVar()
price_data=StringVar()


# Operations

def add_product():
    products.append([
            name_data.get(),
            price_data.get(),
            add_description_entry.get("1.0","end-1c")
            ])
    
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0",END)
    
    # Return tu home page
    home()
    
# Define screen fields

home_label=Label(ventana,text="START HOME")

product_box=Frame(ventana,width=250)

product_box=ttk.Treeview(height=12,columns=2)
product_box.grid(row=1,column=0,columnspan=2)

product_box.heading("#0",text="Product",anchor=W)
product_box.heading("#1",text="Precio",anchor=W)
                       

add_label=Label(ventana,text="ADD Product")
info_label=Label(ventana,text="INFORMATION")
data_label=Label(ventana,text="Created by Alejandro Rubio")

# Form fields
add_frame= Frame(ventana)



add_name_label=Label(add_frame,text="Product Name")
add_name_entry=Entry(add_frame,textvariable=name_data)

add_price_label=Label(add_frame,text="Product Price")
add_price_entry=Entry(add_frame,textvariable=price_data)

add_description_label=Label(add_frame,text="Product description")
add_description_entry=Text(add_frame)

add_separator=Label(add_frame,text="")

#Button

boton= Button(add_frame,text="Guardar",command=add_product)

# Screen

def home():
    
    # Build scree
    home_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=190,
            pady=20
            )
    
    home_label.grid(row=0,column=0,sticky=E)
    
    product_box.grid(row=1)
    
    #Product List:
    """
    for product in products:
        if(len(product)==3):
            product.append("ADDED")
            Label(product_box,text=product[0]).grid()
            Label(product_box,text=product[1]).grid()
            Label(product_box,text=product[2]).grid()
            
            Label(product_box,text="------------").grid()
"""
    for product in products:
        if(len(product)==3):    
            product.append("ADDED")
            product_box.insert('',0,text=product[0],values=(product[1]))
            
    
    # Hide other screens
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

    
    
    
    return True

def add():
    
    # Head
    add_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=190,
            pady=20
            )
    
    add_label.grid(row=0,column=0,columnspan=10,sticky=W)
    
    # Form fields
    
    add_frame.grid(row=1)
    
    add_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
    add_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    add_price_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
    add_price_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    add_description_label.grid(row=3,column=0,padx=5,pady=5,sticky=NW)
    
    add_description_label.config(
            width=20,
            height=5,
            font=("Consolas",10),
            padx=15,
            pady=15
            )
    add_description_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
    
    add_separator.grid(row=5,column=1)
    
    boton.grid(row=5,column=1,sticky=NW)
    
    boton.config(
            pady=10,
            bg="green",
            fg="black"
            )
    
    # Hide other screens
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    product_box.grid_remove()
    return True

def info():
    info_label.config(
            fg="white",
            bg="black",
            font=("Arial",30),
            padx=190,
            pady=20
            )
    info_label.grid(row=0,column=0)
    
    data_label.grid(row=1,column=0)
    
    
    # Hide other screens
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    product_box.grid_remove()
    
    return True

# Load start screen

home()

# Top Menu

menu_superior=Menu(ventana)

menu_superior.add_command(label="Start",command=home)
menu_superior.add_command(label="Add",command=add)
menu_superior.add_command(label="Information",command=info)
menu_superior.add_command(label="Log Out",command=ventana.quit)

#Load menu

ventana.config(menu=menu_superior)


# Load window
ventana.mainloop()
