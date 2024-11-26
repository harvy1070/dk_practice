class Ferrari:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def start(self):
        self.driver.engine_start("부르르릉", self)

class Porsche:
    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def start(self):
        self.driver.engine_start("부아아앙", self)

class Driver:
    def __init__(self):
        self.ferrari = Ferrari()
        self.porsche = Porsche()
        self.ferrari.set_driver(self)
        self.porsche.set_driver(self)

    def engine_start(self, sound, car):
        if car == self.ferrari:
            print(f"페라리 시동 걸림: {sound}")
        else:
            print(f"포르쉐 시동 걸림: {sound}")

driver = Driver()
driver.ferrari.start()
driver.porsche.start()