from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)

        return Car(capulet, spindler)

    def create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)

        return Car(willoughby, spindler)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        sternman = SternmanEngine(warning_light_on)
        spindler = SpindlerBattery(last_service_date, current_date)
        return Car(sternman, spindler)

    def create_rorschach(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        return Car(willoughby, nubbin)

    def create_thovex(
        current_date, last_service_date, current_mileage, last_service_mileage
    ):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        return Car(capulet, nubbin)
