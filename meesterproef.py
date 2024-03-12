# libraries

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
achtergrond_foto_level_2 = py.image.load(os.path.join('achtergrond_level_2.png'))

# algemene game variabele M

game_state = 0
import_game_state = 1
running = True
clock = 0
clock_v2 = 0
index = 0
index_v2 = 0

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
    (breedte, 5), (breedte, 5), (5, hoogte), (5, hoogte), (150, 25), (25, 75), (25, 200), (50, 25), (225, 25),
    (375, 25), (25, 375), (25, 75), (345, 25), (25, 300)
]
wall_position = [
    (0, 0), (0, hoogte - 5), (0, 0), (breedte - 5, 0), (0, 350), (150, 350), (300, hoogte - 150), (250, 350), (75, 275),
    (0, 200), (375, 200), (375, 0), (55, 75), (600, 75)
]
wall_dimensions_level_2 = [
    (breedte, 5), (breedte, 5), (5, hoogte), (5, hoogte), (75, 25), (25, 50), (320, 25), (25, 200), (50, 25), (50, 25),
    (25, 50), (25, 50), (25, 50), (50, 25), (25, 50), (25, 50), (50, 25), (25, 70), (25, 125), (320, 25), (25, 175),
    (75, 25)
]
wall_position_level_2 = [
    (0, 0), (0, hoogte - 5), (0, 0), (breedte - 5, 0), (5, 105), (55, 55), (55, 55), (350, 80), (180, 205), (300, 430),
    (155, 305), (155, 445), (645, 445), (450, 355), (425, 230), (500, 180), (670, 160), (730, 280), (425, 55),
    (425, 55), (720, 55), (720, 205)
]

# spike
# spike level 1

spike_dimensies = [(10, 50)]
spike_plek = [(375, 300)]
# spike_foto = py.image.load(os.path.join('spike.png'))
spike_frame_1 = spike_frame_1_level_2 = py.image.load(os.path.join('spike_frame 1.png'))
spike_frame_2 = spike_frame_2_level_2 = py.image.load(os.path.join('spike_frame 2.png'))
spike_frame_1 = py.transform.rotate(spike_frame_1, 90)
spike_frame_2 = py.transform.rotate(spike_frame_2, 90)
spike_frames = [spike_frame_1, spike_frame_2]

# spikes level 2

spike_dimensies_level_2 = [(5, 50), (5, 50), (5, 50)]
spike_plek_level_2 = [(0, 445), (445, 230), (720, 80)]
# level 2 spike 1
spike_frame_1_level_2_spike_1 = spike_frame_1
spike_frame_2_level_2_spike_1 = spike_frame_2
spike_frame_1_level_2_spike_1 = py.transform.rotate(spike_frame_1_level_2_spike_1, 180)
spike_frame_2_level_2_spike_1 = py.transform.rotate(spike_frame_2_level_2_spike_1, 180)
spike_frames_level_2_spike_1 = [spike_frame_1_level_2_spike_1, spike_frame_2_level_2_spike_1]
# level 2 spike 2
spike_frame_1_level_2_spike_2 = spike_frame_1
spike_frame_2_level_2_spike_2 = spike_frame_2
spike_frame_1_level_2_spike_2 = py.transform.rotate(spike_frame_1_level_2_spike_2, 180)
spike_frame_2_level_2_spike_2 = py.transform.rotate(spike_frame_2_level_2_spike_2, 180)
spike_frames_level_2_spike_2 = [spike_frame_1_level_2_spike_2, spike_frame_2_level_2_spike_2]
# level 2 spike 3
spike_frame_1_level_2_spike_3 = spike_frame_1
spike_frame_2_level_2_spike_3 = spike_frame_2
spike_frame_1_level_2_spike_3 = py.transform.rotate(spike_frame_1_level_2_spike_3, 180)
spike_frame_2_level_2_spike_3 = py.transform.rotate(spike_frame_2_level_2_spike_3, 180)
spike_frame_1_level_2_spike_3 = py.transform.flip(spike_frame_1_level_2_spike_3, flip_x=True, flip_y=False)
spike_frame_2_level_2_spike_3 = py.transform.flip(spike_frame_2_level_2_spike_3, flip_x=True, flip_y=False)
spike_frames_level_2_spike_3 = [spike_frame_1_level_2_spike_3, spike_frame_2_level_2_spike_3]

# teleporter S

teleporteer_frame_1 = py.image.load(os.path.join('teleporteer_frame_1.png'))
teleporteer_frame_2 = py.image.load(os.path.join('teleporteer_frame_2.png'))

# teleporters level 1
# portal 1
teleporteer_frame_1_level_1_portal_1 = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_1 = teleporteer_frame_2

teleporteer_frames_level_1_portal_1 = [teleporteer_frame_1_level_1_portal_1, teleporteer_frame_2_level_1_portal_1]

# portal 2
teleporteer_frame_1_level_1_portal_2 = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_2 = teleporteer_frame_2
teleporteer_frame_1_level_1_portal_2 = py.transform.rotate(teleporteer_frame_1_level_1_portal_2, 90)
teleporteer_frame_2_level_1_portal_2 = py.transform.rotate(teleporteer_frame_2_level_1_portal_2, 90)

teleporteer_frames_level_1_portal_2 = [teleporteer_frame_1_level_1_portal_2, teleporteer_frame_2_level_1_portal_2]

# portal 3
teleporteer_frame_1_level_1_portal_3 = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_3 = teleporteer_frame_2
teleporteer_frame_1_level_1_portal_3 = py.transform.rotate(teleporteer_frame_1_level_1_portal_3, 90)
teleporteer_frame_2_level_1_portal_3 = py.transform.rotate(teleporteer_frame_2_level_1_portal_3, 90)
teleporteer_frame_1_level_1_portal_3 = py.transform.flip(teleporteer_frame_1_level_1_portal_3, True, False)
teleporteer_frame_2_level_1_portal_3 = py.transform.flip(teleporteer_frame_2_level_1_portal_3, True, False)

teleporteer_frames_level_1_portal_3 = [teleporteer_frame_1_level_1_portal_3, teleporteer_frame_2_level_1_portal_3]

# locatie en dimensies
teleporteer_binnen_dimensies = [(50, 5), (5, 50), (5, 50)]
teleporteer_binnen_locatie = [(325, 495), (600, 200), (620, 200)]
teleporteer_buiten_dimensies = [(50, 5), (5, 50), (5, 50)]
teleporteer_buiten_locatie = [(325, 0), (620, 200), (600, 200)]

# portals level 1
# portal 1

teleporteer_frame_1_level_1_portal_1_buiten = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_1_buiten = teleporteer_frame_2
teleporteer_frame_1_level_1_portal_1_buiten = py.transform.flip(teleporteer_frame_1_level_1_portal_1_buiten, False,
                                                                True)
teleporteer_frame_2_level_1_portal_1_buiten = py.transform.flip(teleporteer_frame_2_level_1_portal_1_buiten, False,
                                                                True)

teleporteer_frames_level_1_portal_1_buiten = [teleporteer_frame_1_level_1_portal_1_buiten,
                                              teleporteer_frame_2_level_1_portal_1_buiten]

# portal 2

teleporteer_frame_1_level_1_portal_2_buiten = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_2_buiten = teleporteer_frame_2
teleporteer_frame_1_level_1_portal_2_buiten = py.transform.rotate(teleporteer_frame_1_level_1_portal_2_buiten, 90)
teleporteer_frame_2_level_1_portal_2_buiten = py.transform.rotate(teleporteer_frame_2_level_1_portal_2_buiten, 90)
teleporteer_frame_1_level_1_portal_2_buiten = py.transform.flip(teleporteer_frame_1_level_1_portal_2_buiten, True,
                                                                False)
teleporteer_frame_2_level_1_portal_2_buiten = py.transform.flip(teleporteer_frame_2_level_1_portal_2_buiten, True,
                                                                False)

teleporteer_frames_level_1_portal_2_buiten = [teleporteer_frame_1_level_1_portal_2_buiten,
                                              teleporteer_frame_2_level_1_portal_2_buiten]

# portal 3

teleporteer_frame_1_level_1_portal_3_buiten = teleporteer_frame_1
teleporteer_frame_2_level_1_portal_3_buiten = teleporteer_frame_2
teleporteer_frame_1_level_1_portal_3_buiten = py.transform.rotate(teleporteer_frame_1_level_1_portal_3_buiten, 90)
teleporteer_frame_2_level_1_portal_3_buiten = py.transform.rotate(teleporteer_frame_2_level_1_portal_3_buiten, 90)

teleporteer_frames_level_1_portal_3_buiten = [teleporteer_frame_1_level_1_portal_3_buiten,
                                              teleporteer_frame_2_level_1_portal_3_buiten]

# portals level 2
# binnen
teleporteer_frame_1_level_2_portal_1 = teleporteer_frame_1
teleporteer_frame_2_level_2_portal_1 = teleporteer_frame_2
teleporteer_frame_1_level_2_portal_1 = py.transform.rotate(teleporteer_frame_1_level_2_portal_1, 90)
teleporteer_frame_2_level_2_portal_1 = py.transform.rotate(teleporteer_frame_2_level_2_portal_1, 90)
teleporteer_frame_1_level_2_portal_1 = py.transform.flip(teleporteer_frame_1_level_2_portal_1, True, False)
teleporteer_frame_2_level_2_portal_1 = py.transform.flip(teleporteer_frame_2_level_2_portal_1, True, False)

teleporteer_frames_level_2_portal_1 = [teleporteer_frame_1_level_2_portal_1, teleporteer_frame_2_level_2_portal_1]

teleporteer_frame_1_level_2_portal_2 = teleporteer_frame_1
teleporteer_frame_2_level_2_portal_2 = teleporteer_frame_2

teleporteer_frames_level_2_portal_2 = [teleporteer_frame_1_level_2_portal_2, teleporteer_frame_2_level_2_portal_2]

# buiten
teleporteer_frame_1_level_2_portal_1_buiten = teleporteer_frame_1
teleporteer_frame_2_level_2_portal_1_buiten = teleporteer_frame_2
teleporteer_frame_1_level_2_portal_1_buiten = py.transform.rotate(teleporteer_frame_1_level_2_portal_1_buiten, 90)
teleporteer_frame_2_level_2_portal_1_buiten = py.transform.rotate(teleporteer_frame_2_level_2_portal_1_buiten, 90)
teleporteer_frame_1_level_2_portal_1_buiten = py.transform.flip(teleporteer_frame_1_level_2_portal_1_buiten, True,
                                                                False)
teleporteer_frame_2_level_2_portal_1_buiten = py.transform.flip(teleporteer_frame_2_level_2_portal_1_buiten, True,
                                                                False)

teleporteer_frames_level_2_portal_1_buiten = [teleporteer_frame_1_level_2_portal_1_buiten,
                                              teleporteer_frame_2_level_2_portal_1_buiten]

teleporteer_frame_1_level_2_portal_2_buiten = teleporteer_frame_1
teleporteer_frame_2_level_2_portal_2_buiten = teleporteer_frame_2
teleporteer_frame_1_level_2_portal_2_buiten = py.transform.rotate(teleporteer_frame_1_level_2_portal_2_buiten, 90)
teleporteer_frame_2_level_2_portal_2_buiten = py.transform.rotate(teleporteer_frame_2_level_2_portal_2_buiten, 90)
teleporteer_frame_1_level_2_portal_2_buiten = py.transform.flip(teleporteer_frame_1_level_2_portal_2_buiten, True,
                                                                False)
teleporteer_frame_2_level_2_portal_2_buiten = py.transform.flip(teleporteer_frame_2_level_2_portal_2_buiten, True,
                                                                False)

teleporteer_frames_level_2_portal_2_buiten = [teleporteer_frame_1_level_2_portal_2_buiten,
                                              teleporteer_frame_2_level_2_portal_2_buiten]

teleporteer_binnen_dimensies_level_2 = [(5, 50), (50, 5)]
teleporteer_binnen_locatie_level_2 = [(0, 230), (745, 205)]
teleporteer_buiten_dimensies_level_2 = [(5, 50), (5, 50)]
teleporteer_buiten_locatie_level_2 = [(375, 230), (375, 230)]

# vijanden L

vijanden_locatie = [[400, 5], [400, 200]]
vijanden_dimensies = [(50, 50), (50, 50)]
beweeg_richting = ["rechts", "rechts"]
vijanden_foto = py.image.load(os.path.join('geestje_V3.png'))
vijanden_locatie_level_2 = [[5, 5], [300, 380]]
vijanden_dimensies_level_2 = [(50, 50), (50, 50)]
beweeg_richting_level_2 = ["rechts", "rechts"]

# coin S

coin = []
gedeactiveerd = []
coin_level_2 = []
gedeactiveerd_level_2 = []
coin_foto = py.image.load(os.path.join('Coin_25px25px.png'))
coin_locatie = [(745, 450)]
coin_dimensies = [(25, 25)]
coin_aantal = 0
coin_locatie_level_2 = [(757, 160)]
coin_dimensies_level_2 = [(25, 25)]

# eind zone

eindzone_locatie = (745, 0)
eindzone_dimensies = (50, 5)

eindzone_locatie_level_2 = (5, 55)
eindzone_dimensies_level_2 = (50, 50)


# functie om de spike animaties te cycelen -M
def spike_cycle_animaties(spike_frames_import):
    global clock, index, frame

    clock += 1

    if clock % 10 == 0:
        match index:
            case 0:
                frame = spike_frames_import[index]

                index = 1
            case 1:
                frame = spike_frames_import[index]

                index = 0
    else:
        frame = spike_frames_import[index]
    if clock == 60:
        clock = 0
    return frame


# cycle frames teleporteer
def teleporteer_cycle_animatie(teleporteer_frames_import):
    global clock_v2, index_v2

    clock_v2 += 1

    if clock_v2 % 35 == 0:
        match index_v2:
            case 0:
                frame = teleporteer_frames_import[index_v2]

                index_v2 = 1
            case 1:
                frame = teleporteer_frames_import[index_v2]

                index_v2 = 0
    else:
        frame = teleporteer_frames_import[index_v2]

    if clock_v2 == 180:
        clock_v2 = 0

    return frame


# start up_scherm S

def start_up_scherm():
    global win
    win.fill((255, 255, 255))
    start_scherm = py.image.load(os.path.join('start_scherm.png'))
    win.blit(start_scherm, (0, 0))
    py.display.update()


# eindstand scherm L
def eindstand_scherm():
    win.fill((255, 255, 255))
    eind_scherm = py.image.load(os.path.join('eind_scherm.png'))
    win.blit(eind_scherm, (0, 0))
    py.display.update()


# scherm als je dood gaat
def dood_scherm():
    win.fill((255, 255, 255))
    dood_scherm = py.image.load(os.path.join('dood_scherm.png'))
    win.blit(dood_scherm, (0, 0))
    py.display.update()


# tekent het scherm S


def draw_scr():
    global muren, speler_rect, spike, teleporteer_binnen, teleporteer_buiten, vijanden, eindzone_rect, spike_foto, coin
    muren = []
    spike = []
    teleporteer_binnen = []
    teleporteer_buiten = []
    vijanden = []
    #
    spike_cycle_frame = spike_cycle_animaties(spike_frames)
    # binnen
    teleporteer_cycle_frame_level_1_portal_1 = teleporteer_cycle_animatie(teleporteer_frames_level_1_portal_1)
    teleporteer_cycle_frame_level_1_portal_2 = teleporteer_cycle_animatie(teleporteer_frames_level_1_portal_2)
    teleporteer_cycle_frame_level_1_portal_3 = teleporteer_cycle_animatie(teleporteer_frames_level_1_portal_3)
    # buiten
    teleporteer_cycle_frame_level_1_portal_1_buiten = teleporteer_cycle_animatie(
        teleporteer_frames_level_1_portal_1_buiten)
    teleporteer_cycle_frame_level_1_portal_2_buiten = teleporteer_cycle_animatie(
        teleporteer_frames_level_1_portal_2_buiten)
    teleporteer_cycle_frame_level_1_portal_3_buiten = teleporteer_cycle_animatie(
        teleporteer_frames_level_1_portal_3_buiten)

    # maakt de achtergrond S
    win.fill((0, 0, 0))
    win.blit(achtergrond_foto, (0, 0))
    # foto van de speler S
    win.blit(speler_foto, (speler_x_y[0], speler_x_y[1]))
    # speler vierkant S
    speler_rect = py.Rect(speler_x_y[0], speler_x_y[1], 50, 50)
    # muren S
    for i in range(len(wall_dimensions)):
        muren.append(py.draw.rect(win, (100, 100, 100), (wall_position[i], wall_dimensions[i])))
    # de spikes S
    for i in range(len(spike_dimensies)):
        win.blit(spike_cycle_frame, (spike_plek[i]))
        # spike.append(py.draw.rect(win, (0, 0, 255), (spike_plek[i], spike_dimensies[i])))
        spike.append(py.Rect((spike_plek[i], spike_dimensies[i])))
    # de teleporteer ingang M
    for i in range(len(teleporteer_binnen_locatie)):
        match i:
            case 0:
                win.blit(teleporteer_cycle_frame_level_1_portal_1, teleporteer_binnen_locatie[i])
            case 1:
                win.blit(teleporteer_cycle_frame_level_1_portal_2, teleporteer_binnen_locatie[i])
            case 2:
                win.blit(teleporteer_cycle_frame_level_1_portal_3, teleporteer_binnen_locatie[i])

        teleporteer_binnen.append(py.Rect(teleporteer_binnen_locatie[i], teleporteer_binnen_dimensies[i]))
    # de teleporteer uitgang M
    for i in range(len(teleporteer_buiten_locatie)):
        match i:
            case 0:
                win.blit(teleporteer_cycle_frame_level_1_portal_1_buiten, teleporteer_buiten_locatie[i])
            case 1:
                win.blit(teleporteer_cycle_frame_level_1_portal_2_buiten, teleporteer_buiten_locatie[i])
            case 2:
                win.blit(teleporteer_cycle_frame_level_1_portal_3_buiten, teleporteer_buiten_locatie[i])

        teleporteer_buiten.append(py.Rect(teleporteer_buiten_locatie[i], teleporteer_buiten_dimensies[i]))

    # de vijanden L
    for i in range(len(vijanden_locatie)):
        vijanden.append(py.Rect(vijanden_locatie[i], vijanden_dimensies[i]))

        # vijanden.append(py.draw.rect(win, (125, 125, 125), (vijanden_locatie[i], vijanden_dimensies[i])))
        win.blit(vijanden_foto, vijanden_locatie[i])
    eindzone_rect = py.draw.rect(win, (125, 255, 75), (eindzone_locatie, eindzone_dimensies))

    # coin
    for i in range(len(coin_locatie)):
        if gedeactiveerd:
            for ii in range(len(gedeactiveerd)):
                if i != gedeactiveerd[ii]:
                    coin.append(py.Rect(coin_locatie[i], coin_dimensies[i]))
                    win.blit(coin_foto, coin_locatie[i])
        else:
            coin.append(py.Rect(coin_locatie[i], coin_dimensies[i]))
            win.blit(coin_foto, coin_locatie[i])

    # py.draw.rect(win, (0, 0, 0), speler_rect)
    # ververst het scherm
    py.display.update()


# tekent het scherm voor het tweede level
def draw_scr_level_2():
    global speler_rect, muren_level_2, eindzone_rect_level_2, teleporteer_binnen_level_2, teleporteer_buiten_level_2, vijanden_level_2, spike_level_2
    muren_level_2 = []
    teleporteer_binnen_level_2 = []
    teleporteer_buiten_level_2 = []
    vijanden_level_2 = []
    spike_level_2 = []
    win.fill((255, 255, 255))
    # animaties cyclen
    spike_frame_level_2_spike_1 = spike_cycle_animaties(spike_frames_level_2_spike_1)
    spike_frame_level_2_spike_2 = spike_cycle_animaties(spike_frames_level_2_spike_2)
    spike_frame_level_2_spike_3 = spike_cycle_animaties(spike_frames_level_2_spike_3)
    # teleporteer cyclen
    teleporteer_cycle_frame_level_2_portal_1 = teleporteer_cycle_animatie(teleporteer_frames_level_2_portal_1)
    teleporteer_cycle_frame_level_2_portal_2 = teleporteer_cycle_animatie(teleporteer_frames_level_2_portal_2)

    teleporteer_cycle_frame_level_2_portal_1_buiten = teleporteer_cycle_animatie(
        teleporteer_frames_level_2_portal_1_buiten)
    teleporteer_cycle_frame_level_2_portal_2_buiten = teleporteer_cycle_animatie(
        teleporteer_frames_level_2_portal_2_buiten)

    # achtergrond foto
    win.blit(achtergrond_foto_level_2, (0, 0))

    # muren
    for i in range(len(wall_dimensions_level_2)):
        muren_level_2.append(py.draw.rect(win, (150, 150, 150), (wall_position_level_2[i], wall_dimensions_level_2[i])))

    # teleporteer binnen
    for i in range(len(teleporteer_binnen_locatie_level_2)):
        match i:
            case 0:
                win.blit(teleporteer_cycle_frame_level_2_portal_1, teleporteer_binnen_locatie_level_2[i])
            case 1:
                win.blit(teleporteer_cycle_frame_level_2_portal_2, teleporteer_binnen_locatie_level_2[i])

        teleporteer_binnen_level_2.append(
            py.Rect(teleporteer_binnen_locatie_level_2[i], teleporteer_binnen_dimensies_level_2[i]))

    # teleporteer buiten

    for i in range(len(teleporteer_binnen_locatie_level_2)):
        match i:
            case 0:
                win.blit(teleporteer_cycle_frame_level_2_portal_1_buiten, teleporteer_buiten_locatie_level_2[i])
            case 1:
                win.blit(teleporteer_cycle_frame_level_2_portal_2_buiten, teleporteer_buiten_locatie_level_2[i])

        teleporteer_buiten_level_2.append(
            py.Rect(teleporteer_buiten_locatie_level_2[i], teleporteer_buiten_dimensies_level_2[i]))
        # teleporteer_buiten_level_2.append(py.draw.rect(win, (0, 255, 255), (teleporteer_buiten_locatie_level_2[i], teleporteer_buiten_dimensies_level_2[i])))

    for i in range(len(spike_dimensies_level_2)):
        match i:
            case 0:
                win.blit(spike_frame_level_2_spike_1, spike_plek_level_2[i])
            case 1:
                win.blit(spike_frame_level_2_spike_2, spike_plek_level_2[i])
            case 2:
                win.blit(spike_frame_level_2_spike_3, spike_plek_level_2[i])

        spike_level_2.append(py.Rect(spike_plek_level_2[i], spike_dimensies_level_2[i]))

    # vijanden
    for i in range(len(vijanden_locatie_level_2)):
        vijanden_level_2.append(py.Rect(vijanden_locatie_level_2[i], vijanden_dimensies_level_2[i]))

        # vijanden.append(py.draw.rect(win, (125, 125, 125), (vijanden_locatie[i], vijanden_dimensies[i])))
        win.blit(vijanden_foto, vijanden_locatie_level_2[i])

    # speler
    speler_rect = py.Rect(speler_x_y[0], speler_x_y[1], 50, 50)
    win.blit(speler_foto, (speler_x_y[0], speler_x_y[1]))

    # coin
    for i in range(len(coin_locatie_level_2)):
        if gedeactiveerd_level_2:
            for ii in range(len(gedeactiveerd_level_2)):
                if i != gedeactiveerd_level_2[ii]:
                    coin_level_2.append(py.Rect(coin_locatie_level_2[i], coin_dimensies_level_2[i]))
                    win.blit(coin_foto, coin_locatie_level_2[i])
        else:
            coin_level_2.append(py.Rect(coin_locatie_level_2[i], coin_dimensies_level_2[i]))
            win.blit(coin_foto, coin_locatie_level_2[i])

    eindzone_rect_level_2 = py.draw.rect(win, (125, 255, 75), (eindzone_locatie_level_2, eindzone_dimensies_level_2))

    # vervest het scherm
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
def vijand_beweging(muren_import_V2, vijanden_import, vijanden_locatie_import, beweeg_richting_import,
                    teleporteer_binnen_import, teleporteer_buiten_import):
    # zet de speed van de vijanden
    speed = 3
    for i in range(len(vijanden_locatie_import)):
        # bewaart de oude locatie zodat de vijand terug gezet kan worden als iets raakt
        oude_locatie = vijanden_locatie_import[i]
        # beslist welke kant de vijand op beweegt
        match beweeg_richting_import[i]:
            case "rechts":
                vijanden_locatie_import[i][0] = vijanden_locatie_import[i][0] + speed
            case "links":
                vijanden_locatie_import[i][0] = vijanden_locatie_import[i][0] - speed
        # zet tuple om in list om gegevens te wijzigen
        vijand_locatie = list(vijanden_locatie_import[i])
        # checkt of vijand een teleporter raakt
        vijanden_locatie_import[i], telehit = botsing_teleporteren(vijanden_import[i], teleporteer_binnen_import,
                                                                   teleporteer_buiten_import, vijand_locatie)
        # checkt of vijand een muur raakt
        muur_raking = botsing_muren(vijanden_import[i], muren_import_V2)
        # als de vijand een teleporter raakt en het is teleporter 3(index 2)
        # dan wordt hij de andere kant opgestuurd anders wordt er 5 pixels naar rechts gestuurd om
        # niet terug gestuurd te worden
        if telehit != -1:
            if telehit == 2:
                vijanden_locatie_import[i] = [vijanden_locatie_import[i][0] - 55, vijanden_locatie_import[i][1]]

            vijanden_locatie_import[i] = [vijanden_locatie_import[i][0] + 5, vijanden_locatie_import[i][1]]
        else:
            vijanden_locatie_import[i] = [vijanden_locatie_import[i][0], vijanden_locatie_import[i][1]]
        # als de muur wordt geraakt en je gaat naar rechts ga je naar links met een zetje en andersom
        if muur_raking > -1 and telehit == -1:
            match beweeg_richting_import[i]:
                case "rechts":
                    vijanden_locatie_import[i][0] = oude_locatie[0] - speed * 2
                    vijanden_locatie_import[i][1] = oude_locatie[1]
                    beweeg_richting_import[i] = "links"

                case "links":
                    vijanden_locatie_import[i][0] = oude_locatie[0] + speed * 2
                    vijanden_locatie_import[i][1] = oude_locatie[1]
                    beweeg_richting_import[i] = "rechts"


# kijkt of object botst met teleporters M
def botsing_teleporteren(object_rect, tele_in, tele_uit, object_x_y):
    tele_hit = object_rect.collidelist(tele_in)
    object_plek = []
    if tele_hit != -1:
        object_plek.append(tele_uit[tele_hit][0])
        object_plek.append(tele_uit[tele_hit][1])
    else:
        object_plek = object_x_y
    return object_plek, tele_hit


# checkt of object met muur botst L
def botsing_muren(object_rect, muren_import):
    wallhit = object_rect.collidelist(muren_import)
    return wallhit


# checkt of object met vijand botst, komt veel overeen met botsing_spikes L
def botsing_vijand(object_rect, running_import, vijanden_import):
    vijand_hit = object_rect.collidelist(vijanden_import)
    if vijand_hit > -1:
        running = False
    else:
        running = running_import
    return running


# checkt of object met de spike botst komt veel overeen met botsing_vijand S
def botsing_spikes(object_rect, running_import, spike_import):
    spike_hit = object_rect.collidelist(spike_import)
    if spike_hit != -1:
        running = False
    else:
        running = running_import
    return running


# checkt of object met een coin botst S
def botsing_coin(object_rect, coin_aantal_import, coin_import, gedeactiveerd_import):
    coin_hit = object_rect.collidelist(coin_import)
    coin_aantal = coin_aantal_import
    if coin_hit != -1:
        for i in range(len(gedeactiveerd_import)):
            if coin_hit != i:
                coin_aantal += 1

    return coin_aantal, coin_hit


# botsing met de eind zone L
def botsing_eind_zone(object_rect, eindzone_rect_import):
    eindhit = object_rect.colliderect(eindzone_rect_import)
    if eindhit is True:
        return 1
    else:
        return 0


# de main game functie S
def main(import_game_state):
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
        # startup scherm L
        case 0:
            while running:
                muis = pygame.mouse.get_pos()
                start_up_scherm()
                for events in py.event.get():
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"
                    # checkt of speler op die knoppen heeft geduwd
                    if events.type == py.MOUSEBUTTONDOWN:
                        if (730 <= muis[0] <= 800 and 115 <= muis[1] <= 135):
                            game_state = 1
                            reden = main(import_game_state)
                            running = False

                        if (730 <= muis[0] <= 800 and 175 <= muis[1] <= 195):
                            game_state = 2
                            reden = main(import_game_state)
                            running = False

        case 1:
            while running:
                clock.tick(fps)
                # als de speler al in beweging is, beweegt hij in dezelfde richting als de vorige zet

                # de event loop als er wat gebeurt in het spel komt het hier terecht
                for events in py.event.get():
                    # als er op het kruisje in het pop-up-window word geklikt dan stopt de game loop M
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
                        # als de speler een richting op gaat en het is geen muur dan beweegt hij totdat M
                        # hij een andere muur raakt M
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
                vijand_beweging(muren, vijanden, vijanden_locatie, beweeg_richting, teleporteer_binnen,
                                teleporteer_buiten)
                speler_x_y, tele_hit = botsing_teleporteren(speler_rect, teleporteer_binnen, teleporteer_buiten,
                                                            speler_x_y)
                running = botsing_spikes(speler_rect, running, spike)
                eind_botsing = botsing_eind_zone(speler_rect, eindzone_rect)

                nieuwe_coin_aantal, coin_deactivatie_komt = botsing_coin(speler_rect, coin_aantal, coin, gedeactiveerd)
                coin_aantal = nieuwe_coin_aantal
                if coin_deactivatie_komt > -1:
                    gedeactiveerd.append(coin_deactivatie_komt)

                muur_raak = botsing_muren(speler_rect, muren)
                running = botsing_vijand(speler_rect, running, vijanden)
                # voor het terug zetten van de speler als het tegen een muur dondert
                for i in range(len(muren)):
                    if muur_raak == i and tele_hit == -1:
                        speler_x_y = oude_positie
                        activated = False
                # naar het victory scherm als eindzone bereikt is
                if eind_botsing == 1:
                    game_state = 99
                    activated = False
                    reden = main(import_game_state)
                    running = False

                # als de speler in beweging is gaat die in de zelfde richting door
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
            # timed het level
            eind_tijd = time.time()
            tijd_duratie = eind_tijd - begin_tijd
            tijd_duratie = round(tijd_duratie, 2)
            print(str(tijd_duratie) + " seconde")

        case 2:
            # het tweede level
            speler_x_y = [80, 80]

            while running:
                clock.tick(fps)

                # de event loop als er wat gebeurt in het spel komt het hier terecht
                for events in py.event.get():
                    # als er op het kruisje in het pop-up-window word geklikt dan stopt de game loop M
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"
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
                            # movement
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

                # executeerd een hele hoop functies
                draw_scr_level_2()

                muur_raak = botsing_muren(speler_rect, muren_level_2)
                vijand_beweging(muren_level_2, vijanden_level_2, vijanden_locatie_level_2, beweeg_richting_level_2,
                                teleporteer_binnen_level_2, teleporteer_buiten_level_2)

                running = botsing_vijand(speler_rect, running, vijanden_level_2)
                running = botsing_spikes(speler_rect, running, spike_level_2)

                nieuwe_coin_aantal, coin_deactivatie_komt = botsing_coin(speler_rect, coin_aantal, coin_level_2,
                                                                         gedeactiveerd_level_2)
                coin_aantal = nieuwe_coin_aantal
                if coin_deactivatie_komt > -1:
                    gedeactiveerd_level_2.append(coin_deactivatie_komt)

                speler_x_y, tele_hit = botsing_teleporteren(speler_rect, teleporteer_binnen_level_2,
                                                            teleporteer_buiten_level_2, speler_x_y)

                eind_botsing = botsing_eind_zone(speler_rect, eindzone_rect_level_2)
                for i in range(len(muren_level_2)):
                    if muur_raak == i and tele_hit == -1:
                        speler_x_y = oude_positie
                        activated = False

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

                if eind_botsing == 1:
                    game_state = 99
                    activated = False
                    reden = main(import_game_state)
                    running = False

        case 98:
            # dood scherm als je dood gaat kom je hier
            while running:
                muis = pygame.mouse.get_pos()
                dood_scherm()
                for events in py.event.get():
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"
                    if events.type == py.MOUSEBUTTONDOWN:
                        if (150 <= muis[0] <= 300 and 400 <= muis[1] <= 450):
                            game_state = import_game_state
                            reden = main(import_game_state)
                            running = False

                        if (500 <= muis[0] <= 650 and 400 <= muis[1] <= 450):
                            game_state = 0
                            speler_x_y = speler_start_plek
                            reden = main(import_game_state)
                            running = False

        case 99:
            # win scherm hier kun je door naar het volgende level of naar het menu
            while running:
                muis = pygame.mouse.get_pos()
                eindstand_scherm()
                for events in py.event.get():
                    if events.type == py.QUIT:
                        running = False
                        return "gestopt"
                    if events.type == py.MOUSEBUTTONDOWN:
                        if (245 <= muis[0] <= 350 and 250 <= muis[1] <= 300):
                            game_state = 2
                            reden = main(import_game_state)
                            running = False

                        if (445 <= muis[0] <= 550 and 250 <= muis[1] <= 300):
                            game_state = 0
                            speler_x_y = speler_start_plek
                            reden = main(import_game_state)
                            running = False
    # returned gestopt naar lagere niveaus zodat het programma gestopt kan worden
    if reden == "gestopt":
        return "gestopt"

    # word door gegeven naar beneden dat je dood bent gegaan en welk level
    return "dood", game_state


eind_game_state = 0
# zorgt ervoor dat de goede main word uitgevoerd hier kwam max achter M

if __name__ == "__main__":
    reden, eind_game_state = main(import_game_state)

# zorgt ervoor dat als je niet dood bent dat je opnieuw kan proberen L
while reden != "gestopt":
    if reden == "dood":
        import_game_state = eind_game_state
        game_state = 98
        activated = False
        speler_x_y = speler_start_plek
        reden, eind_game_state = main(import_game_state)
