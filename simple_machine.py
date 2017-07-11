from job import Job
from alert import Alert
from log_file import LogFile
from system_status import SystemStatus
import tkMessageBox
try:
    import Tkinter as sm # Python2
except ImportError:
    import tkinter as sm # Python3


job_1 = Job("SYSTEM PROCEDURE: ")
job_3 = Alert("SYSTEM ALERT: ")
job_4 = LogFile("SYSTEM LOG: ")
job_5 = SystemStatus("SYSTEM STATUS: ")

Job.jobs = [job_1, job_3, job_4, job_5]

def toggle_button():

    if t_btn.config('text')[-1] == 'POWER OFF':
        t_btn.config(text='POWER ON')
        for j in Job.jobs:
            print j.execute()
    else:
        t_btn.config(text='POWER OFF')
        print job_5.execute()

    return "Button Pressed"

root = sm.Tk()
t_btn = sm.Button(text="POWER OFF", width=64, height=16, command=toggle_button)
t_btn.pack(pady=5)
root.mainloop()

try:
    toggle_button()
except:
    print "*****THE MACHINE HAS GONE OFFLINE*****"
