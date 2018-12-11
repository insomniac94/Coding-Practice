import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600

BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)
WHITE = (255,255,255)
BACKGROUND_COLOR = (11,238,207)

speed = 10

score = 0

square_size = 50
user_pos = [WIDTH/2, HEIGHT-(2*square_size)]

randomPos = random.randint(0,WIDTH-square_size)

enemy_pos = [randomPos,0]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)

def level_difficulty(score, speed):
	if score < 20:
		speed = 3
	elif score < 40:
		speed = 4
	elif score < 50:
		speed = 5
	elif score < 60:
		speed = 5
	else:
		speed = 15

	#speed will be proportional to score
	#speed = score / 10 + 3
	
	return speed
	

def drop_enemies(enemy_list):
	delay = random.random()
	if len(enemy_list) < 10 and delay < 0.1:
		x_pos = randomPos
		y_pos = 0
		enemy_list.append([x_pos, y_pos])

def update_enemy_pos(enemy_list, score):
	for index, enemy_pos in enumerate(enemy_list):
		if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
			enemy_pos[1] += speed
		else:
			enemy_list.pop(index)
			score += 1
	return score

def draw_enemies(enemy_list):
	for enemy_pos in enemy_list:
		pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], square_size, square_size))

def collision_check(enemy_list, user_pos):
	for enemy_pos in enemy_list:
		if collision_detection(user_pos,enemy_pos):
			return True
	return False


def collision_detection(user_pos,enemy_pos):
	user_x = user_pos[0]
	user_y = user_pos[1]

	enemy_x = enemy_pos[0]
	enemy_y = enemy_pos[1]
	
	if (enemy_x >= user_x and enemy_x < (user_x + square_size )) or (user_x >= enemy_x and user_x < (enemy_x + square_size)):
		if (enemy_y>= user_y and enemy_y < (user_y + square_size )) or (user_y >= enemy_y and user_y < (enemy_y + square_size)):
			return True
	return False

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:

			x = user_pos[0]
			y = user_pos[1]

			if event.key == pygame.K_a:
				x -= square_size

			elif event.key == pygame.K_d:
				x += square_size

			user_pos = [x,y]

	screen.fill(BACKGROUND_COLOR)

	if collision_detection(user_pos, enemy_pos):
		game_over = True
		#break will show collision on screen

	drop_enemies(enemy_list)
	score = update_enemy_pos(enemy_list, score)
	speed = level_difficulty(score, speed)

	text = "Score: " + str(score)
	label = myFont.render(text, 1, BLACK)
	screen.blit(label, (WIDTH-200,HEIGHT-40))

	if collision_check(enemy_list, user_pos):
		game_over = True
		break

	draw_enemies(enemy_list)

	pygame.draw.rect(screen, BLUE, (user_pos[0], user_pos[1], square_size, square_size))

	clock.tick(30)

	pygame.display.update()