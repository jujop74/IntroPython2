import datetime

# Ejemplo de clase y creación de una instancia de la misma
class FestivalMusical:
    def __init__(self, nombre, pais, estilo_musical):
        # Inicializa los parámetros
        self.nombre = nombre
        self.pais = pais
        self.estilo_musical = estilo_musical

    # Los métodos regulares toman la instancia como primer argumento
    def festival_metodo(self):
      print('El mejor festival es:')
      return self

    # Los métodos de clase toman la clase como primer argumento
    # (no pueden modificar las variables a nivel de instancia)
    @classmethod
    def valor_ticket(cls, valor):
          cls.valor_ticket = valor

    @staticmethod
    def dia_evento(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            print('es un final de semana')
            return dia
        else:
            print('es un día laboral')
            return dia


# Se crea una instancia de la clase FestivalMusical
festival1 = FestivalMusical('Creamfields', 'UK', 'Dance')
festival2 = FestivalMusical('Benicassim', 'ES', 'Pop')

FestivalMusical.valor_ticket(100)
dia1 = datetime.date(2022, 5, 9)
FestivalMusical.dia_evento(dia1)

# Ejemplo usando f-strings para acceder al objeto
print(f'El festival {festival1.nombre} se realizará el {dia1}')

# Accede a la clase
print('El valor del ticket es:', FestivalMusical.valor_ticket)
# Accede a la instancia
print('El valor del festival', festival1.nombre, 'es', festival1.valor_ticket)
      
# Se accede a los atributos del objeto
# print('1.-', festival1.nombre)
# print('2.-', festival1)
# print('3.-', FestivalMusical.festival_metodo(festival1))
# print('4.-', festival1.festival_metodo())
# print('5-.', festival1.nombre.upper())

# del festival1
# print(festival1.nombre.upper())
