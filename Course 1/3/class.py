import os
import csv

FILE_EXT = ('.jpg', '.jpeg', '.png', '.gif')


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        filename, file_extension = os.path.splitext(self.photo_file_name)
        return file_extension


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = "car"
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = "truck"

        try:
            body_length, body_width, body_height = body_whl.split("x")
            self.body_length = float(body_length)
            self.body_width = float(body_width)
            self.body_height = float(body_height)
        except ValueError:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        return float(self.body_length) * float(self.body_width) * float(self.body_height)


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        CarBase.__init__(self, brand, photo_file_name, carrying)
        self.car_type = "spec_machine"
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    cars = []

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            car_list.append(row)

    for item in car_list:
        # item = item.split(";")
        if len(item) > 0:
            if item[0] == 'car':
                try:
                    brand = item[1]
                    photo_file_name = item[3]

                    filename, file_extension = os.path.splitext(photo_file_name)
                    right_file = file_extension in FILE_EXT
                    
                    if len(brand) > 0 and len(photo_file_name) > 0 and right_file:
                        passenger_seats_count = int(item[2])
                        carrying = float(item[5])
                        cars.append(Car(brand, photo_file_name, carrying, passenger_seats_count))
                except ValueError:
                    pass
            elif item[0] == 'truck':
                try:
                    brand = item[1]
                    photo_file_name = item[3]
                    filename, file_extension = os.path.splitext(photo_file_name)
                    right_file = file_extension in FILE_EXT
                    if len(brand) > 0 and len(photo_file_name) > 0 and right_file:
                        carrying = float(item[5])
                        body_whl = item[4]
                        cars.append(Truck(brand, photo_file_name, carrying, body_whl))
                except ValueError:
                    pass
            elif item[0] == 'spec_machine':
                try:
                    brand = item[1]
                    photo_file_name = item[3]
                    extra = item[6]
                    filename, file_extension = os.path.splitext(photo_file_name)
                    right_file = file_extension in FILE_EXT
                    if len(brand) > 0 and len(photo_file_name) > 0 and len(extra) > 0 and right_file:
                        carrying = float(item[5])
                        cars.append(SpecMachine(brand, photo_file_name, carrying, extra))
                except ValueError:
                    pass

    return cars
