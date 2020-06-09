#!/usr/bin/python3
"""Module for class Base"""
import csv
import json
import turtle


class Base:
    """Parent class in the project"""

    # Number objects created
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor Base class"""
        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects

        self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert dictionary into json string"""
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save a list of object in a json file"""
        dicts = []
        if list_objs:
            for ins in list_objs:
                dicts.append(cls.to_dictionary(ins))

        json_string = Base.to_json_string(dicts)
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return list Pyhton objects from json_string"""
        if not json_string:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Create instances from json file"""
        path = cls.__name__ + '.json'
        objects = []

        try:
            with open(path) as f:
                contents = f.read()
        except:
            return objects

        json_data = Base.from_json_string(contents)

        for obj in json_data:
            objects.append(cls.create(**obj))

        return objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save a list of objects into a csv file"""
        dicts = []
        if list_objs:
            for ins in list_objs:
                dicts.append(cls.to_dictionary(ins))

        if cls.__name__ == 'Rectangle':
            headers = ['id', 'width', 'height', 'x', 'y']
        else:
            headers = ['id', 'size', 'x', 'y']

        path = cls.__name__ + '.csv'
        with open(path, 'w') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for data in dicts:
                writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        """Create instances from csv file"""
        path = cls.__name__ + '.csv'
        dict_list = []
        objects = []

        try:
            with open(path) as f:
                reader = csv.DictReader(f)
                for line in reader:
                    res = {key: int(val) for key, val in line.items()}
                    dict_list.append(res)
        except:
            return objects

        for idx, obj in enumerate(dict_list):
            objects.append(cls.create(**dict_list[idx]))

        return objects

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the rectangles and square in an external window"""
        gp = Graphics()
        shapes = list_rectangles + list_squares
        colors = ['red', 'green', 'yellow', 'magenta', 'blue',
                  'pink', 'orange']
        idx = 0
        for shape in shapes:
            if idx >= len(colors):
                idx = 0

            color = colors[idx]
            gp.draw_rectangle(shape.width, shape.height,
                              shape.x, shape.y, color)
            idx += 1

        turtle.mainloop()


class Graphics:
    """Draw objects in the window"""

    def __init__(self):
        """Constructor"""
        turtle.width(3)
        turtle.hideturtle()

    @staticmethod
    def draw_rectangle(width, height, x=0, y=0, color='green'):
        """Draw rectangles and also squares"""
        turtle.pencolor(color)
        turtle.up()
        turtle.setx(x), turtle.sety(y)
        turtle.down()
        turtle.speed(10)
        turtle.shape('classic')
        for i in range(5):
            if i % 2 == 0:
                turtle.forward(width)
            else:
                turtle.forward(height)

            turtle.left(90)
