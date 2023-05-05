from tkinter import *
from tkcalendar import Calendar
app=Tk()
app.geometry("420x420")
app.title("calender Date Picker App")
app.config(bg="darkorange")
calenderObj=Calendar(app,selectmode="day",year=2022,month=1,date=1)
calenderObj.pack(pady=45)
def fetch_date():
    date.config(text="selected date is : "+calenderObj.get_date())


button=Button(app,text="select Date",bg="black",fg="white",command=fetch_date)
button.pack()
date=Label(app,text="",bg="black",fg="white")
date.pack(pady=20)

app.mainloop()