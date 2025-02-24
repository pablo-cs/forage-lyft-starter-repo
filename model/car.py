from abc import ABC, abstractmethod

from servicable import Serviceable


class Car(Serviceable, ABC):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery = battery
        self.tires = tires

    def needs_service(self):
        return (
            self.engine.needs_service()
            or self.battery.needs_service()
            or self.tires.need_service()
        )
