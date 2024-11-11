'''
   Nota: el Method Chaining no es considerado un patrón de diseño formal
   en el sentido clásico (como los patrones de diseño de la Gang of Four)

   El error ocurre porque, en Python, la clase Resultado aún no está completamente definida
   en el momento en que se utiliza en la anotación de tipo del método suma.

   Para resolver este problema, puedes hacer referencia a Resultado
   como una cadena de texto ('Resultado')
   en lugar de usar el nombre de la clase directamente.

   Python interpretará la cadena como una referencia a la clase
   después de que se complete la definición.
'''


class ClaseSumaInfinita: #Metodo constructor
    def __init__(self): #Método constructor
        self.resultado =0

    #Metodo suma que permite el encadenamiento (Method Chaining)
    def suma(self, num)->'SumaInfinita':
        self.resultado += num
        return self #Retorna la misma instancia

    def __str__(self) -> str: #Metodo toString
        return str(self.resultado)
