import pygame
import random
import sys
import os

# Initialisierung von Pygame
pygame.init()

# Festlegen der Fenstergröße
screen_width = 500
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))

# Laden des Autobildes
player_img = pygame.image.load("blue-car.png")
player_width = 150
player_height = 300
player_img = pygame.transform.scale(player_img, (player_width, player_height))
player_x = (screen_width - player_width) / 2
player_y = screen_height - player_height - 10
player_speed = 4

# Laden des Hindernisbildes
obstacle_imgs = [pygame.image.load("red-car.png"), pygame.image.load("green-car.png"), pygame.image.load("yellow-car.png"), pygame.image.load("orange-car.png"), pygame.image.load("purple-car.png"), pygame.image.load("black-car.png")]
obstacle_img = random.choice(obstacle_imgs)
obstacle_width = 150
obstacle_height = 300
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 1.5

# Laden des Münzenbildes
coin_img = pygame.image.load("coin.png")
coin_width = 80
coin_height = 80
coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
coin_x = random.randint(0, screen_width - coin_width)
coin_y = -coin_height
coin_speed = 5

# Laden des kleinen Münzenbildes
coin_count_img = pygame.image.load("coin-count.png")
coin_count_width = 40
coin_count_height = 40
coin_count_img = pygame.transform.scale(coin_count_img, (coin_count_width, coin_count_height))
coin_count_x = 50
coin_count_y = 20
coin_count_speed = 0

# Geräusche
game_over_sound = pygame.mixer.Sound("game-over-sound.wav")
coin_sound = pygame.mixer.Sound("coin-sound.wav")

# Musik
Geometry_Dash_Clubstep_music = pygame.mixer.Sound("Geometry-Dash-Clubstep.wav")
Geometry_Dash_Cant_Let_Go_music = pygame.mixer.Sound("Geometry-Dash-Cant-Let-Go.wav")
Geometry_Dash_Blast_Processing_music = pygame.mixer.Sound("Geometry-Dash-Blast-Processing.wav")
Geometry_Dash_Beast_Mode_music = pygame.mixer.Sound("Geometry-Dash-Beast-Mode.wav")
Geometry_Dash_Base_After_Base_music = pygame.mixer.Sound("Geometry-Dash-Base-After-Base.wav")
Geometry_Dash_Back_on_Track_music = pygame.mixer.Sound("Geometry-Dash-Back-on-Track.wav")
Geometry_Dash_Airborne_Robots_music = pygame.mixer.Sound("Geometry-Dash-Airborne-Robots.wav")
music = [pygame.mixer.Sound(Geometry_Dash_Clubstep_music), pygame.mixer.Sound(Geometry_Dash_Cant_Let_Go_music), pygame.mixer.Sound(Geometry_Dash_Blast_Processing_music), pygame.mixer.Sound(Geometry_Dash_Beast_Mode_music), pygame.mixer.Sound(Geometry_Dash_Base_After_Base_music), pygame.mixer.Sound(Geometry_Dash_Back_on_Track_music), pygame.mixer.Sound(Geometry_Dash_Airborne_Robots_music)]

# Soundkanäle
game_over_sound_channel1 = pygame.mixer.Channel(0)
coin_sound_channel2 = pygame.mixer.Channel(1)

# Farben
black = (0, 0, 0)
white = (255, 255, 255)
gray = (127,127,127)
red = (255,0,0)
blue = (0,0,100)

# Linieneigenschaften
line_width = 20
line_height = 60
line_x = screen_width / 2 - 10
line_y = 0
line_speed = 10

# Quadrateigenschaften
square_width = screen_width
square_height = 115
square_x = 0
square_y = screen_height / 2 - 60
square_speed = 1

# linke Straßenlinie
l_line_width = line_width
l_line_height = 1000
l_line_x = 11
l_line_y = line_y
l_line_speed = 1

# rechte Straßenlinie
r_line_width = line_width
r_line_height = l_line_height
r_line_x = screen_width - 30
r_line_y = line_y
r_line_speed = l_line_speed

# Münzenzähler
coin_score = 0
font = pygame.font.Font(None, 35)
score = 0
highscore = 0 # initialisieren des Highscores

# Highscore-Definierungen
def update_highscore(score):
    global highscore
    if coin_score > highscore:
        highscore = coin_score

# Neustart-Definierungen
def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Variablen für die Anzeige des endgültigen Spielstands
game_over_font = pygame.font.Font(None, 80)
game_over_text = game_over_font.render("GAME OVER", True, blue)
game_over_rect = game_over_text.get_rect(center=(screen_width/2, screen_height/3))
final_score_font = pygame.font.Font(None, 60)
final_score_text = None
final_score_rect = None
final_coin_score_font = pygame.font.Font(None, 60)
final_coin_score_text = None
final_coin_score_rect = None

# Festlegen der Pausen-Taste
pause_key = pygame.K_SPACE
paused = False
pause_value = 1

# Menü Schleife
menu_running = True
while menu_running:

    # Ereignisschleife
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Wenn der Benutzer auf den Play-Button klickt, starte das Spiel
            mouse_pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                menu_running = False
            # Wenn der Benutzer auf den Quit-Button klickt, verlasse das Spiel
            elif quit_button_rect.collidepoint(mouse_pos):
                pygame.quit()
        elif event.type == pygame.KEYDOWN:
            menu_running = False
            
    # Hintergrund zeichnen
    screen.fill(blue)

    # Text "Autorennen" zeichnen
    title_font = pygame.font.Font(None, 80)
    title_text = title_font.render("StreetRacing", True, white)
    title_rect = title_text.get_rect(center=(screen_width/2, screen_height/3))
    screen.blit(title_text, title_rect)
    
    # Hersteller anzeigen
    by_text_font = pygame.font.Font(None, 40)
    by_text_text = by_text_font.render("by b1gm0", True, white)
    by_text_height = 380
    by_text_rect = by_text_text.get_rect(center=(screen_width/2, by_text_height))
    screen.blit(by_text_text, by_text_rect)
    
    # Betreiber anzeigen
    power_text_font = pygame.font.Font(None, 30)
    power_text_text = power_text_font.render("powered by Pygame", True, white)
    power_text_height = screen_height - 100
    power_text_rect = power_text_text.get_rect(center=(screen_width/2, power_text_height))
    screen.blit(power_text_text, power_text_rect)
    
    # Play-Button zeichnen
    play_button_text = font.render("PLAY", True, black)
    play_button_rect = play_button_text.get_rect(center=(screen_width/2, screen_height/2))
    play_button_rect.inflate_ip(140, 60) # Vergrößern des Schaltflächenrechtecks
    pygame.draw.rect(screen, white, play_button_rect, border_radius=90)
    pygame.draw.rect(screen, black, play_button_rect, border_radius=90, width=5)

    play_button_text = pygame.font.Font(None, 50).render("PLAY", True, black) # Vergrößern der Schriftgröße
    play_button_text_rect = play_button_text.get_rect(center=(play_button_rect.centerx, play_button_rect.centery)) # Center the text within the button
    screen.blit(play_button_text, play_button_text_rect)
    
    # Quit-Button zeichnen
    quit_button_text = font.render("QUIT", True, black)
    quit_button_rect = quit_button_text.get_rect(center=(screen_width/2, 600))
    quit_button_rect.inflate_ip(140, 60) # Vergrößern des Schaltflächenrechtecks
    pygame.draw.rect(screen, white, quit_button_rect, border_radius=90)
    pygame.draw.rect(screen, black, quit_button_rect, border_radius=90, width=5)

    quit_button_text = pygame.font.Font(None, 50).render("QUIT", True, black) # Vergrößern der Schriftgröße
    quit_button_text_rect = quit_button_text.get_rect(center=(quit_button_rect.centerx, quit_button_rect.centery)) # Center the text within the button
    screen.blit(quit_button_text, quit_button_text_rect)
    
    # Hilfsanweißung
    help1_text_font = pygame.font.Font(None, 20)
    help1_text_text = help1_text_font.render("Press any key to start", True, white)
    help1_text_height = 20
    help1_text_rect = help1_text_text.get_rect(center=(screen_width/2, help1_text_height))
    screen.blit(help1_text_text, help1_text_rect)
    
    # Versionsanzeige
    version_text_font = pygame.font.Font(None, 20)
    version_text_text = version_text_font.render("v.1", True, white)
    version_text_height = screen_height - 20
    version_text_width = screen_width - 25
    version_text_rect = version_text_text.get_rect(center=(version_text_width, version_text_height))
    screen.blit(version_text_text, version_text_rect)

    # Bildschirm aktualisieren
    pygame.display.flip()

# Hintergrundmusik auswählen und abspielen
random_music = random.choice(music)
random_music.set_volume(0.4)
game_over_sound_channel1.play(random_music)

# Highscore-Initialisierung
with open("highscore.txt", "r") as file:
    highscore = int(file.read())

# Hauptspielschleife
running = True
while running:

    # Ereignisschleife
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEMOTION:
            player_x = event.pos[0] - player_width / 2
        elif event.type == pygame.KEYDOWN:
        
            # Musik pausieren
            if event.key == pause_key:
                paused = not paused  # Schaltet den Pause-Status um
                game_over_sound_channel1.pause()
            # Musik leise oder laut stellen
            elif event.key == pygame.K_m:
                if random_music.get_volume() == 0.0:
                    random_music.set_volume(0.4)
                    pause_value = 1
                else:
                    random_music.set_volume(0.0)
                    pause_value = 0
                  
    # Sicherstellen, dass das Auto innerhalb des Fensters bleibt
    if player_x < 0:
        player_x = 0
    elif player_x > screen_width - player_width:
        player_x = screen_width - player_width

                
    # Spiel aktualisieren, wenn es nicht pausiert ist
    if not paused:
    
       # Musik fortsetzen
       game_over_sound_channel1.unpause() 

       # Spielerbewegung
       keys = pygame.key.get_pressed()
       if keys[pygame.K_LEFT] and player_x > 0:
          player_x -= player_speed
       elif keys[pygame.K_a] and player_x > 0:
          player_x -= player_speed
       if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
          player_x += player_speed
       elif keys[pygame.K_d] and player_x < screen_width - player_width:
          player_x += player_speed 

       # Hindernisbewegung
       obstacle_y += obstacle_speed
       if obstacle_y > screen_height:
          obstacle_img = random.choice(obstacle_imgs)
          obstacle_width = 150
          obstacle_height = 300
          obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_width, obstacle_height))
          obstacle_x = random.randint(0, screen_width - obstacle_width)
          obstacle_y = -obstacle_height
          score += 1
          obstacle_speed += 0.1
          coin_speed += 0.1
          line_speed += 0.1
          player_speed += 0.1
        
       # Münzenbewegung
       coin_y += coin_speed
       if coin_y > screen_height:
          coin_x = random.randint(0, screen_width - coin_width)
          coin_y = -coin_height
        
       # Linienbewegung
       line_y += line_speed
       if line_y > screen_height:
          line_x = screen_width / 2 - 10
          line_y = 0
   
       # Hindernis-Kollisionserkennung
       if player_x < obstacle_x + obstacle_width and \
          player_x + player_width > obstacle_x and \
          player_y < obstacle_y + obstacle_height and \
          player_y + player_height > obstacle_y:
              running = False
              game_over_sound.set_volume(0.5)
              pygame.mixer.Sound.stop(random_music)
              game_over_sound_channel1.play(game_over_sound)
   
       # Münzensichtbarkeit
       if coin_y < 100:
          coin_img = pygame.image.load("coin.png")
          coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))

       # Münzen-Kollisionserkennung
       player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
       coin_rect = pygame.Rect(coin_x, coin_y, coin_width, coin_height)
       if player_rect.colliderect(coin_rect):
          coin_sound_channel2.play(coin_sound)
          coin_x = random.randint(0, screen_width - coin_width)
          coin_y = -coin_height
          coin_score += 1
          coin_img = pygame.image.load("coin_transparent.png")
          coin_img = pygame.transform.scale(coin_img, (coin_width, coin_height))
          coin_sound.set_volume(0.4)
          coin_sound_channel2.play(coin_sound)
          update_highscore(coin_score)  # aktualisieren des Highscores
      
       # Hintergrund zeichnen
       screen.fill(gray)
    
       # Linie zeichnen
       pygame.draw.rect(screen, white, (line_x, line_y, line_width, line_height))
 
       # linke Straßenlinie zeichnen
       pygame.draw.rect(screen, white, (l_line_x, l_line_y, l_line_width, l_line_height))

       # rechte Straßenlinie zeichnen
       pygame.draw.rect(screen, white, (r_line_x, r_line_y, r_line_width, r_line_height))
  
       # Münzen zeichnen
       screen.blit(coin_img, (coin_x, coin_y))  
    
       # Hindernis zeichnen
       screen.blit(obstacle_img, (obstacle_x, obstacle_y)) 
    
       # Spieler zeichnen
       screen.blit(player_img, (player_x, player_y))
    
       # kleine Münze zeichnen
       screen.blit(coin_count_img, (coin_count_x, coin_count_y)) 
    
       # Münzenanzeige
       coin_score_text = font.render(str(coin_score), True, white)
       screen.blit(coin_score_text, (95, 32))
       
       # Hilfsanweißungen
       if running == True:
          help2_text_font = help1_text_font
          help2_text_text = help2_text_font.render("Press SPACE to pause", True, white)
          help2_text_height = 20
          help2_text_rect = help2_text_text.get_rect(center=(screen_width/2, help2_text_height))
          screen.blit(help2_text_text, help2_text_rect)
          
       if running == True and pause_value == 1:
          help4_text_font = help1_text_font
          help4_text_text = help2_text_font.render("Press M to mute the music", True, white)
          help4_text_height = 40
          help4_text_rect = help2_text_text.get_rect(center=(screen_width/2 - 14, help4_text_height))
          screen.blit(help4_text_text, help4_text_rect)
          
       if running == True and pause_value == 0:
          help4_text_font = help1_text_font
          help4_text_text = help2_text_font.render("Press M to unmute the music", True, white)
          help4_text_height = 40
          help4_text_rect = help2_text_text.get_rect(center=(screen_width/2 - 21, help4_text_height))
          screen.blit(help4_text_text, help4_text_rect)
          
       # Highscore-Anzeige
       font = pygame.font.SysFont(None, 30)
       text = font.render("HS: " + str(highscore), True, (255, 255, 255))
       screen.blit(text, (54, 70))
      
       # Bildschirm aktualisieren
       pygame.display.update()  

# Highscore-Speicherung
with open("highscore.txt", "w") as file:
   file.write(str(highscore))

# Hilfsanweißung unsichtbar machen

# Anzeigen des endgültigen Münzenstands und des endgültigen Texts
pygame.draw.rect(screen, blue, (square_x, square_y, square_width, square_height))
final_coin_score_text = final_coin_score_font.render("Coins: " + str(coin_score), True, white)
final_coin_score_rect = final_coin_score_text.get_rect(center=(screen_width/2, screen_height/2))
screen.blit(game_over_text, game_over_rect)
screen.blit(final_coin_score_text, final_coin_score_rect)

# Hilfsanweißung
help3_text_font = help1_text_font
help3_text_text = help3_text_font.render("Press SPACE to play again", True, white)
help3_text_height = 20
help3_text_rect = help3_text_text.get_rect(center=(screen_width/2, help3_text_height))
screen.blit(help3_text_text, help3_text_rect)

# Bildschirm aktualisieren
pygame.display.update()
 
# Warten auf Tastendruck zum Beenden des Spiels
waiting = True
while waiting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            waiting = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                waiting = False
                restart_program()

# Pygame beenden
pygame.quit()

