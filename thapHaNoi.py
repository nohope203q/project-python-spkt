import pygame, sys
from pygame.locals import *
import csv
from button import Button
import time
from Player import Player, PlayerManager
import random
import pygame.mixer
from disk import Disk
from PhaoHoa import Firework
pygame.init()


pygame.display.set_caption("Towers of Hanoi")

SCREEN = pygame.display.set_mode((720, 480))

clock = pygame.time.Clock()
BG = pygame.image.load("images/Background.png")

framerate = 60
isWin = False
NUM_DISKS = 3
TEXT_SIZE = 30
TEXT_TOP = 40
NAME = ""  
YELLOW = (255, 255, 0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)


pygame.init()
pygame.font.init()
pygame.mixer.init()


pygame.mixer.music.load("bground.mp3")
pygame.mixer.music.play(-1)
beep_sound = pygame.mixer.Sound("soundclick.mp3")
win_sound = pygame.mixer.Sound("soundwin.mp3")
def get_font(size): 
    return pygame.font.Font("font/font.ttf", size)

def play():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("TOWER OF HANOI", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        DAUXEPHAN_BUTTON = Button(image=None, pos=(360, 220), 
                            text_input="RANKING", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        LUYENTAP_BUTTON = Button(image=None, pos=(360, 280), 
                            text_input="PRACTICE", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        MAYGIAI_BUTTON = Button(image=None, pos=(360, 340), 
                            text_input="AUTO SOVLE", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        BACK_BUTTON = Button(image=None, pos=(360, 400), 
                        
                            text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [DAUXEPHAN_BUTTON, LUYENTAP_BUTTON, MAYGIAI_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if DAUXEPHAN_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    rankingMenu()
                if LUYENTAP_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    luyenTap()
                if MAYGIAI_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    mayGiai()
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(framerate)

def rankingMenu():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("TOWER OF HANOI", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        CHEDOTHUONG_BUTTON = Button(image=None, pos=(360, 250), 
                            text_input="NORMAL", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        NANGCAO_BUTTON = Button(image=None, pos=(360, 320), 
                            text_input="ADVANCED", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        BACK_BUTTON = Button(image=None, pos=(360, 390), 
                            text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CHEDOTHUONG_BUTTON, NANGCAO_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if CHEDOTHUONG_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    dauXepHang()
                if NANGCAO_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    dauXepHangMagnatic()
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(framerate)

def nhapTen(filename):
    global NAME
    clock = pygame.time.Clock()
    NAME = ""

    def name_exists(name):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == name:
                        return True
        except FileNotFoundError:
            return False
        return False

    while True:
        SCREEN.blit(BG, (0, 0))
        USER_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(TEXT_TOP).render("ENTER YOUR NAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        NAME_TEXT = get_font(TEXT_SIZE).render("NAME", True, "YELLOW")
        NAME_RECT = NAME_TEXT.get_rect(center=(130, 200))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        NAME_INPUT = pygame.Rect(250, 180, 400, 40)
        pygame.draw.rect(SCREEN, "#d3d3d3", NAME_INPUT)
        name_surface = get_font(TEXT_SIZE).render(NAME, True, "BLACK")
        SCREEN.blit(name_surface, (NAME_INPUT.x + 5, NAME_INPUT.y + 5))
        NAME_INPUT.w = max(200, name_surface.get_width() + 10)

        BACK_BUTTON = Button(image=None, pos=(360, 400), 
                             text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        for button in [BACK_BUTTON]:
            button.changeColor(USER_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    NAME = NAME[:-1]
                elif event.key == pygame.K_RETURN:
                    if name_exists(NAME):
                        show_message("This name already exists. Try another.")
                        NAME = ""
                    else:
                        return NAME
                elif len(NAME) < 13:
                    NAME += event.unicode
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(USER_MOUSE_POS):
                    play()
        
        pygame.display.update()
        clock.tick(framerate)

def show_message(message):
    font = pygame.font.Font("font/font.ttf", 13)
    text = font.render(message, True, "RED")
    text_rect = text.get_rect(center=(360, 240))
    SCREEN.blit(text, text_rect)
    pygame.display.update()
    time.sleep(1)

def game_over_player():
    global isWin
    global win_played
    win_played = False
    
    fireworks = [Firework(random.randint(50, 670), 400) for _ in range(10)]  # More fireworks

    while True:
        SCREEN.blit(BG, (0, 0))
        GAMEOVER_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("CONGRATULATIONS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        BACK_BUTTON = Button(image=None, pos=(360, 400), 
                            text_input="HOME", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for firework in fireworks:
            firework.update()
            firework.draw(SCREEN)

        if random.random() < 0.05: 
            fireworks.append(Firework(random.randint(50, 670), 400))

        if isWin:
            WIN_TEXT = get_font(TEXT_SIZE).render("YOU WON!", True, "GREEN")
            WIN_RECT = WIN_TEXT.get_rect(center=(360, 200))
            SCREEN.blit(WIN_TEXT, WIN_RECT)

        if not win_played:
            pygame.mixer.music.stop()
            win_sound.play()
            win_played = True

        if move_count == 2 ** NUM_DISKS - 1:
            PERFECT_TEXT = get_font(TEXT_SIZE).render("PERFECT SCORE!", True, "GREEN")
            PERFECT_RECT = PERFECT_TEXT.get_rect(center=(360, 250))
            SCREEN.blit(PERFECT_TEXT, PERFECT_RECT)

        for button in [BACK_BUTTON]:
            button.changeColor(GAMEOVER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                win_played = False
                if BACK_BUTTON.checkForInput(GAMEOVER_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        pygame.mixer.music.play(-1)
        clock.tick(framerate)


def game_over_machine():
    global isWin
    global win_played
    win_played = False
    fireworks = [Firework(random.randint(50, 670), 400) for _ in range(10)]  

    while True:
        SCREEN.blit(BG, (0, 0))
        GAMEOVER_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("DONE!", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        BACK_BUTTON = Button(image=None, pos=(360, 400), 
                            text_input="HOME", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for firework in fireworks:
            firework.update()
            firework.draw(SCREEN)

        if random.random() < 0.05:  
            fireworks.append(Firework(random.randint(50, 670), 400))

        if not win_played:
            pygame.mixer.music.stop()
            win_sound.play()
            win_played = True

        for button in [BACK_BUTTON]:
            button.changeColor(GAMEOVER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                win_played = False
                if BACK_BUTTON.checkForInput(GAMEOVER_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        pygame.mixer.music.play(-1)
        clock.tick(framerate)


def scoreBoard(fileName):
    with open(fileName, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
    current_page=0
    items_per_page=10
    
    while True:
        SCREEN.blit(BG, (0, 0))
        SCOREBOARD_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("SCORE BOARD", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 50))

        BACK_BUTTON = Button(image=None, pos=(360, 380), 
                            text_input="HOME", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        NEXT_BUTTON = Button(image=None, pos=(600, 400), 
                            text_input=">", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        PREV_BUTTON = Button(image=None, pos=(120, 400), 
                            text_input="<", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        FIND_BUTTON = Button(image=None, pos=(360, 420), 
                            text_input="FIND", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BACK_BUTTON, NEXT_BUTTON, PREV_BUTTON, FIND_BUTTON]:
            button.changeColor(SCOREBOARD_MOUSE_POS)
            button.update(SCREEN)
        count=current_page*items_per_page+1
        j=0
        for i in range(current_page*items_per_page, min(len(data), (current_page+1)*items_per_page)):
            name = data[i][0]
            soDia = data[i][1]
            soBuoc  = data[i][2]
            time= data[i][3]
            score = data[i][4]
            
            tieu_de = get_font(10).render("RANK", True, "YELLOW")
            tieu_de_name = get_font(10).render("NAME", True, "YELLOW")
            tieu_de_soDia = get_font(10).render("DISK", True, "YELLOW")
            tieu_de_soBuoc = get_font(10).render("MOVE", True, "YELLOW")
            tieu_de_time = get_font(10).render("TIME", True, "YELLOW")
            tieu_de_score = get_font(10).render("SCORE", True, "YELLOW")

            number_text = get_font(10).render(str(count), True, "YELLOW")
            name_text = get_font(10).render(name, True, "YELLOW")
            soDia_text = get_font(10).render(soDia, True, "YELLOW")
            soBuoc_text = get_font(10).render(soBuoc, True, "YELLOW")
            time_text = get_font(10).render(time, True, "YELLOW")
            score_text = get_font(10).render(score, True, "YELLOW")

            SCREEN.blit(tieu_de, (50, 100))
            SCREEN.blit(tieu_de_name, (100, 100))
            SCREEN.blit(tieu_de_soDia, (280, 100))
            SCREEN.blit(tieu_de_soBuoc, (350, 100))
            SCREEN.blit(tieu_de_time, (450, 100))
            SCREEN.blit(tieu_de_score, (600, 100))

            SCREEN.blit(number_text, (50, 150 + j * 20))
            SCREEN.blit(name_text, (100, 150 + j * 20))
            SCREEN.blit(soDia_text, (280, 150 + j * 20))
            SCREEN.blit(soBuoc_text, (350, 150 + j * 20))
            SCREEN.blit(time_text, (450, 150 + j * 20))
            SCREEN.blit(score_text, (600, 150 + j * 20))
            count+=1
            j+=1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(SCOREBOARD_MOUSE_POS):
                    main_menu()
                if NEXT_BUTTON.checkForInput(SCOREBOARD_MOUSE_POS):
                    if current_page<len(data)//items_per_page:
                        current_page+=1
                if FIND_BUTTON.checkForInput(SCOREBOARD_MOUSE_POS):
                    timKiemPlayer(fileName)
                if PREV_BUTTON.checkForInput(SCOREBOARD_MOUSE_POS):
                    if current_page>0:
                        current_page-=1

        pygame.display.update()
        clock.tick(framerate)
def draw_towers(towers):
    SCREEN.blit(BG, (0, 0))
    tower_width = 10
    disk_height = 20
    tower_height = 150
    tower_positions = [(150, 300), (360, 300), (570, 300)]

    disk_colors = [
        (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
        (255, 165, 0), (128, 0, 128), (255, 192, 203), (0, 255, 255), 
        (255, 0, 255), (128, 128, 128), (255, 255, 255)
    ]
    disk_color_mapping = []
    for i in range(3):
        tower_colors = []
        for j, disk in enumerate(towers[i]):
            tower_colors.append(disk_colors[disk % len(disk_colors)])
        disk_color_mapping.append(tower_colors)

    for pos in tower_positions:
        pygame.draw.rect(SCREEN, (0, 0, 0), (pos[0] - tower_width // 2, pos[1] - tower_height, tower_width, tower_height))

    for i in range(3):
        x, y = tower_positions[i]
        for j, disk in enumerate(towers[i]):
            disk_width = 20 + disk * 20
            disk_rect = pygame.Rect(x - disk_width // 2, y - (j + 1) * disk_height, disk_width, disk_height)
            disk_color = disk_color_mapping[i][j]
            pygame.draw.rect(SCREEN, disk_color, disk_rect, border_radius=10)
            border_color = (0, 0, 0)
            border_width = 2
            pygame.draw.rect(SCREEN, border_color, disk_rect, border_width, border_radius=10)

def scoreBoardMenu():
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("SCORE BOARD", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        CHEDOTHUONG_BUTTON = Button(image=None, pos=(360, 250), 
                            text_input="NORMAL", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        NANGCAO_BUTTON = Button(image=None, pos=(360, 320), 
                            text_input="ADVANCED", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        BACK_BUTTON = Button(image=None, pos=(360, 390), 
                            text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [CHEDOTHUONG_BUTTON, NANGCAO_BUTTON, BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if CHEDOTHUONG_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    scoreBoard("scoreboardnormal.csv")
                if NANGCAO_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    scoreBoard("scoreboardadvanced.csv")
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
        clock.tick(framerate)
def chonSoDia():
    
    global NUM_DISKS
    while True:
        SCREEN.blit(BG, (0, 0))
        
        USER_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(30).render("CHOOSE NUMBER OF DISKS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        PLUS_BUTTON = Button(image=None, pos=(600, 250), 
                            text_input="+", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        MINUS_BUTTON = Button(image=None, pos=(120, 250), 
                            text_input="-", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        PLAY_BUTTON = Button(image=None, pos=(360, 350), 
                            text_input="PLAY", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        BACK_BUTTON = Button(image=None, pos=(360, 400), 
                            text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLUS_BUTTON, MINUS_BUTTON, PLAY_BUTTON, BACK_BUTTON]:
            button.changeColor(USER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if PLUS_BUTTON.checkForInput(USER_MOUSE_POS):
                    NUM_DISKS += 1
                    if NUM_DISKS > 10:
                        NUM_DISKS = 10
                if MINUS_BUTTON.checkForInput(USER_MOUSE_POS):
                    NUM_DISKS -= 1
                    if NUM_DISKS < 1:
                        NUM_DISKS = 1
                if PLAY_BUTTON.checkForInput(USER_MOUSE_POS):
                    return
                if BACK_BUTTON.checkForInput(USER_MOUSE_POS):
                    play()

        font = pygame.font.Font("font/font.ttf", 40)
        disks_text = font.render(f"{NUM_DISKS}", True, (255, 255, 255))
        SCREEN.blit(disks_text, (360, 200))

        pygame.display.update()
        clock.tick(framerate)

def dauXepHang():
    global selected_disk, selected_tower, start_time, move_count
    global isWin
    isWin = True
    nhapTen("scoreboardnormal.csv")
    chonSoDia()
    towers = [[], [], []]
    for i in range(NUM_DISKS, 0, -1):
        towers[0].append(i)
    selected_disk = None
    selected_tower = None
    move_count = 0
    start_time = pygame.time.get_ticks()

    while True:
        SCREEN.blit(BG, (0, 0))
        draw_towers(towers)
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000 
        font = pygame.font.Font("font/font.ttf", 15)
        time_text = font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
        SCREEN.blit(time_text, (20, 20))
        move_text = font.render(f"Moves: {move_count}", True, (255, 255, 255))
        SCREEN.blit(move_text, (200, 20))
        USER_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=None, pos=(360, 450),
                             text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        MAYGIAI_BUTTON = Button(image=None, pos=(600, 450),
                             text_input="AUTO", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        RESTART_BUTTON = Button(image=None, pos=(120, 450),
                             text_input="RESTART", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        optimal_moves = 2 ** NUM_DISKS - 1
        optimal_time = 2 ** NUM_DISKS - 1
        score = 100
        move_diff = move_count - optimal_moves
        time_diff = elapsed_time - optimal_time
        if move_diff > 0:
            score -= move_diff * 5
        if time_diff > 0:
            score -= time_diff//10 * 2
        optimal_moves_text = font.render(f"Optimal moves: {optimal_moves}", True, (255, 255, 255))
        SCREEN.blit(optimal_moves_text, (400, 20))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (20, 60))
        
        for button in [BACK_BUTTON, MAYGIAI_BUTTON, RESTART_BUTTON]:
            button.changeColor(USER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(USER_MOUSE_POS):
                    main_menu()
                if MAYGIAI_BUTTON.checkForInput(USER_MOUSE_POS):
                    mayGiai()
                if RESTART_BUTTON.checkForInput(USER_MOUSE_POS):
                    towers = [[], [], []]
                    for i in range(NUM_DISKS, 0, -1):
                        towers[0].append(i)
                    selected_disk = None
                    selected_tower = None
                    move_count = 0
                    start_time = pygame.time.get_ticks()
                    continue
                    
                tower_positions = [(150, 300), (360, 300), (570, 300)]
                for i, (x, y) in enumerate(tower_positions):
                    if abs(USER_MOUSE_POS[0] - x) < 50:  
                        if selected_disk is None and towers[i]: 
                            selected_disk = towers[i].pop()
                            selected_tower = i
                        elif selected_disk is not None:  
                            if i != selected_tower:  
                                if not towers[i] or towers[i][-1] > selected_disk:  
                                    towers[i].append(selected_disk)
                                    selected_disk = None
                                    selected_tower = None
                                    move_count += 1
                                else:  
                                    towers[selected_tower].append(selected_disk)  
                                    selected_disk = None
                                    selected_tower = None


                time.sleep(0.1)
                if towers[2] == list(range(NUM_DISKS, 0, -1)):
                    isWin = True
                    player = Player(name=NAME, disks=NUM_DISKS, moves=move_count, time=elapsed_time, score=score)
                    player_manager = PlayerManager()
                    player_manager.load_players("scoreboardnormal.csv")
                    player_manager.add_player(player)
                    player_manager.sort_players()
                    player_manager.save_players("scoreboardnormal.csv")
                    game_over_player()

        pygame.display.update()
        clock.tick(framerate)

def tower_of_hanoi(towers, source, target, temp, n):
    if n == 1:
        target.append(source.pop())
        draw_towers(towers)
        pygame.display.update()
        time.sleep(0.5)
        return
    tower_of_hanoi(towers, source, temp, target, n - 1)
    target.append(source.pop())
    draw_towers(towers)
    pygame.display.update()
    time.sleep(0.5)
    clock.tick(framerate)
    tower_of_hanoi(towers, temp, target, source, n - 1)

def mayGiai():
    global NUM_DISKS
    chonSoDia()
    towers = [[], [], []]
    for i in range(NUM_DISKS, 0, -1):
        towers[0].append(i)  

    draw_towers(towers)
    pygame.display.update()
    time.sleep(1) 
    tower_of_hanoi(towers, towers[0], towers[2], towers[1], NUM_DISKS)
    game_over_machine()

def random_disks(stacks, n):
    random.seed() 
    disks = list(range(1, n + 1))
    random.shuffle(disks) 
    disks_per_column = [0, 0, 0]
    remaining_disks = n
    for i in range(2):
        if remaining_disks > 1:
            disks_per_column[i] = random.randint(1, remaining_disks - 1)
            remaining_disks -= disks_per_column[i]
        else:
            disks_per_column[i] = 1
            remaining_disks -= 1
    disks_per_column[2] = remaining_disks

    if disks_per_column[2] == n:
        disks_per_column[2] = random.randint(1, n - 1)
        remaining_disks = n - disks_per_column[2]
        for i in range(2):
            disks_per_column[i] = random.randint(1, remaining_disks - 1)
            remaining_disks -= disks_per_column[i]

    disk_index = 0
    for i in range(3):
        if disks_per_column[i] > 0:
            stacks[i] = disks[disk_index:disk_index + disks_per_column[i]]
            stacks[i].sort(reverse=True)  
            disk_index += disks_per_column[i]

def luyenTap():
    
    global isWin, selected_disk, selected_tower, move_count
    isWin = True
    chonSoDia()
    towers = [[], [], []]
    random_disks(towers, NUM_DISKS)
    selected_disk = None
    selected_tower = None
    move_count = 0

    while True:
        SCREEN.blit(BG, (0, 0))
        draw_towers(towers)
        font = pygame.font.Font("font/font.ttf", 15)
        USER_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=None, pos=(360, 450),
                             text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        for button in [BACK_BUTTON]:
            button.changeColor(USER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(USER_MOUSE_POS):
                    play()
                tower_positions = [(150, 300), (360, 300), (570, 300)]
                for i, (x, y) in enumerate(tower_positions):
                    if abs(USER_MOUSE_POS[0] - x) < 50:  
                        if selected_disk is None and towers[i]: 
                            selected_disk = towers[i].pop()
                            selected_tower = i

                        elif selected_disk is not None:  
                            if i != selected_tower:  
                                if not towers[i] or towers[i][-1] > selected_disk:  
                                    towers[i].append(selected_disk)
                                    selected_disk = None
                                    selected_tower = None
                                    move_count += 1
                                else:  
                                    towers[selected_tower].append(selected_disk) 
                                    selected_disk = None
                                    selected_tower = None

                time.sleep(0.1)
                if towers[2] == list(range(NUM_DISKS, 0, -1)):
                    isWin = True
                    game_over_player()

        pygame.display.update()
        clock.tick(framerate)

def draw_towers_magnatic(towers):
    SCREEN.blit(BG, (0, 0))
    tower_width = 10
    disk_height = 20
    tower_height = 150
    tower_positions = [(150, 300), (360, 300), (570, 300)]

    for pos in tower_positions:
        pygame.draw.rect(SCREEN, (0, 0, 0), (pos[0] - tower_width // 2, pos[1] - tower_height, tower_width, tower_height))

    for i, tower in enumerate(towers):
        x, y = tower_positions[i]
        for j, disk in enumerate(tower):
            disk_width = 20 + disk.size * 20
            disk_rect = pygame.Rect(x - disk_width // 2, y - (j + 1) * disk_height, disk_width, disk_height)

            disk_color = (255, 0, 0) if disk.isRedTop else (0, 0, 255) 
            pygame.draw.rect(SCREEN, disk_color, disk_rect, border_radius=10)
            border_color = (0, 0, 0)
            border_width = 2
            pygame.draw.rect(SCREEN, border_color, disk_rect, border_width, border_radius=10)

def dauXepHangMagnatic():
    global selected_disk, selected_tower, start_time, move_count
    selected_disk = None
    selected_tower = None
    move_count = 0
    start_time = pygame.time.get_ticks()

    nhapTen("scoreboardadvanced.csv")
    chonSoDia()

    towers = [[], [], []]
    for i in range(NUM_DISKS, 0, -1):
        disk = Disk(size=i, isRedTop=True) 
        towers[0].append(disk)

    while True:
        SCREEN.blit(BG, (0, 0))
        draw_towers_magnatic(towers)
        elapsed_time = (pygame.time.get_ticks() - start_time) // 1000 
        font = pygame.font.Font("font/font.ttf", 15)
        time_text = font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
        SCREEN.blit(time_text, (20, 20))
        move_text = font.render(f"Moves: {move_count}", True, (255, 255, 255))
        SCREEN.blit(move_text, (200, 20))
        USER_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON = Button(image=None, pos=(360, 450),
                             text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        RESTART_BUTTON = Button(image=None, pos=(120, 450),
                             text_input="RESTART", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        optimal_time = 2 ** NUM_DISKS - 1
        score = 100
        time_diff = elapsed_time - optimal_time
        if time_diff > 0:
            score -= time_diff//10 * 2

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        SCREEN.blit(score_text, (20, 60))
        
        for button in [BACK_BUTTON, RESTART_BUTTON]:
            button.changeColor(USER_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(USER_MOUSE_POS):
                    main_menu()
                elif RESTART_BUTTON.checkForInput(USER_MOUSE_POS):
                    towers = [[], [], []]
                    for i in range(NUM_DISKS, 0, -1):
                        disk = Disk(size=i, isRedTop=True)
                        towers[0].append(disk) 
                    selected_disk = None
                    move_count = 0
                    start_time = pygame.time.get_ticks()
                else:
                    for i, (x, y) in enumerate([(150, 300), (360, 300), (570, 300)]):
                        if abs(USER_MOUSE_POS[0] - x) < 50:

                            if selected_disk is None and towers[i]:
                                selected_disk = towers[i].pop()
                                selected_tower = i
                            elif selected_disk is not None:
                                if selected_tower == i:
                                    continue

                                if not towers[i] or (towers[i][-1].size > selected_disk.size and towers[i][-1].isRedTop != selected_disk.isRedTop):
                                    towers[i].append(selected_disk)
                                    selected_disk.flip()  
                                    selected_disk = None
                                    selected_tower = None
                                    move_count += 1
                                else:
                                    towers[selected_tower].append(selected_disk)
                                    selected_disk = None
                                    selected_tower = None

                    if len(towers[2]) == NUM_DISKS:
                        if all(towers[2][i].size == NUM_DISKS - i for i in range(NUM_DISKS)):
                            isWin = True
                            player = Player(name=NAME, disks=NUM_DISKS, moves=move_count, time=elapsed_time, score=score)
                            player_manager = PlayerManager()
                            player_manager.load_players("scoreboardadvanced.csv")
                            player_manager.add_player(player)
                            player_manager.sort_players()
                            player_manager.save_players("scoreboardadvanced.csv")
                            game_over_player()

        pygame.display.update()
        clock.tick(framerate)

def timKiemPlayer(filename):
    global NAME
    clock = pygame.time.Clock()
    NAME = "" 

    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(TEXT_TOP).render("SEARCH PLAYER", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        NAME_TEXT = get_font(TEXT_SIZE).render("NAME", True, "YELLOW")
        NAME_RECT = NAME_TEXT.get_rect(center=(130, 200))
        SCREEN.blit(NAME_TEXT, NAME_RECT)

        NAME_INPUT = pygame.Rect(250, 180, 400, 40)
        pygame.draw.rect(SCREEN, "#d3d3d3", NAME_INPUT)
        name_surface = get_font(TEXT_SIZE).render(NAME, True, "BLACK")
        SCREEN.blit(name_surface, (NAME_INPUT.x + 5, NAME_INPUT.y + 5))
        
        NAME_INPUT.w = max(200, name_surface.get_width() + 10)

        BACK_BUTTON = Button(image=None, pos=(360, 420),
                             text_input="BACK", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [BACK_BUTTON]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    NAME = NAME[:-1] 
                elif event.key == pygame.K_RETURN:
                    player_manager = PlayerManager()
                    player_manager.load_players(filename)
                    player = player_manager.find_player(NAME)
                    if player:
                        show_player_info(player) 
                    else:
                        show_message(f"Player {NAME} not found.")
                    NAME = ""  
                elif len(NAME) < 13:
                    NAME += event.unicode  
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if BACK_BUTTON.checkForInput(PLAY_MOUSE_POS):
                    scoreBoard(filename)
               

        pygame.display.update()
        clock.tick(framerate)

def show_player_info(player):
    font = pygame.font.Font("font/font.ttf", 18)
    
    player_info = [
        f"Name: {player.name}",
        f"Score: {player.score}",
        f"Disks: {player.disks}",
        f"Moves: {player.moves}",
        f"Time: {player.time}s"
    ]

    max_width = max(font.size(info)[0] for info in player_info)

    y_position = 250
    line_height = 30
    for info in player_info:
        message_text = font.render(info, True, "GREEN")
        message_rect = message_text.get_rect(center=(360, y_position))
        message_rect.x = (SCREEN.get_width() - max_width) // 2  
        SCREEN.blit(message_text, message_rect)
        y_position += line_height

    pygame.display.update()
    pygame.time.wait(3000)

def main_menu():
    
    while True:
    
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(TEXT_TOP).render("TOWER OF HANOI", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(360, 100))

        PLAY_BUTTON = Button(image=None, pos=(360, 250), 
                            text_input="PLAY", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        SCOREBOARD_BUTTON = Button(image=None, pos=(360, 320), 
                            text_input="SCORE BOARD", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")
        QUIT_BUTTON = Button(image=None, pos=(360, 390), 
                            text_input="QUIT", font=get_font(TEXT_SIZE), base_color="#d7fcd4", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, SCOREBOARD_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                beep_sound.play()
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if SCOREBOARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                    scoreBoardMenu()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

        clock.tick(framerate)


def main():
    main_menu()
if __name__ == '__main__':
    main()
