class Rectangle:
    """A class to represent rectangle objects."""

    def __init__(self, width, height):
        """Create rectangle object with width and height."""

        self.width = width
        self.height = height

    def set_width(self, width):
        """Set the rectangle width."""

        self.width = width

    def set_height(self, height):
        """Set the rectangle height."""

        self.height = height

    def get_area(self):
        """Get the rectangle area."""

        return self.width * self.height

    def get_perimeter(self):
        """Get the rectangle perimeter."""

        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        """Get the rectangle diagonal."""

        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        """Draw a picture with '*' characters representing the rectangle"""

        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for line in range(self.height):
            picture += self.width * "*" + "\n"
        return picture

    def get_amount_inside(self, other_shape):
        """Take another shape (square or rectangle) as an argument.
        Return the number of times the passed in shape could fit inside the shape (with no rotations).
        """

        vertical = int(self.height / other_shape.height)
        horizontal = int(self.width / other_shape.width)
        return vertical * horizontal

    def __str__(self):
        """Return (str): 'Rectangle(width={}, height={})'."""
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    """A class to represent square objects."""

    def __init__(self, side):
        """Create square object with same width and height."""

        self.width = side
        self.height = side

    def set_side(self, side):
        """Set square sides (same width and height)."""
        self.width = side
        self.height = side

    def set_width(self, width):
        """Set square sides (same width and height)."""
        self.width = width
        self.height = width

    def set_height(self, height):
        """Set square sides (same width and height)."""

        self.height = height
        self.width = height

    def __str__(self):
        """Return (str): 'Square(side={})'."""

        return f"Square(side={self.height})"
