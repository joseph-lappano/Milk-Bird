# Joseph Lappano
# August 17
# Milk Bird

# imports
import pygame
from pygame import mixer

# initialize game
pygame.init()
pygame.mixer.init()

# create window
screen = pygame.display.set_mode((1200, 704), pygame.RESIZABLE, pygame.DOUBLEBUF)
icon = pygame.image.load('app_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Milk Bird")

# load and scale backgrounds
splash = pygame.image.load('splash.png').convert()
splash = pygame.transform.scale(splash, (1300, 704))
game_background = pygame.image.load('background.png').convert()
game_background = pygame.transform.scale(game_background, (1300, 704))
select_background = pygame.image.load('level_select.png').convert()
select_background = pygame.transform.scale(select_background, (1200, 704))
ending_background = pygame.image.load('happy_family.png').convert()
ending_background = pygame.transform.scale(ending_background, (1200, 704))

# load and scale icons
body = pygame.image.load('pipe_body.png').convert_alpha()
top = pygame.image.load('pipe_head_DOWN.png').convert_alpha()
bottom = pygame.image.load('pipe_head_UP.png').convert_alpha()
body = pygame.transform.scale(body, (64, 64))
top = pygame.transform.scale(top, (80, 64))
bottom = pygame.transform.scale(bottom, (80, 64))

# fonts
fontL = pygame.font.Font('MarkerFelt.ttc', 120)
fontM = pygame.font.Font('MarkerFelt.ttc', 50)
fontS = pygame.font.Font('MarkerFelt.ttc', 30)

# colours
colour = (0, 0, 0)
colour2 = (140, 140, 140)

# text
title = fontL.render('Milk Bird', True, colour)
press = fontS.render('Press Any Key To Play', True, colour2)
start_text = fontS.render("Press Space To Start", True, colour2)
start_text_rect = start_text.get_rect()
start_text_rect.center = (600, 350)
# render win text
win_text = fontL.render("You Won!", True, colour)
win_text_rect = win_text.get_rect()
win_text_rect.center = (600, 350)
# render return to level selection text
selection_text = fontM.render("To Level Selection", True, colour)
selection_text_rect = selection_text.get_rect()
selection_text_rect.center = (600, 475)
# render, display, and center the Game Over text
death_text = fontL.render("Game Over", True, colour)
death_text_rect = death_text.get_rect()
death_text_rect.center = (600, 350)
# render, display, and center the Try Again? text
restart_text = fontM.render("Try Again?", True, colour)
restart_text_rect = restart_text.get_rect()
restart_text_rect.center = (600, 475)
# render and center the Pause text
pause_text = fontM.render("| |", True, colour)
pause_text_rect = pause_text.get_rect()
pause_text_rect.center = (1175 - pause_text_rect[0], 35)
# render and center the Options text
options_text = fontM.render("Options", True, colour)
options_text_rect = options_text.get_rect()
options_text_rect.center = (1100 - options_text_rect[0], 35)
# render and center the Delete Save Data text
delete_text = fontM.render("Delete All Save Data", True, colour)
delete_text_rect = delete_text.get_rect()
delete_text_rect.center = (600, 625)
# render and center the "Are You Sure" text
are_you_sure_text = fontM.render("Are You Sure?", True, colour)
are_you_sure_text_rect = are_you_sure_text.get_rect()
are_you_sure_text_rect.center = (600, 350)
# render and center the Volume text
volume_text = fontL.render("Volume Settings", True, colour)
volume_text_rect = volume_text.get_rect()
volume_text_rect.center = (600, 150)
# render and center the Controls text
controls_text = fontL.render("Controls", True, colour)
controls_text_rect = controls_text.get_rect()
controls_text_rect.center = (600, 500)
# render and center the Jump text
jump_text = fontM.render("Jump: Space", True, colour)
jump_text_rect = jump_text.get_rect()
jump_text_rect.center = (600, 150)
# render and center the Glide text
glide_text = fontM.render("Glide: G", True, colour)
glide_text_rect = glide_text.get_rect()
glide_text_rect.center = (600, 250)
# render and center the Escape text
escape_text = fontM.render("Pause: ESC", True, colour)
escape_text_rect = escape_text.get_rect()
escape_text_rect.center = (600, 350)

# music/sounds
kaboom = pygame.mixer.Sound('explosion.wav')
mixer.music.load('splash_level_select.wav')

# data bank
playing = True
left = False
right = True
splash_x = 0
splashing = True
gaming = False
selected = False
level_select = False
overall_game = True
controls = False
offset = 0
player_x = 100
background_offset = 0
player_y = 300
new_jump = False
velocity = 4
down = 0
up = -10
Score = 0
high_score = 0
player_sprite_list = []
lev_list = []
level_text_list = []
selection_y = 150
level_counter = -3
explosion_graphic = False
explosion_sprite_list = []
explosion_change_val = 0
explosion = 1
close_file = False
available_level_list = []
options = False
final_chance = False
music = False
volume_sprite_list = []
end_cutscene = False
fade = 0
alpha = 255

# load and scale player sprites
for num in range(6, -1, -1):
    player_sprite = pygame.image.load(f"Player Sprites/sprite_{num}.png").convert_alpha()
    player_sprite = pygame.transform.scale(player_sprite, (32, 32))
    player_sprite_list.append(player_sprite)

# load and scale explosion sprites
for num in range(0, 6):
    explosion_sprite = pygame.image.load(f"Explosion Sprites/explosion_{num}.png").convert_alpha()
    explosion_sprite = pygame.transform.scale(explosion_sprite, (256, 256))
    explosion_sprite_list.append(explosion_sprite)

for num in range(0, 3):
    volume_sprite = pygame.image.load(f"Volume Sprites/volume_{num}.png").convert_alpha()
    volume_sprite = pygame.transform.scale(volume_sprite, (96, 96))
    volume_sprite_rect = volume_sprite.get_rect()
    volume_sprite_rect.center = ((num + 1) * 300, 350)
    volume_sprite_list.append([volume_sprite, volume_sprite_rect])


# limit fps
clock = pygame.time.Clock()

# levels

level_1 = [
    '    X     X    X    X  X     T  X',
    '    X     T    X    X  X        X',
    '    X          X    X  T        X',
    '    T          T    X           T',
    '                    T            ',
    '                                 ',
    '          B                  B   ',
    '          X    B             X   ',
    '    B     X    X       B     X  B',
    '    X     X    X    B  X     X  X',
    '    X     X    X    X  X     X  X']
lev_list.append(level_1)

level_2 = [
    '    X   X      X   X    X   X   XX',
    '    X   X      X   X    X   X   XX',
    '    T   X      X   T    X   T   XX',
    '        X      T        T       TT',
    '        T                         ',
    '                                  ',
    '                                  ',
    '    B              B        B   BB',
    '    X          B   X    B   X   XX',
    '    X   B      X   X    X   X   XX',
    '    X   X      X   X    X   X   XX']
lev_list.append(level_2)

level_3 = [
    '    X   X  X XX    X  X X X  X       X',
    '    X   X  X XX    T  X X X  X       X',
    '    X   T  T TT       X X T  X       X',
    '    T                 X X    T   B   X',
    '                      T T        X   X',
    '                                 X   X',
    '           B BB    B             X   T',
    '        B  X XX    X      B      X    ',
    '    B   X  X XX    X    B X  B   X    ',
    '    X   X  X XX    X  B X X  X   X    ',
    '    X   X  X XX    X  X X X  X   X    ']
lev_list.append(level_3)

level_4 = [
    '    X X  X  XX  X X  X  X XX  TTT  X  X  T  X   X  X',
    '    X X  X  XX  X X  X  X TT       X  X     X   X  X',
    '    T X  T  XX  X X  X  T          X  T     X   X  T',
    '      T     XX  T T  X             T        T   X   ',
    '            TT       T        BBB        B      T   ',
    '                              XXX        T          ',
    '         B              B     TTT     B             ',
    '      B  X      B B     X BB       B  X     B       ',
    '    B X  X   B  X X  B  X XX       X  X     X   B  B',
    '    X X  X  BX  X X  X  X XX  BBB  X  X  B  X   X  X',
    '    X X  X  XX  X X  X  X XX  XXX  X  X  X  X   X  X']
lev_list.append(level_4)

level_5 = [
    '    X  T   X XX  X   X   X   T  X  X  X  X  X  X  X  X  TT  X    X',
    '    X      X XX  X   X   T      X  X  X  T  X  X  T  X      X    X',
    '    X      T TT  X   X          T  X  X     T  X     X      T    X',
    '    T            X   T             X  T        X     T  BB       T',
    '       B         X                 X     B     T        TT        ',
    '       X         X       B   B     X     X                        ',
    '       T     BB  T       T   X     T     T  B               B     ',
    '             XX              X  B           X     B  B      T    B',
    '    B      B XX      B       X  X     B     X  B  X  X  BB       X',
    '    X      X XX      X       X  X     X     X  X  X  X  XX       X',
    '    X  B   X XX  B   X   B   X  X  B  X  B  X  X  X  X  XX  B    X']
lev_list.append(level_5)

level_6 = [
    '    X  X X XXT  X X X X  X X      X    X  X      X  X   X  X   T X XX  X',
    '    X  T X XT   T X X X  X X      X    X  X      X  X   T  X     T XX  X',
    '    X    X T      X X X  X X      X    T  X      X  T      X       XX  X',
    '    T    T        T X X  T X      X       T      T         T       TT  T',
    '                    X T    T      X           B                         ',
    '       B     B      T          B  T           X     B   B      B B      ',
    '       T    BX  B              X       B      X     T   T      T T      ',
    '    B      BXX  X        B     X       T      X  B                     B',
    '    X    B XXX  X B   B  X     X          B   X  X         B       BB  X',
    '    X    X XXX  X X   X  X B   X          X   X  X  B      X     B XX  X',
    '    X  B X XXX  X X B X  X X   X       B  X   X  X  X   B  X   B X XX  X']
lev_list.append(level_6)

level_7 = [
    '   X  T XX   X X X  XX    X X X  X XXX X   XXX   XX  X X X X X    X XX  XX',
    '   X    XX   T X X  TT    X X X  X TTT X   XXX   TT  X X T X X    X XX  XX',
    '   T    TT     X T        X X X  T     X   XXX       X T   T X    T XX  TX',
    '               T          X X T        X   TTT       T       T      TT   T',
    '      B             BB    X X          T                        B         ',
    '      T             TT    T T                                   X         ',
    '                                         B                      T         ',
    '   B    BB     B B                 BBB   X BBB       B       B      BB  B ',
    '   X    XX   B X X            B  B XXX   X XXX       X B   B X    B XX  XB',
    '   X    XX   X X X  BB        X  X XXX   X XXX   BB  X X B X X    X XX  XX',
    '   X  B XX   X X X  XX    B B X  X XXX   X XXX   XX  X X X X X    X XX  XX']
lev_list.append(level_7)

level_8 = [
    '    X  X  X  X   X   X X  X XX   X X X   X X X   XX X   X  X    T X X  X X',
    '    X  X  X  T   X   X X  X TX   X X X   X X T   XX X   T  X      X T  X X',
    '    X  T  X      X   T X  T  T   X X X   X T     XX X      X      T    X T',
    '    T     T      X     T         T X X   T       XT X      X           X  ',
    '                 X                 T T           T  T      T           X  ',
    '             B   T                           B          B       B      T  ',
    '       B     X       B    B B              B X          X       X   B     ',
    '    B  X     X       X B  X XB           B X X          X       X B X     ',
    '    X  X  B  X       X X  X XX   B       X X X    B     X  B    X X X    B',
    '    X  X  X  X   B   X X  X XX   X B B   X X X   BX B   X  X    X X X    X',
    '    X  X  X  X   X   X X  X XX   X X X   X X X   XX X   X  X    X X X  B X']
lev_list.append(level_8)

level_9 = [
    '   X X        X T XX     X X           X  X   X   XX  X   X X T XX  X     X   ',
    '   X X        X   TT     X X           T  X   X   XX  X   X X   XX  X     X   ',
    '   X T        T          T T   B B        T   X   TT  X   T X   TX  X     X   ',
    '   T    BB                     X X            T       T     T    T  T     T   ',
    '        XX            BB       X X                            B        B     B',
    '        XX            XX       X X                            T        X     X',
    '     B  XX        BB  TT       X X        B                            T     T',
    '     X  XX        XX       B   T T        X   B           B B    B  B     B   ',
    '   B X  XX        XX     B X              X   X       B   X X   BX  X     X   ',
    '   X X  XX    B B XX     X X           B  X   X   BB  X   X X B XX  X     X   ',
    '   X X  XX    X X XX     X X           X  X   X   XX  X   X X X XX  X     X   ']
lev_list.append(level_9)

level_10 = [
    '    X   T  X XX    X   X  X XX   X  X XX X       X  T   X    T    X   X  X',
    '    X      X XX    X   X  X XX   X  X XX X       X      X         X   X  X',
    '    T      T TT    X   X  X TT   T  X XX X       X      X         T   X  X',
    '                   X   X  T         T XX T       T      T             T  T',
    '        B          T   X              TT                     B            ',
    '        T              T                    B                X            ',
    '    B        BB                             T                T            ',
    '    X        XX             BB   B  B BB         B      B             B  B',
    '    X      B XX           B XX   X  X XX B       X      X         B   X  X',
    '    X   B  X XX    B      X XX   X  X XX X       X      X         X   X  X',
    '    X   X  X XX    X      X XX   X  X XX X       X  B   X    B    X   X  X']
lev_list.append(level_10)

level_11 = [
    '   X   X        X   X     X  X   X X            X',
    '   X   X        X   X     X  X   T X            X',
    '   X   X        X   X     X  X     T            X',
    '   T   T        T   X     X  X                  T',
    '                    T     X  X                   ',
    '                          X  T   B               ',
    '                          T      X B            B',
    '   B   B                         X X            X',
    '   X   X            B            X X            X',
    '   X   X        B   X            X X            X',
    '   X   X        X   X     B  B   X X            X']
lev_list.append(level_11)

level_12 = [
    '    X  X  X  X  X  X  X  T      TXXXXXXX',
    '    X  X  X  X  X  X  T          TXXXXXX',
    '    X  X  X  X  X  T              TXXXXX',
    '    X  X  X  X  T           B      TXXXX',
    '    X  X  X  T           B  X  B    TXXX',
    '    X  X  T           B  X  X  XB    TXX',
    '    X  T           B  X  X  X  XXB    TX',
    '    T           B  X  X  X  X  XXXB    T',
    '             B  X  X  X  X  X  XXXXB    ',
    '          B  X  X  X  X  X  X  XXXXXB   ',
    '       B  X  X  X  X  X  X  X  XXXXXXB  ']
lev_list.append(level_12)

level_13 = [
    '   X   X X   X T X  X X   X X T    X X   X      T X   X    T',
    '   X   X X   T   X  X X   X T      X X   X        X   X     ',
    '   T   X T       T  X X   T        X X   T        X   T     ',
    '       T            X X         B  T X            T        B',
    '                    T X       B X    T      B              X',
    '               B      T     B X X           X              X',
    '             B X          B X X X           T              X',
    '       B     X X B        X X X X  B              B        X',
    '   B   X B   X X X        X X X X  X B   B        X   B    X',
    '   X   X X   X X X  B     X X X X  X X   X        X   X    X',
    '   X   X X   X X X  X B   X X X X  X X   X      B X   X    X']
lev_list.append(level_13)

level_14 = [
    '   TTTTTTTTTTT  XTTTTTTX  TTTTTTTT  XTTTTTTT   TTTTTTTX  X     X',
    '        X       X      T            X                 X  X     X',
    '        X       X                   X                 X  X     X',
    '        X       T                   T                 X  X     X',
    '        X              B                       B      X  X     X',
    '        X              X  XXXXXXXT      XXXX   XX    XT  XXXXXXX',
    '        T              X                       T         T     X',
    '                B      X            B                          T',
    '   B            X      X            X                           ',
    '   X            X      X         B  X                           ',
    '   XBBBBB       XBBBBBBX  BBBBBBBX  XBBBBBBB   B         B      ']
lev_list.append(level_14)

level_15 = [
    '    X  X T XX    X X    X     X        XXX   XXXXXX',
    '    X  X   XX    X X    X     X        TTT   XXXXXX',
    '    X  X   XT    T X    T     X              XXXXXX',
    '    T  X   T       T          X     B        TTTTTT',
    '       T                      X     X  B           ',
    '                              X     X  XB          ',
    '         B         B          X     X  XXB         ',
    '    B    X  B    B X    B     T     X  XXX   BBBBBB',
    '    X    X BX    X X    X           X  XXX   XXXXXX',
    '    X    X XX    X X    X           X  XXX   XXXXXX',
    '    X  B X XX    X X    X           X  XXX   XXXXXX']
lev_list.append(level_15)

level_16 = [
    '        X  X       X    X X X    X  X XX XX   X X X',
    '        X  X       X    X X T    T  X XX XX   X X X',
    '        T  T       T    X T         X XX XX   X T X',
    '                        T           X TT XX   X   T',
    '     B          B                   T    TT   T    ',
    '     X          X           B    B                 ',
    '     X     B    T         B X    X              B B',
    '     X  B  X            B X X    X    BB        X X',
    '     X  X  X       B    X X X    X  B XX BB   B X X',
    '     X  X  X       X    X X X    X  X XX XX   X X X',
    '     X  X  X       X    X X X    X  X XX XX   X X X']
lev_list.append(level_16)

level_17 = [
    '     X   T  XX     T XXX    X X    X X    X X X X X T',
    '     X      XX       TTT    X X    X X    X X X X T  ',
    '     X      TX              X X    X X    X X X T    ',
    '     T       T              X T    T X    X X T      ',
    '         B       B B B      T        T    X T        ',
    '         X       X X X                    T         B',
    '         T       X X XBB                          B X',
    '     B       B   X X XXX      B    B            B X X',
    '     X      BX   X X XXX    B X    X B        B X X X',
    '     X      XX   X X XXX    X X    X X      B X X X X',
    '     X   B  XX   X X XXX    X X    X X    B X X X X X']
lev_list.append(level_17)

level_18 = [
    '    X   X X X   X X X   X X X    T T T    X X X    XXX',
    '    X   X X X   X X X   X X X             X X X    XXX',
    '    T   X X X   X X X   X X X             X X X    XXX',
    '        T T T   X X X   T T T             T T T    TTX',
    '                X X X            B B B               T',
    '    B           X X X            X X X                ',
    '    T           T T T            X X X                ',
    '        B B B           B B B    X X X    B B B    BBB',
    '        X X X           X X X    X X X    X X X    XXX',
    '    B   X X X           X X X    X X X    X X X    XXX',
    '    X   X X X   B B B   X X X    X X X    X X X    XXX']
lev_list.append(level_18)

level_19 = [
    '    X   X XX    XXX  X XX XX   X X   X XX   XX XX XX   X',
    '    X   X XX    XTT  X XX XX   X X   X XX   XX XX XX   X',
    '    T   X XX    T    X XX XX   T X   X XX   TT XX XX   X',
    '        X XX         T XX XX     X   T TX      XX TT   T',
    '        T TT           TX TT     T      T      TT       ',
    '                BBB     T                               ',
    '    B           XXX                         BB          ',
    '    X     BB    XXX            B     B B    XX    BB   B',
    '    X     XX    XXX  B B  BB   X     X XB   XX BB XX   X',
    '    X   B XX    XXX  X XB XX   X B   X XX   XX XX XX   X',
    '    X   X XX    XXX  X XX XX   X X   X XX   XX XX XX   X']
lev_list.append(level_19)

level_20 = [
    '    X     X    X    X  X     T  X       X',
    '    X     T    X    X  X        X       X',
    '    X          X    X  T        X       X',
    '    T          T    X           T       X',
    '                    T                   T ',
    '                                         ',
    '          B                  B          B',
    '          X    B             X          X',
    '    B     X    X       B     X  B       X',
    '    X     X    X    B  X     X  X       X',
    '    X     X    X    X  X     X  X       X']
lev_list.append(level_20)

# set up level select screen
# for all the levels in the level list, render that level's number and get rectangle
for selection in range(1, len(lev_list) + 1):
    level_text = fontL.render(str(selection), True, colour)
    level_rect = level_text.get_rect()
    # check if the new level button needs to be on a new line (Level_counter starts at -3 on first run)
    level_counter += 1
    if level_counter > 2:
        # add y
        selection_y += 150
        # reset level_counter
        level_counter = -2
    # do math to center the rectangle on the right y and x based on amount of previous numbers
    level_rect.center = (600 + (level_counter * 225), selection_y)
    # add to level text list
    level_text_list.append([level_text, level_rect])

# game function


def gaming_func(lev, lev_offset, bg_offset, jump, vel, d, u, score):

    # while playing the game
    game = True
    wait = True
    pause = False

    # reset glide
    glide = False

    # set y value
    y = len(lev) * 64 / 2
    # calculate the height of the screen
    screen_y = (len(lev)) * 64
    # scale screen
    pygame.display.set_mode((1200, screen_y))

    # calculate total characters (length) in level
    length = len(lev[0]) * 64 + 50

    # reset variables for character image
    sprite_change = 0
    current_player = 0
    char = player_sprite_list[0]

    # create pause text for level
    pause_level_text = fontL.render(("level " + str(level_possibility + 1)), True, colour)
    pause_level_text_rect = pause_level_text.get_rect()
    pause_level_text_rect.center = (600, 350)

    # load new music
    mixer.music.load('game_music.wav')

    while game:
        # limit fps
        clock.tick(120)

        # player input (Quit, Space)
        # if the game closes
        for w in pygame.event.get():
            if w.type == pygame.QUIT:
                # quit the game
                result = "3"
                return result, bg_offset, y, score, current_player
            # if key is pressed
            if w.type == pygame.KEYDOWN:
                # if key is pressed
                if w.key == pygame.K_SPACE:
                    # reset the down value
                    d = 0
                    # start the jump mechanic
                    jump = True
                # turn on pause, reset glide
                elif w.key == pygame.K_ESCAPE:
                    pause = True
                    glide = False
                # turn on glide
                elif w.key == pygame.K_g:
                    glide = True
            # if key is lifted
            if w.type == pygame.KEYUP:
                # if the key is space
                if w.key == pygame.K_SPACE:
                    # reset the up value
                    u = -10
                    # stop the jump mechanic
                    jump = False
                if w.key == pygame.K_g:
                    glide = False
            # if mouse is pressed
            if w.type == pygame.MOUSEBUTTONDOWN:
                pos = w.pos
                # turn on pause, reset glide
                if pause_text_rect.collidepoint(pos):
                    print("did")
                    pause = True

        # reset the collision lists
        body_list = []
        top_list = []
        bottom_list = []

        # blit the background
        screen.blit(game_background, (0 + bg_offset, 0))

        # jump/fall mechanic
        # if jumping
        if jump:
            # count amounts for image, if 3, reset and change image
            sprite_change += 1
            if sprite_change == 3:
                sprite_change = 0
                # if already at highest image
                if current_player == 6:
                    pass
                # change image
                else:
                    current_player += 1
                    char = player_sprite_list[current_player]

            # if the up value is less than 6, add 0.4 (for parabola)
            if u <= 8:
                u += 0.4
            # if the up value is larger than 4, reset it back to -10 (for the parabola)
            elif u > 6:
                u = -10
            # change the player's y based on up value
            y -= (vel + u ** 2) / 12.5

        elif glide:
            y += 0.2
            # count amounts for image
            sprite_change += 1
            if sprite_change == 3:
                sprite_change = 0
                if current_player == 0:
                    pass
                # change image
                else:
                    current_player -= 1
                    char = player_sprite_list[current_player]

        # if not jumping (gravity)
        else:
            # count amounts for image, if 3, reset and change image
            sprite_change += 1
            if sprite_change == 3:
                sprite_change = 0
                # if already at highest image
                if current_player == 0:
                    pass
                else:
                    current_player -= 1
                    char = player_sprite_list[current_player]

            # if the down value is less than ten, add 0.4 (for increasing the rate of fall
            if d < 10:
                d += 0.4
            # change the player's y based on down value
            y += vel * d / 9

        # generate the level
        # read the level map to see how many strings it has
        for i in range(len(lev)):
            # find the column's base y
            # read the amount of characters in one of the strings
            total_characters = len(lev[i])
            # identify the type of character in the string
            for r in range(total_characters):
                # set up where the character will blit (including scroll)
                placement = 64 * r + lev_offset
                # get the character
                character = lev[i][r]
                # if the character is a space
                if character == ' ':
                    pass
                # if the character is an X (Body of pipe)
                if character == 'X':
                    # blit a pipe body
                    column_y = 64 * i
                    screen.blit(body, (placement, column_y))
                    # get the character's rectangle, center it
                    body_rect = body.get_rect()
                    body_rect.topleft = (placement, column_y)
                    # add rectangle to body's collision list
                    body_list.append(body_rect)
                # if the character is a T (Top of pipe)
                elif character == 'T':
                    # follow lines 616 - 623, change "Body" to "Top"
                    column_y = 64 * i
                    screen.blit(top, ((placement - 8), column_y))
                    top_rect = top.get_rect()
                    top_rect.topleft = (placement, column_y)
                    top_list.append(top_rect)
                # if the character is a B (Bottom of pipe)
                elif character == 'B':
                    # follow lines 616 - 623, change "Body" to "Bottom"
                    column_y = 64 * i
                    screen.blit(bottom, ((placement - 8), column_y))
                    bottom_rect = bottom.get_rect()
                    bottom_rect.topleft = (placement, column_y)
                    bottom_list.append(bottom_rect)

        # foreground and background scrolling
        lev_offset -= 1.5
        # if the background has scrolled to the end of the level, stop scrolling
        if bg_offset <= -100:
            pass
        # if the background has not scrolled to the end of the level
        else:
            # move the background left
            bg_offset -= 0.05

        # boundaries
        # if the player is at the top of the screen, stop them
        if y <= 0:
            y = 0
        # if the player is at the bottom of the screen, stop them
        elif y >= 700 - 32:
            y = 700 - 32

        # player collision
        # get player rectangle, center it
        player_rect = char.get_rect()
        player_rect.topleft = (100, y)

        # if player's rect collides with any of the body rectangles
        for i in body_list:
            if player_rect.colliderect(i):
                # set result to death
                results = "2"
                return results, bg_offset, y, score, current_player
        for i in top_list:
            if player_rect.colliderect(i):
                # set result to death
                results = "2"
                return results, bg_offset, y, score, current_player
        for i in bottom_list:
            if player_rect.colliderect(i):
                # set result to death
                results = "2"
                return results, bg_offset, y, score, current_player

        # check if player has won
        if abs(lev_offset) >= length:
            results = "1"
            return results, bg_offset, y, score, current_player, u

        # update score
        score += 1

        # blit pause button
        screen.blit(pause_text, pause_text_rect)

        # blit character
        screen.blit(char, (100, y))

        # update display
        pygame.display.update()

        # pause the game so player can get ready
        while wait:
            # for every event, check for space
            for event_wait in pygame.event.get():
                # if game is quit, return and quit
                if event_wait.type == pygame.QUIT:
                    result = "3"
                    return result, bg_offset, y, score, current_player
                # if a key is pressed, check if it was space
                if event_wait.type == pygame.KEYDOWN:
                    if event_wait.key == pygame.K_SPACE:
                        # turn off wait
                        wait = False
                        # play music
                        mixer.music.play(-1)

            # display text
            screen.blit(start_text, start_text_rect)

            # update screen
            pygame.display.update()

        # pause loop
        while pause:

            # get event
            for w in pygame.event.get():
                if w.type == pygame.QUIT:
                    # stop the game
                    result = "3"
                    return result, bg_offset, y, score, current_player
                # if escape is pressed, resume the game
                if w.type == pygame.KEYDOWN:
                    if w.key == pygame.K_ESCAPE:
                        pause = False
                # if mouse is clicked
                if w.type == pygame.MOUSEBUTTONDOWN:
                    pos = w.pos
                    # if level selection text is pressed, end the function
                    if restart_text_rect.collidepoint(pos):
                        result = "4"
                        return result, bg_offset, y, score, current_player
                    # if pause button is clicked, turn off pause
                    elif pause_text_rect.collidepoint(pos):
                        pause = False

            # blit background
            screen.blit(game_background, (0 + bg_offset, 0))
            # blit pause button
            screen.blit(pause_text, pause_text_rect)
            # blit character
            screen.blit(char, (100, y))
            # blit level text
            screen.blit(pause_level_text, pause_level_text_rect)
            # blit return to selection text
            screen.blit(selection_text, selection_text_rect)

            # update display
            pygame.display.update()


# overall game loop
while overall_game:

    # splash screen loop
    while splashing:

        # set frame rate
        clock.tick(120)

        # turn on music if not already on
        if not music:
            # play music
            mixer.music.play(-1)
            music = True

        # get event for every frame
        for event in pygame.event.get():
            # if the game is quit
            if event.type == pygame.QUIT:
                splashing = False
                overall_game = False
            # if key is pressed down, go to level select screen
            if event.type == pygame.KEYDOWN:
                splashing = False
                level_select = True
            # if the mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                # get mouse pos, check if on options text
                mouse_pos = event.pos
                if options_text_rect.collidepoint(mouse_pos):
                    options = True

        # Pan the screen left and right
        # left
        if left:
            # add to the splash screen's x
            splash_x -= 0.2
            # add splash screen to the screen update
            screen.blit(splash, (splash_x, 0))
            # if splash screen's x = 0, move it right.
            if splash_x <= -50:
                left = False
                right = True

        # right (refer to lines 793-801)
        if right:
            splash_x += 0.2
            screen.blit(splash, (splash_x, 0))
            # if splash screen's x =-100, move it left
            if splash_x >= 0:
                right = False
                left = True

        # blit text
        screen.blit(title, (splash_x + 100, 450))
        screen.blit(press, (splash_x + 500, 240))
        screen.blit(options_text, options_text_rect)

        # update display
        pygame.display.update()

        # while options screen is on
        while options:
            # get event
            for event in pygame.event.get():
                # if game is quit
                if event.type == pygame.QUIT:
                    options = False
                    splashing = False
                    overall_game = False
                # if event is keyboard down, check if escape and end options
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        options = False
                # if mouse is clicked, get pos and check if it hit delete box
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse position
                    mouse_pos = event.pos
                    # if any of the volume buttons are clicked, set to respective volume
                    if volume_sprite_list[0][1].collidepoint(mouse_pos):
                        kaboom.set_volume(0)
                        pygame.mixer.music.set_volume(0)
                    if volume_sprite_list[1][1].collidepoint(mouse_pos):
                        kaboom.set_volume(0.3)
                        pygame.mixer.music.set_volume(0.3)
                    if volume_sprite_list[2][1].collidepoint(mouse_pos):
                        kaboom.set_volume(1)
                        pygame.mixer.music.set_volume(1)
                    # if delete all save data text is clicked
                    if delete_text_rect.collidepoint(mouse_pos):
                        # turn on last chance loop
                        final_chance = True
                        # pause music
                        mixer.music.pause()
                        # final chance loop
                        while final_chance:
                            # get event
                            for event_1 in pygame.event.get():
                                # if game is quit
                                if event_1.type == pygame.QUIT:
                                    final_chance = False
                                    options = False
                                    splashing = False
                                    overall_game = False
                                # if event is keyboard down, check if escape and end final chance
                                if event_1.type == pygame.KEYDOWN:
                                    if event_1.key == pygame.K_ESCAPE:
                                        # play music
                                        mixer.music.play(-1)
                                        final_chance = False
                                # if mouse is clicked, get pos and check if it hit the text
                                if event_1.type == pygame.MOUSEBUTTONDOWN:
                                    mouse_pos = event_1.pos
                                    if are_you_sure_text_rect.collidepoint(mouse_pos):
                                        # delete all save data
                                        with open("level_completion.txt", "w") as file_object:
                                            file_object.close()
                                        with open("scores.txt", "w") as file_object:
                                            file_object.close()
                                        # play music
                                        mixer.music.play(-1)
                                        # return to splash screen
                                        final_chance = False
                                        options = False

                            # blit background
                            screen.fill((255, 255, 255))

                            # blit are you sure text
                            screen.blit(are_you_sure_text, are_you_sure_text_rect)

                            # update display
                            pygame.display.update()

                    # if controls rect is selected, start controls
                    if controls_text_rect.collidepoint(mouse_pos):
                        controls = True
                        while controls:
                            for event_1 in pygame.event.get():
                                if event_1.type == pygame.QUIT:
                                    controls = False
                                    options = False
                                    splashing = False
                                    overall_game = False
                                if event_1.type == pygame.KEYDOWN:
                                    if event_1.key == pygame.K_ESCAPE:
                                        controls = False

                            # blit background
                            screen.blit(splash, (splash_x, 0))

                            # blit controls text
                            screen.blit(controls_text, controls_text_rect)

                            # blit jump text
                            screen.blit(jump_text, jump_text_rect)

                            # blit glide text
                            screen.blit(glide_text, glide_text_rect)

                            # blit escape text
                            screen.blit(escape_text, escape_text_rect)

                            pygame.display.update()

            # blit background
            screen.blit(splash, (splash_x, 0))

            # blit delete text
            screen.blit(delete_text, delete_text_rect)

            # blit volume text
            screen.blit(volume_text, volume_text_rect)

            # blit volume buttons
            for sprite in volume_sprite_list:
                screen.blit(sprite[0], sprite[1])

            # blit control text
            screen.blit(controls_text, controls_text_rect)

            # update display
            pygame.display.update()

    # level select loop
    while level_select:

        # if music is not playing, play music
        if not music:
            mixer.music.play(-1)
            music = True

        # reset selected variable
        selected = False

        # check if level_1 is accesable at all times
        with open('level_completion.txt', 'r+') as file_object:
            # go through each line in file, strip new line
            for line in file_object:
                line = line.rstrip('\n')
                # if level_1 exists, close the file
                if line == "level_1":
                    close_file = True
                    file_object.close()
                    break
            # if file needs to be closed
            if close_file:
                close_file = False
                pass
            # if file needs to be written on
            else:
                # write level_1 so it is accesable
                file_object.write("level_1\n")
                # close file
                file_object.close()

        # reset available levels
        available_level_list = []

        # open level_completion file to check if a level has been beat
        with open('level_completion.txt', 'r') as file_object:
            # for every line in the file, strip the new line
            for line in file_object:
                line = line.rstrip('\n')
                # go through each item in the level list
                for item in range(1, len(lev_list)+1):
                    # if the level in the list is in the file, add it to the available levels list, so it can be played
                    if "level_" + str(item) == line:
                        available_level_list.append(level_text_list[item - 1])
                        break
            # close the file
            file_object.close()

        # if the level hasn't been selected, get events
        if not selected:
            for event in pygame.event.get():
                # quit the game
                if event.type == pygame.QUIT:
                    level_select = False
                    overall_game = False
                # if escape is clicked, end slection screen and go back to splash
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        selected = True
                        level_select = False
                        splashing = True
                # if mouse is clicked, get the position
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # reset level possibility
                    level_possibility = -1
                    # if a level is selected, turn on that level
                    for button in available_level_list:
                        level_possibility += 1
                        if button[1].collidepoint(mouse_pos):
                            level = lev_list[level_possibility]
                            level_select = False
                            gaming = True
                            mixer.music.pause()
                            break

            # blit select background
            screen.blit(select_background, (0, 0))

            # blit available select buttons
            for button in available_level_list:
                screen.blit(button[0], button[1])

            # update display
            pygame.display.update()

    # gaming loop
    while gaming:

        # play the game, get results in function
        game_results = list(gaming_func(level, offset, background_offset, new_jump, velocity, down, up, Score))

        # reset the screen
        screen = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)

        # get score
        Score = game_results[3]
        Score = str(Score)

        # get high score, save current score
        # writing the document
        with open('scores.txt', 'a') as file_object:
            # write a new line and the score
            file_object.write(Score + '\n')
            # close the writing document
            file_object.close()
        # reading the document
        with open('scores.txt', 'r') as file_object:
            # read the line in a for loop
            for line in file_object:
                # make int value
                line = line.rstrip('\n')
                new_line = int(line)
                # check if the new score is the high core
                if new_line > high_score:
                    high_score = new_line
                else:
                    pass
            # close the file
            file_object.close()

        # render and center the Score text
        Score_text = "Score: " + Score
        score_text = fontS.render(Score_text, True, colour)
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (600, 425)

        # render and center the High Score text
        high_score_text = "High Score: " + Score
        high_score_text = fontS.render(high_score_text, True, colour)
        high_score_text_rect = high_score_text.get_rect()
        high_score_text_rect.center = (600, 425)

        # get character sprite, and set up character change value
        player = game_results[4]
        current_character = player_sprite_list[player]
        sprite_change_val = 0

        # if the player has won
        if game_results[0] == "1":

            # open the completed levels text
            with open('level_completion.txt', 'r+') as file_object:
                # go through each line in the file, remove the new line
                for line in file_object:
                    line = line.rstrip('\n')
                    # if the next level is already unlocked, close the file
                    if "level_"+str(level_possibility + 2) == line:
                        close_file = True
                        file_object.close()
                        break
                # if file should be closed, reset check variable
                if close_file:
                    close_file = False
                # if the file needs to have the next level added, append it and close the file
                else:
                    file_object.write("level_" + str(level_possibility + 2) + '\n')
                    file_object.close()

            # turn on win loop
            win = True

            # get player y
            player_y = game_results[2]
            player_x = 100

            # get current jumping value
            up = game_results[5]

            # turn off music
            mixer.music.stop()
            music = False

            # play win sound
            mixer.music.load('win.wav')
            mixer.music.play(1)

            # win loop
            while win:

                # limit fps
                clock.tick(100)

                # if the game is quit
                for event in pygame.event.get():
                    # turn everything off and quit
                    if event.type == pygame.QUIT:
                        win = False
                        gaming = False
                        overall_game = False
                    # if mouse is clicked, get position
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = event.pos
                        # if select text is clicked
                        if selection_text_rect.collidepoint(mouse_pos):
                            if level_possibility + 1 == 20:
                                # stop music
                                mixer.music.stop()
                                end_cutscene = True
                                fade_in = True
                                fade_out = False
                                win = False
                                gaming = False
                            else:
                                # reset game dependant variables
                                high_score = 0
                                down = 0
                                up = -10
                                Score = 0
                                offset = 0
                                background_offset = 0
                                player_y = 300
                                # reset music
                                mixer.music.stop()
                                music = False
                                mixer.music.load('splash_level_select.wav')
                                # turn off win
                                win = False
                                check = True
                                gaming = False
                                level_select = True

                # blit background
                screen.blit(game_background, (0 + game_results[1], 0))

                # blit win over text
                screen.blit(win_text, win_text_rect)

                # blit restart text
                screen.blit(selection_text, selection_text_rect)

                if high_score > int(Score):
                    # blit score text
                    screen.blit(score_text, score_text_rect)
                else:
                    # blit score text
                    screen.blit(high_score_text, high_score_text_rect)

                # count amounts for image
                sprite_change_val += 1
                if sprite_change_val == 3:
                    sprite_change_val = 0
                    if player == 6:
                        pass
                    else:
                        player += 1
                        current_character = player_sprite_list[player]

                # if the up value is less than 6, add 0.4 (for parabola)
                if up <= 8:
                    up += 0.4
                # if the up value is larger than 4, reset it back to -10 (for the parabola)
                elif up > 6:
                    up = -10
                    current_character = player_sprite_list[0]
                # change the player's y based on up value
                player_y -= (velocity + up ** 2) / 12.5

                # change players x
                player_x += 3

                # blit the character
                screen.blit(current_character, (player_x, player_y))

                # update display
                pygame.display.update()

        # if the player has lost
        elif game_results[0] == "2":

            # reset explosion variables for sound effect/explosion
            blow_up = 0
            current_explosion = explosion_sprite_list[0]

            # turn off music
            mixer.music.stop()
            music = False

            # play lose music
            mixer.music.load('lose.wav')
            mixer.music.play(1)

            # turn on death, get player's y
            death = True
            player_y = game_results[2]

            while death:
                check = False

                # limit fps for faster performance
                clock.tick(120)

                # get event
                for event in pygame.event.get():
                    # if the game is quit
                    if event.type == pygame.QUIT:
                        death = False
                        gaming = False
                        overall_game = False
                    # if the mouse is clicked
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # get mouse position
                        mouse_pos = event.pos
                        # if restart button is clicked
                        if restart_text_rect.collidepoint(mouse_pos):
                            # reset game dependant variables
                            high_score = 0
                            down = 0
                            up = -10
                            Score = 0
                            offset = 0
                            background_offset = 0
                            player_y = 300
                            # turn off death
                            death = False
                            check = True
                            level_select = True
                            explosion = 0
                            explosion_change_val = 0
                            sprite_change_val = 0
                            explosion_graphic = False
                            # reset music
                            mixer.music.load('splash_level_select.wav')

                # if the game should not be closed
                if not check:

                    # blit background
                    screen.blit(game_background, (0 + game_results[1], 0))

                    # blit game over text
                    screen.blit(death_text, death_text_rect)

                    # if there is no high score
                    if high_score > int(Score):
                        # blit score text
                        screen.blit(score_text, score_text_rect)
                    # if there is a new high score
                    else:
                        # blit score text
                        screen.blit(high_score_text, high_score_text_rect)

                    # blit restart text
                    screen.blit(restart_text, restart_text_rect)

                    # make the player fall
                    # if the down value is less than ten, add 0.4 (for increasing the rate of fall)
                    if down < 10:
                        down += 0.4
                    # change the player's y based on down value
                    player_y += velocity * down / 9

                    # if the player is at the bottom
                    if player_y >= 672:
                        blow_up += 1
                        # if blow up has just began, start the explosion graphics and sound
                        if blow_up == 1:
                            explosion_graphic = True
                            kaboom.play()
                    # blit the current player
                    else:
                        screen.blit(current_character, (100, player_y))

                    # change player image
                    sprite_change_val += 1
                    # if the sprite needs to be changed, change and reset
                    if sprite_change_val == 3:
                        sprite_change_val = 0
                        # if there is no more sprites
                        if player == 0:
                            pass
                        # if there is still more sprites, change it
                        else:
                            player -= 1
                            current_character = player_sprite_list[player]

                    # change explosion image
                    if explosion_graphic:
                        # count to 20, change graphic, reset explosion_change_val
                        explosion_change_val += 1
                        if explosion_change_val == 20:
                            explosion_change_val = 0
                            explosion += 1
                            # if on the last graphic, stop blitting it
                            if explosion == 6:
                                explosion_graphic = False
                        # set current explosion graphic
                        else:
                            current_explosion = explosion_sprite_list[explosion]

                        # blit current explosion
                        screen.blit(current_explosion, (50, 475))

                    # update display
                    pygame.display.update()

            # turn off gaming
            gaming = False

        # if the game has quit
        elif game_results[0] == "3":
            gaming = False
            overall_game = False

        # if the level has been quit
        elif game_results[0] == "4":
            gaming = False
            level_select = True
            # reset game dependant variables
            high_score = 0
            down = 0
            up = -10
            Score = 0
            offset = 0
            background_offset = 0
            player_y = 300
            death = False
            check = True
            explosion = 0
            explosion_change_val = 0
            sprite_change_val = 0
            explosion_graphic = False
            # stop and reset music
            mixer.music.pause()
            mixer.music.load('splash_level_select.wav')
            music = False

    # ending cutscene
    while end_cutscene:
        # get event, if quit, close game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_cutscene = False
                overall_game = False
                gaming = False

        # while the game fades in, add one to fade
        if fade_in:
            fade += 1
            # if the fade is at its max, reverse it
            if fade == 2000:
                fade_out = True
                fade_in = False
        # while the game fades out, remove one from fade
        if fade_out:
            fade -= 1
            if fade == 0:
                # reset all variables, restart game
                high_score = 0
                down = 0
                up = -10
                Score = 0
                offset = 0
                background_offset = 0
                player_y = 300
                fade_in = True
                fade_out = False
                end_cutscene = False
                gaming = False
                splashing = True
                # reload music
                mixer.music.load('splash_level_select.wav')
                music = False

        # get what fade is, change fade according to how much the value is for timing
        if fade < 300:
            alpha = 255 * (fade / 300)
        elif 300 <= fade <= 200:
            alpha = 255

        # reset the screen
        screen.fill(colour)

        # set transparency and blit background
        ending_background.set_alpha(alpha)
        screen.blit(ending_background, (0, 0))

        # update display
        pygame.display.update()
