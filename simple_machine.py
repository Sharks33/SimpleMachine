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
job_2 = Alert("SYSTEM ALERT: ")
job_3 = LogFile("SYSTEM LOG: ")
job_4 = SystemStatus("SYSTEM STATUS: ")

status = "OFF"

Job.jobs = [job_1, job_2, job_3, job_4]

def toggle_button():
    global status

    if status == "OFF":
        status = "ON"
        t_btn.config(text='POWER OFF MACHINE')
    else:
        status = "OFF"
        t_btn.config(text='POWER ON MACHINE')

    for j in Job.jobs:
        output = j.execute(status)
        if output:
            print output

    return "Button Pressed"

root = sm.Tk()
t_btn = sm.Button(text="POWER OFF", width=64, height=16, command=toggle_button)
t_btn.pack(pady=5)
root.mainloop()

try:
    toggle_button()
except:
    print "*****THE MACHINE HAS GONE OFFLINE*****"
