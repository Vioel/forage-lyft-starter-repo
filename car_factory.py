from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

class CarFactory():
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Calliope(last_service_date,current_mileage,last_service_mileage)
        return car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Glissade(last_service_date,current_mileage,last_service_mileage)
        return car
    
    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        car = Palindrome(last_service_date, warning_light_on)
        return car

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Rorschach(last_service_date,current_mileage,last_service_mileage)
        return car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        car = Thovex(last_service_date,current_mileage,last_service_mileage)
        return car
