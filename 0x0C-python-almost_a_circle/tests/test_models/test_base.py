import unittest
import csv
from models.base import Base
from models.rectangle import Rectangle

"""creating a test that inherits from unittest.TestCase"""
class TestBase(unittest.TestCase):

    def test_unit(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)
        """ b1 = Base(10)
        self.assertEqual(b1.id, 10)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        """

    def test_to_json_string(self):
        """chech if the method returns the correct JSON string
        """
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([{"id": 1},
            {"id": 2}]), '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string(
            '[{"id": 1}, {"id": 2}]'), [{"id": 1}, {"id": 2}])
    
    def test_save_to_file(self):
        """creating the list of instance of the class"""
        b1 = Base(1)
        b2 = Base(2)
        b3 = Base(3)
        Base.save_to_file([b1, b2, b3])
        """opening the file that was created and read it
        content"""
        import json
        with open('Base.json', 'r') as f:
            json_lists = f.read()
        self.assertEqual(json.loads(json_lists),
                [{"id": b1.id}, {"id": b2.id}, {"id": b3.id}])

    def setUp(self):
        """Create some instances of Rectangle and save
        them to a JSON file
        """
        self.rectangles = [Rectangle(2, 3), Rectangle(4, 5), Rectangle(6, 7)]
        Rectangle.save_to_file(self.rectangles)

    def test_load_from_file(self):
        """Load the instances from the JSON file and
        compare them to the original list
        """
        loaded_rectangles = Rectangle.load_from_file()
        self.assertListEqual(loaded_rectangles, self.rectangles)

    def test_save_to_file_csv(self):
        r1 = Rectangle(2, 3, 1, 2, 1)
        r2 = Rectangle(4, 5, 3, 4, 2)
        r3 = Rectangle(6, 7, 5, 6, 3)

        Rectangle.save_to_file_csv([r1, r2, r3])

        with open("Rectangle.csv", "r") as f:
            reader = csv.reader(f)
            csv_list = list(reader)
            self.assertEqual(csv_list,
                         [[str(r1.id), "2", "3", "1", "2"],
                          [str(r2.id), "4", "5", "3", "4"],
                          [str(r3.id), "6", "7", "5", "6"]])

    def tearDown(self):
        """Delete the temporary JSON file
        """
        import os
        os.remove("Rectangle.json")
if __name__ == "__main__":
    unittest.main()
