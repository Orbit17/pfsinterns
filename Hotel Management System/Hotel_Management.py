import tkinter as tk
import customtkinter
from tkinter import *
from tkcalendar import Calendar, DateEntry

# MySQL connection code
customerInfo = {}

#checks if reservation is found
def isReservation(key):
    if key in customerInfo:
        return True
    return False

def add():
    # Creates a new window on top of the main menu
    addWindow = customtkinter.CTkToplevel(root)
    addWindow.title("Add a Reservation")
    addWindow.geometry("350x450")

    # Title
    heading2 = customtkinter.CTkLabel(addWindow, text="Add a Reservation", font=('Helvetica', 20))
    heading2.pack(padx = 10, pady = 20)

    # Prompt User for info
    firstName = customtkinter.CTkEntry(master=addWindow, placeholder_text="First Name: ")
    firstName.pack(padx = 10, pady = 10)

    lastName = customtkinter.CTkEntry(master=addWindow, placeholder_text="Last Name: ")
    lastName.pack(padx = 10, pady = 10)

    phoneNum = customtkinter.CTkEntry(master=addWindow, placeholder_text="Phone Number: ")
    phoneNum.pack(padx = 10, pady = 10)

    email = customtkinter.CTkEntry(master=addWindow, placeholder_text="Email: ")
    email.pack(padx = 10, pady = 10)
 
    checkIn = DateEntry(addWindow, font=('Helvetica', 15))
    checkIn.pack(padx = 10, pady = 10)

    checkOut = DateEntry(addWindow, font=('Helvetica', 15))
    checkOut.pack(padx = 10, pady = 10)

    numGuests = tk.Spinbox(addWindow, from_=1, to=8, width=5, font=('Helvetica', 20), justify="center")
    numGuests.pack(padx = 10, pady = 10)

    #Retrieve Entered Info
    def getAdd():
        firstNameEntered = firstName.get()
        lastNameEntered = lastName.get()
        phoneNumEntered = phoneNum.get()
        emailEntered = email.get()
        checkInDate = checkIn.get_date()
        checkOutDate = checkOut.get_date()
        guestCount = numGuests.get()

        #Add to dictionary
        customerInfo[emailEntered] = [firstNameEntered.capitalize(), lastNameEntered.capitalize(), phoneNumEntered, emailEntered,
                               checkInDate, checkOutDate, guestCount]
        print(customerInfo[emailEntered])

    submit = customtkinter.CTkButton(addWindow, text="Add Reservation", command=getAdd)
    submit.pack(padx = 20, pady = 20)
    
def update():
    updateWindow = customtkinter.CTkToplevel(root)
    updateWindow.title("Update Reservation")
    updateWindow.geometry("350x450")

    checkEmail = customtkinter.CTkEntry(updateWindow, placeholder_text="Enter registered email")
    checkEmail.pack()
    
    def getUpdate():
        if(isReservation(checkEmail.get())):
            add()
            del customerInfo[checkEmail.get()]

        else:
            print("Reservation not found")

    submit = customtkinter.CTkButton(updateWindow, text="Find Reservation", command=getUpdate)
    submit.pack(padx = 20, pady = 20)               
        

def cancel():
    cancelWindow = customtkinter.CTkToplevel(root)
    cancelWindow.title("Cancel Reservation")
    cancelWindow.geometry("350x450")

    checkEmail = customtkinter.CTkEntry(cancelWindow, placeholder_text="Enter registered email")
    checkEmail.pack()   

    def cancelReservation():
        key = checkEmail.get()

        if key in customerInfo:
            del customerInfo[key]
            print(customerInfo)
        else:
            print("Reservation not found")

    submit = customtkinter.CTkButton(cancelWindow, text="Cancel Reservation", command=cancelReservation)
    submit.pack(padx = 20, pady = 20)   

root = customtkinter.CTk()
customtkinter.set_appearance_mode("System")
root.title("Hotel Management System")
root.geometry("500x350")

frame = customtkinter.CTkFrame(master = root)
frame.pack(padx = 30, pady = 20, fill="both", expand=True)

heading = customtkinter.CTkLabel(master=frame, text="Hotel Management System")
heading.pack(padx = 10, pady = 15)

addCustomer = customtkinter.CTkButton(master = frame, text="Add a Reservation", command=add)
addCustomer.pack(padx = 15, pady = 15)

updateReservation = customtkinter.CTkButton(master = frame, text="Update a Reservation", command=update)
updateReservation.pack(padx = 15, pady = 15)

cancelReservation = customtkinter.CTkButton(master = frame, text="Cancel a Reservation", command=cancel)
cancelReservation.pack(padx = 15, pady = 15)

root.mainloop()
