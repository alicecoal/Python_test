bus_list = []
class Autobus:
    def __init__(self, route_number, start_point, end_point, travel_time):
        self.start_point = start_point
        self.end_point = end_point
        self.route_number = route_number
        self.travel_time = travel_time

    def info(self):
        print("--------------------")
        print("Route number: ", self.route_number)
        print("Starting point: ", self.start_point)
        print("Ending point: ", self.end_point)
        print("Travel time: ", self.travel_time)
        print("--------------------")

    def set_start_point(self, start_point):
        self.start_point = start_point

    def set_end_point(self, end_point):
        self.end_point = end_point

    def set_route_number(self, route_number):
        self.route_number = route_number

    def set_travel_time(self, travel_time):
        self.travel_time = travel_time

    def get_start_point(self):
        return self.start_point

    def get_end_point(self):
        return self.end_point

    def get_route_number(self):
        return self.route_number

    def get_travel_time(self):
        return self.travel_time

def create_autopark():
    global bus_list
    kol = int(input("Enter the number of buses: "))
    print("--------------------")
    for i in range(kol):
         route_number = input(f'Enter the route number of {i+1} bus: ')
         start_point = input(f'Enter the starting point of {i+1} bus: ')
         end_point = input(f'Enter the ending point of {i+1} bus: ')
         travel_time = input(f'Enter the travel time of {i+1} bus: ')
         bus = Autobus(route_number, start_point, end_point, travel_time)
         bus_list.append(bus)
         print("--------------------")
    save_bus_list_to_file(bus_list)

def save_bus_list_to_file(bus_list):
    with open('my_file.txt', 'w') as file:
        for bus in bus_list:
            file.write(f"{bus.get_route_number()},{bus.get_start_point()},{bus.get_end_point()},{bus.get_travel_time()}\n")

def show_autopark():
    global bus_list
    bus_list = []
    try:
        with open('my_file.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                route_number, start_point, end_point, travel_time = data
                bus = Autobus(route_number, start_point, end_point, travel_time)
                bus_list.append(bus)
        for bus in bus_list:
             bus.info()
    except FileNotFoundError:
        print("File not found")

def sort_by_number():
    buses = sorted(bus_list, key=lambda bus: bus.get_route_number(), reverse=True)
    for bus in buses:
        bus.info()


def search_by_point(stop_name):
    matching_buses = [bus for bus in bus_list if stop_name in bus.get_start_point() or stop_name in bus.get_end_point()]
    for bus in matching_buses:
        bus.info()

create_autopark()
show_autopark()
search_by_point("Prague")
sort_by_number()
