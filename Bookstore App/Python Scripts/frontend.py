from tkinter import *
import backend22

def get_selected_row(event): #since this function is binded to an widget event tihs function gets special parameter 'event'
    try:
        global selected_tuple    #selected_tuple is declared as global variable so that it can be used or called directly outside this function
        index = list1.curselection()[0] # curselection is the method of listbox gives tuple of index(tuple of one item) and [0] is added to get just index not tuple
        selected_tuple = list1.get(index) # from list1(i.e.listbox ) get tuple with index 'x' [0] gets id of selected tuple
        e1.delete(0,END)                 #clears the entrybox e1
        e1.insert(END,selected_tuple[1])  # adds 1st value(i.e.title) of the selected_tuple at the 'END'
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass


def view_command(): 
    list1.delete("0",END) #this deletes the earliarackend.view content in list
    for row in backend22.viewall():
        list1.insert(END,row)  # ENd helps to put new row at the end 

def search_command():
    list1.delete(0,END)
    for row in backend22.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)

def add_command():
    backend22.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    backend22.delete(selected_tuple[0]) # [0] gets id of selected tuple

def update_command():
    backend22.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    #here id is send from selected_tuple and other four arguments of update() function from backend are send from e1,e2,e3,e4 entry box so that it gets updated content



window = Tk()

window.wm_title("BookStore")


l1 = Label(window,text="Title")
l1.grid(row=0,column=0)

l2 = Label(window,text="Author")
l2.grid(row=0,column=2)

l3 = Label(window,text="Year")
l3.grid(row=1,column=0)

l4 = Label(window,text="ISBN")
l4.grid(row=1,column=2)

title_text = StringVar()
e1 = Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text = StringVar()
e2 = Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text = StringVar()
e3 = Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text = StringVar()
e4 = Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

b1 = Button(window,text="View all",width=12,command=view_command)
b1.grid(row=2,column=3)

b2 = Button(window,text="Search entry",width=12,command=search_command)
b2.grid(row=3,column=3)

b3 = Button(window,text="Add entry",width=12,command=add_command)
b3.grid(row=4,column=3)

b4 = Button(window,text="Update selected",width=12,command=update_command)
b4.grid(row=5,column=3)

b5 = Button(window,text="Delete selected",width=12,command=delete_command)
b5.grid(row=6,column=3)

b6 = Button(window,text="Close",width=12,command=window.destroy) # '.destory' method destorys the window
b6.grid(row=7,column=3)

list1 = Listbox(window,height=8,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)


list1.bind('<<ListboxSelect>>',get_selected_row) #bind() method takes two argument first is 'event type' and 'function' that you want to bind
#line77 selects the row form listbox 'list1'
list1.configure(yscrollcommand=sb1.set) # y stands for Y-axis i.e vertical scroll
sb1.configure(command=list1.yview) 

window.mainloop()