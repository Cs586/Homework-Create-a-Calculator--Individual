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

    def test_mul(self):
        test_data_mul = CsvReader("/src/CsvData/Multiplication.csv").return_data_as_mul()
        for row in test_data_mul:
            result_mul = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), result_mul)
            self.assertEqual(self.calculator.result, result_mul)

    def test_sq(self):
        test_data_mul = CsvReader("/src/CsvData/Square.csv").return_data_as_mul()
        for row in test_data_mul:
            result_sq = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1']), result_sq)
            self.assertEqual(self.calculator.result, result_sq)


if __name__ == '__main__':
    unittest.main()
