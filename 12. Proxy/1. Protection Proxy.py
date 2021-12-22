"""
Simplest proxy people build - Protection proxy

Is used for access control
e.g. the proxy that checks if user is logged in

So this thing u can add after. U designed the system and then u can add additional functionality
building the proxy on top of that
"""


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        print(f"Car is being driven by {self.driver.name}")


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)  # you should use this car via proxy and not directly

    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print("Driver too young")


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    driver = Driver("John", 12)
    # car = Car(driver)
    car = CarProxy(driver) # the only change we need to perform - change class. All other things should work
    car.drive()
    # imagine we have tested everything and
    # and now we dont want to make age control
    # as we cant modify drive method
    # you can build a proxy
