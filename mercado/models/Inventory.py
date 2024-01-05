from collections import namedtuple
from functools import singledispatchmethod


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


    @singledispatchmethod
    def add_entry() -> None:
        raise NotImplementedError()    
    
    @add_entry.register(Entry)
    def _(self:object, entry: Entry) -> None:
        if((old_entry := self.__find(entry)) != None):
            self.update_entry(entry.product.name, new_quantity = entry.quantity + old_entry.quantity)
        else:
            self.__products.add(entry)

    @add_entry.register(str)
    def _(self: object, name: str, value: float, quantity: int) -> None:
        name = name.title()
        self.add_entry(Entry(Product(name, value), quantity))


    @singledispatchmethod
    def pop_entry() -> Entry:
        raise NotImplementedError()

    @pop_entry.register(Entry)
    def _(self: object, entry: Entry) -> Entry:
        if self.__find(entry) is None:
            return None
        else:
            self.__products.remove(entry)
            return entry

    @pop_entry.register(str)
    def _(self: object, name: str) -> Entry:
        name = name.title()
        if (entry := self.__find(name)) is None:
            return None
        else:
            self.__products.remove(entry)
            return entry


    @singledispatchmethod
    def update_entry() -> None:
        raise NotImplementedError()

    @update_entry.register(Entry)
    def _(self: object, entry: Entry, new_entry: Entry) -> None:
        if self.__find(entry) is None:
            return None
        
        self.pop_entry(entry)
        self.add_entry(new_entry)

    @update_entry.register(str)
    def _(self: object, name: str, *,new_name: str = None, new_value: float = None, new_quantity: int = None) -> None:
        name = name.title()
        if (entry := self.__find(name)) is None:
            return None
        
        if(new_name is None): new_name = entry.product.name
        if(new_value is None): new_value = entry.product.value
        if(new_quantity is None): new_quantity = entry.quantity

        self.pop_entry(entry)
        self.add_entry(new_name, new_value, new_quantity)


    @singledispatchmethod
    def transfer_entry() -> None:
        raise NotImplementedError()
    
    @transfer_entry.register(Entry)
    def _(self: object, entry: Entry, quantity: int, inventory: object) -> None:
        if(self.__find(entry) is None):
            return None
        
        if(entry.quantity > quantity):
            inventory.add_entry(entry.product.name, entry.product.value, quantity)
            self.update_entry(entry.product.name, new_quantity =  entry.quantity - quantity)
        else:
            inventory.add_entry(entry.product.name, entry.product.value, entry.quantity)
            self.pop_entry(entry)
    
    @transfer_entry.register(str)
    def _(self: object, name: str, quantity: int, inventory: object) -> None:
        name = name.title()
        if((entry := self.__find(name)) is None):
            return None
        self.transfer_entry(entry, quantity, inventory)
        
    


    @singledispatchmethod
    def __find() -> Entry:
        raise NotImplementedError()

    @__find.register(Entry)
    def _(self: object, entry: Entry) -> Entry:
        return self.__find(entry.product.name)

    @__find.register(str)
    def _(self: object, product_name: str) -> Entry:
        product_name = product_name.title()
        try:
            return next(entry for entry in self.__products if entry.product.name == product_name)
        except:
            return None

    def __get_total(self: object) -> float:
        return sum((entry[0][1] * entry[1] for entry in self.__products))