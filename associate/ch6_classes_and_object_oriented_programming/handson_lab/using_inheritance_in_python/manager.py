
from employee import Employee

class Manager(Employee):
    def __init__(self, name, email_address, titile, phone_number=None):
        super().__init__(name, email_address, titile, phone_number)
        self.meetings = []
    
    def schedule_meeting(self, invitees, time):
        self.meetings.append({"invitees": invitees, "time": time})
        # sort it every time we schedule a meeting
        self.meetings.sort(key=lambda m: m["time"])
    
    def run_next_meeting(self):
        return self.meetings.pop(0)
    
    

