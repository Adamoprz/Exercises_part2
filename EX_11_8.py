# TODO LOGGING
import logging
logging.basicConfig(filename='tank-log.log', level=logging.INFO,
                    format='%(message)s')


class Tank:

    def __init__(self) -> None:
        """init class with name and volume of the tank"""
        self.t = {}

    def add_tank(self, name: str, volume: float) -> None:
        ifsuccess = 'successful'
        if name not in self.t:
            self.t[name] = (0, volume)
        else:
            ifsuccess = 'unsuccessful'
        logging.info(name + ", add_tank, "+ifsuccess)

    def pourwater(self, name: str, volumeadd: float) -> None:
        """pour the water function"""
        ifsuccess = 'successful'
        value_water = self.t[name][0] + volumeadd
        if self.t[name][1] < value_water:
            value_water = self.t[name][1]
            ifsuccess = 'unsuccessful'
        self.t[name] = (value_water, self.t[name][1])
        logging.info(name + ", pourwater, " + ifsuccess)

    def pouroutwater(self, name: str, volumeadd: float) -> None:
        """pour out the water function"""
        ifsuccess = 'successful'
        value_water = self.t[name][0] - volumeadd
        if 0 > value_water:
            value_water = 0
        self.t[name] = (value_water, self.t[name][1])
        logging.info(name + ", pouroutwater, " + ifsuccess)

    def transferwater(self, name1, name2) -> None:
        """function of pouring the water from one tank to another"""
        ifsuccess = 'successful'
        new_value = self.t[name1][0] + self.t[name2][0]
        if new_value <= 150:
            self.t[name2] = (new_value, self.t[name2][1])
            self.t[name1] = (0, self.t[name1][1])
        else:
            ifsuccess = 'unsuccessful'
        logging.info(name2 + ", transferwater, " + ifsuccess)

    def find_tank_max_water(self) -> None:
        """function that find tank with the greatest amount of the water """
        return max(self.t.keys(), key=(lambda k: self.t[k]))

    def find_tank_max_used(self) -> None:
        """function that find tank which is most filled """
        return max(self.t.keys(), key=(lambda k: self.t[k]))

    def find_tank_empty(self) -> list:
        """find empty tank function"""
        empty_tanks = []
        for key in self.t.keys():
            if self.t[key][0] == 0:
                empty_tanks.append(key)
        return empty_tanks

    def analyze_logs(self):
        all_ops = ['add_tank', 'pourwater', 'pouroutwater', 'transferwater']
        all_logs = []
        with open('tank-log.log') as f:
            for lines in f.readlines():
                line = lines.strip().split(", ")
                all_logs.append(line)
        all_el = {}
        for element in all_logs:
            if element[0] not in all_el.keys():
                all_el[element[0]] = {}
                for el in all_ops:
                    all_el[element[0]][el] = [0, 0]
            if element[0] in all_el.keys():
                if element[2] == 'successful':
                    suc = all_el[element[0]][element[1]][0] + 1
                    unsuc = all_el[element[0]][element[1]][1]
                else:
                    suc = all_el[element[0]][element[1]][0]
                    unsuc = all_el[element[0]][element[1]][1] + 1
                all_el[element[0]][element[1]] = [suc, unsuc]
        return all_el

    def find_most_unsuccessful(self):
        """function that find tank with the greatest number of unsuccessful operations."""
        init = self.analyze_logs()
        tanks = {}
        for key in init.keys():
            if key not in tanks.keys():
                tanks[key] = 0
            for el in init[key].keys():
                tanks[key] = tanks[key] + init[key][el][1]
        return max(tanks.items(), key=lambda k: k[1])

    def find_most_used(self, op_type) -> (str, int):
        """function that find tank with the greatest number of operations of the given type."""
        init = self.analyze_logs()
        tanks = {}
        for key in init.keys():
            tanks[key] = sum(init[key][op_type])
        return max(tanks.items(), key=lambda k: k[1])

    def show_tank(self):
        return self.t

'''
t1 = Tank()
t1.add_tank('tank1', 150)

t1.add_tank('tank9', 150)
print(t1.show_tank())
t1.pourwater('tank1', 20)
print(t1.show_tank())
t1.pourwater('tank1', 40)
print(t1.show_tank())
t1.pourwater('tank1', 20)
print(t1.show_tank())
t1.pouroutwater('tank1', 20)
print(t1.show_tank())
t1.pouroutwater('tank1', 20)
print(t1.show_tank())
t1.add_tank('tank2', 150)
t1.pourwater('tank2', 50)
print(t1.show_tank())
print(t1.find_tank_max_water())
t1.transferwater('tank1', 'tank2')
print(t1.show_tank())
print(t1.find_tank_empty())
t1.add_tank('tank2', 150)
t1.add_tank('tank9', 150)

print(t1.analyze_logs())
print(t1.find_most_unsuccessful())
print(t1.find_most_used('pourwater'))
'''