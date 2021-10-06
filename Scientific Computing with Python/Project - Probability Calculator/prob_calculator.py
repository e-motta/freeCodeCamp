import copy
import random


class Hat:
    """A class to represent hats filled with different colored balls."""
    def __init__(self, **kwargs):
        """Create a hat with a variable number of differente balls.
        
        Args:
            kwargs (int): color of ball as arg name and corresponding number (eg 'red=8')
        Attributes:
            contents (list): a list contaning all the inidivual balls, with color name
        """
        contents = []
        for color, num in kwargs.items():
            for i in range(num):
                contents.append(color)
        self.contents = contents

    def draw(self, num_balls):
        """Draw a random number of balls from the hat, without replacing

        Args:
            num_balls (int): Number of balls to draw

        Returns:
            list: List of balls drawn
        """
        if num_balls >= len(self.contents):
            return self.contents
        return [self.contents.pop(random.randint(0, len(self.contents)-1)) for i in range(num_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """Calculates the probability of a number of balls being drawn from a hat.

    The probability is calculted through a number of random experiments.

    Args:
        hat (Hat object): A hat containing different colored balls
        expected_balls (dict): A group of balls to attempt to draw from the hat
        num_balls_drawn (int): The number of balls to draw out of the hat in each experiment.
        num_experiments (int): The number of experiments to perform.

    Returns:
        float: The probability of the ball being drawn from the hat.
    """
    expected_balls_list = []

    for color, num in expected_balls.items():
        for i in range(num):
            expected_balls_list.append(color)
    
    matches = 0

    for i in range(num_experiments):

        hat_copy = copy.deepcopy(hat)
        expected_balls_list_copy = copy.deepcopy(expected_balls_list)
        drawn_balls_list = hat_copy.draw(num_balls_drawn)

        for ball in drawn_balls_list:
            if ball in expected_balls_list_copy:
                expected_balls_list_copy.remove(ball)

        if not expected_balls_list_copy:
            matches += 1

    return matches / num_experiments
