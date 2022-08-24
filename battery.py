from sqlite3 import Date
from xmlrpc.client import DateTime


class battery:
    def __init__(self, last_service_date:Date, current_date:Date):
        self.last_service_date:Date
        self.current_date:Date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < DateTime.today().date():
            return True
        else:
            return False
