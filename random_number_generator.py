#import random

#class RandomNumberGenerator:
#    def __init__(self):
#        self.generator = random.Random()
#
#    def get_random_number(self, min, max):
#        return self.generator.randint(min, max)

import os
import math

class RandomNumberGenerator:
    def __init__(self):
        pass

    @staticmethod
    def number_between(minimum_value, maximum_value):
        random_number = os.urandom(1)
        ascii_value_of_random_character = ord(random_number)
        multiplier = max(0, (ascii_value_of_random_character / 255.0) - 0.00000000001)
        range_value = maximum_value - minimum_value + 1
        random_value_in_range = math.floor(multiplier * range_value)
        return int(minimum_value + random_value_in_range)