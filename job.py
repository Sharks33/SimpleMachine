class Job:
    # Execute when on

    def __init__(self, name):
        self.name = name

    def execute(self, status):
        if status == "ON":
            return '{} MACHINE ONLINE'.format(self.name)

