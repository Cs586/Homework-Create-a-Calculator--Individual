import csv

from pprint import pprint


# def ClassFactory(class_name, dictionary):
#    return type(class_name, (object,), dictionary)

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

    #    def return_data_as_objects(self, class_name):
    #        objects = []
    #        for row in self.data:
    #            objects.append(ClassFactory(class_name, row))
    #        return objects

    def return_data_as_subtraction(self):
        subtraction_data = []
        for row in self.data_s:
            subtraction_data.append(row)
        return subtraction_data

    def return_data_as_division(self):
        division_data = []
        for row in self.data_d:
            division_data.append(row)
        return division_data

    def return_data_as_addition(self):
        addition_data = []
        for row in self.data_d:
            addition_data.append(row)
        return addition_data

    def return_data_as_mul(self):
        mul_data = []
        for row in self.data_m:
            mul_data.append(row)
        return mul_data

    def return_data_as_sq(self):
        sq_data = []
        for row in self.data_sq:
            sq_data.append(row)
        return sq_data