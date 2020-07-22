import sys
import pygame
from random import randint
from bullet import Bullet
from alien import Alien
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # 响应按键
    # bullets 到时候传递的实参是在alien_inversion主程序中赋值的bullets=Group（）的bullet编组
    if event.key == pygame.K_RIGHT:
        # make ship right
        ship.moving_right = True

    elif event.key == pygame.K_LEFT:
        # make ship left
        ship.moving_left = True

    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
            # # create a new bullet into Group of bullet
            #  if len(bullets) < ai_settings.bullet_allowed:
            #     new_bullet = Bullet(ai_settings, screen, ship)
            #     bullets.add(new_bullet)

    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event,ship):
    # respond to keyboard loose
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            # if event.key == pygame.K_RIGHT:
            #     # make ship right
            #     ship.moving_right =True
            #
            # elif event.key == pygame.K_LEFT:
            #     # make ship left
            #     ship.moving_left =True

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            # if event.key == pygame.K_RIGHT:
            #     ship.moving_right = False
            # elif event.key == pygame.K_LEFT:
            #     ship.moving_left = False

        # check whether mouse click Play button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)



# following is the part about bullet
def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):

    # 更新子弹的位置
    bullets.update()

    # delete the bullets which moving out of screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

    # show the left number of bullets, but I think there is no meaning
    #print(len(bullets))

def fire_bullet(ai_settings, screen, ship, bullets):
    # create a new bullet into Group of bullet
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """take action for bullet hit alien"""
    # delete bullet existed and create a new group of aliens
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():

            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()

        check_high_score(stats, sb)

    # check if aliens are all hit
    if len(aliens) ==0:
        # delete the bullet, then create a new group of aliens, and make level up
        bullets.empty()
        ai_settings.increase_speed()

        # level up
        stats.level +=1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)

def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """take action for ship hit by alien"""
    if stats.ships_left >0:
        # ship_left subtract 1
        stats.ships_left -=1

        # update scoreboard
        sb.prep_ships()

        # delete aliens and bullets
        aliens.empty()
        bullets.empty()

        # set up a new group of aliens and put a new ship into the central bottom of screen
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


# following is the part of alien
def get_number_aliens_x(ai_settings, alien_width):
    """calculate how many aliens in a line"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """"""
    available_space_y = (ai_settings.screen_height-3*(alien_height)-ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien then put it in line"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """set up a group of aliens"""
    # create a Alien 实例
    # calculate certain parameters of position of alien
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    # why use 'alien.rect.width' rather than 'alien_width',
    # because alien_width 是在create_alien function definite a value
    # alien.rect.width is a property of rect, which can use directly rather than definite a value

    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # set up a group of aliens (many lines)
    for row_number in range(number_rows):

        # set up the first of aliens
        random_number = randint(1,7)
        for alien_number in range(random_number):
            # each line has a random number of alien
        # for alien_number in range(number_aliens_x):
            # each line has same number of alien
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):
    """if the aline is on the margin of screen, it need to take certain action"""
    for alien in aliens.sprites():
        if alien.check_edges():
            # if the function named alien.check_edges return 'True', the moving direction will change
            change_fleet_direction(ai_settings, aliens)
            break

def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >=screen_rect.bottom:
            # take action like aliens hit the ship
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
            break

def change_fleet_direction(ai_settings, aliens):
    """make the whole aliens down and change the moving direction"""
    for alien in aliens.sprites():
        alien.rect.y +=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *=-1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """check whether aliens is on the margin of the screen, then update the position of the whole aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check whether alien hits ship
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets)
        print("ship hit")

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets)

# action of Play button
def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """the game is active when Play button is clicked"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # reset game
        ai_settings.initialize_dynamic_settings()

        # reset scoreboard image
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()


        # hide the mouse
        pygame.mouse.set_visible(False)

        # reset the game stats
        stats.reset_stats()
        stats.game_active = True

        # clear aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new alien and make ship center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_high_score(stats, sb):
    """check if there is a new highest score """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

# update the whole screen
def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # why the py doesn't import Ship and Alien, can also use the function in the two class
    # because in the main application(alien_invasion)，在调用update_screen之前已经创建的Ship和Alien的实例ship和alien
    # so 调用update_screen时，ship和alien其实已经是Ship和Alien的实例

    ship.blitme()
    # alien.blitme(),这个是之前编写单一alien时的代码
    aliens.draw(screen)

    # show the score
    sb.show_score()

    # if game isn't activated, then paint "Play" button
    if not stats.game_active:
        play_button.draw_button()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
