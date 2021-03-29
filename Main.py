import tkinter as tk
import random

robotPoints = 0
playerPoints = 0
textMessage = "¡Empate!"
tieColor = "SystemButtonFace"
position = [240, 90]

def start():
    choices = ["piedra", "papel", "tijera"]
    element = random.choice(choices)
    
    puntosUser = tk.Label(root, text= ("Tus Puntos: "+str(playerPoints)), font=("Calibri", 20))
    puntosUser.place(x=10, y=10)
    
    puntosRobot = tk.Label(root, text= ("Puntos del Robot: "+str(robotPoints)), font=("Calibri", 20))
    puntosRobot.place(x=365, y=10)  
    
    def destroy():
        piedra.destroy()
        papel.destroy()
        tijera.destroy()
        tieText.destroy()
        start()
    
    def doubleCheck():
        global playerPoints, robotPoints, textMessage, tieColor, tieColor
        if playerPoints <= 3 or robotPoints <= 3: return False
        else: return True
    
    def win(x, y): 
        global playerPoints, robotPoints, puntosUser, textMessage, tieColor, position
        if x == "client":
            if doubleCheck() == False:
                playerPoints +=1
                if playerPoints == 3: 
                    textMessage="¡Enhorabuena! Has ganado!"
                    tieColor="black"
                    position = [145, 90]
        else:
            if doubleCheck() == False:
                robotPoints +=1
                if robotPoints == 3: 
                    textMessage="¡Lo Sentimos! Has perdido!"
                    tieColor="black"
                    position = [145, 90]
        destroy()
    def empate():
        global tieColor
        if doubleCheck() == False: 
            tieColor = "black"
            destroy()
    
    def check(x, y):
        global tieColor
        tieColor="SystemButtonFace"
        if x == y: empate()
        elif x == "piedra" and y == "papel": win("robot", y)
        elif x == "piedra" and y == "tijera": win("client", y)
        elif x == "papel" and y == "tijera": win("robot", y)
        elif x == "papel" and y == "piedra": win("client", y)
        elif x == "tijera" and y == "piedra": win("robot", y)
        else: win("client", y)    
    
    startTitle.destroy()
    startButton.destroy()
    
    piedra = tk.Button(root, text="Piedra", command= lambda: check("piedra", element))
    piedra.pack()
    
    papel = tk.Button(root, text="Papel", command= lambda: check("papel", element))
    papel.pack()
    
    tijera = tk.Button(root, text="Tijera", command= lambda: check("tijera", element))
    tijera.pack()
    
    tieText = tk.Label(root, text=textMessage, font=("Calibri", 20), fg=tieColor)
    tieText.place(x=position[0], y=position[1])

root = tk.Tk()
root.title("Piedra, Papel o Tijera")
root.geometry("600x300")
root.resizable(False, False)

### StarButton ###

startTitle = tk.Label(root, text="Piedra, Papel o Tijera", font=("Calibri", 25))
startTitle.pack()

startButton = tk.Button(root, text="Empezar", width=20, font=("Calibri", 20), fg="white", bg="green", command=start)
startButton.place(x=155, y=105)

root.mainloop()