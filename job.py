class Job:

    def __init__(self, name):
        self.name = name

    def execute(self):
        return '{} MACHINE ONLINE'.format(self.name)

