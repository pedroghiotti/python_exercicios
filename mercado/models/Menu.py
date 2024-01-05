from os import system
import msvcrt

class Menu:
    def __init__(self, title: str, *, border_char: str = ':', width: int = 36, border: int = 2, extra_data=None, **kwargs: object) -> None:
        self.__header = f'''{border_char * width}
{border_char * border}{''.center(width-2*border)}{border_char*border}
{border_char * border}{title.center(width-2*border).replace('_', ' ')}{border_char*border}
{border_char * border}{''.center(width-2*border)}{border_char*border}
{border_char * width}'''
        self.__options = kwargs
        self.__option = 0
        self.__extra_data = extra_data

    def render(self) -> None:
        system('cls')
        print(self.__header)
        for i, (name, function) in enumerate(self.__options.items()):
            print(f'{'> ' if self.__option == i else ''}{i} - {name}')
        if(self.__extra_data != None):
            for item in self.__extra_data:
                try:
                    print(f'{f"{item.product.name}" : <12}{f"{item.product.value}" : ^12}{f"{item.quantity}" : >12}')
                except:
                    print(f'O valor total do carrinho é de {item} reais.')
    
    def show(self) -> None:
        while True:
            self.render()

            if (ch := msvcrt.getch()) == b'\x00':
                ch = msvcrt.getch()

            match ch:
                case b'H' | b'w':
                    self.__option = (self.__option + len(self.__options) - 1) % len(self.__options)
                case b'P' | b's':
                    self.__option = (self.__option + len(self.__options) + 1) % len(self.__options)
                case b'\r':
                    list(self.__options.values())[self.__option]()
                    break
        self.show()