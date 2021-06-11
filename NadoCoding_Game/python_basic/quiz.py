import pygame
import random
###############################################################################
# 기본 초기화 (반드시 해야 함)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기")

# FPS
clock = pygame.time.Clock()

###############################################################################
# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

# 배경
background = pygame.image.load("C:/Users/tlgns/OneDrive/바탕 화면/SihoonPythonWorkspace/NadoCoding_Game/paper_background.jpg")
# 주인공
character = pygame.image.load("C:/Users/tlgns/OneDrive/바탕 화면/SihoonPythonWorkspace/NadoCoding_Game/doggie.jpg")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height
# 똥
enemy = pygame.image.load("C:/Users/tlgns/OneDrive/바탕 화면/SihoonPythonWorkspace/NadoCoding_Game/ddong.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) / 2
enemy_y_pos = 0

character_speed = 0.6

enemy_speed = 0.6

to_x = 0

game_font = pygame.font.Font(None, 40)

total_time = 30
start_ticks = pygame.time.get_ticks()





running = True 
while running :
    dt = clock.tick(30) 

    # 2. 이벤트 처리(키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
        
    

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    enemy_y_pos += enemy_speed * dt
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0,screen_width - enemy_width)

    # 4. 충돌 처리
    
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("충돌했어요")
        running = False


    # 5. 화면에 그리기
    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))

    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (0,0,0))

    screen.blit(timer,(10,10))

    if total_time - elapsed_time < 0:
        print("시간 동안 잘 버텼습니다!!!")
        running = False

    pygame.display.update() # 게임화면을 매번 다시 그리기

pygame.quit()