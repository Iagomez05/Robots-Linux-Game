# The above code is importing necessary libraries for a project in Python. It includes libraries such
# as tkinter, threading, random, time, PIL (Python Imaging Library), pygame, natsort, and messagebox.
# It also imports specific modules from some of these libraries. The code is setting up the necessary
# environment for a graphical user interface (GUI) application.
#Importamos todas las librerías necesarias para el proyecto
import tkinter as tk
from tkinter import *
from threading import Thread
import random
import time
from PIL import ImageTk, Image
from tkinter import Toplevel
import pygame
import natsort
from tkinter import font, PhotoImage
from natsort import natsorted
from tkinter import messagebox
import math

# Codigo para Pantalla Inicial
#The code creates a window with a title "Diviértete" and a background image, and plays music.
window = None
puntos = 0

#Inicializa Pygame y carga la música en la función play()
pygame.mixer.init()
def play():
    pygame.mixer.music.load("musica.mp3")
    pygame.mixer.music.play(loops=0)

def stop_music():
    pygame.mixer.music.stop()

#Abre la ventana principal
def ventana_inicio():
    global window
    ventana1 = tk.Tk()
    ventana1.title("Diviértete")
    ventana1.minsize(height=480, width=800)
    ventana1.configure(background="black") #Color del tk
    play()
    
    #Fondo ventana_principal
    fondo = tk.PhotoImage(file="Fondo PAC-MAN.png")
    fondo_label = tk.Label(ventana1, image=fondo)
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
    ventana1.resizable(height=False, width=False)
    
    #Titulo Ventana Principal
    tituloPrincipal = tk.Label(ventana1, text="ROBOTS", font=("Courier New", 12, "bold"), background="grey", fg="white")
    tituloPrincipal.place(x=1400, y=25) 

#__________________________________________________Parte de Juego_________________________________________________________________________________________________

    #Función abrir ventana de NickName
    #The function "abrirventana_nickname" opens a window where the user can enter their nickname and
    #then proceed to the game window.
    
    def abrirventana_nickname(): #niveles
        ventana1.withdraw()
        ventana_nickname = Toplevel()
        ventana_nickname.title("Nickname")
        ventana_nickname.geometry("800x480")
        ventana_nickname.configure(background="black")
        canvasC2 = tk.Canvas(ventana_nickname, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo4= tk.Label(canvasC2, text="Introduce tu nombre", font=("Courier New", 12, "bold"), background="black", fg="white")
        titulo4.place(x=280, y=210)
        ventana_nickname.resizable(height=False, width=False)
        
        #Botón back de la pestaña de NickName
        #The above code creates a "back" button in a tkinter window that, when clicked, destroys the
        #current window and brings back the previous window.
           
        def back():
            ventana_nickname.destroy()
            ventana1.deiconify()
        botonBack = tk.Button(ventana_nickname, text="back", command= back, font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)
        
        # Agregar una barra de entrada para el nombre. Niveles
        #The function "nombre" checks if a name is entered in the input field and displays an error
        #message if it is empty, otherwise it opens a game window with the specified level and name.
        #:param nivel: The level of the game
        #:param nombre: The parameter "nombre" is a string that represents the name entered by the
        #user
        #:return: The function `nombre` returns the result of either `messagebox.showinfo("Error",
        #"Debes insertar tu nombre")` or `abrirventana_juego(nivel, nombre)`.
        def nombre(nivel, nombre):
            if nombre == "":
                return messagebox.showinfo("Error", "Debes insertar tu nombre")
            else:
                return abrirventana_juego(nivel, nombre)
        
        nombre_entry = tk.Entry(ventana_nickname, font=("Times New Roman", 12))
        nombre_entry.place(x=300, y=150)

        puntos = 0
            
        #The function "abrirventana_juego" opens a new window for a game with a specified level and
        #player name.
        #:param nivel: The "nivel" parameter represents the level of the game. It could be an integer
        #alue indicating the difficulty level or a string value representing the name of the level
        #param nombre: The parameter "nombre" is a variable that represents the name of the player
        #Función abrir ventana Juego
        def abrirventana_juego():
            ventana_juego = tk.Toplevel()
            ventana_juego.title("Game")
            ventana_juego.geometry("850x700")
            ventana_juego.resizable(height=False, width=False)
            canvasC8 = tk.Canvas(ventana_juego, width=800, height=700, borderwidth=0, highlightthickness=0, background="white")
            canvasC8.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            
            #Botón back del juego
            #The function creates a "Back" button in a game window that, when clicked, closes the
            #game window and brings back the main window.
                
            def back():
                ventana_juego.destroy()
                ventana1.deiconify()
            botonBack = tk.Button(ventana_juego, text="Back", font=("Courier New", 12, "bold"), command=back, fg=("white"), bg=("black"), width=8)
            botonBack.pack()
            botonBack.place(x=650, y=600)

            #Contador de puntos
            #The function `actualizar_puntuacion` updates the score by adding the new points and
            #displays the rounded score on a tkinter label.
            #param puntos_nuevos: The parameter "puntos_nuevos" represents the number of new points
            #that will be added to the current score
            def actualizar_puntuacion(puntos_nuevos):
                global puntos
                puntos += puntos_nuevos
                puntos_redondeados = math.ceil(puntos)
                texto_puntuacion = tk.Label(canvasC8, font=("Courier New", 9, "bold"), background="red", fg="white")
                texto_puntuacion.pack()
                texto_puntuacion.place(x=680, y=230)
                texto_puntuacion.config(text=f'Puntuación: {puntos_redondeados}')    
            
            
            # The above code is creating a label widget in a tkinter canvas. The label is used to
            # display a timer. The initial value of the timer is set to 0 seconds.
            #Contador de tiempo
            contador_label = tk.Label(canvasC8, font=("Courier New", 13, "bold"), background="black", fg="white")
            contador_label.pack()
            contador_label.place(x=220, y=600)

            segundos = 0

            #The function `actualizar_contador` updates a counter every second and displays the elapsed time in seconds.
            def actualizar_contador():
                nonlocal segundos
                segundos += 1
                contador_label.config(text=f"Tiempo transcurrido: {segundos} segundos"), 
                ventana_juego.after(1000, actualizar_contador)

            actualizar_contador()
            
            # The above code is creating a label widget in a tkinter canvas. The label is displayed
            # with a red background and white text. It is positioned at coordinates (680, 200) on the
            # canvas. The label text is set to "Bomba letra (B)".
            #Bomba en la pantalla de juego
            bomba_label = tk.Label(canvasC8, font=("Courier New", 9, "bold"), background="red", fg="white")
            bomba_label.pack()
            bomba_label.place(x=680, y=200)
            bomba_label.config(text=f"Bomba letra (B)")
            
            # The above code is creating a label widget in a tkinter canvas. The label is displaying
            # the text "Puntuación" and has a red background with white text. It is positioned at
            # coordinates (680, 230) on the canvas.
            #Contador pantalla juego para que se vea desde que se inicia
            bomba_label = tk.Label(canvasC8, font=("Courier New", 9, "bold"), background="red", fg="white")
            bomba_label.pack()
            bomba_label.place(x=680, y=230)
            bomba_label.config(text=f"Puntuación")
            
            # The above code is creating a label widget in a tkinter canvas. The label is displayed
            # with a red background and white text. It is positioned at coordinates (280, 560) on the
            # canvas. The label's text is set to "Teletransportar seguro (K)".
            #Teletransportar en la pantalla de juego
            bomba_label = tk.Label(canvasC8, font=("Courier New", 9, "bold"), background="red", fg="white")
            bomba_label.pack()
            bomba_label.place(x=280, y=560)
            bomba_label.config(text=f"Teletransportar seguro (K)")
            
            # The above code is creating a label widget in a tkinter canvas. The label is displayed
            # with a red background and white text. It is positioned at coordinates (50, 560) on the
            # canvas. The label's text is set to "Teletransportar letra (T)".
            #Teletransportar en la pantalla de juego
            bomba_label = tk.Label(canvasC8, font=("Courier New", 9, "bold"), background="red", fg="white")
            bomba_label.pack()
            bomba_label.place(x=50, y=560)
            bomba_label.config(text=f"Teletransportar letra (T)")
            
            # The above code is loading an image of a board onto a canvas in a tkinter window. The
            # image is loaded using the `tk.PhotoImage` function and the file path is specified. The
            # canvas is then created with the same dimensions as the image and the image is displayed
            # on the canvas using the `create_image` method.
            # Cargar la imagen del tablero en el canvas
            imagen = tk.PhotoImage(file="Tablero.png")  # Asegúrate de que la ruta sea correcta
            canvasC6 = tk.Canvas(ventana_juego, width=imagen.width(), height=imagen.height())
            canvasC6.pack()
            canvasC6.create_image(0, 0, anchor=tk.NW, image=imagen)

            # The above code is loading an image of the main character onto a canvas and adjusting its
            # coordinates. It creates a PhotoImage object from the file "Personaje.png" and sets the
            # initial coordinates of the character to (252, 255). Then, it creates an image item on
            # the canvas using the create_image method, specifying the anchor as tk.NW (northwest) and
            # the image as the loaded image.
            # Cargar la imagen del personaje principal en el canvas y ajustar las coordenadas
            imagen_personaje = tk.PhotoImage(file="Personaje.png")  # Asegúrate de que la ruta sea correcta
            x_personaje, y_personaje = 252, 255  # Ajustar las coordenadas iniciales
            personaje = canvasC6.create_image(x_personaje, y_personaje, anchor=tk.NW, image=imagen_personaje)

            # The above code is defining a function to move robots on a grid. It also defines the
            # valid coordinates within the grid.
            #FUNCION PARA MOVER LOS ROBOTS
            # Definir las coordenadas válidas dentro del tablero
            coordenadas_validas_x = list(range(0, 500, 36))  # 0, 36, 72, ..., 468
            coordenadas_validas_y = list(range(0, 450, 36))  # 0, 36, 72, ..., 396

            # Función para mover los robots aleatoriamente
            #The function moves the robots randomly.

            def mover_robots_aleatoriamente():
                
                #The function "mover_robots_aleatoriamente" generates random coordinates for each robot
                #within valid coordinates and moves the robots to the new coordinates on a canvas.
                
                global x_robot1, y_robot1, x_robot2, y_robot2, x_robot3, y_robot3, x_robot4, y_robot4, x_robot5, y_robot5

                # Generar nuevas coordenadas aleatorias para cada robot dentro de las coordenadas válidas
                x_robot1, y_robot1 = random.choice(coordenadas_validas_x), random.choice(coordenadas_validas_y) 
                x_robot2, y_robot2 = random.choice(coordenadas_validas_x), random.choice(coordenadas_validas_y)
                x_robot3, y_robot3 = random.choice(coordenadas_validas_x), random.choice(coordenadas_validas_y)
                x_robot4, y_robot4 = random.choice(coordenadas_validas_x), random.choice(coordenadas_validas_y)
                x_robot5, y_robot5 = random.choice(coordenadas_validas_x), random.choice(coordenadas_validas_y)

                # Mover los robots a las nuevas coordenadas
                canvasC6.coords(robot1, x_robot1, y_robot1)
                canvasC6.coords(robot2, x_robot2, y_robot2)
                canvasC6.coords(robot3, x_robot3, y_robot3) 
                canvasC6.coords(robot4, x_robot4, y_robot4)
                canvasC6.coords(robot5, x_robot5, y_robot5)

            # FUNCION PARA MOVER EL PERSONAJE
            #The function "mover_jugador" is used to move the character in a game and update thescore.
            #:param event: The event parameter is an object that represents the event that triggered
            #the function. In this case, it is used to determine which key was pressed by the user
              
            def mover_jugador(event):
                nonlocal x_personaje, y_personaje  # Usamos nonlocal para modificar las variables globales

                if event.keysym == 'w':
                    y_personaje -= 36.3
                elif event.keysym == 'x':
                    y_personaje += 36.3
                elif event.keysym == 'a':
                    x_personaje -= 36.3
                elif event.keysym == 'd':
                    x_personaje += 36.3
                elif event.keysym == 'q':
                    x_personaje -= 36.3
                    y_personaje -= 36.3
                elif event.keysym == 'e':
                    y_personaje -= 36.3
                    x_personaje += 36.3
                elif event.keysym == 'z':
                    y_personaje += 36.3
                    x_personaje -= 36.3
                elif event.keysym == 'c':
                    y_personaje += 36.3
                    x_personaje += 36.3
                if event.keysym in ['w', 'x', 'a', 'd', 'q', 'e', 'z', 'c']:
                    actualizar_puntuacion(5)
                    mover_robots_aleatoriamente()
                    
                    
           # The above code is checking if the character's position exceeds the size of the board in
           # the X and Y axes. If the character's position is less than 0 or greater than the
           # width/height of the board, it wraps around to the opposite side of the board. The code
           # then updates the character's position on the canvas using the `coords()` method.
            
            #TRASPASAR TABLERO
                # Verificar si el personaje excede el tamaño del tablero en el eje X (horizontal)
                if x_personaje < 0:
                    x_personaje = canvasC6.winfo_width() - 36.3
                elif x_personaje > canvasC6.winfo_width():
                    x_personaje = 0
                # Verificar si el personaje excede el tamaño del tablero en el eje Y (vertical)
                if y_personaje < 0:
                    y_personaje = canvasC6.winfo_height() - 36.3
                elif y_personaje > canvasC6.winfo_height():
                    y_personaje = 0

                canvasC6.coords(personaje, x_personaje, y_personaje)
     
            # The above code is binding the function "mover_jugador" to the "KeyPress" event of the
            # "ventana_juego" object. This means that whenever a key is pressed while the game window
            # is in focus, the function "mover_jugador" will be called.
            
            #Enlazar para que se mueva el jugador
            ventana_juego.bind("<KeyPress>", mover_jugador)
                        
            #The code defines a function called "teletransportar" that is associated with the "k" key
            #event in a game. When the key is pressed, the function generates random coordinates
            #within the boundaries of a game board, updates the position of a character on the
            #canvas, and moves robots randomly.
            
            #:param event: The event parameter represents the event that triggered the
            #teletransportar function. In this case, it is the key press event for the "k" key
            #Bandera para controlar si el teletransporte ya se ha realizado
            global teletransporte_realizado
            teletransporte_realizado = False

            # Función para teletransportarse
            def teletransportar(event):
                global x_personaje, y_personaje, teletransporte_realizado

                # Verificar si el teletransporte aún no se ha realizado
                if not teletransporte_realizado:
                    # Obtenemos las dimensiones del tablero y convertirlas en enteros
                    ancho_tablero = int(canvasC6.winfo_width()) 
                    altura_tablero = int(canvasC6.winfo_height())
                    # Calcular el número de casillas en el tablero
                    num_casillas_ancho = ancho_tablero // 36
                    num_casillas_altura = altura_tablero // 36
                    # Generar coordenadas aleatorias múltiples de 36 dentro de los límites del tablero
                    x_personaje = random.randint(0, num_casillas_ancho - 1) * 36
                    y_personaje = random.randint(0, num_casillas_altura - 1) * 36
                    # Actualizar la posición del personaje en el canvas
                    canvasC6.coords(personaje, x_personaje, y_personaje)
                    mover_robots_aleatoriamente()

                    # Establecer la bandera a True para indicar que el teletransporte se ha realizado
                    teletransporte_realizado = True

                    # Desvincular la función de teletransporte del evento
                    ventana_juego.unbind("k")

            # Asocia la función de teletransporte a una tecla (por ejemplo, "k")
            ventana_juego.bind("k", teletransportar)
                        
            #FUNCION PARA TELETRANSPORTARSE
            #The function "teletransportar" allows the character in the game to teleport to a random
            #location on the game board.
                
            def teletransportar():
                global x_personaje, y_personaje
                # Obtenemos las dimensiones del tablero y convertirlas en enteros
                ancho_tablero = int(canvasC6.winfo_width()) 
                altura_tablero = int(canvasC6.winfo_height())
                # Calcular el número de casillas en el tablero
                num_casillas_ancho = ancho_tablero // 36
                num_casillas_altura = altura_tablero // 36
                # Generar coordenadas aleatorias múltiples de 36 dentro de los límites del tablero
                x_personaje = random.randint(0, num_casillas_ancho - 1) * 36
                y_personaje = random.randint(0, num_casillas_altura - 1) * 36
                # Actualizar la posición del personaje en el canvas
                canvasC6.coords(personaje, x_personaje, y_personaje)
                mover_robots_aleatoriamente()

            ventana_juego.bind("t", lambda event: teletransportar())
                        
            
            #FUNCION PARA DISPARO    
            #The function "disparar" is used to shoot a projectile in a game, updating the score as
            #the projectile moves upwards.
            #:param x: The x-coordinate of the starting position of the bullet
            #:param y: The parameter "y" represents the current y-coordinate of the bullet on the
            #canvas. It is used to determine the position of the bullet and to control the recursion
            #of the function
            
            def disparar(x, y):
                # Cargar la imagen del disparo en el canvas y ajustar las coordenadas
                imagen_disparo = tk.PhotoImage(file="Bala.png")  # Asegúrate de que la ruta sea correcta
                canvasC6.create_image(x, y, anchor=tk.NW, image=imagen_disparo)
                
                # Caso base: si se han disparado las dos casillas
                if y > y_personaje - 100.2:  # Dispara solo 2 casillas hacia arriba
                    ventana_juego.update()
                    time.sleep(0.1)  # Agrega un pequeño retraso para la animación
                    disparar(x, y - 36.3)  # Llamada recursiva con las nuevas coordenadas del disparo
                    
                #Puntos barra space
                actualizar_puntuacion(3.33)

             # Asocia el evento de teclado 'space' a la función 'disparar' con las coordenadas iniciales
            ventana_juego.bind("<space>", lambda event: disparar(x_personaje, y_personaje - 40.6))
    
            #FUNCION PARA COLOCAR BOMBAS
            #The function `colocar_bomba` is used to place a bomb image on a canvas at specific
            #coordinates based on the direction of the character.
            #Función para cargar imágenes
            def cargar_imagen():
                # Cargar la imagen de la bomba y guardar una referencia en una variable global
                global imagen_bomba
                imagen_bomba = tk.PhotoImage(file="Bomba.png")

            def colocar_bomba(event, direccion):
                # Calcular las coordenadas de la casilla delante del personaje
                if event.keysym == 'b':
                    if direccion == 'w':
                        x_bomba = x_personaje
                        y_bomba = y_personaje - 36.3
                    elif direccion == 's':
                        x_bomba = x_personaje
                        y_bomba = y_personaje + 36.3
                    elif direccion == 'a':
                        x_bomba = x_personaje - 36.3
                        y_bomba = y_personaje
                    elif direccion == 'd':
                        x_bomba = x_personaje + 36.3
                        y_bomba = y_personaje

                    canvasC6.create_image(x_bomba, y_bomba, anchor=tk.NW, image=imagen_bomba)

            # Llamar a la función para cargar la imagen antes de usarla
            cargar_imagen()

            # Modificar la llamada a la función bind para incluir la dirección
            ventana_juego.bind("b", lambda event: colocar_bomba(event, 'w'))

            # The above code is creating multiple instances of a robot image on a canvas using the
            # Tkinter library in Python. Each robot is created with a different set of coordinates and
            # displayed on the canvas. The code also creates a window to display the canvas with the
            # robots.
            #ROBOTS
            #Función para cargar imágenes
            imagen_robot = tk.PhotoImage(file="Robot.png")  # Asegúrate de que la ruta sea correcta
            x_robot, y_robot = 392, 255  # Ajustar las coordenadas iniciales
            robot1 = canvasC6.create_image(x_robot, y_robot, anchor=tk.NW, image=imagen_robot)
            
            imagen_robot2 = tk.PhotoImage(file="Robot.png")  # Asegúrate de que la ruta sea correcta
            x_robot, y_robot = 0, 150  # Ajustar las coordenadas iniciales
            robot2 = canvasC6.create_image(x_robot, y_robot, anchor=tk.NW, image=imagen_robot2)
            
            imagen_robot3 = tk.PhotoImage(file="Robot.png")  # Asegúrate de que la ruta sea correcta
            x_robot, y_robot = 140, 510  # Ajustar las coordenadas iniciales
            robot3 = canvasC6.create_image(x_robot, y_robot, anchor=tk.NW, image=imagen_robot3)
            
            imagen_robot4 = tk.PhotoImage(file="Robot.png")  # Asegúrate de que la ruta sea correcta
            x_robot, y_robot = 140, 255  # Ajustar las coordenadas iniciales
            robot4 = canvasC6.create_image(x_robot, y_robot, anchor=tk.NW, image=imagen_robot4)
            
            imagen_robot5 = tk.PhotoImage(file="Robot.png")  # Asegúrate de que la ruta sea correcta
            x_robot, y_robot = 70, 40  # Ajustar las coordenadas iniciales
            robot5 = canvasC6.create_image(x_robot, y_robot, anchor=tk.NW, image=imagen_robot5)
                    
            ventana_nickname.mainloop()


















        # The above code is creating two buttons labeled "Nivel 1" and "Nivel 2" with different
        # positions on a canvas. These buttons have a black background, white text, and a bold Courier
        # New font. When clicked, they will call the function "nombre" with the arguments 1 or 2
        # (depending on the button clicked) and the value entered in the "nombre_entry" entry field.
        #Boton de Niveles" 
        botonpuntaje = tk.Button(canvasC2, text="Nivel 1", bg="black", fg=("white"), font=("Courier New", 12, "bold",), width=8,
        command=abrirventana_juego)
        botonpuntaje.place(x=300, y=340, anchor=tk.S)

        botonpuntaje = tk.Button(canvasC2, text="Nivel 2", bg="black", fg=("white"), font=("Courier New", 12, "bold"), width=8,
        command=lambda: nombre(2, nombre_entry.get()))
        botonpuntaje.place(x=470, y=340, anchor=tk.S)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
    
    
    
    
    #Función abrir venta "Mejores puntajes"
    #The function "abrirventana3" opens a new window titled "Mejores Puntajes" and displays a list of
    #the best scores.

    def abrirventana3():
        ventana1.withdraw()
        ventana3 = Toplevel()
        ventana3.title("Mejores Puntajes")
        ventana3.geometry("800x480")
        ventana3.configure(background="black")
        canvasC3 = tk.Canvas(ventana3, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC3, text="Mejores Puntuaciones", font=("Times New Roman", 17), background="black", fg="white")
        titulo.place(x=290, y=120)
        ventana3.resizable(height=False, width=False)
        
        texto= tk.Label(canvasC3, text="Jeff: 1500pts "
                                        "\nJose: 1000pts" 
                                        "\nIan: 950pts"

                                        
                                ,font=("Courier New", 17, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto.place(x=50, y=180)
    
        #Botón back de Mejores Puntajes
        #The function creates a "Back" button in a tkinter window that, when clicked, closes the
        #current window and opens another window.
        
        def back():
            ventana3.destroy()
            ventana1.deiconify()
        botonBack = tk.Button(ventana3, text="Back", command= back,  font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)
        
        abrirventana3.mainloop()
    
    #Fución abrir ventana de Configuración
    #The function "abrirventana4" opens a new window for sound configuration.
    def abrirventana4():
        ventana1.withdraw()
        ventana4 = Toplevel()
        ventana4.title("Ventana 4")
        ventana4.geometry("800x480")
        ventana4.configure(background="black")
        canvasC4 = tk.Canvas(ventana4, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo= tk.Label(canvasC4, text="Sonido", font=("Courier New", 16, "bold"), background="black", fg="white")
        titulo.place(x=330 ,y=170)
        ventana4.resizable(height=False, width=False)

        # Botón de play
        botonP = Button(ventana4, text="Play", font=("Courier New", 12, "bold"), command=play, fg=("white"), bg=("black"), width=8)
        botonP.pack()
        botonP.place(x=500, y=300)
        
        # Botón de stop music
        botonBack = tk.Button(ventana4, text="Stop Music", font=("Courier New", 12, "bold"), command=stop_music, fg=("white"), bg=("black"), width=12)
        botonBack.pack()
        botonBack.place(x=600, y=300)

        #Botón de back Ventana Configuración
        def back():
            ventana4.destroy()
            ventana1.deiconify()
  
        botonBack = tk.Button(ventana4, text="Back", command= back, font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)

        abrirventana4.mainloop()



    #Fución abrir ventana de Ayuda
    #The function "abrirventana5" opens a new window with information about the controls of a game.
        
    def abrirventana5():
        ventana1.withdraw()
        ventana5 = Toplevel()
        ventana5.title("Ventana 3")
        ventana5.geometry("800x480")
        ventana5.configure(background="white")
        canvasC4 = tk.Canvas(ventana5, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        titulo= tk.Label(canvasC4, text="Controles", font=("Courier New", 15, "bold"), fg=("white"), bg=("black"))
        titulo.place(x=310, y=120)
        ventana5.resizable(height=False, width=False)

        texto= tk.Label(canvasC4, text="Mover hacia arriba: W "
                                        "\nMover hacia abajo: X" 
                                        "\nMover hacia la derecha: D"
                                        "\nMover hacia la izquierda: A"
                                        "\nMover hacia arriba a la derecha: E"
                                        "\nMover hacia arriba a la izquierda: Q"
                                        "\nMover hacia la abajo a la derecha: C"
                                        "\nMover hacia abajo a la izquierda: Z"
                                        "\nDisparar: barra espaciadora"
                                        "\nPoner bomba: B"
                                        "\nTeletransportarse: T"
                                        
                                ,font=("Courier New", 12, "bold"), fg=("white"), bg=("black"), justify=tk.LEFT)
        texto.place(x=50, y=180)

        image= Image.open("Teclado.png")
        image = image.resize((500,150))
        img = ImageTk.PhotoImage(image)
        yo_img = Label(canvasC4, image=img)
        yo_img.pack()
        yo_img.place(x=110, y=405)

        #Botón de back Ventana Ayuda
        #The above code creates a button in a tkinter window that, when clicked, closes the current
        #window and opens another window.
        
        def back():
            ventana5.destroy()
            ventana1.deiconify()

        botonBack = tk.Button(ventana5, text="Back", command= back, fg=("white"), font=("Courier New", 12, "bold"), bg=("black"), width=8)
        botonBack.pack()
        botonBack.place(x=650, y=420)

        abrirventana5.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    #Fución abrir ventana "Acerca de"
    #The function "abrirventana6" opens a new window called "Acerca de" with personal information and
    #a back button.
    def abrirventana6():
        ventana1.withdraw()
        
        # Crear la primera ventana
        ventana6_1 = Toplevel()
        ventana6_1.title("Ventana 6-1")
        ventana6_1.geometry("800x480")
        ventana6_1.configure(background="black")

        canvasC4_1 = tk.Canvas(ventana6_1, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4_1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo_1 = tk.Label(canvasC4_1, text="Informacion Personal 1", fg=("white"), font=("Courier New", 12, "bold"), bg=("black"))
        titulo_1.place(x=308, y=110)

        # Crear la segunda ventana
        ventana6_2 = Toplevel()
        ventana6_2.title("Ventana 6-2")
        ventana6_2.geometry("800x480")
        ventana6_2.configure(background="black")

        canvasC4_2 = tk.Canvas(ventana6_2, width=800, height=680, borderwidth=0, highlightthickness=0, background="black")
        canvasC4_2.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        titulo_2 = tk.Label(canvasC4_2, text="Informacion Personal 2", fg=("white"), font=("Courier New", 12, "bold"), bg=("black"))
        titulo_2.place(x=308, y=110)

        # Hacer que las nuevas ventanas sean resizables
        ventana6_1.resizable(height=False, width=False)
        ventana6_2.resizable(height=False, width=False)
        
        
        
        
        abrirventana6.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # The above code is creating a GUI window using the Tkinter library in Python. It creates several
    # buttons with different functionalities such as "Jugar" (Play), "Configuración" (Settings),
    # "Ayuda" (Help), "Mejores Puntajes" (Best Scores), and "Acerca de" (About). Each button is placed
    # at a specific position on the window. The code then runs the main loop of the window to display
    # it and handle user interactions.
    #Botones Principales VENTANA 1
    boton1 = tk.Button(ventana1, text="Jugar", command= abrirventana_nickname,font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton1.place(x=240, y=60)
    boton2 = tk.Button(ventana1, text="Configuración",command=abrirventana4 and abrirventana6, font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton2.place(x=185, y=217)
    boton3 = tk.Button(ventana1, text="Ayuda", command=abrirventana5, font=("Courier New", 14, "bold"), fg=("white"), bg=("black"))
    boton3.place(x=75, y=420)
    boton4 = tk.Button(ventana1, text="Mejores Puntajes",command=abrirventana3, font=("Courier New", 16, "bold"), fg=("white"), bg=("black"))
    boton4.place(x=170, y=140)
    boton5 = tk.Button(ventana1, text="Acerca de", command=abrirventana6,  font=("Courier New", 14, "bold"), fg=("white"), bg=("black"))
    boton5.place(x=350, y=420)
    
    ventana1.mainloop()
ventana_inicio()





        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
