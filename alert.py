import pymsgbox
from job import Job

class Alert(Job):

    def execute(self):
        pymsgbox.alert('The machine has stoped', 'Alert')
        return "An alert has been sent to the user"
