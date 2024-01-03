from collections import namedtuple

Product = namedtuple('Product', ['name', 'value'])
Entry = namedtuple('Entry', ['product', 'quantity'])

class Inventory:
    def __init__(self: object, products: list[Entry] = None):
        
        self.__products = products

        if(products is None):
            self.__products = set()
            
        self.__total = self.__get_total()
    
    @property
    def products(self: object) -> dict:
        return self.__products
    
    @property
    def total(self: object) -> float:
        return self.__get_total()
    
    def add_entry(self: object, product_name: str, product_value: float, quantity: int = 1) -> None:
        product_name = product_name.title()
        self.__products.add(Entry(Product(product_name, product_value), quantity))

    def remove_entry(self: object, product_name: str) -> None:
        product_name = product_name.title()
        self.__products.remove(self.__find(product_name))

    def update_entry(self: object, product_name: str, quantity: int) -> None:
        product_name = product_name.title()
        entry = self.__find(product_name)
        self.remove_entry(product_name)
        self.add_entry(entry[0][0], entry[0][1], quantity)

    def __get_total(self: object) -> float:
        return sum((entry[0][1] * entry[1] for entry in self.__products))

    def __find(self: object, product_name: str) -> Entry:
        product_name = product_name.title()
        return next(entry for entry in self.__products if entry[0][0] == product_name)
    



