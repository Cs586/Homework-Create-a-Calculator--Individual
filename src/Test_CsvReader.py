import unittest
from CsvReader import CsvReader, ClassFactory
from pprint import pprint
from pathlib import Path


def absolutepath(filepath):
    relative = Path(filepath)
    return relative.absolute()


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = CsvReader('src/CsvData/Addition.csv')

    def test_return_data_as_objects(self):
        people = self.csv_reader.return_data_as_subtraction
        self.assertIsInstance(people, list)
        test_class = ClassFactory('person', self.csv_reader.data[0])

        for person in people:
            self.assertEqual(person.__name__, test_class.__name__)
            pprint(vars(people))


if __name__ == '__main__':
    unittest.main()
