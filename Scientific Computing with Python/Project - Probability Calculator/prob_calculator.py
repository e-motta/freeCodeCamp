import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        instance = []
        for key, value in kwargs.items():
            for i in range(value):
                instance.append(key)
        self.instance = instance

    def draw(self, num_balls):
        if num_balls >= len(self.instance):
            return self.instance
        return [self.instance.pop(random.randint(0, len(self.instance)-1)) for i in range(num_balls)]


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat1 = Hat(red=3, blue=2, yellow=7)
print(hat1.instance)
print(hat1.draw(3))
