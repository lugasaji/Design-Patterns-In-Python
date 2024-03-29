# OPEN CLOSE PRINCIPLE: open for extensios and close for  modification

from __future__ import annotations
from enum import Enum
from typing import Generator, List



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
    
    def filter_by_color(self, products: List[Product], color: Color) -> Generator[Product]:
        for p in products:
            if p.color == color: 
                yield p


    def filter_by_size(self, products: List[Product], size: Size) -> Generator[Product]:
        for p in products:
            if p.size == size:
                yield p

    
    def filter_by_size_and_color(self, products:List[Product], size: Size, color: Color) -> Generator[Product]:
        for p in products:
            if p.color == color and p.size == size:
                yield p

            

# Pattern SPECIFICATION to solve this violation

class Specification:
    
    def is_satisfied(self, item: Product) -> bool:
        pass

    def __and__(self, other: Specification) -> Specification:
        return AndSpecification(self, other)

    def __or__(self, other: Specification) -> Specification:
        return OrSPecification(self, other)

class AndSpecification(Specification):
    
    def __init__(self, *args: Specification) -> None:
        self.args = args

    def is_satisfied(self, item: Product) -> bool:
        return all(map(lambda spec: spec.is_satisfied(item) , self.args))


class OrSPecification(Specification):
    
    def __init__(self, *args: Specification) -> None:
        self.args = args
    
    def is_satisfied(self, item: Product) -> bool:
        return any(map(lambda spec: spec.is_satisfied(item), self.args))
    

class Filter:
    
    def filter(self, items: List[Product], spec: Specification) -> Generator[Product]:
        pass


class colorSpecification(Specification):
    
    def __init__(self, color: Color) -> None:
        self.color = color
    
    def is_satisfied(self, item: Product) -> bool:
        return item.color == self.color

class sizeSpecification(Specification):
    
    def __init__(self, size) -> None:
        self.size = size
    
    def is_satisfied(self, item: Product) -> bool:
        return item.size == self.size
    

class BetterFilter(Filter): 
    def filter(self, items: List[Product], spec: Specification) -> Generator[Product]:
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    pfilter = ProductFilter()
    print('Green products (old)')
    for p in pfilter.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')


    pbfilter = BetterFilter()
    print('Green products (new):')
    green = colorSpecification(Color.GREEN)
    for p in pbfilter.filter(products, green):
        print(f' - {p.name} is green')
    

    print('Large products:')
    large = sizeSpecification(Size.LARGE)
    for p in pbfilter.filter(products, large):
        print(f' - {p.name} is large')

    print('Blue large items: ')
    blue = colorSpecification(Color.BLUE)
    #blue_and_large = AndSpecification(blue, large)
    blue_and_large = blue & large
    for p in pbfilter.filter(products, blue_and_large):
        print(f' - {p.name} is large and blue')

    print('Small or blue items:')
    small_or_blue = blue | sizeSpecification(Size.SMALL)
    for p in pbfilter.filter(products, small_or_blue):
        print(f' - {p.name} is small or blue')