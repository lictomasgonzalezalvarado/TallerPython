#https://youtu.be/EMDmXyb4PeQ?si=zH927vF2K4ngvg1r
#jacklyon
class Persona:
    edad = 27
    nombre = 'Victor'
    pais = 'Brasil'

doctor = Persona()
print('Antes era',doctor.nombre)

setattr(doctor,'nombre','Hector') #con esta función hago un cambio de valor y se utiliza para hacer el cambio de valor en tiempo de ejecución
doctor.nombre="Hestor"
print('Ahora se llama',doctor.nombre)

print('Antes de que me eliminen',doctor.pais)
delattr(Persona, 'pais') #Esta función elimina el atributo pais
#print('¡Rayos! ya me eliminaron',doctor.pais)