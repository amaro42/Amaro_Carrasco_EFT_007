peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    ...
}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    ...
}

def cuposygeneros(peliculas,cartelera):
genero=int(input("escriba el genero de la pelicula que desea ver"))
for genero in peliculas [list]:
        print (cartelera[str:[1]])

def busqueda_precio(cartelera):
     valor1=int(input("indique el precio minimo"))
     valor2=int(input("indique el precio maximo"))
     if valor1<=0 and valor2<=0:
             print("Debe ingresar valores enteros ")

def actualizar_price(peliculas,cartelera):
    codi=int(input("Ingrese el codigo de la pelica"))
    if codi==peliculas[str]:
        price=int(input)("ingrese el precio que desea actualizaar")
        print ("precio actualizado")
        return True
    else:
        print("el codigo no existe")
        return False

def agregar_peli(peliculas,cartelera):
    try:
        while True:
            codii=int(input("ingrese el codigo de la pelicula que desea agregar: "))
            if codii==peliculas[str]:
                peliculas.append[str]=codii
                print("codigo agregado exitosamente ")

            else:
                print("este codigo ya existe")
                return False
            nombre=int(input)("ingrese el nombre de la pelicula que quiere agregar: ")
            peliculas.append[str[0]]=nombre
            print("pelicula agregada ")
            genero=int(input("ingrese el genero de la pelicula que quiere agregar: "))
            peliculas.append[str:[1]]=genero
            print("genero agregada")
            tiempo=int(input("ingrese la duracion de la pelicula que quiere agregar (en minutos): "))
            peliculas.append[str[2]]=tiempo
            print("tiempo agregado")
            clasificacion=int(input("ingrese la clasificacion de la pelicula: A, B, C: "))
            peliculas.append[str[3]]=clasificacion
            idioma=int(input("ingrese el idioma de la pelicula: "))
            peliculas.append[str[4]]=idioma
            tresDDD=int(input("la pelicula esta en 3D? s/n"))
            if tresDDD=="s":
                 peliculas.append[str[5]]=True
            elif tresDDD=="n":
                 peliculas.append[str[5]]=False
            precio=int(input("ingrese el precio de la entrada para la pelicula: "))
            cartelera.append[str[0]]=precio
            print("precio agregado ")
            cupos=int(input("ingrese los cupos para la pelicula: "))
            cartelera.append[str[1]]=cupos
    except ValueError:
         print("")

def eliminarpeli(peliculas,cartelra):
     try:
          delete=int(input("ingrese el codigo de la pelicula que desea eliminar: "))
          if delete in peliculas[str]:
               peliculas.pop[str]=delete
               cartelera.pop[str]=delete
               return True
          else: 
               print ("el codigo no existe ")
     except ValueError:
def menu():
    print ("========== MENÚ PRINCIPAL ==========")
    print ("1. Cupos por género")
    print ("2. Búsqueda de películas por rango de precio")
    print ("3. Actualizar precio de película")
    print ("4. Agregar película")
    print ("5. Eliminar película")
    print ("6. Salir")
    print ("=====================================")
    match op: 
         case "1":
              def cuposygeneros():
         case "2":
              def busqueda_precio():
         case "3":
              def actualizar_price():  
         case "4":
              def agregar_peli():
         case "5":
              def eliminarpeli():
         case "6":
              print("finzalizado ")
              return False
         except ValueError
print("Opcion invalida, seleccione nuevamente")