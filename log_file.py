import logging
import time
from job import Job

class LogFile(Job):
    # Execute when off

    @classmethod
    def sys_off_time(cls):
        sys_off_date = time.strftime('%d.%m.%Y')
        sys_off_time = time.strftime('%H:%M:%S')
        logging.basicConfig(filename='sys_log.log',level=logging.DEBUG)
        logging.info(' **********SYSTEM POWERED OFF**********')
        logging.info(' Date: {}'.format(sys_off_date))
        logging.info(' Time: {}'.format(sys_off_time))
        logging.info('')
        return "System shutdown information has been logged to sys_log.log"

    def execute(self, status):
        if status == "OFF":
            return LogFile.sys_off_time()
