# Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es 
# opcional. Crear los siguientes métodos para la clase:

class Cuenta():
    # • Un constructor, donde los datos pueden estar vacíos.
    def __init__(self,titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad

    # • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar 
    # directamente, sólo ingresando o retirando dinero.
    @property
    def titular(self):
        return self.__titular
    
    @property
    def cantidad(self):
        return self.__cantidad

    @titular.setter
    def titular(self,titular):
        self.__titular=titular

    # • mostrar(): Muestra los datos de la cuenta.   
    def mostrar(self):
        return "Cuenta\n"+" Titular: "+ self.titular +" - Cantidad: "+str(self.cantidad)

    # • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es 
    # negativa, no se hará nada.
    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad

    # • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números 
    # rojos.
    def retirar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad - cantidad

# nueva = Cuenta("Daniela")
# print(nueva.mostrar())
# nueva.ingresar(1000)
# print(nueva.mostrar())


    