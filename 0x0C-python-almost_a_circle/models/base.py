#!/usr/bin/python3
"""importing"""
import json
import random
import csv
import turtle


class Base:
    """initialazing the class of Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """public instance attribute id.
        Arg:
            id(int): integer value to manage the id.
        Return:
            nothing.
        """
        if id is not None:
            """self.id = id"""
            self.id = random.randint(1, 100)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_dictionary(self):
        dict = {}
        for key, value in self.__dict__.items():
            dict[key] = value
        return dict

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        empty_list = []
        if json_string is None:
            return empty_list
        else:
            empty_list = json.loads(json_string)
            return empty_list

    @classmethod
    def save_to_file(cls, list_objs):
        """the JSON string representesantion of
        list_objs to afile."""
        if not list_objs:
            json_lists = "[]"
        else:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_lists = cls.to_json_string(dict_list)
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(json_lists)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise TypeError("Invalid class name")
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                json_list = json.loads(json_string)
                for dictionary in json_list:
                    instance_list.append(cls.create(**dictionary))
        except FileNotFoundError:
            pass
        return instance_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        if not list_objs:
            csv_list = []
        else:
            class_name = cls.__name__
            if class_name == "Rectangle":
                attrs = ["id", "width", "height", "x", "y"]
            elif class_name == "Square":
                attrs = ["id", "size", "x", "y"]
            else:
                return
            csv_list = [[getattr(obj, attr)
                        for attr in attrs] for obj in list_objs]
        filename = class_name + ".csv"
        with open(filename, "w") as f:
            writer = csv.writer(f)
            writer.writerows(csv_list)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a list of objects from a CSV file."""
        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, "r") as f:
                reader = csv.reader(f)
                class_name = cls.__name__
                if class_name == "Rectangle":
                    attrs = ["id", "width", "height", "x", "y"]
                elif class_name == "Square":
                    attrs = ["id", "size", "x", "y"]
                else:
                    return
                """convert each row to a dictionary using zip method"""
                for row in reader:
                    dict_obj = dict(zip(attrs, [int(x) for x in row]))
                    instance_list.append(cls.create(**dict_obj))
        except FileNotFoundError:
            pass
        return instance_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
