import pygame as py
import pygame.freetype
import time
import os
py.init()

# beeldscherm variabele S
hoogte = 500
breedte = 800
fps = 60
win = py.display.set_mode((breedte, hoogte))
py.display.set_caption("mooi spelletje")
achtergrond_foto = py.image.load(os.path.join('achtergrond_foto.png'))
#algemene game variabele M
game_state = 0
running = True
clock = 0
index = 0
# speler variabele L
speler_x_y = speler_start_plek = [5, 445]
oude_positie = speler_x_y
speler_foto = py.image.load(os.path.join('speler_v1.png'))
# bewegingsvariabele S
activated = False
last_key = py.K_w
nieuwe_speler_positie = speler_x_y
# muren S
wall_dimensions = [
    (breedte, 5), (breedte, 5), (5, hoogte), (5, hoogte), (150, 25), (25, 75)  , (25, 200)         , (50, 25), (225, 25) , (375, 25) , (25, 375)   , (25, 75) , (345, 25), (25, 300)
]
wall_position = [
    (0, 0), (0, hoogte - 5), (0, 0), (breedte - 5, 0)     , (0, 350) , (150, 350), (300, hoogte-150), (250, 350) , (75, 275) , (0, 200) , (375, 200), (375, 0), (55, 75) , (600, 75)
]
# spike M
spike_dimensies = [(10, 50)]
spike_plek = [(375, 300)]
#spike_foto = py.image.load(os.path.join('spike.png'))
spike_frame_1 = py.image.load(os.path.join('spike_frame 1.png'))
spike_frame_2 = py.image.load(os.path.join('spike_frame 2.png'))
spike_frame_1 = py.transform.rotate(spike_frame_1,90)
spike_frame_2 = py.transform.rotate(spike_frame_2,90)
spike_frames = [spike_frame_1, spike_frame_2]
# teleporter S
teleporteer_binnen_dimensies = [(50, 5), (5, 50)    , (5, 50)]
teleporteer_binnen_locatie = [(325, 495), (600, 200), (620, 200)]
teleporteer_buiten_dimensies = [(50, 5), (5, 50)    , (5, 50)]
teleporteer_buiten_locatie = [(325, 0), (620, 200)  , (600, 200)]
# vijanden L
vijanden_locatie = [[400, 5]  , [400, 200]]
vijanden_dimensies = [(50, 50), (50, 50)]
beweeg_richting = ["rechts", "rechts"]
vijanden_foto = py.image.load(os.path.join('geestje_V3.png'))
#coin S
coin = []
coin_aantal = 0
coin_foto = py.image.load(os.path.join('Coin_25px25px.png'))
coin_locatie = [(745, 450)]
coin_dimensies = [(25,25)]
coin_deactivatie = [-1, ]
for i in range(len(coin_locatie)):
    coin.append(py.Rect(coin_locatie[i], coin_dimensies[i]))
# eind zone
eindzone_locatie = (745,0)
eindzone_dimensies = (50,5)

#functie om de animaties te cycelen -M
def cycle_animaties():
    global clock, index, frame

    clock += 1

    if clock % 10 == 0:
        match index:
            case 0:
                frame = spike_frames[index]

                index = 1
            case 1:
                frame = spike_frames[index]

                index = 0
    else:
        frame = spike_frames[index]
    if clock == 60:
        clock = 0
    return frame
#start up_scherm S

def start_up_scherm():
    global tekst_rect, tekst, win
    win.fill((255, 255, 255))

    font = pygame.freetype.Font('PressStart2P-vaV7.ttf', 26)
    font.render_to(win,(20, 200), "druk op spatie om te beginnen ", (255, 0, 255))
    py.display.update()


#eindstand scherm L
def eindstand_scherm():
    win.fill((255,255,255))

    font = pygame.freetype.Font('PressStart2P-vaV7.ttf',26)
    font.render_to(win, (20,200), "Je hebt het gehaald woe hoee", (255, 0, 255))
    py.display.update()

# tekent het scherm S


def draw_scr():
    global muren, speler_rect, spike, teleporteer_binnen, teleporteer_buiten, vijanden, eindzone_rect, spike_foto
    muren = []
    spike = []
    teleporteer_binnen = []
    teleporteer_buiten = []
    vijanden = []
    skip = -1
    #
    spike_cycle_frame = cycle_animaties()
    # maakt de achtergrond S
    win.fill((0, 0, 0))
    win.blit(achtergrond_foto, (0,0))
    # foto van de speler S
    win.blit(speler_foto, (speler_x_y[0], speler_x_y[1]))
    # speler vierkant S
    speler_rect = py.Rect(speler_x_y[0], speler_x_y[1], 50, 50)
    # muren S
    for i in range(len(wall_dimensions)):
        muren.append(py.draw.rect(win, (255, 255, 0), (wall_position[i], wall_dimensions[i])))
    # de spikes S
    for i in range(len(spike_dimensies)):

        win.blit(spike_cycle_frame, (spike_plek[i]))
        #spike.append(py.draw.rect(win, (0, 0, 255), (spike_plek[i], spike_dimensies[i])))
        spike.append(py.Rect((spike_plek[i], spike_dimensies[i])))
    # de teleporteer ingang M
    for i in range(len(teleporteer_binnen_locatie)):
        teleporteer_binnen.append(py.draw.rect(win, (255, 255, 0), (teleporteer_binnen_locatie[i], teleporteer_binnen_dimensies[i])))
    # de teleporteer uitgang M
    for i in range(len(teleporteer_buiten_locatie)):
        teleporteer_buiten.append(py.draw.rect(win, (0, 255, 0), (teleporteer_buiten_locatie[i], teleporteer_buiten_dimensies[i])))
    # de vijanden L
    for i in range(len(vijanden_locatie)):
        vijanden.append(py.Rect(vijanden_locatie[i], vijanden_dimensies[i]))

        #vijanden.append(py.draw.rect(win, (125, 125, 125), (vijanden_locatie[i], vijanden_dimensies[i])))
        win.blit(vijanden_foto, vijanden_locatie[i])
    eindzone_rect = py.draw.rect(win, (125, 255, 75), (eindzone_locatie, eindzone_dimensies))

    # coin S
    for i in range(len(coin_deactivatie)):
        for ii in range(len(coin_locatie)):
            if coin_deactivatie[i] == ii:
                skip = ii
    for i in range(len(coin_locatie)):
        if i == skip:
            break
        win.blit(coin_foto, coin_locatie[i])


    # oude code niet gebruikt S
    # for i in range(len(coin_deactivatie)):
    #
    #     for j in range(len(coin_locatie)):
    #         if coin_deactivatie[i] == j:
    #             match = coin_deactivatie[i]
    #
    #             coin.append(py.Rect(coin_locatie[j], coin_dimensies[j]))
    #
    #
    #             win.blit(coin_foto, coin_locatie[j])

    # py.draw.rect(win, (0, 0, 0), speler_rect)
    # ververst het scherm
    py.display.update()

# functie voor het bewegen van de speler S
def moving(object_pos, object_velocity, direction):
    final_position = [0, 0]
    # kijkt naar welke kant de speler beweegt
    match direction:
        case "up":
            final_position[0] = object_pos[0]
            final_position[1] = object_pos[1] - object_velocity
        case "down":
            final_position[0] = object_pos[0]
            final_position[1] = object_pos[1] + object_velocity
        case "right":
            final_position[1] = object_pos[1]
            final_position[0] = object_pos[0] + object_velocity
        case "left":
            final_position[1] = object_pos[1]
            final_position[0] = object_pos[0] - object_velocity
    return final_position

# functie voor de beweging van de vijand S
def vijand_beweging():
    # zet de speed van de vijanden
    speed = 3
    for i in range(len(vijanden_locatie)):
        # bewaart de oude locatie zodat de vijand terug gezet kan worden als iets raakt
        oude_locatie = vijanden_locatie[i]
        # beslist welke kant de vijand op beweegt
        match beweeg_richting[i]:
            case "rechts":
                vijanden_locatie[i][0] = vijanden_locatie[i][0] + speed
            case "links":
                vijanden_locatie[i][0] = vijanden_locatie[i][0] - speed
        # zet tuple om in list om gegevens te wijzigen
        vijand_locatie = list(vijanden_locatie[i])
        # checkt of vijand een teleporter raakt
        vijanden_locatie[i], telehit = botsing_teleporteren(vijanden[i], teleporteer_binnen, vijand_locatie)
        # checkt of vijand een muur raakt
        muur_raking = botsing_muren(vijanden[i])
        # als de vijand een teleporter raakt en het is teleporter 3(index 2)
        # dan wordt hij de andere kant opgestuurd anders wordt er 5 pixels naar rechts gestuurd om
        # niet terug gestuurd te worden
        if telehit != -1:
            if telehit == 2:
                vijanden_locatie[i] = [vijanden_locatie[i][0] - 55, vijanden_locatie[i][1]]

            vijanden_locatie[i] = [vijanden_locatie[i][0] + 5, vijanden_locatie[i][1]]
        else:
            vijanden_locatie[i] = [vijanden_locatie[i][0], vijanden_locatie[i][1]]
        # als de muur wordt geraakt en je gaat naar rechts ga je naar links met een zetje en andersom
        if muur_raking > -1 and telehit == -1:
            match beweeg_richting[i]:
                case "rechts":
                    vijanden_locatie[i][0] = oude_locatie[0] - speed * 2
                    vijanden_locatie[i][1] = oude_locatie[1]
                    beweeg_richting[i] = "links"

                case "links":
                    vijanden_locatie[i][0] = oude_locatie[0] + speed * 2
                    vijanden_locatie[i][1] = oude_locatie[1]
                    beweeg_richting[i] = "rechts"

# kijkt of object botst met teleporters M
def botsing_teleporteren(object_rect, tele_in, object_x_y):
    tele_hit = object_rect.collidelist(tele_in)
    object_plek = []
    if tele_hit != -1:
        object_plek.append(teleporteer_buiten_locatie[tele_hit][0])
        object_plek.append(teleporteer_buiten_locatie[tele_hit][1])
        print(tele_hit)
    else:
        object_plek = object_x_y
    return object_plek, tele_hit

# checkt of object met muur botst M
def botsing_muren(object_rect):
    wallhit = object_rect.collidelist(muren)
    return wallhit

# checkt of object met vijand botst, komt veel overeen met botsing_spikes L
def botsing_vijand(object_rect, running_import):
    vijand_hit = object_rect.collidelist(vijanden)
    if vijand_hit > -1:
        running = False
    else:
        running = running_import
    return running

# checkt of object met de spike botst komt veel overeen met botsing_vijand S
def botsing_spikes(object_rect, running_import):
    spike_hit = object_rect.collidelist(spike)
    if spike_hit > -1:
        running = False
    else:
        running = running_import
    return running

# checkt of object met een coin botst S
def botsing_coin(object_rect, coin_aantal_import):
    coin_hit = object_rect.collidelist(coin)
    coin_aantal = coin_aantal_import
    if coin_hit != -1 and coin_aantal < 1:
        coin_aantal += 1
        print(coin_aantal)
        return coin_aantal, coin_hit

    return coin_aantal, -1
# botsing met de eind zone L
def botsing_eind_zone(object_rect):
    eindhit = object_rect.colliderect(eindzone_rect)
    if eindhit == True:
        return 1
    else:
        return 0

# de main game functie S
def main():
    # stelt aantal variabele op
    global speler_x_y, moving_direction, oude_positie, activated, game_state, coin_aantal, coin_deactivatie
    running = True
    reden = ""
    last_key = py.K_w
    # speed van de speler
    speed = 5
    # clock zodat het beeldscherm maar 60 keer per seconde ververst
    clock = py.time.Clock()
    begin_tijd = time.time()
    # de main game loop
    match game_state:
        case 0:
            while running:

                start_up_scherm()
                for events in py.event.get():
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"

                    if events.type == py.KEYDOWN:
                        match events.key:
                            case py.K_SPACE:
                                game_state = 1
                                reden = main()
                                running = False
                            case _:
                                pass
        case 1:
            while running:
                clock.tick(fps)
                # als de speler al in beweging is, beweegt hij in dezelfde richting als de vorige zet

                # de event loop als er wat gebeurt in het spel komt het hier terecht
                for events in py.event.get():
                    # als er op het kruisje in het pop-up-window word geklikt dan stopt de game loop
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"
                    # als de speler op een knop duwt en hij is niet aan het bewegen wordt de laatste key gezet
                    if events.type == py.KEYDOWN and activated is False:
                        match events.key:
                            case py.K_w:
                                last_key = events.key
                            case py.K_s:
                                last_key = events.key
                            case py.K_a:
                                last_key = events.key
                            case py.K_d:
                                last_key = events.key
                            case _:
                                break
                        # als de speler een richting op gaat en het is geen muur dan beweegt hij totdat
                        # hij een andere muur raakt
                        if events.key == py.K_w and muur_raak != 0:
                            activated = True
                            moving_direction = "up"
                            nieuwe_speler_positie = moving(speler_x_y, 5, moving_direction, )
                        elif events.key == py.K_s and muur_raak != 1:
                            activated = True
                            moving_direction = "down"
                            nieuwe_speler_positie = moving(speler_x_y, 5, moving_direction, )
                        elif events.key == py.K_a and muur_raak != 2:
                            activated = True
                            moving_direction = "left"
                            nieuwe_speler_positie = moving(speler_x_y, 5, moving_direction, )
                        elif events.key == py.K_d and muur_raak != 3:
                            activated = True
                            moving_direction = "right"
                            nieuwe_speler_positie = moving(speler_x_y, 5, moving_direction, )
                        # hier wordt de oude positie gezet voor mogelijke terugzetting
                        # en de nieuwe locatie wordt op de speler gedrukt
                        oude_positie = speler_x_y
                        speler_x_y = nieuwe_speler_positie
                # executeert een hoop functies voor de speler en omgeving

                draw_scr()
                vijand_beweging()
                speler_x_y, tele_hit = botsing_teleporteren(speler_rect, teleporteer_binnen, speler_x_y)
                running = botsing_spikes(speler_rect, running)
                eind_botsing = botsing_eind_zone(speler_rect)
                nieuwe_coin_aantal, coin_deactivatie_komt = botsing_coin(speler_rect, coin_aantal)
                coin_aantal = nieuwe_coin_aantal
                if coin_deactivatie_komt > -1:
                    coin_deactivatie.append(coin_deactivatie_komt)
                muur_raak = botsing_muren(speler_rect)
                running = botsing_vijand(speler_rect, running)
                # voor het terug zetten van de speler als het tegen een muur dondert
                for i in range(len(muren)):
                    if muur_raak == i and tele_hit == -1:
                        speler_x_y = oude_positie
                        activated = False
                #
                if eind_botsing == 1:
                    game_state = 2
                    activated = False
                    reden = main()
                    running = False


                if activated is True:
                    match last_key:
                        case py.K_w:
                            moving_direction = "up"
                            nieuwe_speler_positie = moving(speler_x_y, speed, moving_direction, )
                            oude_positie = speler_x_y
                            speler_x_y = nieuwe_speler_positie
                        case py.K_s:
                            moving_direction = "down"
                            nieuwe_speler_positie = moving(speler_x_y, speed, moving_direction, )
                            oude_positie = speler_x_y
                            speler_x_y = nieuwe_speler_positie
                        case py.K_a:
                            moving_direction = "left"
                            nieuwe_speler_positie = moving(speler_x_y, speed, moving_direction, )
                            oude_positie = speler_x_y
                            speler_x_y = nieuwe_speler_positie
                        case py.K_d:
                            moving_direction = "right"
                            nieuwe_speler_positie = moving(speler_x_y, speed, moving_direction, )
                            oude_positie = speler_x_y
                            speler_x_y = nieuwe_speler_positie
            eind_tijd = time.time()
            tijd_duratie = eind_tijd - begin_tijd
            tijd_duratie = round(tijd_duratie, 2)
            print(str(tijd_duratie) + " seconde")
        case 2:
            while running:
                eindstand_scherm()
                for events in py.event.get():
                    if events.type == py.QUIT:
                        running = False
                        print("gestopt")

                        return "gestopt"

    if reden == "gestopt":
        return "gestopt"


    return "dood"
# zorgt ervoor dat de goede main word uitgevoerd hier kwam max achter M
if __name__ == "__main__":
    reden = main()
# zorgt ervoor dat als je niet dood bent dat je opnieuw kan proberen L
while reden != "gestopt":
    if reden == "dood":
        game_state = 0
        activated = False
        speler_x_y = speler_start_plek
        reden = main()
