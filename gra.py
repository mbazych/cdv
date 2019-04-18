import pygame


# Stałe zmienne

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# ROZMIARY OKNA
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 600


class Gracz(pygame.sprite.Sprite):
    # Ta klasa reprezentuje pasek który gracz kontroluje

    # Metody
    def __init__(self):
        # Konstruktor

        # Wywołanie konstruktora rodzica
        super().__init__()

        # Zrób obraz bloku i wypełnij go kolorem
        width = 40
        height = 60
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)

        # odwołanie do kwadratu obrazu
        self.rect = self.image.get_rect()

        # Prędkosc wektora gracza
        self.change_x = 0
        self.change_y = 0

        # Lista sprite'ów na które skaczemy
        self.level = None

    def update(self):
        # Ruch gracza

        # Grawitacja
        self.calc_grav()

        # Prawo/lewo
        self.rect.x += self.change_x

        # Sprawdź, czy gracz w nic nie uderzył
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Jeżeli idziemy w prawo,
            # ustaw nasz prawy bok na lewy bok obiektu w który uderzymy
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # W innym wypadku jeżeli idziemy w lewo,
                # ustaw nasz lewy bok na prawy bok obiektu w który uderzymy
                self.rect.left = block.rect.right

        # Góra/dół
        self.rect.y += self.change_y

        # Sprawdź i zobacz czy uderzamy w cos
        block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_hit_list:
            # Zresetuj naszą pozycję bazując na górze/dole naszego obiektu
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Zatrzymaj nasz ruch
            self.change_y = 0

    def calc_grav(self):
        # Oblicz efekt grawitacji
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35

        # Sprawdź czy jestesmy na ziemi
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = SCREEN_HEIGHT.bit_length() - self.rect.height

    def jump(self):
        # Wywołuje się jesli gracz wcisnie klawisz skoku

        # idź w dół i zobacz czy jest platforma pod nami
        # idź w dół 2 pixele
        # 1 jesli platforma idzie w dol
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # Jesli mozna skoczyc, ustaw nasza predkosc na wieksza
        if len(platform_hit_list) > 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y = -10

    # Sterowanie
    def go_left(self):
        # Strzałka w lewo
        self.change_x = -6

    def go_right(self):
        # Strzałka w prawo
        self.change_x = 6

    def stop(self):
        # Nic nie klika
        self.change_x = 0

class Platform(pygame.sprite.Sprite):
    # Platforma na która gracz może skoczyć

    def __init__(self, width, height):
        # Konstruktor platformy

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(GREEN)

        self.rect = self.image.get_rect()


class Level(object):
    # Klasa rodzica konkretnego levela, kolejne levele będa dziećmi tej klasy

    def __init__(self, gracz):
        # Konstruktor klasy
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.gracz = gracz

        self.background = None

    # AKtualizuj wszystko na poziomie
    def update(self):
        self.platform_list.update()
        self.enemy_list.update()

    def draw(self, screen):
        # Rysuj wszystko na poziomie

        # Tło
        screen.fill(BLUE)

        # Rysuj wszystkie sprity
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)


class Level_01(Level):
    # Level 1

    def __init__(self, gracz):
        # Konstruktor rodzica:
        Level.__init__(self, gracz)

        # Lista szerokoci, wysokoci, pozycji x i y latform na poziomie
        level = [[210, 70, 500, 500],
                 [210, 70, 200, 400],
                 [210, 70, 600, 300],
                 [210, 70, 800, 700]
                 ]
        # Dodawanie platform
        for platform in level:
            block = Platform(platform[0], platform[1])
            block.rect.x = platform[2]
            block.rect.y = platform[3]
            block.gracz = self.gracz
            self.platform_list.add(block)


def main():
    # Funkcja main
    pygame.init()

    # Ustaw wysokosc i szerokosc ekranu
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformówka")

    # Stwórz gracza
    gracz = Gracz()

    # Stwórz poziomy
    level_list = []
    level_list.append(Level_01(gracz))

    # Ustaw poziom
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    gracz.level = current_level

    gracz.rect.x = 340
    gracz.rect.y = SCREEN_HEIGHT - gracz.rect.height
    active_sprite_list.add(gracz)

    # Pętla póki Graczn nie wyłączy gry
    done = False

    # Ustawienie jak szybko ekran sie odswieza
    clock = pygame.time.Clock()

    # -----------GŁÓWNA PĘTLA------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    gracz.go_left()
                if event.key == pygame.K_RIGHT:
                    gracz.go_right()
                if event.key == pygame.K_UP:
                    gracz.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and gracz.change_x < 0:
                    gracz.stop()
                if event.key == pygame.K_RIGHT and gracz.change_x > 0:
                    gracz.stop()

        # AKtualizacja gracza
        active_sprite_list.update()

        # akTUALIZACJA PRZEDMIOTÓw
        current_level.update()

        # JEŻELI GRACZ JEST BLISKO PRAWEJ STRONY, ŚWIAT IDZIE W LEWO (-x)
        if gracz.rect.right > SCREEN_WIDTH:
            gracz.rect.right = SCREEN_WIDTH

        # JEŻELI GRACZ BLISKO LEWEJ STRONy, ŚWIAT IDZIE W PRAWO(+x)
        if gracz.rect.left < 0:
            gracz.rect.left = 0

        # TUTAJ RYSUJEMY
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        # DOTĄD

        # 60 klatek na sekunde
        clock.tick(60)

        # Aktualizacja gry tym co narysowalimy
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
