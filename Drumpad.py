#Modules importés
import pygame
import sys
from pygame import mixer
import time as time

mixer.init() #Initialise le module

#Affectation de fichiers audio à des variables
Snare='Sounds/Snare.wav'
Hihat_Open='Sounds/HihatOpen.wav'
Hihat_Closed='Sounds/HihatClosed.wav'
Kick='Sounds/Kick.wav'
Hihat_Pedal='Sounds/Hihat_Pedal.wav'
Mid_Tom='Sounds/Mid_Tom.wav'
Shake='Sounds/Shake.wav'
Slap='Sounds/Slap.wav'
Clap='Sounds/Clap.wav'
Triangle='Sounds/Triangle.mp3'
Cymbale='Sounds/Cymbale.mp3'
Drum='Sounds/Drum.mp3'
Light_Drum='Sounds/Light_Drum.mp3'
Drum2='Sounds/Drum2.mp3'
Drum3='Sounds/Drum3.mp3'
Clap2='Sounds/Clap2.mp3'
Blank='Sounds/BlankSound.wav'

#Variables de départ
record=False
rep=0
Liste_Son=[]
Dico_Son={'1':Snare, '2':Hihat_Open, '3':Hihat_Closed, '4':Kick, '5':Hihat_Pedal, '6':Mid_Tom, '7':Shake, '8':Slap, '9':Clap, '10':Triangle, '11':Cymbale, '12':Drum, '13':Light_Drum, '14':Drum2, '15':Drum3, '16':Clap2, '17':Blank}
i=0
play=0
tempo=0.2

#COULEURS
# 1ère colonne
white = pygame.Color(255, 255, 255)
light_red = pygame.Color(255, 130, 130)
light_blue = pygame.Color (180, 255, 255)
black = pygame.Color(0, 0, 0) 
# 2ème colonne
yellow = pygame.Color(255, 255, 100)
orange = pygame.Color(255, 128, 0)
turquoise_blue = pygame.Color(64, 224, 208)
light_grey = pygame.Color (200, 200, 200)
# 3ème colonne
light_green = pygame.Color (115, 255, 115)
pink = pygame.Color(212, 115, 212)
regular_blue = pygame.Color (90, 190, 255)
grey = pygame.Color(130, 130, 130)
# 4ème colonne
green = pygame.Color(0, 255, 0)
violet = pygame.Color (150, 75, 255)
dark_blue = pygame.Color(50, 50, 255)
red = pygame.Color(255, 50, 50)

#Fonctions pour assertions
def choix(a):
    assert (a==1 or a==2 or a==3) and type(a)==int,"Aucunes options n'est associé à ce nombre"
    return a
    
def choix_2(b):
    assert b<= (len(Liste_Son)) and b>= 1 and type(b)==int, "Aucun son n'est associé à ce placement"
    b-=1
    return b

def choix_3(c):
    assert c<=17 and c>=1 and type(c)==int, "Ce son n'existe pas"
    return c

def boucle_assert(play):
    assert play>=0, "Le nombre de boucle choisi ne peut pas être négatif"
    return play

def tempo_assert(tempo):
    assert tempo>=0, "Une durée ne peut être négative"
    return tempo

#DEBUT DU CODE POUR L'INSTRUMENT
while True :
    #Code de la fenêtre du menu
    if i==0 :
        while i==0:
            pygame.init()
  
            res = (1600,900) #Résolution de la fenêtre

            screen = pygame.display.set_mode(res) #Créer une fenêtre
  
            color = (255,255,255) #Couleur blanche
  
            color_light = (170,170,170) #Gris clair pour les boutons
  
            color_dark = (100,100,100) #Gris foncé pour les boutons
  
            width = screen.get_width() #Largeur de la fenêtre
  
            height = screen.get_height() #Hauteur de la fenêtre
  
#Polices d'écriture utilisées dans cette fenêtre
            bigfont = pygame.font.SysFont('bahnschrift',45)
            titlefont = pygame.font.SysFont('bahnschrift',100)
            
#Textes présents dans cette fenêtre
            Titre_jeu = titlefont.render('DRUMPAD SIMULATOR',True,color)
            Quit = bigfont.render('QUIT' , True , color)
            Start = bigfont.render('START' ,True, color)
            Tutoriel = bigfont.render('TUTORIEL',True,color)

#Code du MENU
            while True and i==0:
      
                for ev in pygame.event.get(): #Analyse les évènements que provoque l'utilisateur
          
                    if ev.type == pygame.QUIT:
                        pygame.quit() #Quitte le jeu si la croix est appuyée
              
        #Teste si l'évènement "La souris est cliquée" se produit
                    if ev.type == pygame.MOUSEBUTTONDOWN:
              
            #Si on clique dans cette zone, on quitte le jeu
                        if width/2-100 <= mouse[0] <= width/2+100 and height/2+100 <= mouse[1] <= height/2+155:
                            pygame.quit()
            #Si on clique dans cette zone, on passe à la page principale (ligne 105)
                        elif width/2-100 <= mouse[0] <= width/2+100 and height/2-100 <= mouse[1] <= height/2:
                            i=1
            #Si on clique dans cette zone, on va à la fenêtre du tutoriel (ligne 275)
                        elif width/2-100 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+55:
                            i=2
                
    #Couleur d'arrière-plan de la fenêtre
                screen.fill((60,25,60))
    
    #Stocke les coordonnées de la souris dans une variable
                mouse = pygame.mouse.get_pos()
      
   #Si la souris passe par dessus les boutons, ils deviennent plus clairs. Sinon, ils restent sombre
                if width/2-100 <= mouse[0] <= width/2+100 and height/2-100 <= mouse[1] <= height/2:
                    pygame.draw.rect(screen,color_light,[width/2-100,height/2-100,200,55])
                elif width/2-100 <= mouse[0] <= width/2+100 and height/2 <= mouse[1] <= height/2+55:
                    pygame.draw.rect(screen,color_light,[width/2-100,height/2,200,55])
                elif width/2-100 <= mouse[0] <= width/2+100 and height/2+100 <= mouse[1] <= height/2+155:
                    pygame.draw.rect(screen,color_light,[width/2-100, height/2+100,200,55])
                else:
                    pygame.draw.rect(screen,color_dark,[width/2-100, height/2-100,200,55])
                    pygame.draw.rect(screen,color_dark,[width/2-100,height/2,200,55])
                    pygame.draw.rect(screen,color_dark,[width/2-100,height/2+100,200,55])
 
     #Superpose les textes sur les boutons
                screen.blit(Quit , (width/2-100,height/2+100))
                screen.blit(Start, (width/2-100,height/2-100))
                screen.blit(Tutoriel, (width/2-100,height/2))
                screen.blit(Titre_jeu,(width/2-500,height/2-400))
    #Affiche les éléments dessinés sur la fenêtre
                pygame.display.update()
                
#CODE DE LA PAGE PRINCIPALE
    elif i==1:
    
        while i==1:
        #Initialisation de la fenêtre
            pygame.init()
            
            pygame.mixer.music.stop()
        #Spécificités de la fenêtre (résolution, lancement de la fenêtre, longueur, largeur)
            res = (1600,900)

            screen = pygame.display.set_mode(res)
  
            width = screen.get_width()

            height = screen.get_height()
            
            
            while True and i==1:
        
                mouse = pygame.mouse.get_pos()
                
                for ev in pygame.event.get(): #Analyse les évènements que provoque l'utilisateur
          
                     if ev.type == pygame.QUIT: #Teste si l'utilisateur a effacé la page
                            pygame.quit()
            
                     if ev.type == pygame.MOUSEBUTTONDOWN: #Teste si l'utilisateur a cliqué avec la souris
                        
                        #CODE DES BOUTONS DE LA PAGE
                         #Code du bouton de retour au menu
                            if width/2-780 <= mouse[0] <= width/2-730 and height/2-425 <= mouse[1] <= height/2-375:                    
                                i=0
                                
                        #CODE DES BOUTONS AVEC SONS    
                            elif 550 <= mouse[0] <= 625 and 200 <= mouse[1] <= 275:
                                Snare=mixer.Sound(Dico_Son['1'])
                                Snare.play()
                                if record==True:
                                    Liste_Son.append(Snare)
                                
                            elif 550 <= mouse[0] <= 625 and 320 <= mouse[1] <= 395: 
                                Hihat_Open=mixer.Sound(Dico_Son['2'])
                                Hihat_Open.play()
                                if record==True:
                                    Liste_Son.append(Hihat_Open)
                                
                            elif 550 <= mouse[0] <= 625 and 440 <= mouse[1] <= 515:
                                Hihat_Closed=mixer.Sound(Dico_Son['3'])
                                Hihat_Closed.play()
                                if record==True:
                                    Liste_Son.append(Hihat_Closed)
                                    
                            elif 550 <= mouse[0] <= 625 and 560 <= mouse[1] <= 635:
                                Kick=mixer.Sound(Dico_Son['4'])
                                Kick.play()
                                if record==True:
                                    Liste_Son.append(Kick)
                                    
                            elif 670 <= mouse[0] <= 745 and 200 <= mouse[1] <= 275:
                                Hihat_Pedal=mixer.Sound(Dico_Son['5'])
                                Hihat_Pedal.play()
                                if record==True:
                                    Liste_Son.append(Hihat_Pedal)
                                    
                            elif 670 <= mouse[0] <= 745 and 320 <= mouse[1] <= 395:  
                                Mid_Tom=mixer.Sound(Dico_Son['6'])
                                Mid_Tom.play()
                                if record==True:
                                    Liste_Son.append(Mid_Tom)
                                    
                            elif 670 <= mouse[0] <= 745 and 440 <= mouse[1] <= 515:
                                Shake=mixer.Sound(Dico_Son['7'])
                                Shake.play()
                                if record==True:
                                    Liste_Son.append(Shake)
                                    
                            elif 670 <= mouse[0] <= 745 and 560 <= mouse[1] <= 635:
                                Slap=mixer.Sound(Dico_Son['8'])
                                Slap.play()
                                if record==True:
                                    Liste_Son.append(Slap)
                                    
                            elif 790 <= mouse[0] <= 865 and 200 <= mouse[1] <= 275:
                                Clap=mixer.Sound(Dico_Son['9'])
                                Clap.play()
                                if record==True:
                                    Liste_Son.append(Clap)
                                    
                            elif 790 <= mouse[0] <= 865 and 320 <= mouse[1] <= 395:
                                Triangle=mixer.Sound(Dico_Son['10'])
                                Triangle.play()
                                if record==True:
                                    Liste_Son.append(Triangle)
                                    
                            elif 790 <= mouse[0] <= 865 and 440 <= mouse[1] <= 515:
                                Cymbale=mixer.Sound(Dico_Son['11'])
                                Cymbale.play()
                                if record==True:
                                    Liste_Son.append(Cymbale)
                                    
                            elif 790 <= mouse[0] <= 865 and 560 <= mouse[1] <= 635:
                                Drum=mixer.Sound(Dico_Son['12'])
                                Drum.play()
                                if record==True:
                                    Liste_Son.append(Drum)
                                    
                            elif 910 <= mouse[0] <= 985 and 200 <= mouse[1] <= 275:
                                Light_Drum=mixer.Sound(Dico_Son['13'])
                                Light_Drum.play()
                                if record==True:
                                    Liste_Son.append(Light_Drum)
                                    
                            elif 910 <= mouse[0] <= 985 and 320 <= mouse[1] <= 395:
                                Drum2=mixer.Sound(Dico_Son['14'])
                                Drum2.play()
                                if record==True:
                                    Liste_Son.append(Drum2)
                                    
                            elif 910 <= mouse[0] <= 985 and 440 <= mouse[1] <= 515:
                                Drum3=mixer.Sound(Dico_Son['15'])
                                Drum3.play()
                                if record==True:
                                    Liste_Son.append(Drum3)
                                    
                            elif 910 <= mouse[0] <= 985 and 560 <= mouse[1] <= 635:
                                Clap2=mixer.Sound(Dico_Son['16'])
                                Clap2.play()
                                if record==True:
                                    Liste_Son.append(Clap2)
                                    
                        #Cercle noir et blanc    
                            elif width/2-50 <= mouse[0] <= width/2+50 and height/2+200 <= mouse[1] <= height/2+300:
                                Blank=mixer.Sound(Dico_Son['17'])
                                Blank.play()
                                if record==True:
                                    Liste_Son.append(Blank)
                        
                         #Code du bouton Play
                            elif width/2+480 <= mouse[0] <= width/2+520 and height/2-100 <= mouse[1] <= height/2-60:
                                play=int(input("Combien de fois la musique doit-elle être jouée ?"))
                                for boucle in range (boucle_assert(play)):
                                    for indice in Liste_Son:
                                        indice=mixer.Sound(indice)
                                        indice.play()
                                        time.sleep(tempo)
                                        boucle+=1
                                        
                        #Code du bouton pause
                            elif width/2+480 <= mouse[0] <= width/2+520 and height/2-30 <= mouse[1] <= height/2+50:
                                if record == True:
                                    record=False
                                    print("Fin de l'enregistrement")
                                    
                        #Code du bouton enregistrement
                            elif width/2+470 <= mouse[0] <= width/2+530 and height/2+70 <= mouse[1] <= height/2+130:
                                if record == False:
                                    record=True
                                    print("Enregistrement en cours ...")
                                
                        #Code du bouton pour modifier l'enregistrement
                            elif width/2+470 <= mouse[0] <= width/2+530 and height/2+170 <= mouse[1] <= height/2+210:
                                a=int(input("Voulez-vous : ""\n 1 : Supprimer un son \n"
                                                            "\n 2 : Modifier un son \n"
                                                            "\n 3 : Tout supprimer \n"))

                                if choix(a)==1 : #Suppression d'un son
                                    b=int(input("Entrez le classement du son que vous voulez supprimer"))
                                    del Liste_Son[choix_2(b)]
                                    print("Le son a bien été supprimé")
        
                                elif choix(a)==2: #Remplacement d'un son
                                    b=int(input("Entrez le classement du son que vous voulez modifier"))
                                    choix_2(b)
                                    c=int(input("Entrez le numéro du son qui va le remplacer"))
                                    Liste_Son[choix_2(b)]=Dico_Son[str(choix_3(c))]
                                    print("Le son a bien été remplacé")
        
                                elif choix(a)==3 : #Effacement de tout l'enregistrement
                                    Liste_Son.clear()
                                    print("Plus rien n'est enregistré")
                            
                        #Code du bouton tempo
                            elif width/2+480 <= mouse[0] <= width/2+520 and height/2-180 <= mouse[1] <= height/2-120:
                                tempo=float(input("Choisissez le tempo de votre musique (durée entre chaque son)"))
                                tempo=tempo_assert(tempo)
                                
            #Couleur en arrière plan de la fenêtre                       
                screen.fill((60,25,60))
            #Dessin des carrés colorés
            # 1ère colonne
                pygame.draw.rect(screen, white, ((550,200), (75,75)))
                pygame.draw.rect(screen, light_red, ((550,320),(75,75)))
                pygame.draw.rect(screen, light_blue, ((550,440), (75,75)))
                pygame.draw.rect(screen, black, ((550,560), (75,75)))
            # 2ème colonne
                pygame.draw.rect(screen, yellow, ((670,200), (75,75)))
                pygame.draw.rect(screen, orange, ((670,320), (75,75)))
                pygame.draw.rect(screen, turquoise_blue, ((670,440), (75,75)))
                pygame.draw.rect(screen, light_grey, ((670, 560), (75,75)))
            # 3ème colonne
                pygame.draw.rect(screen, light_green, ((790, 200), (75,75)))
                pygame.draw.rect(screen, pink, ((790,320), (75,75)))
                pygame.draw.rect(screen, regular_blue, ((790,440), (75,75)))
                pygame.draw.rect(screen, grey, ((790,560), (75,75)))
            # 4ème colonne
                pygame.draw.rect(screen, green, ((910,200), (75,75)))
                pygame.draw.rect(screen, violet, ((910,320), (75,75)))
                pygame.draw.rect(screen, dark_blue, ((910,440), (75,75)))
                pygame.draw.rect(screen, red, ((910,560), (75,75)))
            #Dessin du bouton pour quitter la page
                pygame.draw.polygon(screen, white,[(width/2-780,height/2-400),(width/2-730,height/2-425),(width/2-730,height/2-375)])
            #Dessin du bouton pour enregistrer
                pygame.draw.circle(screen, red,[width/2+500,height/2+100],30)
            #Dessin du bouton pour mettre en pause
                pause_font = pygame.font.SysFont('bahnschrift',70)
                Button_Pause = pause_font.render('II',True,white)
                screen.blit(Button_Pause,(width/2+480, height/2-30))
            #Dessin du bouton pour jouer la musique enregistrée
                pygame.draw.polygon(screen, white, [(width/2+480,height/2-80),(width/2+520,height/2-60),(width/2+520,height/2-100)])
            #Dessin du bouton pour le son blanc
                pygame.draw.circle(screen, black,[width/2-30,height/2+275],50)
                pygame.draw.circle(screen, white,[width/2-30,height/2+275],35)
            #Dessin du bouton pour les modifications
                pygame.draw.lines(screen, white, True, [(width/2+470,height/2+170),(width/2+530,height/2+170)],8)
                pygame.draw.lines(screen, white, True, [(width/2+470,height/2+190),(width/2+530,height/2+190)],8)
                pygame.draw.lines(screen, white, True, [(width/2+470,height/2+210),(width/2+530,height/2+210)],8)
            #Bouton Tempo
                Button_Tempo = pause_font.render('T', True, white)
                screen.blit(Button_Tempo,(width/2+480, height/2-200))
            
            #Affiche les éléments dessinés sur la fenêtre
                pygame.display.update()

#PAGE DU TUTORIEL
    elif i==2:

        while i==2:
            pygame.init() #Initialisation du module pygame
            
            res = (1720,800) #Résolution de la fenêtre

            screen = pygame.display.set_mode(res) #Initialisation de la fenêtre et son attribution à une variable
  
            color = (255,255,255) #Couleur en arrière plan
  
            width = screen.get_width() #Attribue la largeur de la fenêtre à width

            height = screen.get_height() #Attribue la hauteur de la fenêtre à height
    
        #Attribution des polices d'écritures à des variables
            titlefont = pygame.font.SysFont('bahnschrift',35)
            smallfont = pygame.font.SysFont('bahnschrift',20)
            
        #Attribution des textes sur des variables
            Titre = titlefont.render('TUTORIEL' , True , color)
            
            Tuto_Part_1 = smallfont.render('JOUER DE LA MUSIQUE : Appuyer sur les carrés colorés pour jouer différentes percussions' , True , color)
            Tuto_Part_2 = smallfont.render("ENREGISTRER DE LA MUSIQUE : Appuyer sur le cercle rouge afin d'enregistrer les différents sons que vous jouez ; Appuyer sur II pour mettre en pause l'enregistrement" , True , color)
            Tuto_Part_3 = smallfont.render("AJOUTER UN SON BLANC : Appuyer sur le cercle noir et blanc afin de jouer un son blanc d'une durée de 0.2 secondes" , True , color)
            Tuto_Part_4 = smallfont.render('AJUSTER LE TEMPO DE VOTRE MUSIQUE : Appuyer sur T et choisissez la durée entre chaque son joué (de préférence entre 0.1 et 1 secondes).La manipulation est à faire sur la console... ' , True , color)
            Tuto_Part_5 = smallfont.render("JOUER VOTRE MUSIQUE ENREGISTREE : Appuyer sur le petit triangle afin d'écouter votre création" , True , color)
            Tuto_Part_6 = smallfont.render("MODIFIER VOTRE MUSIQUE ENREGISTREE : Appuyer sur les 3 traits et choisissez l'option de votre choix (Les manipulations sont à faire sur la console):" , True , color)
            Tuto_Part_6a = smallfont.render('- Supprimer un son en entrant le numéro de sa position' , True , color)
            Tuto_Part_6b = smallfont.render('- Modifier un son en entrant le numéro de sa position puis en jouant le son qui va le remplacer' , True , color)
    
            while True and i==2:
        
                mouse = pygame.mouse.get_pos() #Affectation des coordonnées de la souris à un tuple
                
                for ev in pygame.event.get(): #Analyse les évènements provoqués par l'utilisateur
          
                     if ev.type == pygame.QUIT: #Teste si l'utilisateur a effacé la fenêtre
                            pygame.quit()
            
                     elif ev.type == pygame.MOUSEBUTTONDOWN: #Teste si l'utilisateur a cliqué avec la souris
                          
                          #Code du bouton de retour au menu
                            if width/2-850 <= mouse[0] <= width/2-800 and height/2-375 <= mouse[1] <= height/2-325:                    
                                i=0
                            #Code du bouton vers la suite du tutoriel
                            elif width/2+800 <= mouse[0] <= width/2+850 and height/2-375 <= mouse[1] <= height/2-325:
                                i=2.5
                                
                screen.fill((60,25,60)) #Couleur d'arrière-plan de la fenêtre
                
                #Affiche les textes sur la fenêtre
                screen.blit(Titre, (width/2-90,height/2-400))
                screen.blit(Tuto_Part_1,(width/2-800,height/2-300))
                screen.blit(Tuto_Part_2,(width/2-800,height/2-200))
                screen.blit(Tuto_Part_3,(width/2-800,height/2-100))
                screen.blit(Tuto_Part_4,(width/2-800,height/2))
                screen.blit(Tuto_Part_5,(width/2-800,height/2+100))
                screen.blit(Tuto_Part_6,(width/2-800,height/2+200))
                screen.blit(Tuto_Part_6a,(width/2-800,height/2+250))
                screen.blit(Tuto_Part_6b,(width/2-800,height/2+300))
                 
                #Dessin du bouton de retour au menu
                pygame.draw.polygon(screen, (255,255,255),[(width/2-850,height/2-350),(width/2-800,height/2-375),(width/2-800,height/2-325)])
                #Dessin du bouton vers la suite du tutoriel
                pygame.draw.polygon(screen, (255,255,255),[(width/2+850,height/2-350),(width/2+800,height/2-375),(width/2+800,height/2-325)])
        
                pygame.display.update() #Affiche les éléments dessinés sur la fenêtre 
    
    #CODE DE LA SUITE DU TUTORIEL
    elif i==2.5:
        
        while i==2.5:
        
            pygame.init() #Initialisation du module pygame
            
            res = (1720,800) #Résolution de la fenêtre

            screen = pygame.display.set_mode(res) #Initialisation de la fenêtre et son attribution à une variable
  
            color = (255,255,255) #Couleur en arrière plan
  
            width = screen.get_width() #Attribue la largeur de la fenêtre à width

            height = screen.get_height() #Attribue la hauteur de la fenêtre à height
            
            #Attribution de chaînes de caractères à des variables
            Titre = titlefont.render('LES SONS' , True , color)
            Description = smallfont.render('Ici vous pouvez trouver tous les boutons du drumpad, afin de voir quel son est associé à chaque bouton :' , True , color)
            white_square = smallfont.render(": 1) Son de caisse claire" , True , color)
            light_red_square = smallfont.render(": 2) Son de cymbale (électrique)" , True , color)
            light_blue_square = smallfont.render(': 3) Son de cymbale (électrique) 2' , True , color)
            black_square = smallfont.render(": 4) Son de percussion électrique (grave)" , True , color)
            yellow_square = smallfont.render(": 5) Son de percussion électrique (aiguë)" , True , color)
            orange_square = smallfont.render(': 6) Son de percussion électrique (aiguë) 2' , True , color)
            turquoise_blue_square = smallfont.render(': 7) Son de maracas' , True , color)
            light_grey_square = smallfont.render(': 8) Son de clapement de mains' , True , color)
            light_green_square = smallfont.render(': 9) Son de clapement de mains 2' , True , color)
            pink_square = smallfont.render(': 10) Son de triangle' , True , color)
            regular_blue_square = smallfont.render(': 11) Son de cymbale' , True , color)
            grey_square = smallfont.render(': 12) Son de precussion électrique (grave) 2' , True , color)
            green_square = smallfont.render(': 13) Son de tambour' , True , color)
            violet_square = smallfont.render(': 14) Son de tambour 2' , True , color)
            dark_blue_square = smallfont.render(': 15) Son de tambour 3' , True , color)
            red_square = smallfont.render(': 16) Son de clapement de mains (grave)' , True , color)
            
        
    # 1ère colonne
            white = pygame.Color(255, 255, 255)
            light_red = pygame.Color(255, 130, 130)
            light_blue = pygame.Color (180, 255, 255)
            black = pygame.Color(0, 0, 0) 
    # 2ème colonne
            yellow = pygame.Color(255, 255, 100)
            orange = pygame.Color(255, 128, 0)
            turquoise_blue = pygame.Color(64, 224, 208)
            light_grey = pygame.Color (200, 200, 200)
    # 3ème colonne
            light_green = pygame.Color (115, 255, 115)
            pink = pygame.Color(212, 115, 212)
            regular_blue = pygame.Color (90, 190, 255)
            grey = pygame.Color(130, 130, 130)
    # 4ème colonne
            green = pygame.Color(0, 255, 0)
            violet = pygame.Color (150, 75, 255)
            dark_blue = pygame.Color(50, 50, 255)
            red = pygame.Color(255, 50, 50)
            
            while True and i==2.5:
                
                mouse = pygame.mouse.get_pos() #Collecte les coordonnées de la souris dans un tuple
                
                for ev in pygame.event.get(): #Analyse les évènements provoqués par l'utilisateur
          
                     if ev.type == pygame.QUIT: #Teste si l'utilisateur a effacé la page
                            pygame.quit()
                        
                     elif ev.type == pygame.MOUSEBUTTONDOWN: #Teste si l'utilisateur a cliqué sur sa souris
                         
                         #Code des boutons avec son
                         if 120 <= mouse[0] <= 160 and 175 <= mouse[1] <= 215:
                            Snare=mixer.Sound(Dico_Son['1'])
                            Snare.play()
                            
                         elif 120 <= mouse[0] <= 160 and 275 <= mouse[1] <= 315: 
                                Hihat_Open=mixer.Sound(Dico_Son['2'])
                                Hihat_Open.play()
                                
                         elif 120 <= mouse[0] <= 160 and 375 <= mouse[1] <= 415:
                                Hihat_Closed=mixer.Sound(Dico_Son['3'])
                                Hihat_Closed.play()
                                
                         elif 120 <= mouse[0] <= 160 and 475 <= mouse[1] <= 515:
                                Kick=mixer.Sound(Dico_Son['4'])
                                Kick.play()
                                
                         elif 120 <= mouse[0] <= 160 and 575 <= mouse[1] <= 615:
                                Hihat_Pedal=mixer.Sound(Dico_Son['5'])
                                Hihat_Pedal.play()
                                
                         elif 120 <= mouse[0] <= 160 and 675 <= mouse[1] <= 715:  
                                Mid_Tom=mixer.Sound(Dico_Son['6'])
                                Mid_Tom.play()
                                
                         elif 560 <= mouse[0] <= 600 and 175 <= mouse[1] <= 215:
                                Shake=mixer.Sound(Dico_Son['7'])
                                Shake.play()
                                
                         elif 560 <= mouse[0] <= 600 and 275 <= mouse[1] <= 315:
                                Slap=mixer.Sound(Dico_Son['8'])
                                Slap.play()
                                    
                         elif 560 <= mouse[0] <= 600 and 375 <= mouse[1] <= 415:
                                Clap=mixer.Sound(Dico_Son['9'])
                                Clap.play()
                                    
                         elif 560 <= mouse[0] <= 600 and 475 <= mouse[1] <= 515:
                                Triangle=mixer.Sound(Dico_Son['10'])
                                Triangle.play()
                                
                         elif 560 <= mouse[0] <= 600 and 575 <= mouse[1] <= 615:
                                Cymbale=mixer.Sound(Dico_Son['11'])
                                Cymbale.play()
                                
                         elif 560 <= mouse[0] <= 600 and 675 <= mouse[1] <= 715:
                                Drum=mixer.Sound(Dico_Son['12'])
                                Drum.play()
                                
                         elif 1000 <= mouse[0] <= 1040 and 175 <= mouse[1] <= 215:
                                Light_Drum=mixer.Sound(Dico_Son['13'])
                                Light_Drum.play()
                                  
                         elif 1000 <= mouse[0] <= 1040 and 275 <= mouse[1] <= 315:
                                Drum2=mixer.Sound(Dico_Son['14'])
                                Drum2.play()
                                   
                         elif 1000 <= mouse[0] <= 1040 and 375 <= mouse[1] <= 415:
                                Drum3=mixer.Sound(Dico_Son['15'])
                                Drum3.play()
                                    
                         elif 1000 <= mouse[0] <= 1040 and 475 <= mouse[1] <= 515:
                                Clap2=mixer.Sound(Dico_Son['16'])
                                Clap2.play()
                            
                         #Code du bouton de retour en arrière   
                         elif width/2-850 <= mouse[0] <= width/2-800 and height/2-375 <= mouse[1] <= height/2-325:                    
                                i=2
                
                screen.fill((60,25,60)) #Couleur d'arrière-plan de la fenêtre
            #Affichage des différents textes
                screen.blit(Titre, (width/2-110,height/2-400))
                screen.blit(Description,(width/2-800,height/2-300))
                screen.blit(white_square,(width/2-685,height/2-215))
                screen.blit(light_red_square,(width/2-685,height/2-115))
                screen.blit(light_blue_square,(width/2-685,height/2-15))
                screen.blit(black_square,(width/2-685,height/2+85))
                screen.blit(yellow_square,(width/2-685,height/2+185))
                screen.blit(orange_square,(width/2-685,height/2+285))
                screen.blit(turquoise_blue_square,(width/2-240,height/2-215))
                screen.blit(light_grey_square,(width/2-240,height/2-115))
                screen.blit(light_green_square,(width/2-240,height/2-15))
                screen.blit(pink_square,(width/2-240,height/2+85))
                screen.blit(regular_blue_square,(width/2-240,height/2+185))
                screen.blit(grey_square,(width/2-240,height/2+285))
                screen.blit(green_square,(width/2+200,height/2-215))
                screen.blit(violet_square,(width/2+200,height/2-115))
                screen.blit(dark_blue_square,(width/2+200,height/2-15))
                screen.blit(red_square,(width/2+200,height/2+85))
                
            # 1ère colonne de carrés
                pygame.draw.rect(screen, white, ((120,175), (40,40)))
                pygame.draw.rect(screen, light_red, ((120,275),(40,40)))
                pygame.draw.rect(screen, light_blue, ((120,375), (40,40)))
                pygame.draw.rect(screen, black, ((120,475), (40,40)))
                pygame.draw.rect(screen, yellow, ((120,575), (40,40)))
                pygame.draw.rect(screen, orange, ((120,675), (40,40)))
            # 2ème colonne
                pygame.draw.rect(screen, turquoise_blue, ((560,175), (40,40)))
                pygame.draw.rect(screen, light_grey, ((560, 275), (40,40)))
                pygame.draw.rect(screen, light_green, ((560, 375), (40,40)))
                pygame.draw.rect(screen, pink, ((560,475), (40,40)))
                pygame.draw.rect(screen, regular_blue, ((560,575), (40,40)))
                pygame.draw.rect(screen, grey, ((560,675), (40,40)))
            # 3ème colonne
                pygame.draw.rect(screen, green, ((1000,175), (40,40)))
                pygame.draw.rect(screen, violet, ((1000,275), (40,40)))
                pygame.draw.rect(screen, dark_blue, ((1000,375), (40,40)))
                pygame.draw.rect(screen, red, ((1000,475), (40,40)))
            #Dessin de la flèche de retour en arrière
                pygame.draw.polygon(screen, (255,255,255),[(width/2-850,height/2-350),(width/2-800,height/2-375),(width/2-800,height/2-325)])
                
                pygame.display.update() #Affiche les éléments dessinés sur la fenêtre