from models.Inventory import Inventory
from models.Menu import Menu
from sys import exit as sys_exit

def main():

    MENU_MAIN = Menu('Bem-vindo!', 
                             Admin = lambda: MENU_ADM.show(), 
                             Usuario = lambda: MENU_USER.show(),
                             Sair = lambda: sys_exit())
    MENU_ADM  = Menu('ADM',
                            Registrar = lambda: store.add_entry(input('Nome do produto: '), float(input('Valor do produto: ')), int(input('Quantidade: '))),
                            Remover = lambda: store.pop_entry(input('Nome do produto: ')),
                            Listar = lambda: Menu('Produtos',
                                                    Voltar = lambda: MENU_ADM.show(),
                                                    extra_data = store.products
                                                ).show(),
                            Voltar = lambda: MENU_MAIN.show())
    MENU_USER = Menu('User',
                            Adicionar = lambda: store.transfer_entry(input('Nome do produto: '), int(input('Quantidade: ')), cart),
                            Remover = lambda: cart.transfer_entry(input('Nome do produto: '), int(input('Quantidade: ')), store),
                            Listar = lambda: Menu('Produtos',
                                                    Voltar = lambda: MENU_USER.show(),
                                                    extra_data = cart.products
                                                ).show(),
                            Fechar_Compra = lambda: Menu('Fechar Compra',
                                                    Voltar = lambda: MENU_USER.show(),
                                                    Sair = lambda: sys_exit(),
                                                    extra_data = [cart.total]
                                                ).show(),
                            Voltar = lambda: MENU_MAIN.show())
    
    store = Inventory()
    cart = Inventory()


    MENU_MAIN.show()

    print(store.total)
    print(cart.total)


if __name__ == '__main__':
    main()
