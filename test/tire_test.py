import unittest
from model.tire.carrigan_tires import CarriganTire
from model.tire.octoprime_tires import OctoprimeTire


class TestCarrigan(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_arr = [0.3, 0.2, 0.9, 0.1]
        tires = CarriganTire(tires_arr)
        self.assertTrue(tires.needs_service())

    def test_battery_should_not_be_serviced(self):
        tires_arr = [0.3, 0.2, 0.8, 0.1]
        tires = CarriganTire(tires_arr)

        self.assertFalse(tires.needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tires_should_be_serviced(self):
        tires_arr = [0, 1, 2, 3]
        tires = OctoprimeTire(tires_arr)
        self.assertTrue(tires.needs_service())

    def test_tires_should_not_be_serviced(self):
        tires_arr = [0, 1, 2, 0]
        tires = OctoprimeTire(tires_arr)
        self.assertFalse(tires.needs_service())


if __name__ == "__main__":
    unittest.main()
