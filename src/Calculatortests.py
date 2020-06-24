import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_division(self):
        test_data = CsvReader("src/CsvData/Division.csv").return_data_as_division()
        for row in test_data:
            result = round(float(row['Result']), 9)
            self.assertEqual(self.calculator.division(row['Value 1'], row['Value 2']), result)
            self.assertEqual(self.calculator.result, result)

    def test_subtraction(self):
        test_data_sub = CsvReader("/src/CsvData/Subtraction.csv").return_data_as_subtraction()
        for row in test_data_sub:
            result_sub = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result_sub)
            self.assertEqual(self.calculator.result, result_sub)

    def test_addition(self):
        test_data_add = CsvReader("/src/CsvData/Addition.csv").return_data_as_addition()
        for row in test_data_add:
            result_add = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result_add)
            self.assertEqual(self.calculator.result, result_add)


if __name__ == '__main__':
    unittest.main()
