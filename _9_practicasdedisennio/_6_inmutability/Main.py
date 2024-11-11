from Persona import Persona

if __name__ == '__main__':
    personaInmutable=Persona("Tomas",44)
    print(personaInmutable.getNombre)
    print(personaInmutable.getEdad)

    personaInmutable._nombre="Hector"

    #personaInmutable.setNombre("Braulio")
    print(personaInmutable.getNombre)


