from job import Job

class SystemStatus(Job):

    global status
    status = "ON"

    @classmethod
    def is_running(cls, status, i=[0]):
        i[0] += 1
        if i[0] % 2 == 0:
            status = "ON"
        else:
            status = "OFF"
        return "The system is currently powered {} ".format(status)

    def execute(self):
        return SystemStatus.is_running(status)
