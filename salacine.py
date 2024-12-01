from asientos import Asientos

class SalaCine:
    def __init__(self):
        self.__asientos = []

    def agregar_asiento(self, numero, fila):
        # Verificar si el asiento ya existe
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                print("El asiento ya está registrado.")
                return
        nuevo_asiento = Asientos(numero, fila)
        self.__asientos.append(nuevo_asiento)
        print(f"Asiento {numero} en la fila {fila} agregado correctamente.")

    def reservar_asiento(self, numero, fila, edad, dia):
        # Buscar el asiento
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            print("Asiento no encontrado.")
            return
        if asiento.get_reservado():
            print("Este asiento ya está reservado.")
            return
        # Calcular el precio según el día y la edad
        precio = self.calcular_precio(edad, dia)
        asiento.set_precio(precio)
        asiento.set_reservado(True)
        print(f"Asiento {numero} reservado con éxito. Precio: ${precio}")

    def cancelar_reserva(self, numero, fila):
        # Buscar el asiento
        asiento = self.buscar_asiento(numero, fila)
        if asiento is None:
            print("Asiento no encontrado.")
            return
        if not asiento.get_reservado():
            print("Este asiento no está reservado.")
            return
        asiento.set_reservado(False)
        print(f"Reserva de asiento {numero} cancelada con éxito.")

    def mostrar_asientos(self):
        if not self.__asientos:
            print("No hay asientos registrados.")
            return
        for asiento in self.__asientos:
            print(asiento.mostrar_asiento())

    def buscar_asiento(self, numero, fila):
        for asiento in self.__asientos:
            if asiento.get_numero() == numero and asiento.get_fila() == fila:
                return asiento
        return None

    def calcular_precio(self, edad, dia):
        precio_base = 10
        # Descuento por día (miércoles)
        if dia.lower() == 'miércoles':
            precio_base *= 0.8  # 20% de descuento
        # Descuento para mayores de 65 años
        if edad >= 65:
            precio_base *= 0.7  # 30% de descuento
        return round(precio_base, 2)