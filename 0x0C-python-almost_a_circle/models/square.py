#!/usr/bin/python3
"""
Module Square
Inherits from class Rectangle,
That inherits from class Base
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square inherits from class Rectangle
    Methods:
        def __init__(self,size,x,y,id)
        def __str__(self)
        def update(self, *args, **kwargs)
        def to_dictionary(self)
    Getter:
       def size(self)
    Setter:
        def size(self, value)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialization
        calls the supper class rectangle
        and assigns width and height to size
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """Overrides to return
        "[Square] (<id>) <x>/<y> - <size>"
        """
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """Assign arguments to attributes"""
        if args:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                elif i == 1:
                    self.size = j
                elif i == 2:
                    self.x = j
                else:
                    self.y = j

        else:
            """kwargs"""
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """returns the dictionary representation of square"""
        dic = {}
        dic["id"] = self.id
        dic["size"] = self.size
        dic["x"] = self.x
        dic["y"] = self.y
        return dic
