from abc import ABC

from car import Car

from datetime import datetime

class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = datetime.today().date()

    def battery_should_be_serviced(self):
        return self.current_date.year - self.last_service_date.year >= 2