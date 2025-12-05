# 📌 Ejercicio 1 – Cuentas bancarias
# Crea una clase base CuentaBancaria con:
# Atributo privado __saldo.
# Métodos depositar(monto) y retirar(monto) 
# con validación (no permitir montos negativos, 
# ni saldo insuficiente).
# Método mostrar_saldo() que devuelve el saldo.
# Subclases:
# CuentaAhorro → gana un interés de 2% cuando se consulta el saldo. 
# CuentaCorriente → permite sobregiro de hasta -500.
# 👉 Recorre una lista de cuentas y llama a mostrar_saldo() 
# en cada una, mostrando polimorfismo.
class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo=saldo
        
    def depositar(self, monto):
        if monto <0:
            raise ValueError("El monto no puede ser inferior a un peso")
        self.__saldo+=monto
    
    def retirar(self, monto):
        if monto <0:
            raise ValueError("  monto no puede ser inferior a un peso")
        if monto>self.__saldo:
            raise ValueError("Tu saldo es insuficiente para realizar esta operación")
        self.__saldo-=monto
        
    def mostrar_saldo(self):
        return self.__saldo
    
    def establecer_saldo(self,saldo):
        self.__saldo=saldo