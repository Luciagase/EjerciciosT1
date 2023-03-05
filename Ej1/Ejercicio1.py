class Alumno:
    def ___init__(self, cadena):
        self.cadena = cadena
    
    @staticmethod
    def voltear(cadena):
        cadena_ordenada = cadena[::-1]
        nota = cadena_ordenada[0:2]
        nombre = cadena_ordenada[2:]
        return nombre + "ha sacado un" + nota


cadena = "zeréP nauJ,01"
Alumno(cadena)