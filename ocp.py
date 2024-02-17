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
    


class ProductFilter:
    def filter_by_color(self, products: List[Product], color: Color):
        for p in products:
            if p.color == color: 
                yield p


    def filter_by_size(self, products: List[Product], size: Size):
        for p in products:
            if p.size == size:
                yield p

                
