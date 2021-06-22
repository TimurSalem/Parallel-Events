from first_engine.game import Game
from first_engine import object

import pygame
from pygame.locals import *
import random


class FirstGame(Game):
    def run(self):

        pygame.init()

        riz = pygame.display.set_mode(pygame.display.list_modes()[0])

        monitor_size = [pygame.display.Info().current_w, pygame.display.Info().current_h]
        screen = pygame.display.set_mode((1200, 700), pygame.RESIZABLE)

        health = 460

        temp = 0

        hero = object.Character(self.surface, speed=2, color=(45, 85, 85), width=100, height=100, x=1230, y=750)

        platform_1 = object.Barrier(self.surface, objects=[hero], width=200, height=50, x=-8000, y=-10000)
        platform_2 = object.Barrier(self.surface, objects=[hero], width=200, height=50, x=-1000, y=-200)
        fon_start = object.Barrier(self.surface, objects=[hero], width=200, height=50, x=0, y=0)

        meteor = object.Barrier(self.surface, objects=[hero], width=200, height=200, x=100, y=450)
        meteor_2 = object.Barrier(self.surface, objects=[hero], width=200, height=200, x=1500, y=1000)
        gui_substrate = object.Object(parent=self.surface, width=500, height=240, x=0, y=0, color=(30, 30, 40))
        gui_substrate_2 = object.Object(parent=self.surface, width=770, height=340, x=0, y=1260, color=(30, 30, 40))
        gui_substrate_3 = object.Object(parent=self.surface, width=730, height=100, x=20, y=1440, color=(20, 20, 30))
        gui_substrate_4 = object.Object(parent=self.surface, width=20, height=100, x=115, y=1440, color=(30, 30, 40))
        gui_substrate_5 = object.Object(parent=self.surface, width=20, height=100, x=240, y=1440, color=(30, 30, 40))
        gui_substrate_6 = object.Object(parent=self.surface, width=20, height=100, x=365, y=1440, color=(30, 30, 40))
        gui_substrate_7 = object.Object(parent=self.surface, width=460, height=100, x=20, y=120, color=(20, 20, 30))
        gui_substrate_8 = object.Object(parent=self.surface, width=20, height=100, x=480, y=1440, color=(30, 30, 40))
        gui_substrate_9 = object.Object(parent=self.surface, width=20, height=100, x=595, y=1440, color=(30, 30, 40))
        gui_substrate_10 = object.Object(parent=self.surface, width=20, height=100, x=710, y=1440, color=(30, 30, 40))

        moon = object.Barrier(self.surface, objects=[hero], width=200, height=200, x=565, y=220)

        distante_vision = object.Object(parent=self.surface, width=2500, height=2500, x=2430, y=250, color=(0, 0, 0))

        enemie = object.Character(self.surface, speed=2, color=(20, 5, 40), width=160, height=160, x=2430, y=250)

        gui_shop_3_st = object.Object(parent=self.surface, width=310, height=310, x=180, y=210, color=(30, 30, 40))
        gui_shop_esc = object.Object(parent=self.surface, width=60, height=60, x=110, y=60, color=(40, 40, 50))

        dest_x_enemie = hero.body.centerx
        dest_y_enemie = hero.body.centerx

        # bullet = object.Barrier(parent=self.surface, objects=[meteor], width=60, height=60, x=1265, y=835, color=(255, 0, 30))

        cursor_coor = (1, 1)

        weap = False

        speed_bulet = 8

        cof = 1

        cooldown = 0

        enemi_cooldown = 0

        bullets_move = [object.Barrier(parent=self.surface, objects=[meteor, meteor_2], width=60, height=60, x=1265, y=835, color=(255, 0, 30))]

        bullets_right = [object.Barrier(parent=self.surface, objects=[meteor, meteor_2], width=60, height=60, x=1265, y=835, color=(255, 0, 30))]
        bullets_left = [object.Barrier(parent=self.surface, objects=[meteor, meteor_2], width=60, height=60, x=1265, y=835, color=(255, 0, 30))]

        bullets_enemie_right = [object.Barrier(parent=self.surface, objects=[meteor, meteor_2], width=60, height=60, x=1265, y=835,
                                        color=(255, 0, 30))]
        bullets_enemie_left = [object.Barrier(parent=self.surface, objects=[meteor, meteor_2], width=60, height=60, x=1265, y=835,
                                       color=(255, 0, 30))]

        speeds_x = []
        speeds_y = [0]
        speeds_enemie_y = [0]

        r = False

        sprite_ship = './sprites/govno.png'
        e_ship = './sprites/govno.png'
        sprite_ship2 = './sprites/govno5.png'

        fon = './sprites/fon_game.png'
        fon2 = './sprites/fon_game.jpg'

        space_ship = './sprites/Ships/4/Pattern1/Red/Left/1.png'
        space_hero_ship_right = './sprites/Ships/1/Pattern2/Yellow/Right/1.png'
        space_hero_ship_left = './sprites/Ships/1/Pattern2/Yellow/Right/1.png'
        bullets_hero_sprite = './sprites/bullets_hero.png'
        bullets_enemie_sprite = './sprites/bullets_enemie.png'
        bullets_hero_sprite2 = './sprites/bullets_hero_2.png'
        bullets_enemie_sprite2 = './sprites/bullets_enemie_2.png'

        meteor_sprite = './sprites/meteor_1.png'
        meteor_sprite_2 = './sprites/meteor_2.png'

        enemie.load_sprites(name='explosion_enemie', path='./sprites/explosion/', update=3)
        hero.load_sprites(name='explosion', path='./sprites/explosion/', update=3)
        hero.load_sprites(name='motion_right', path='./sprites/Ships/1/Pattern2/Yellow/Right/', update=7)
        hero.load_sprites(name='motion_left', path='./sprites/Ships/1/Pattern2/Yellow/Left/', update=7)
        # moon.load_sprites(name='moon_animation', path='./Moon/', update=10)


        platform_1.skin = pygame.image.load(fon)
        platform_2.skin = pygame.image.load(fon2)
        fon_start.skin = pygame.image.load(fon2)
        hero.skin = pygame.image.load(space_hero_ship_right)
        enemie.skin = pygame.image.load(space_ship)
        meteor.skin = pygame.image.load(meteor_sprite)
        meteor_2.skin = pygame.image.load(meteor_sprite_2)
        # meteor.skin = pygame.image.load(space_ship)


        t = False
        r = False

        s = False
        m = False

        speed_x = 22
        speed_y = 22

        speed_enemie_x = 12
        speed_enemie_y = 12

        dest_x = 0
        dest_y = 0

        delta_x = 0
        delta_y = 0

        count_up = 0

        x = 10
        y = 10

        q = 0

        p = False

        timer = 80

        time = 0

        score = 0

        speed_bulet_y = 1
        speed_bulet_x = 1

        i: int = 0
        shot_sound = pygame.mixer.Sound('sci-fi_shot_sound.wav')
        click_sound = pygame.mixer.Sound('click_sound.wav')

        win_sound = pygame.mixer.Sound('sci-fi_win_sound.wav')
        explosion_sound = pygame.mixer.Sound('explosion_sound.mp3')


        pygame.mixer.music.load('Checking Manifest.mp3')
        pygame.mixer.music.set_volume(1)
        pygame.mixer.music.play(-1)

        fullscreen = False

        # def print_text(message, x, y, font_color=(255, 255, 255), font='spacefont.otf', font_size=30):
        #     font = pygame.font.Font(font, font_size)
        #     text = font.render(message, True, font_color)
        #     pygame.Surface.blit(text, (x, y))

        cash = 0



        f_start = pygame.font.Font('SpaceFont.ttf', 200)
        f = pygame.font.Font('SpaceFont.ttf', 100)
        f_menu = pygame.font.Font('SpaceFont.ttf', 50)
        f_temp = pygame.font.Font('SpaceFont.ttf', 70)
        f_cash = pygame.font.Font('SpaceFont.ttf', 30)

        sc_text = f.render('Health', True, (255, 255, 255))
        sc_text_menu = f_menu.render('Press SPACE to open menu', True, (255, 255, 255))

        sc_text_temp = f_temp.render('Перегрев', True, (250, 150, 0))
        sc_text_temp_bar = f.render('Temperathure', True, (255, 255, 255))
        sc_text_start = f_start.render('Parallel Events', True, (255, 255, 255))

        peregrev = False

        enemie_health = 230

        angle = 0

        color_temp = (250, 150, 0)

        direction_y = random.randint(1, 6)
        direction_x = (random.randint(1, 6) - direction_y)

        game_ov = False

        tim = 0

        timer_death = 0

        exp = False

        end = False

        text_start_y = 120
        text_start_x = 180

        text_start_size = 100

        color_start_button = (30, 30, 40)
        color_shop_button = (30, 30, 40)

        death = False

        shop = False

        start_menu = True

        cooldown_hero = 20

        choose_bullets = 0

        hero_damage = 20

        game_over = True
        while self.RUNNER:
            if start_menu == True:
                gui_start = object.Object(parent=self.surface, width=300, height=140, x=440, y=340, color=color_start_button)
                gui_shop = object.Object(parent=self.surface, width=300, height=140, x=440, y=500, color=color_shop_button)

                platform_2.blit()
                gui_start.blit()
                gui_shop.blit()

                # moon.blit()

                # moon.play_animation(action='moon_animation')

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                # pygame.mixer.music.pause()

                f_start = pygame.font.Font('SpaceFont.ttf', text_start_size)
                sc_text_start = f_start.render('Parallel Events', True, (255, 255, 255))
                sc_text_start_game = f_temp.render('START', True, (255, 255, 255))
                sc_text_start_shop = f_temp.render('Shop', True, (255, 255, 255))

                self.surface.blit(sc_text_start, (text_start_x, text_start_y))
                self.surface.blit(sc_text_start_game, (490, 370))
                self.surface.blit(sc_text_start_shop, (510, 530))

                self.set_capture('Parallel Events')

                self.set_icon('ole.png')

                if text_start_y > 60:

                    text_start_y -= 2

                self.display_update()

                # if gui_start.body.x < click[0] < gui_start.body.right:
                #     if gui_start.body.y < click[1] < gui_start.body.bottom:
                #         game_over = False


                for event in self.events():
                    print(event)  # отслеживание событий
                    self.close(event)
                    if gui_start.body.x < mouse[0] < gui_start.body.right:
                        if gui_start.body.y < mouse[1] < gui_start.body.bottom:
                            color_start_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)

                                game_over = False
                                start_menu = False
                                screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)


                        else:
                            color_start_button = (30, 30, 40)
                    else:
                        color_start_button = (30, 30, 40)

                    if gui_shop.body.x < mouse[0] < gui_shop.body.right:
                        if gui_shop.body.y < mouse[1] < gui_shop.body.bottom:
                            color_shop_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)

                                shop = True
                                start_menu = False
                                # screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)


                        else:
                            color_shop_button = (30, 30, 40)
                    else:
                        color_shop_button = (30, 30, 40)


                    if event.type == 768:
                        game_over = False
                        start_menu = False

            if shop == True:
                mouse = pygame.mouse.get_pos()

                gui_shop_list = object.Object(parent=self.surface, width=1000, height=600, x=100, y=50, color=(50, 50, 60))
                gui_shop_1 = object.Object(parent=self.surface, width=1000, height=80, x=100, y=50, color=(60, 60, 70))
                gui_shop_2 = object.Object(parent=self.surface, width=1000, height=30, x=100, y=130, color=(40, 40, 50))
                gui_shop_3 = object.Object(parent=self.surface, width=300, height=300, x=180, y=210, color=(40, 40, 50))
                gui_shop_4 = object.Object(parent=self.surface, width=300, height=300, x=720, y=210, color=(40, 40, 50))
                gui_shop_ch_1 = object.Object(parent=self.surface, width=500, height=60, x=100, y=130, color=(40, 40, 50))
                gui_shop_ch_2 = object.Object(parent=self.surface, width=500, height=40, x=600, y=130, color=(40, 40, 50))
                gui_shop_5 = object.Object(parent=self.surface, width=420, height=100, x=120, y=530, color=(40, 40, 50))
                gui_shop_6 = object.Object(parent=self.surface, width=420, height=100, x=660, y=530, color=(40, 40, 50))
                gui_tovar = object.Object(parent=self.surface, width=300, height=100, x=170, y=200, color=(40, 40, 50))
                gui_tovar_2 = object.Object(parent=self.surface, width=300, height=100, x=770, y=260, color=(40, 40, 50))
                gui_shop = object.Object(parent=self.surface, width=300, height=130, x=440, y=560,
                                         color=color_shop_button)

                gui_tovar.skin = pygame.image.load(bullets_hero_sprite2)
                gui_tovar_2.skin = pygame.image.load(bullets_enemie_sprite2)

                gui_shop_list.blit()
                gui_shop_1.blit()
                gui_shop_2.blit()
                gui_shop_3_st.blit()
                gui_shop_3.blit()
                gui_shop_4.blit()
                gui_shop_5.blit()
                gui_shop_6.blit()
                gui_tovar.blit()
                gui_shop_ch_1.blit()
                gui_shop_ch_2.blit()
                gui_tovar_2.blit()
                gui_shop_esc.blit()

                f_start = pygame.font.Font('SpaceFont.ttf', text_start_size)
                f_tovar = pygame.font.Font('SpaceFont.ttf', 38)
                # sc_text_start = f_start.render('Parallel Events', True, (255, 255, 255))
                # sc_text_start_game = f_temp.render('START', True, (255, 255, 255))
                sc_text_shop_tovar1 = f_tovar.render('плазменный сгусток', True, (255, 255, 255))
                sc_text_shop_tovar2 = f_tovar.render('Энтропийный разряд', True, (255, 255, 255))
                sc_text_shop_ch = f_tovar.render('Bullets', True, (255, 255, 255))
                sc_text_shop_ch2 = f_tovar.render('Ships', True, (255, 255, 255))
                sc_text_shop_shop = f_temp.render('Shop', True, (255, 255, 255))

                # self.surface.blit(sc_text_start, (text_start_x, text_start_y))
                self.surface.blit(sc_text_shop_shop, (520, 50))
                self.surface.blit(sc_text_shop_tovar1, (135, 557))
                self.surface.blit(sc_text_shop_tovar2, (672, 557))
                self.surface.blit(sc_text_shop_ch, (270, 140))
                self.surface.blit(sc_text_shop_ch2, (800, 130))

                if choose_bullets == 0:
                    bullets_hero_sprite = './sprites/bullets_hero.png'
                    cooldown_hero = 20
                    hero_damage = 20

                if choose_bullets == 1:
                    bullets_hero_sprite = './sprites/bullets_enemie.png'
                    cooldown_hero = 50
                    hero_damage = 50

                self.display_update()

                for event in self.events():
                    # print(event)  # отслеживание событий
                    self.close(event)


                    if gui_shop_ch_1.body.x < mouse[0] < gui_shop_ch_1.body.right:
                        if gui_shop_ch_1.body.y < mouse[1] < gui_shop_ch_1.body.bottom:
                            # color_start_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)
                                # gui_shop_ch_1.body.

                                choose_bullets = 0


                    if gui_shop_3.body.x < mouse[0] < gui_shop_3.body.right:
                        if gui_shop_3.body.y < mouse[1] < gui_shop_3.body.bottom:
                            # color_start_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)
                                gui_shop_3_st.body.x = 180

                                choose_bullets = 0

                    if gui_shop_4.body.x < mouse[0] < gui_shop_4.body.right:
                        if gui_shop_4.body.y < mouse[1] < gui_shop_4.body.bottom:
                            # color_start_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)
                                gui_shop_3_st.body.x = 720

                                choose_bullets = 1

                    if gui_shop_esc.body.x < mouse[0] < gui_shop_esc.body.right:
                        if gui_shop_esc.body.y < mouse[1] < gui_shop_esc.body.bottom:
                            # color_start_button = (20, 20, 33)
                            if event.type == 1025:
                                pygame.mixer.Sound.play(click_sound)
                                shop = False
                                start_menu = True


            if not game_over:

                angle += 1

                # pygame.mixer.music.play()

                meteor.body = meteor.skin.get_rect(topleft=(meteor.body.x, meteor.body.y))
                meteor_2.body = meteor_2.skin.get_rect(topleft=(meteor_2.body.x, meteor_2.body.y))
                sc_text_cash = f_start.render(str(cash), True, (30, 125, 105))

                if enemie_health < 0:
                    enemie_health = 0
                    exp = True

                if enemie_health == 230:
                    exp = False
                if exp == True:
                    enemie.play_animation('explosion_enemie')
                    tim += 1
                if tim == 3 * 21:
                    end = True
                    score += 500
                    pygame.mixer.Sound.play(explosion_sound)

                if tim == 350:
                    pygame.mixer.Sound.play(win_sound)

                if health <= 0:
                    health = 0
                    death = True

                if death == True:
                    hero.play_animation('explosion')
                    timer_death += 1

                if timer_death == 3 * 21:
                    pygame.mixer.Sound.play(explosion_sound)
                    game_over = True
                    start_menu = True
                    screen = pygame.display.set_mode((1200, 700),
                                                     pygame.RESIZABLE)



                # print(self.surface.get_size())
                # pygame.mixer.music.load('SoundTreck.mp3')
                # distante_vision.blit()
                hero.blit()
                if end == False:
                    enemie.blit()

                meteor.blit()
                meteor_2.blit()
                # moon.blit()

                gui_substrate_11 = object.Object(parent=self.surface, width=250, height=60, x=enemie.body.centerx - 80,
                                                 y=enemie.body.centery - 160, color=(30, 30, 40))
                gui_substrate_12 = object.Object(parent=self.surface, width=230, height=40,
                                                    x=enemie.body.centerx - 115,
                                                    y=enemie.body.centery - 150, color=(20, 20, 30))
                gui_enemi_healthbar = object.Object(parent=self.surface, width=enemie_health, height=40, x=enemie.body.centerx - 70,
                                                 y=enemie.body.centery - 150, color=(200, 0, 40))

                gui_tempbar = object.Object(parent=self.surface, width=temp, height=100, x=20, y=1440,
                                            color=color_temp)
                gui_healthbar = object.Object(parent=self.surface, width=health, height=100, x=20, y=120,
                                              color=(200, 0, 40))

                sc_text_score = f.render('Score - ' + str(score), True, (255, 255, 255))

                if end == False:
                    if enemie_health < 230:
                        gui_substrate_11.blit()
                        gui_enemi_healthbar.blit()
                gui_substrate_2.blit()
                gui_substrate_3.blit()
                gui_tempbar.blit()

                gui_substrate.blit()
                gui_substrate_7.blit()
                gui_healthbar.blit()
                self.surface.blit(sc_text, (70, 0))
                self.surface.blit(sc_text_score, (2030, 0))
                self.surface.blit(sc_text_temp_bar, (30, 1300))
                self.surface.blit(sc_text_cash, (2500, 200))

                gui_substrate_4.blit()
                gui_substrate_5.blit()
                gui_substrate_6.blit()
                gui_substrate_8.blit()
                gui_substrate_9.blit()
                gui_substrate_10.blit()

                self.cycle_init(FPS=300)

                print(hero.body.x)

                # Объекты
                platform_1.blit()

                meteor.resistance()

                # bullet.blit()

                if meteor.resistance() == True:
                    r = True

                distante_vision.body.centerx = enemie.body.centerx
                distante_vision.body.centery = enemie.body.centery


                # platform_2.blit()
                # platform_3.blit()
                # platform_4.blit()


                down_motion = 0
                left_motion = 0
                right_motion = 0

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                time += 1
                if temp > 0:
                    temp -= 0.3

                self.surface.blit(sc_text, (20, 0))
                self.surface.blit(sc_text_menu, (1930, 1540))
                self.set_capture('Parallel Events')
                self.set_icon('ole.png')


                # проверяем - уперся ли персонаж в преграду
                self.window_borders([hero])

                # если да, то даем ему возможность прыгать
                hero.action_jump()

                X = hero.body.x
                Y = hero.body.y


                # platform_1.body.y = motion_up

                # y_bul = bullet.body.y
                # x_bul = bullet.body.x

                tap_x = mouse[0] - 1280

                # if tap_x > 0:
                #     hero.skin = pygame.image.load(space_hero_ship_right)
                # if tap_x < 0:
                #     hero.skin = pygame.image.load(space_hero_ship_right)

                # pygame.draw.polygon(self.surface, color=(30, 30, 40), points=[(500, 240), (600, 0), (530, 100), (530, 220)])

            # SHOOTING

                print(gui_substrate.body)

                '''
                Основной код отвечающий за расчёт траектории
                '''
                if cooldown <= 0:
                    if click[0]:
                        if temp < 730:

                            temp += 20

                        pygame.mixer.Sound.play(shot_sound)

                        dest_x = mouse[0]
                        dest_y = mouse[1]
                        delta_x = dest_x - 1250
                        count_up = delta_x // speed_x
                        delta_y = 800 - dest_y

                        if -0.1 < count_up < 0.1:
                            count_up = 0.1

                        speed_y = delta_y / count_up
                        weap = True
                        bullet = object.Barrier(parent=self.surface, objects=[], width=60, height=60, x=hero.body.centerx- 120, y=hero.body.y - 20, speed_x=speed_x, speed_y=speed_y, color=(255, 0, 30))
                        if tap_x > 0:
                            bullets_right.append(bullet)
                        if tap_x < 0:
                            bullets_left.append(bullet)

                        speeds_y.append(speed_y)
                        i += 1

                        if peregrev == False:
                            cooldown = cooldown_hero
                        if peregrev == True:
                            cooldown = 70
                            health -= 10

                else:
                    cooldown -= 1

                # moon.play_animation(action='moon_animation')

                if dest_x_enemie > hero.body.centerx:
                    dest_x_enemie -= 3
                if dest_y_enemie > hero.body.centery:
                    dest_y_enemie -= 3
                if dest_x_enemie < hero.body.centerx:
                    dest_x_enemie += 3
                if dest_y_enemie < hero.body.centery:
                    dest_y_enemie += 3


                if hero.body.colliderect(distante_vision.body) == 1:
                    if time/120 == int(time/120):
                        direction_y = random.randint(-2, 2)
                        direction_x = (random.randint(-2, 2) - direction_y)

                    enemie.body.y += direction_y
                    enemie.body.x += direction_x

                if hero.body.colliderect(distante_vision.body) and end == False:
                    if enemi_cooldown <= 0:

                        # if temp < 730:
                        #
                        #     temp += 20

                        pygame.mixer.Sound.play(shot_sound)
                        dest_x = hero.body.centerx
                        dest_y = hero.body.centery
                        delta_x = dest_x - enemie.body.centerx
                        count_up = delta_x // speed_x
                        delta_y = enemie.body.centery - dest_y

                        if -0.1 < count_up < 0.1:
                            count_up = 0.1

                        speed_enemie_y = delta_y / count_up
                        weap = True
                        bullet = object.Barrier(parent=self.surface, objects=[], width=60, height=60, x=enemie.body.centerx, y=enemie.body.centery, speed_x=speed_enemie_x, speed_y=speed_enemie_y, color=(255, 0, 30))
                        if hero.body.centerx > enemie.body.centerx:
                            bullets_enemie_right.append(bullet)
                        if hero.body.centerx < enemie.body.centerx:
                            bullets_enemie_left.append(bullet)

                        speeds_enemie_y.append(speed_enemie_y)
                        i += 1

                        enemi_cooldown = 50

                    else:
                        enemi_cooldown -= 1

                if health <= 0:
                    game_ov = True

                if temp >= 720:
                    color_temp = (210, 60, 20)
                    self.surface.blit(sc_text_temp, (1135, 650))
                    peregrev = True

                else:
                    color_temp = (250, 150, 0)
                    peregrev = False

                # print(speed_y, speed_x)
                '''
                Этот код отвечает за списки пуль перебирает их,
                отрисовывает и удаляет когда они вышли за пределы экрана'''

                for bull in bullets_right[1:]:
                    bull_sprite = pygame.image.load(bullets_hero_sprite)

                    bull_sprite = pygame.transform.rotate(bull_sprite, -(angle))

                    bull.skin = bull_sprite
                    bull.blit()
                    bull.motions_bullet_right()
                    bull.resistance()

                    if bull.body.y > 3600:
                        bullets_right.remove(bull)

                    if bull.body.colliderect(enemie.body) == 1:
                        bullets_right.remove(bull)
                        enemie_health -= hero_damage
                    if bull.body.colliderect(meteor.body) == 1:
                        bullets_right.remove(bull)
                    if bull.body.colliderect(meteor_2.body) == 1:
                        bullets_right.remove(bull)

                    if bull.body.x > 4560:
                        g = bullets_right.remove(bull)



                for bull in bullets_left[1:]:
                    bull_sprite = pygame.image.load(bullets_hero_sprite)

                    bull_sprite = pygame.transform.rotate(bull_sprite, angle)

                    bull.skin = bull_sprite
                    bull.blit()
                    bull.motions_bullet_left()
                    bull.resistance()

                    if bull.body.y < -3000:
                        bullets_left.remove(bull)
                    if end == False:
                        if bull.body.colliderect(enemie.body) == 1:
                            bullets_left.remove(bull)
                            enemie_health -= hero_damage


                    if bull.body.x < -3000:
                        bullets_left.remove(bull)

                    bull.body = bull.skin.get_rect(topleft=(bull.body.x, bull.body.y))

                    if bull.body.colliderect(meteor_2.body) == 1:
                        bullets_left.remove(bull)
                    if bull.body.colliderect(meteor.body) == 1:
                        bullets_left.remove(bull)

                    # print(bull.body.colliderect(meteor.body))


                for bull in bullets_enemie_right[1:]:
                    bull_sprite = pygame.image.load(bullets_enemie_sprite)

                    # bull_sprite = pygame.transform.rotate(bull_sprite, angle)

                    bull.skin = bull_sprite
                    bull.blit()
                    bull.motions_bullet_right()
                    bull.resistance()
                    if bull.body.y > 4600:
                        bullets_enemie_right.remove(bull)

                    if bull.body.colliderect(hero.body) == 1:
                        bullets_enemie_right.remove(bull)
                        health -= 20
                    if bull.body.colliderect(meteor.body) == 1:
                        bullets_enemie_right.remove(bull)
                    if bull.body.colliderect(meteor_2.body) == 1:
                        bullets_enemie_right.remove(bull)

                    if bull.body.x > 4560:
                        bullets_enemie_right.remove(bull)

                for bulls in bullets_enemie_left[1:]:
                    bull_sprite = pygame.image.load(bullets_enemie_sprite)

                    # bull_sprite = pygame.transform.rotate(bull_sprite, angle)

                    bulls.skin = bull_sprite
                    bulls.blit()
                    bulls.motions_bullet_left()
                    bulls.resistance()
                    if bulls.body.y < -2000:
                        bullets_enemie_left.remove(bulls)
                    if end == False:
                        if bulls.body.colliderect(hero.body) == 1:
                            bullets_enemie_left.remove(bulls)
                            health -= 20
                        if bulls.body.colliderect(meteor.body) == 1:
                            bullets_enemie_left.remove(bulls)
                        if bulls.body.colliderect(meteor_2.body) == 1:
                            bullets_enemie_left.remove(bulls)

                    if bulls.body.x < -3000:
                        bullets_enemie_left.remove(bulls)


                # MOTION
                '''
                Этот код отвечает за передвижение камеры и плавное ускорение вначале.
                '''

                if t == True:
                    hero.play_animation(action='motion_right')
                    timer -= 1
                    if timer > 10:
                        X += ((timer+(80 - timer)) - timer)/8
                        # x_bul += ((timer+(80 - timer)) - timer)/10

                        hero.body.x = X

                    if timer <= 10:
                        for bull in bullets_right:
                            bull.body.x -= 10
                        for bull in bullets_left:
                            bull.body.x -= 10
                        for bull in bullets_enemie_right:
                            bull.body.x -= 10
                        for bull in bullets_enemie_left:
                            bull.body.x -= 10


                        platform_1.body.x -= 4
                        meteor.body.x -= 6
                        meteor_2.body.x -= 6
                        enemie.body.x -= 6
                        moon.body.x -= 5

                        if hero.body.x > 1280:
                            X -= ((hero.body.centerx - 1280) * -timer) / 700
                            # print(X)
                            hero.body.x = X


                if r == True:
                    hero.play_animation(action='motion_left')

                    timer -= 1
                    if timer > 10:
                        X -= ((timer+(80 - timer)) - timer)/8

                        hero.body.x = X

                    if timer <= 10:
                        for bull in bullets_right:
                            bull.body.x += 10
                        for bull in bullets_left:
                            bull.body.x += 10
                        for bull in bullets_enemie_right:
                            bull.body.x += 10
                        for bull in bullets_enemie_left:
                            bull.body.x += 10



                        platform_1.body.x += 4
                        meteor.body.x += 6
                        meteor_2.body.x += 6
                        enemie.body.x += 6
                        moon.body.x += 5


                        if hero.body.x < 1280:
                            X += (((1280 - hero.body.centerx) * -timer) / 700) + 1
                            hero.body.x = X


                if s == True:
                    timer -= 1
                    if timer > 10:
                        Y += ((timer+(80 - timer)) - timer)/8

                        hero.body.y = Y

                    if timer <= 10:
                        for bull in bullets_right:
                            bull.body.y -= 10
                        for bull in bullets_left:
                            bull.body.y -= 10
                        for bull in bullets_enemie_right:
                            bull.body.y -= 10
                        for bull in bullets_enemie_left:
                            bull.body.y -= 10


                        platform_1.body.y -= 4
                        meteor.body.y -= 6
                        meteor_2.body.y -= 6
                        enemie.body.y -= 6
                        moon.body.y -= 5

                        if hero.body.centery > 800:
                            Y -= ((hero.body.centery - 800) * -timer) / 700
                            # print(((hero.body.y - 325) * -timer) / 300)
                            hero.body.y = Y

                if m == True:
                    timer -= 1
                    if timer > 10:
                        Y -= (((timer+(80 - timer)) - timer)/8)

                        hero.body.y = Y
                    if timer <= 10:
                        for bull in bullets_right:
                            bull.body.y += 10
                        for bull in bullets_left:
                            bull.body.y += 10
                        for bull in bullets_enemie_right:
                            bull.body.y += 10
                        for bull in bullets_enemie_left:
                            bull.body.y += 10

                        platform_1.body.y += 4
                        meteor.body.y += 6
                        meteor_2.body.y += 6
                        enemie.body.y += 6
                        moon.body.y += 5


                        if hero.body.y < 750:
                            Y += (((750 - hero.body.y) * -timer) / 750) + 1

                            hero.body.y = Y

                if q == 1:
                    Y -= (hero.body.y - 325) / 10
                    hero.body.y = Y

                # print(speed_bulet_y)

            # EVENTS

            for event in self.events():
                # print(event)  # отслеживание событий
                self.close(event)
                # if event.type == VIDEORESIZE:
                #     if not fullscreen:
                #         screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                if event.type == 1025:
                    cursor_coor = event.pos
                    # print(cursor_coor)

                    # bullet.body.y = 835
                    # bullet.body.x = 1265

                if event.type == KEYDOWN:
                    if event.key == K_f:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((1200, 700),
                                                             pygame.RESIZABLE)

                if event.type == 768 and event.key == 100:
                    t = True
                    x = hero.body.x
                    y = hero.body.y

                if event.type == 769 and event.key == 100:
                    timer = 80
                    t = False
                    hero.skin = pygame.image.load(space_hero_ship_right)

                    # platform_1.body.x += 1230 - hero.body.x
                    # meteor.body.x += 1230 - hero.body.x
                    # enemie.body.x += 1230 - hero.body.x

                if event.type == 768 and event.key == 119:
                    m = True
                    x = hero.body.x
                    y = hero.body.y
                if event.type == 769 and event.key == 119:
                    timer = 80
                    m = False
                    hero.skin = pygame.image.load(space_hero_ship_left)

                    # platform_1.body.y += 750 - hero.body.y
                    # meteor.body.y += 750 - hero.body.y
                    # enemie.body.y += 750 - hero.body.y

                if event.type == 768 and event.key == 97:
                    r = True
                    x = hero.body.x
                    y = hero.body.y
                if event.type == 769 and event.key == 97:
                    timer = 80
                    r = False
                    # platform_1.body.x += 1230 - hero.body.x
                    # meteor.body.x += 1230 - hero.body.x
                    # enemie.body.x += 1230 - hero.body.x


                if event.type == 768 and event.key == 115:
                    s = True
                    y = hero.body.y
                    q = 0
                if event.type == 769 and event.key == 115:
                    timer = 80
                    s = False
                    # platform_1.body.y = 750 - hero.body.y
                    # meteor.body.y -= 750 - hero.body.y
                    # enemie.body.y -= 750 - hero.body.y

                if not event.type == 768:
                    pass

                if event.type == 769:
                    hero.body.centerx = 1280
                    hero.body.centery = 800

                if event.type == 768 and event.key == 32:
                    game_over = True
                    start_menu = True
                    screen = pygame.display.set_mode((1200, 700),
                                                     pygame.RESIZABLE)
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound.play(click_sound)


FirstGame(width=2560, height=1600).run()
