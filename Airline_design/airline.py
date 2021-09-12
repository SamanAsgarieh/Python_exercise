import time
from threading import Thread
class airline(Thread):
    def __init__(self):
        super().__init__()
        self.logs = []
        self.stop=False
        # flight_number=None

    def take_off(self,flight_number):
        self.logs.append('landing, Flight number: '+str(flight_number)+" ,Time: "+str(time.time()))
        return

    def landing(self,flight_number):
        self.logs.append('landing, Flight number: '+str(flight_number)+" ,Time: "+str(time.time()))
        return

    def run(self):
        while not self.stop:
            cmd = input('please enter the flight number: ')
            log_type = input('Please select 1 for landing and 2 for takeoff')
            if log_type!="Stop":
                self.landing(cmd) if log_type==1 else self.take_off(cmd) 
            else:
                print(self.logs)
                

airline_logger = airline()
airline_logger.start()
