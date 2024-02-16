import pygame
import random
import import_sprite as sprite

SIZE_SPRITES = (80, 100) # добавила фиксированный размер спрайта

################# ваш код ##################
# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) # Добавляем белый цвет

# Константы
ROAD_WIDTH = 300
SCREEN_HEIGHT = 500

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((ROAD_WIDTH, SCREEN_HEIGHT))

# Флаг выполнения основного цикла1
run = True
# Начальные координаты игрока, X и Y необходимо устанавливать так, чтобы 
# игрок не сталкивался с машинами сразу при начале игры
player_x = 0
player_y = 350

# Переменные для контроля генерации
y_generation_car = 0
y_generation_coin = 100
y1 = 100


# cars = []
coins = []  # Создаем список для монет
coin_count = 0  # Счетчик монет
#####################################
# вместо списка cars, создаем группу спрайтов:
cars_group = pygame.sprite.Group()
hero_groups = pygame.sprite.Group()
coins_groups = pygame.sprite.Group()
# добавила наследование
class AngryCar(pygame.sprite.Sprite):
    # картинку грузим сразу в классе
    car = pygame.transform.scale(pygame.image.load("data/car.png"), SIZE_SPRITES)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = pygame.transform.rotate(AngryCar.car, 180) # Изменяем размер изображения машины
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(x, y)

    # draw_car -> update, тк этот метод самостоятельно определяется в нашем классе
    def update(self):
        # screen.blit(self.image, (self.x, self.y)) # убираем рисование на холсте, спрайт умеет рисовать себя сам
        self.move(self.x, self.y + 2) # перемещаем спрайт в заданные координаты
        

    def move(self, x, y):
        # перемещение спрайта в заданные координаты
        x_c, y_c = self.image.get_size()
        self.rect = self.image.get_rect(center=(x_c // 2, y_c // 2)).move(x, y)
        self.x = x
        self.y = y

class Player(pygame.sprite.Sprite):
    hero = pygame.transform.scale(pygame.image.load("data/vasiliy.png"), SIZE_SPRITES)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = Player.hero
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(x, y)

    # draw_car -> update, тк этот метод самостоятельно определяется в нашем классе
    def update(self, *args):
        # screen.blit(self.image, (self.x, self.y)) # убираем рисование на холсте, спрайт умеет рисовать себя сам
        self.move(self.x, self.y) # перемещаем спрайт в заданные координаты
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_LEFT and self.x > 0:
                self.move(self.x - 100, self.y )
            elif args[0].key == pygame.K_RIGHT and self.x < ROAD_WIDTH:
                self.move(self.x + 100, self.y )

        # ПРОВЕРКА НА СТОЛКНОВЕНИЯ
        if pygame.sprite.spritecollideany(self, cars_group):
            global run
            print('Проигрыш')
            run = False
        class Player(pygame.sprite.Sprite):
    # другой код класса Player
            def update(self, *args):
        # другой код обновления игрока
                if pygame.sprite.spritecollideany(self, coins_groups):
                    for coin in pygame.sprite.spritecollide(self, coins_groups, True):
                        coin_count += 1

    def move(self, x, y):
        # перемещение спрайта в заданные координаты
        x_c, y_c = self.image.get_size()
        self.rect = self.image.get_rect(center=(x_c // 2, y_c // 2)).move(x, y)
        self.x = x
        self.y = y


class Coin(pygame.sprite.Sprite):
    # картинку грузим сразу в классе
    coin = pygame.transform.scale(pygame.image.load("data/coin.png"), SIZE_SPRITES)

    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.x = x
        self.y = y
        self.image = Coin.coin
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(x, y)

    # draw_car -> update, тк этот метод самостоятельно определяется в нашем классе
    def update(self, *args):
        # screen.blit(self.image, (self.x, self.y)) # убираем рисование на холсте, спрайт умеет рисовать себя сам
        self.move(self.x, self.y + 5) # перемещаем спрайт в заданные координаты
      
    def move(self, x, y):
        # перемещение спрайта в заданные координаты
        x_c, y_c = self.image.get_size()
        self.rect = self.image.get_rect(center=(x_c // 2, y_c // 2)).move(x, y)
        self.x = x
        self.y = y
       

clock = pygame.time.Clock()  # Таймер для контроля FPS

# Основной цикл игры
Player(player_x, player_y, hero_groups) # заранее создаем персонажа

while run:
    y1 += 1
    i = random.randint(1, 3)
    j = random.randint(1, 3)

    # Генерация машин (не понимаю для чего...)
    if y1 > y_generation_car:
        x3 = random.choice(range(0, ROAD_WIDTH, ROAD_WIDTH // 3)) + 5
        y_generation_car += 300
        # cars.append(AngryCar(x3, -sprite.car.image.get_height()))  # Начальная позиция над экраном
        AngryCar(x3, -SIZE_SPRITES[1] // 2, cars_group)

    # Генерация монет
    if y1 > y_generation_coin:
        x4 = random.choice([10, 15, 120])
        y_generation_coin += 100
        Coin(x3, -SIZE_SPRITES[1] // 2, coins_groups)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            hero_groups.update(event)

    screen.fill(BLACK)
    screen.blit(sprite.road.image, (0, 0))
    # screen.blit(sprite.Vasia.image, (player_x, player_y))
    hero_groups.draw(screen)
    hero_groups.update()

    coins_groups.draw(screen)
    coins_groups.update()

    cars_group.draw(screen) # вот эта одна строчка заменяет весь ваш цикл for
    cars_group.update()
    # Отображаем счетчик монет
    GREEN = (50,255,0)
    coin_font = pygame.font.SysFont("Arial", 32, bold = True)
    coin_text = coin_font.render("Монеты: " + str(coin_count), True, GREEN) # Создаем текст с белым цветом
    screen.blit(coin_text, (10, 10)) # Рисуем текст в левом верхнем углу
    
    # pygame.display.update() ????
    pygame.display.flip()
    clock.tick(60)  # Установка FPS
    
else:
        message_font = pygame.font.SysFont("Arial", 48, bold = True)
        message_text = message_font.render("Ты проиграл", True, (255, 0, 0))
        screen.blit(message_text, (ROAD_WIDTH // 2 - message_text.get_width() // 2, SCREEN_HEIGHT // 2 - message_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
pygame.quit()