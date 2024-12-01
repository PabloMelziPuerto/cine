class Asientos:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__reservado = False
        self.__precio = 10 

    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_reservado(self):
        return self.__reservado

    def get_precio(self):
        return self.__precio

    def set_reservado(self, reservado):
        self.__reservado = reservado

    def set_precio(self, precio):
        self.__precio = precio

    def mostrar_asiento(self):
        estado = "Reservado" if self.__reservado else "Disponible"
        return f"Fila: {self.__fila}, Asiento: {self.__numero}, Estado: {estado}, Precio: ${self.__precio}"