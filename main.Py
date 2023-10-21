import pygame
import random
import time
pygame.init()
back = (0, 50, 250)
window = pygame.display.set_mode((500, 500))
window.fill(back)
clock = pygame.time.Clock()

class Area:
    def __init__(self, x, y, win_w, win_h, color):
        self.rect = pygame.Rect(x, y, win_w, win_h)
        self.fill_color = color
    def color(self, new_color):
        self.fill_color = new_color
    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def outlite(self, freym_color, tolshina):
        pygame.draw.rect(window, freym_color, self.rect, tolshina)
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Leabel(Area):
    def set_text(self, text, size, text_color):
        self.image = pygame.font.SysFont('verdana', size).render(text, True, text_color)
    def draw(self, shift_x, shift_y):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 51)
RED = (255, 0, 0)
cards = list()
num_cards = 4
x = 70
for i in range(num_cards):
    new_card = Leabel(x, 170, 60, 100, YELLOW)
    new_card.outlite(GREEN, 14)
    new_card.set_text('CLICK', 20, BLACK)
    cards.append(new_card)
    x += 100
whate = 0
time_text = Leabel(0, 0, 32, 27, back)
time_text.set_text('Время', 32, BLACK)
time_text.draw(20, 20)
timer = Leabel(50, 55, 55, 50, back)
timer.set_text('0', 32, BLACK)
timer.draw(0, 0)
scor_text = Leabel(345, 0, 32, 27, back)
scor_text.set_text('Попадания', 32, BLACK)
scor_text.draw(20, 20)
scor = Leabel(430, 55, 55, 50, back)
scor.set_text('0', 32, BLACK)
scor.draw(0, 0)
start_time = time.time()
cur_time = start_time
point = 0
while True:
    if whate == 0:
        whate = 20
        click = random.randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(YELLOW)
            if i + 1 == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        whate -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].color(GREEN)
                        point += 1
                    else:
                        cards[i].color(RED)
                        point -= 1
                    cards[i].fill()
                    scor.set_text(str(point), 32, BLACK)
                    scor.draw(0, 0)
    new_time = time.time()
    if new_time - cur_time >= 1:
        timer.set_text(str(int(new_time - start_time)), 32, BLACK)
        timer.draw(0, 0)
        cur_time = new_time
    if point == 5:
        pobeda = Leabel(0, 0, 500, 500, GREEN)
        pobeda.set_text('ПОБЕДА', 80, BLACK)
        pobeda.draw(140, 190)
        break
    if new_time - start_time >= 11:
        proigrish = Leabel(0, 0, 500, 500, RED)
        proigrish.set_text('ПРОИГРЫШ', 80, BLACK)
        proigrish.draw(140,190)
        break
    pygame.display.update() 
    clock.tick(40)
pygame.display.update()
