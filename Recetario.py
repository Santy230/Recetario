import os
import shutil

from Pathlib import Path
from os import system

mi_ruta = Path("/Users/sotel/OneDrive/Documentos/Curso/Recetas")


def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f"Categorias: {carpeta_str}")
        lista_categorias.append(carpeta)

    return lista_categorias


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador


def elegir_receta():
    ruta = Path("/Users/sotel/OneDrive/Documentos/Curso/Recetas")
    categoria = input("Elegi una categoria ")
    ruta_usario = ruta / categoria
    for txt in Path(ruta_usario).glob("**/*.txt"):
        print(txt.stem)
    receta = input("Elegi una Receta ")
    with open(os.path.join("Recetas", categoria, receta + ".txt"), "r") as file:
        contenido = file.read()
        print(f"\nReceta: {receta}\n")
        print(contenido)


def crear_receta():
    ruta = Path("/Users/sotel/OneDrive/Documentos/Curso/Recetas")
    categoria = input("Elegi una categoria ")

    receta = input("Ingresa el Nombre de la receta ") + ".txt"
    ruta_usario = ruta / categoria / receta
    print(f"Ingresar La receta de {receta}")
    ruta_usario.write_text(input(" "))


def crear_categoria():
    ruta = Path("/Users/sotel/OneDrive/Documentos/Curso/Recetas")
    categoria = input("Elegi el nombre de la categoria a crear ")
    ruta_usuario = ruta / categoria
    os.makedirs(ruta_usuario)


def eliminar_receta():
    ruta = Path("/Users/sotel/OneDrive/Documentos/Curso/Recetas")
    categoria = input("Elegi una categoria ")
    ruta_usuario = ruta / categoria
    for txt in Path(ruta_usuario).glob("**/*.txt"):
        print(txt.stem)
    receta = input("Elegi una Receta ")
    os.remove(os.path.join("Recetas", categoria, receta + ".txt"))


def eliminar_categoria():

    categoria = input("Elegi el nombre de la categoria a eliminar ")
    ruta = os.path.join("Recetas", categoria)
    shutil.rmtree(ruta)


def inicio():
    while True:
        system("cls")
        print("-------------------------------")
        print("BIENVENIDO A TU ADM DE RECETAS")
        print("-------------------------------")
        print(f"total recetas: {contar_recetas(mi_ruta)}")

        print("elige una opcion")
        menu = input("1)Leer receta\n2)Crear receta nueva \n3)Crear categoria nueva\n4)Eliminar receta\n5)Eliminar Categoria\n6)Salir del programa ")
        if menu == "1":
            print("opcion 1")
            mostrar_categorias(mi_ruta)
            elegir_receta()
        elif menu == "2":
            print("opcion 2")
            crear_receta()

        elif menu == "3":
            print("opcion 3")
            crear_categoria()

        elif menu == "4":
            print("opcion 4")
            eliminar_receta()

        elif menu == "5":
            print("opcion 5")
            mostrar_categorias(mi_ruta)
            eliminar_categoria()

        elif menu == "6":
            print("PROGRAMA FINALIZADO")
            break


inicio()
