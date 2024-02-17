# OPEN CLOSE PRINCIPLE: open for extensios and close for  modification

from enum import Enum
from typing import List


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:

    def __init__(self, name: str, color: Color, size: Size):
        self.name = name
        self.color = color
        self.size = size
    


# It's not scalable because if there are others parameters like Cost, Weight, dimensions... the class ProductFilter will be very big

class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color):
        for p in products:
            if p.color == color: 
                yield p


    def filter_by_size(self, products: List[Product], size: Size):
        for p in products:
            if p.size == size:
                yield p

    
    def filter_by_size_and_color(self, products:List[Product], size: Size, color: Color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

            

# Pattern SPECIFICATION to solve this violation

class Specification:
    def is_satisfied(self, item: Product):
        pass


class Filter:
    def filter(self, items: List[Product], spec: Specification):
        pass


class colorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item: Product):
        return item.color == self.color

class sizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item: Product):
        return item.size == self.size
    

class BetterFilter(Filter):
    """
    docstring
    """
    pass