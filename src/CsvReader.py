import csv

from pprint import pprint


def ClassFactory(class_name, dictionary):
    return type(class_name, (object,), dictionary)


class CsvReader(object):
    data = []
    data_s = []
    data_d = []
    data_a = []
    data_sq = []
    data_sr = []
    data_m = []

    def __init__(self, filepath):
        with open(filepath) as text_data:
            csv_data = csv.DictReader(text_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
        pass

    def return_data_as_objects(self, class_name):
        objects = []
        for row in self.data:
            objects.append(ClassFactory(class_name, row))
        return objects

    def return_data_as_subtraction(self):
        return self.data_s

    def return_data_as_division(self):
        return self.data_d

    def return_data_as_addition(self):
        return self.data_a

    def return_data_as_mul(self):
        return self.data_m

    def return_data_as_sq(self):
        return self.data_sq

    def return_data_as_sqr(self):
        return self.data_sr
