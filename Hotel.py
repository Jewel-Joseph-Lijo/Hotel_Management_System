from tkinter import *
from tkinter import ttk,messagebox
from database import mycol,mycol2
from prettytable import PrettyTable
import datetime

#function to add customers
def add_customer():
    flag=0
    name=name_input.get()
    room_number=room_number_input.get()
    place=place_input.get()
    ph_no=ph_no_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            messagebox.showerror("Error","Room number already occupied")
            room_number_input.set('')
            flag=1     
            break
    if flag==0:
        mycol.insert_one({"Name":name,"Room_number":room_number,"Place":place,"Phone_number":ph_no,"Checked_in":False})
        messagebox.showinfo("Success","Customer added successfully")
        name_input.set('')
        room_number_input.set('')
        place_input.set('')
        ph_no_input.set('')

#function for customer check-in
def check_in():
    flag=0
    room_number=check_in_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            if data["Checked_in"]==False:
                date_fun=datetime.datetime.now().date()
                date=""
                for i in str(date_fun):
                    if i in "-0123456789":
                        date+=i
                mycol.update_one({"Room_number":room_number},{"$set":{"Checked_in":True,"Check_in_date":date}})
                messagebox.showinfo("Success","Customer checked-in successfully")
            else:
                messagebox.showerror("Error","Customer already checked-in")
            check_in_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found") 
        check_in_input.set('')               

#function for customer check-out
def check_out():
    flag=0
    room_number=check_in_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            if data["Checked_in"]==True:
                date_fun=datetime.datetime.now().date()
                date=""
                for i in str(date_fun):
                    if i in "-0123456789":
                        date+=i
                del data['_id']
                mycol2.insert_one(data)
                mycol2.update_one({"Room_number":room_number},{"$set":{"Check_out_date":date}})
                mycol.delete_one({"Room_number":room_number})
                messagebox.showinfo("Success","Customer checked-out successfully")
            else:
                messagebox.showerror("Error","Customer not checked-in")
            check_in_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found")
        check_in_input.set('')

#function to view customers
def view_customers():
    headings=["Name","Room Number","Place","Phone Number","Checked IN","Check IN Date"]
    table=PrettyTable(headings)
    for data in mycol.find({},{"_id":0,"Name":1,"Room_number":1,"Place":1,"Phone_number":1,"Checked_in":1,"Check_in_date":1}):
        data_values=[]
        for info in data:
            data_values.append(data[info])
        while len(headings)!=len(data_values):
            data_values.append("NULL")
        table.add_row(data_values)
    customers_text.insert(CURRENT,table)

#function to refresh customer details
def refresh():
    customers_text.delete('1.0',END)
    headings=["Name","Room Number","Place","Phone Number","Checked IN","Check IN Date"]
    table=PrettyTable(headings)
    for data in mycol.find({},{"_id":0,"Name":1,"Room_number":1,"Place":1,"Phone_number":1,"Checked_in":1,"Check_in_date":1}):
        data_values=[]
        for info in data:
            data_values.append(data[info])
        while len(headings)!=len(data_values):
            data_values.append("NULL")
        table.add_row(data_values)
    customers_text.insert(CURRENT,table)

#function to delete customers
def delete_customer():
    flag=0
    room_number=delete_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            mycol.delete_one({"Room_number":room_number})
            messagebox.showinfo("Success","Customer deleted successfully")
            delete_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found")
        delete_input.set('')

#function to update the name of a customer
def update_name():
    flag=0
    room_number=update_input.get()
    name=update_name_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            mycol.update_one({"Room_number":room_number},{"$set":{"Name":name}})
            messagebox.showinfo("Success","Customer data updated successfully")
            update_input.set('')
            update_name_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found")
        update_input.set('')

#function to update the place of a customer
def update_place():
    flag=0
    room_number=update_input.get()
    place=update_place_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            mycol.update_one({"Room_number":room_number},{"$set":{"Place":place}})
            messagebox.showinfo("Success","Customer data updated successfully")
            update_input.set('')
            update_place_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found")
        update_input.set('')

#function to update the phone number of a customer
def update_ph_no():
    flag=0
    room_number=update_input.get()
    ph_no=update_ph_no_input.get()
    for data in mycol.find():
        if data["Room_number"]==room_number:
            mycol.update_one({"Room_number":room_number},{"$set":{"Phone_number":ph_no}})
            messagebox.showinfo("Success","Customer data updated successfully")
            update_input.set('')
            update_ph_no_input.set('')
            flag=1
            break
    if flag==0:
        messagebox.showerror("Error","Room number not found")
        update_input.set('')

#function to view Vacated customers
def vacated_view_customers():
    headings=["Name","Room Number","Place","Phone Number","Check IN Date","Check OUT Date"]
    table=PrettyTable(headings)
    for data in mycol2.find({},{"_id":0,"Name":1,"Room_number":1,"Place":1,"Phone_number":1,"Check_in_date":1,"Check_out_date":1}):
        data_values=[]
        for info in data:
            data_values.append(data[info])
        table.add_row(data_values)
    vacated_customers_text.insert(CURRENT,table)

#function to refresh vacated customer details
def vacated_refresh():
    vacated_customers_text.delete('1.0',END)
    headings=["Name","Room Number","Place","Phone Number","Check IN Date","Check OUT Date"]
    table=PrettyTable(headings)
    for data in mycol2.find({},{"_id":0,"Name":1,"Room_number":1,"Place":1,"Phone_number":1,"Check_in_date":1,"Check_out_date":1}):
        data_values=[]
        for info in data:
            data_values.append(data[info])
        table.add_row(data_values)
    vacated_customers_text.insert(CURRENT,table)

window=Tk()
window.title("Hotel Management System")
window.geometry("950x450")

tab_control = ttk.Notebook(window)
tab1 = Frame(bg='#1a5276',height="450",width="900")
tab2 = Frame(bg='#1a5276',height="450",width="900")
tab3 = Frame(bg='#1a5276',height="450",width="900")
tab4 = Frame(bg='#1a5276',height="450",width="900")
tab5 = Frame(bg='#1a5276',height="450",width="900")
tab6 = Frame(bg='#1a5276',height="450",width="900")
tab_control.add(tab1,text="Add Customer")
tab_control.add(tab2,text="Check-in/Check-out")
tab_control.add(tab3,text="View Customers")
tab_control.add(tab4,text="Delete Customer")
tab_control.add(tab5,text="Update Customer Details")
tab_control.add(tab6,text="Vacated Customers")
tab_control.pack(fill="both")

#Add customers
name_label=Label(tab1,text="Name:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
name_label.pack()
name_label.place(x=324,y=24)
name_input=StringVar()
name_entry=Entry(tab1,textvariable=name_input,width='37')
name_entry.pack()
name_entry.place(x=386,y=30)
room_number_label=Label(tab1,text="Room Number:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
room_number_label.pack()
room_number_label.place(x=324,y=60)
room_number_input=StringVar()
room_number_entry=Entry(tab1,textvariable=room_number_input,width='24')    
room_number_entry.pack()
room_number_entry.place(x=461,y=66)
place_label=Label(tab1,text="Place:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
place_label.pack()
place_label.place(x=324,y=94)
place_input=StringVar()
place_entry=Entry(tab1,textvariable=place_input,width='37')    
place_entry.pack()
place_entry.place(x=386,y=100)
ph_no_label=Label(tab1,text="Ph.No:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
ph_no_label.pack()
ph_no_label.place(x=324,y=128)
ph_no_input=StringVar()
ph_no_entry=Entry(tab1,textvariable=ph_no_input,width='36')    
ph_no_entry.pack()
ph_no_entry.place(x=388,y=134)
add_customer_button=Button(tab1,text="Add Customer",command=add_customer,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
add_customer_button.pack()
add_customer_button.place(x=394,y=190)

#Check-in/Check-out
check_in_label=Label(tab2,text="Room Number:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
check_in_label.pack()
check_in_label.place(x=324,y=20)
check_in_input=StringVar()
check_in_entry=Entry(tab2,textvariable=check_in_input,width='30')
check_in_entry.pack()
check_in_entry.place(x=461,y=26)
check_in_button=Button(tab2,text="Check-in",command=check_in,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
check_in_button.pack()
check_in_button.place(x=358,y=80)
check_out_button=Button(tab2,text="Check-out",command=check_out,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
check_out_button.pack()
check_out_button.place(x=508,y=80)

#View Customers
customer_details_label=Label(tab3,text="Customer Details",bg='#1a5276',fg='#fff',font=("sans-serif",15,'underline'))
customer_details_label.pack()
customers_text=Text(tab3,height=20,width=94)
customers_text.pack()
customers_text.place(x=90,y=35)
refresh_button=Button(tab3,text="⟳",command=refresh,font=("sans-serif",13,'normal'),bg='#BBB',fg='#000')
refresh_button.pack()
refresh_button.place(x=855,y=36)
view_cutomers_button=Button(tab3,text="View Customers",command=view_customers,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
view_cutomers_button.pack()
view_cutomers_button.place(x=399,y=375)

#Delete Customers
delete_label=Label(tab4,text="Room Number:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
delete_label.pack()
delete_label.place(x=324,y=20)
delete_input=StringVar()
delete_entry=Entry(tab4,textvariable=delete_input,width='30')
delete_entry.pack()
delete_entry.place(x=461,y=26)
delete_customer_button=Button(tab4,text="Delete Customer",command=delete_customer,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
delete_customer_button.pack()
delete_customer_button.place(x=406,y=80)

#Update Customer Details
update_label=Label(tab5,text="Room Number:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
update_label.pack()
update_label.place(x=322,y=24)
update_input=StringVar()
update_entry=Entry(tab5,textvariable=update_input,width='24')    
update_entry.pack()
update_entry.place(x=459,y=30)
update_name_label=Label(tab5,text="Name:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
update_name_label.pack()
update_name_label.place(x=322,y=60)
update_name_input=StringVar()
update_name_entry=Entry(tab5,textvariable=update_name_input,width='37')
update_name_entry.pack()
update_name_entry.place(x=384,y=67)
update_name_button=Button(tab5,text="Update",command=update_name,font=("sans-serif",7,'normal'),bg='#BBB',fg='#000')
update_name_button.pack()
update_name_button.place(x=630,y=67)
update_place_label=Label(tab5,text="Place:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
update_place_label.pack()
update_place_label.place(x=322,y=94)
update_place_input=StringVar()
update_place_entry=Entry(tab5,textvariable=update_place_input,width='37')    
update_place_entry.pack()
update_place_entry.place(x=384,y=100)
update_place_button=Button(tab5,text="Update",command=update_place,font=("sans-serif",7,'normal'),bg='#BBB',fg='#000')
update_place_button.pack()
update_place_button.place(x=630,y=100)
update_ph_no_label=Label(tab5,text="Ph.No:",bg='#1a5276',fg='#fff',font=("sans-serif",15,'normal'))
update_ph_no_label.pack()
update_ph_no_label.place(x=322,y=128)
update_ph_no_input=StringVar()
update_ph_no_entry=Entry(tab5,textvariable=update_ph_no_input,width='36')    
update_ph_no_entry.pack()
update_ph_no_entry.place(x=386,y=134)
update_ph_no_button=Button(tab5,text="Update",command=update_ph_no,font=("sans-serif",7,'normal'),bg='#BBB',fg='#000')
update_ph_no_button.pack()
update_ph_no_button.place(x=630,y=134)

#View Vacated Customers
vacated_customer_details_label=Label(tab6,text="Customer Details",bg='#1a5276',fg='#fff',font=("sans-serif",15,'underline'))
vacated_customer_details_label.pack()
vacated_customers_text=Text(tab6,height=20,width=98)
vacated_customers_text.pack()
vacated_customers_text.place(x=78,y=35)
vacated_refresh_button=Button(tab6,text="⟳",command=vacated_refresh,font=("sans-serif",13,'normal'),bg='#BBB',fg='#000')
vacated_refresh_button.pack()
vacated_refresh_button.place(x=875,y=36)
vacated_view_cutomers_button=Button(tab6,text="View Customers",command=vacated_view_customers,font=("sans-serif",15,'normal'),bg='#BBB',fg='#000')
vacated_view_cutomers_button.pack()
vacated_view_cutomers_button.place(x=399,y=375)

window.mainloop()
