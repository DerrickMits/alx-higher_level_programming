#!/usr/bin/python3

class Rectangle:
    """Defines a Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Calculates the area of the Rectangle.

        Returns:
            int: The area of the Rectangle.
        """
        return self._width * self._height

    def perimeter(self):
        """Calculates the perimeter of the Rectangle.

        Returns:
            int: The perimeter of the Rectangle.
        """
        return 2 * (self._width + self._height)

    def __str__(self):
        """Returns the string representation of the Rectangle.

        Returns:
            str: The string representation of the Rectangle.
        """
        if self._width == 0 or self._height == 0:
            return ""
        
        rect = []
        for i in range(self._height):
            rect.append("#" * self._width)
            if i != self._height - 1:
                rect.append("\n")
        return "".join(rect)

    def __repr__(self):
        """Returns the formal string representation of the Rectangle.

        Returns:
            str: The formal string representation of the Rectangle.
        """
        return f"Rectangle({self._width}, {self._height})"
