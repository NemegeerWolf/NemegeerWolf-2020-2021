#snake 
#made by wolf nemegeer

import time
import keyboard
import random
snake = [[6,6]]
RichtingBlok = [0]
food = [0,0]
speelveld = []
milisec = 0;

def teken_speelveld():
    global snake

    global food
    global speelveld
    for i in range(0, 12):
        rij = []
        for e in range(0, 12):
            rij.append("   ")
        speelveld.append(rij)

    speelveld[food[1]][food[0]] = "$"

    for stukje in snake:
        speelveld[stukje[1]][stukje[0]] = " * "

    speelveld[snake[0][1]][snake[0][0]] = " O "  

    for i in range(0, 12):
        rij = ""
        for e in range(0, 12):
            rij += speelveld[i][e]
        print(rij)

def controleer_keyboard():
    global RichtingBlok
    global snake
    
    global food
    if keyboard.is_pressed('Right'):
        
            # kan niet keren.
        if not(RichtingBlok[0] == 4 and len(snake) > 1):
            RichtingBlok[0] = 2;
            
        
    elif keyboard.is_pressed('Up'):
        
        if not(RichtingBlok[0] == 3 and len(snake) > 1):
            RichtingBlok[0]= 1;
            
        
    elif keyboard.is_pressed('Left'):
        
        if not (RichtingBlok[0] == 2 and len(snake) > 1):
            RichtingBlok[0] = 4;
            
        
    elif keyboard.is_pressed('Down'):
        
        if not(RichtingBlok[0] == 1 and len(snake) > 1):
            
            RichtingBlok[0] = 3;
            
def bereken_spel():
    global snake
    global stukje
    global food
    try:
        
        # detectie eten
        if snake[0][0] == food[0] and snake[0][1] == food[1]:
        
            # voeg een stukje staart toe
            stukje = [0,0]
            #hoofd.Height = hoofd.Width = 10;
            if (RichtingBlok[len(RichtingBlok) - 1] == 1): stukje = snake[len(snake)- 1][0], snake[len(snake) - 1][1] + 1
            if (RichtingBlok[len(RichtingBlok) - 1] == 2): stukje = snake[len(snake)- 1][0] - 1, snake[len(snake) - 1][1]
            if (RichtingBlok[len(RichtingBlok) - 1] == 3): stukje = snake[len(snake)- 1][0], snake[len(snake) - 1][1] - 1
            if (RichtingBlok[len(RichtingBlok) - 1] == 4): stukje = snake[len(snake)- 1][0] + 1, snake[len(snake) - 1][1]
            
            
            snake.append(stukje)
            RichtingBlok.append(RichtingBlok[len(RichtingBlok) - 1])
           # score++;
            
            # verplaats eten
            food = [(random.randrange(1, 12)), (random.randrange(1, 12))]
        

        
        # verplaating snake
        # verplaats snake
        i = 0;
        for stukje in snake:
            x = stukje[0]
            y = stukje[1]
            if RichtingBlok[i] == 1:
            
                y = y - 1;
                
            
            if RichtingBlok[i] == 2:
            
                x = x + 1;
                
            
            if RichtingBlok[i] == 3:
            
                y = y + 1;
                
            
            if RichtingBlok[i] == 4:
            
                x = x - 1;
            stukje = [x,y]    
            
            # raak je je eigen staart
            if not i == 0:
            
                if stukje == snake[0]:
                
                    
                    
                    
                    
                    RichtingBlok.clear();
                    RichtingBlok.append(0);
                    snake = [[6,6]]
                    
                    food = [(random.randrange(1, 12)), (random.randrange(1, 12))]
                    
                    
                   
                    

                
            
            # als je raakt de rand ga naar de andere kant
            # muur portalen
            if x == -1:
            
                x = 11
            
            if x == 12:
            
                x = 1
            
            if y == -1:
            
                y = 11;
            
            if y == 12: 
            
                y = 1;
            

            
            snake[i] = [x,y]
            i += 1
        


        # toekomstige verplaatsing µ
        j = len(RichtingBlok) - 1
        while j >= 0:
        
            if not j == 0:
            
                RichtingBlok[j] = RichtingBlok[j - 1];
            
            j-=1
        

    except:
        print()


while(True):

    if milisec == 500:
        bereken_spel()
        speelveld.clear()
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        teken_speelveld()
        milisec = 0

    controleer_keyboard()
    
    

    

    time.sleep(0.02)
    milisec += 20;
