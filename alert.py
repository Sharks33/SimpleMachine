import pymsgbox
from job import Job

class Alert(Job):
    # Execute when on

    def execute(self, status):
        if status == "ON":
            pymsgbox.alert('The machine is now {}'.format(status), 'Alert')
            return "An alert has been sent to the user"
