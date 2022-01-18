class Usuario: # esto es lo que tenemos hasta ahora
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0
    # agregando el método de depósito
    def hacer_depósito(self, amount):  # toma un argumento que es el monto del depósito
        # la cuenta del usuario específico aumenta en la cantidad del valor recibido
        self.balance_cuenta += amount
    # Método Hacer retiro
    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
    # Método Mostrar Balance
    def mostrar_balance_usuario(self):
        print("Usuario: %s, Balance: %d" % (self.name, self.balance_cuenta))
    # Método Transferir Dinero
    def transferir_dinero(self, other_user, amount):
        self.balance_cuenta -= amount
        other_user.hacer_depósito(amount)

mitch = Usuario("Mitchell Rodríguez", "mitrodle@gmail.com")
mitch.hacer_depósito(800)
mitch.hacer_depósito(500)
mitch.hacer_depósito(200)
mitch.hacer_retiro(100)
mitch.mostrar_balance_usuario()

astrid = Usuario("Astrid Rodríguez", "astrid@gmail.com")
astrid.hacer_depósito(1500)
astrid.hacer_depósito(600)
astrid.hacer_retiro(300)
astrid.hacer_retiro(900)
astrid.mostrar_balance_usuario()

gabriel = Usuario("Gabriel Acurio", "gabriel@gmail.com")
gabriel.hacer_depósito(3500)
gabriel.hacer_retiro(1200)
gabriel.hacer_retiro(200)
gabriel.hacer_retiro(250)
gabriel.mostrar_balance_usuario()

# Antes de la transferencia
mitch.mostrar_balance_usuario()
gabriel.mostrar_balance_usuario()

# Transferir dinero
mitch.transferir_dinero(gabriel,200)

# Después de la transferencia
mitch.mostrar_balance_usuario()
gabriel.mostrar_balance_usuario()