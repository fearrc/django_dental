'''
from django.db import models

# Create your models here.
class Calendar(models.Model):
	day = models.DateField(u'Day of the Event', help_text = u'Day of the Event')

	class Meta:
	    verbose_name = u'Scheduling'
	    verbose_name_plural = u'Scheduling'
'''	    
'''
from pymsgbox import *
import tkinter
import calendar
import tkcalendar
'''

def test():
	#alert(text='Testing',title='This is a test',button='OK')
	#alert(text='Second Alert',title='Test',button='OK') # second alert won't appear until the first one is exited
	showCal()

# Function for showing the calendar of the given year 

# import all methods and classes from the tkinter    
from tkinter import *
  
# import calendar module 
import calendar 

# Function for showing the calendar of the given year 
def showCal() : 
  
    # Create a GUI window 
    new_gui = Tk() 
      
    # Set the background colour of GUI window 
    new_gui.config(background = "white") 
  
    # set the name of tkinter GUI window  
    new_gui.title("CALENDER") 
  
    # Set the configuration of GUI window 
    new_gui.geometry("550x600") 
  
    # get method returns current text as string 
    fetch_year = int(2020) 
    fetch_month = int(5)
  
    # calendar method of calendar module return 
    # the calendar of the given year . 
    cal_content = calendar.month(fetch_year,fetch_month,2,1) 
  
    # Create a label for showing the content of the calender 
    cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold") 
  
    # grid method is used for placing  
    # the widgets at respective positions  
    # in table like structure. 
    cal_year.grid(row = 5, column = 1, padx = 20) 
      
    # start the GUI  
    new_gui.mainloop() 