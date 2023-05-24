from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class CarFactory:
    def create_calliope(
        current_date, last_service_date, current_mileage, last_service_mileage, tires
    ):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)

        return Car(capulet, spindler, tires)

    def create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage, tires
    ):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)

        return Car(willoughby, spindler, tires)

    def create_palindrome(current_date, last_service_date, warning_light_on, tires):
        sternman = SternmanEngine(warning_light_on)
        spindler = SpindlerBattery(last_service_date, current_date)
        return Car(sternman, spindler, tires)

    def create_rorschach(
        current_date, last_service_date, current_mileage, last_service_mileage, tires
    ):
        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        return Car(willoughby, nubbin, tires)

    def create_thovex(
        current_date, last_service_date, current_mileage, last_service_mileage, tires
    ):
        capulet = CapuletEngine(current_mileage, last_service_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        return Car(capulet, nubbin, tires)
