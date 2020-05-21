from pymsgbox import *
'''
import tkinter
import calendar
import tkcalendar
'''

def test():	
    #calendar = print(showCal())
    #showCal()
    alert(text=showCal(),title='Test',button='OK') # second alert won't appear until the first one is exited
    #showCal()    
# Function for showing the calendar of the given year 

# import all methods and classes from the tkinter    
from tkinter import *
#from tkinterhtml import HtmlFrame
from tk_html_widgets import HTMLLabel
# import calendar module 
import calendar 

# Function for showing the calendar of the given year 
def showCal() :
    from tkinter import ttk
    from datetime import date
    from tkcalendar import DateEntry
    from datetime import date

    today = date.today()
    today = str(today).split('-')
    i = 0
    for each in today:
        today[i] = int(each)
        i += 1
    root = tk.Tk()
    cal = DateEntry(root, width=12, year=today[0], month=today[1], day=today[2], 
    background='darkblue', foreground='white', borderwidth=2,button='OK')
    cal.pack(padx=10, pady=10)
    date = cal.get_date()
    root.mainloop()
    return date
    '''
    c = calendar.HTMLCalendar(calendar.SUNDAY)
    s = c.formatmonth(2020,5)
    root = tk.Tk()
    #html_label = HTMLLabel(root, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
    html_label = HTMLLabel(root, html="<html>{}</html>".format(s))
    html_label.pack(fill="both", expand=True)
    html_label.fit_height()
    root.mainloop()
    return s
    '''
'''
    # Create a GUI window 
    new_gui = Tk() 
      
    # Set the background colour of GUI window 
    new_gui.config(background = "white") 
  
    # set the name of tkinter GUI window  
    new_gui.title("CALENDER") 
  
    # Set the configuration of GUI window 
    new_gui.geometry("300x300") 
  
    # get method retu rns current text as string 
    fetch_year = int(2020) 
    fetch_month = int(5)
  
    # calendar method of calendar module return 
    # the calendar of the given year . 
    #cal_content = calendar.month(fetch_year,fetch_month,2,1) 
    #cal_content = calendar.TextCalendar.formatmonth(2020,'May',w=100,l=100)
    # Create a label for showing the content of the calender 
    #cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold") 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
    #cal_year.grid(row = 5, column = 1, padx = 20) 
     
    c = calendar.HTMLCalendar(calendar.SUNDAY)
    s = c.formatmonth(2020,5)
    #print(s)
    return s
    # start the GUI  
    #new_gui.mainloop() 
    #return

    root = tk.Tk()
    html_label = HTMLLabel(root, html='<h1 style="color: red; text-align: center"> Hello World </H1>')
    html_label.pack(fill="both", expand=True)
    html_label.fit_height()
    root.mainloop()
    '''