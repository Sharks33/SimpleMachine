from job import Job

class SystemStatus(Job):
    # Execute when on or off

    @classmethod
    def is_running(cls, status):
        return "The system is currently powered {} ".format(status)

    def execute(self, status):
        return SystemStatus.is_running(status)
