from os import system
import time

# Lista con los clientes para despues poder llamarla para iniciar sesión
clientes = []


# Clase Persona - Padre
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


# Clase Cliente - Hija
class Cliente(Persona):

    # Variable autoincremental para los números de cuenta
    numero_cuenta = 0

    def __init__(self, nombre, apellido, balance):
        super().__init__(nombre, apellido)
        Cliente.numero_cuenta += 1  # Cada vez que se cree un nuevo cliente el número incrementa en 1
        self.numero_cuenta = Cliente.numero_cuenta
        self.balance = balance

    def __str__(self):
        return f'Cliente: {self.nombre} {self.apellido}\n' \
               f'Núm. de cuenta: {self.numero_cuenta}\n' \
               f'Balance: ${self.balance}'

    def depositar(self, cantidad):
        self.balance += cantidad
        print(f'Se ha depositado ${cantidad}.\n'
              f'Nuevo saldo: ${self.balance}')

    def retirar(self, cantidad):
        if cantidad <= self.balance:
            self.balance -= cantidad
            print(f'Se han retirado ${cantidad}\n'
                  f'Nuevo saldo: ${self.balance}')
        else:
            print('Saldo insuficiente.')


def crear_cliente():
    nombre = input('Escribe tu(s) nombre(s): ')
    apellido = input('Escribe tu(s) apellido(s): ')
    balance = 0     # El balance inicia en 0 para cada cliente nuevo

    cliente = Cliente(nombre, apellido, balance)    # sin numero de cuenta porque ese se asigna arriba
    clientes.append(cliente)    # Se añade el cliente a la lista de clientes

    print(f'\n¡Cliente creado con exito!\n'
          f'Número de cuenta asignado: {cliente.numero_cuenta}\n'
          f'Por favor recuerda tu Número de cuenta.\n')

    time.sleep(6)
    system('cls')

    return cliente


def inicio():
    print('*' * 13 + '~~' + '*' * 13)
    print('\nBienvenido a Roderick\'s Bank\n')
    print('*' * 13 + '~~' + '*' * 13)
    print(f'\n¿Qué desea hacer?'
          f'\n[1] - Crear nuevo cliente'
          f'\n[2] - Iniciar sesión'
          f'\n[3] - Finalizar')

    eleccion_inicio = int(input('\n[?] '))

    time.sleep(.75)
    system('cls')

    return eleccion_inicio


def iniciar_sesion():

    while True:
        print('Digite su número de cuenta')
        numcuenta = int(input('[?] '))
        cliente_encontrado = None

        for cliente in clientes:
            if cliente.numero_cuenta == numcuenta:
                cliente_encontrado = cliente

        if cliente_encontrado is not None:
            print(f'Número de cuenta {cliente_encontrado.numero_cuenta} valido.')
            time.sleep(2)
            system('cls')
            break
        else:
            print(f'Númeo de cuenta invalido.')
            time.sleep(2)
            system('cls')
            continue

    return cliente_encontrado


def depositar_retirar(cliente_enc):

    def menu_depositar_retirar():
        (print(f'¿Qué quieres hacer?\n'
               f'[1] - Depositar\n'
               f'[2] - Retirar\n'
               f'[3] - Menú principal\n'))

        eleccion_menu = int(input('[?] '))
        return eleccion_menu

    while True:
        eleccion = menu_depositar_retirar()
        system('cls')
        if eleccion == 1:
            print('¿Cuánto quieres depositar?')
            deposito = int(input('[?]'))
            cliente_enc.balance += deposito
            print(f'\nNuevo balance: ${cliente_enc.balance}\n')
            continue
        elif eleccion == 2:
            print('¿Cuánto quieres retirar?')
            retiro = int(input('[?]'))
            if retiro <= cliente_enc.balance:
                cliente_enc.balance -= retiro
                print(f'\n Nuevo balance: ${cliente_enc.balance}\n')
            else:
                print('Saldo insuficiente.\n')
                time.sleep(3)
                system('cls')
        else:
            break


def loop_menus():

    while True:

        eleccion = inicio()
        system('cls')

        if eleccion == 1:
            crear_cliente()
            continue
        elif eleccion == 2:
            cliente = iniciar_sesion()
            depositar_retirar(cliente)
            system('cls')
        elif eleccion == 3:
            raise SystemExit


loop_menus()
