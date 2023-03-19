# Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los 
# siguientes métodos para la clase:

class Persona():
   # • Un constructor, donde los datos pueden estar vacíos.
   def __init__(self, nombre="", edad=0, DNI=""):
      self.nombre = nombre
      self.edad = edad
      self.DNI = DNI


   # • Los setters y getters para cada uno de los atributos. Hay que validar las entradas de 
   # datos. 
   @property
   def nombre(self):
        return self.__nombre

   @property
   def edad(self):
        return self.__edad

   @property
   def DNI(self):
        return self.__DNI
   
   @nombre.setter
   def nombre(self,nombre):
        self.__nombre=nombre

   def DNI_valid(self):
      if len(self.__DNI)!=8:
         print("DNI incorrecto")
         self.__DNI = ""
    

   @DNI.setter
   def DNI(self,DNI):
        self.__DNI=DNI
        self.DNI_valid()
      
   @edad.setter
   def edad(self,edad):
        if edad < 0:
            print("Edad incorrecta")
            self.__edad=0
        else:
            self.__edad=edad
    
   # • mostrar(): Muestra los datos de la persona.
   def mostrar(self):
        return "Nombre:"+self.nombre+" ,Edad:"+str(self.edad)+" ,DNI:"+self.DNI
   
   # • es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
   def es_mayor_de_edad(self):
        return self.edad>=18

# persona1 = Persona("Eva",33,"12154546")
# print(persona1.mostrar())