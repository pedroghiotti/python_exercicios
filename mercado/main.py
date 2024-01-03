from models.Inventory import Inventory

def main():

    store = Inventory()
    cart = Inventory()

    print(store.products)
    print(cart.products)    
    print(store.total)
    print(cart.total)
    
    store.add_entry('Eggs', 1, 12)
    store.add_entry('Beef', 25, 2)
    cart.add_entry('poultry', 15, 2)

    print(store.products)
    print(cart.products)
    print(store.total)
    print(cart.total)
    
    store.remove_entry('Eggs')
    cart.update_entry('PoulTry', 5)

    print(store.products)
    print(cart.products)
    print(store.total)
    print(cart.total)

    pass

if __name__ == '__main__':
    main()
