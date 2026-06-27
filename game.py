from pygame import Rect
import sys

# Window settings
WIDTH = 1000
HEIGHT = 600
TITLE = "Forest Escape"

# Different screens in the game
MENU = "menu"
PLAYING = "playing"
GAME_OVER = "game_over"
WIN = "win"

current_state = MENU
music_on = True

class Player:
    #Main character 

    def __init__(self):

        self.width = 40
        self.height = 60

        self.x = 120
        self.y = HEIGHT - 100

        self.speed = 5

        self.velocity_y = 0
        self.gravity = 0.6
        self.jump_power = -12

        self.on_ground = True
        # Player starts with three lives
        self.health = 3
        self.score = 0
        self.animation_frame = 0
        self.animation_timer = 0          

    def move(self):

        if keyboard.left:
            self.x -= self.speed

        if keyboard.right:
            self.x += self.speed

        # Apply gravity
        self.velocity_y += self.gravity
        self.y += self.velocity_y

        # Stop at the ground
        ground = HEIGHT - 60

        if self.y >= ground - self.height:
            self.y = ground - self.height
            self.velocity_y = 0
            self.on_ground = True

        #keeping the player within the screen boundaries
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.width:
            self.x = WIDTH - self.width

    def update_animation(self):

        self.animation_timer += 1

        if self.animation_timer >= 10:
            self.animation_timer = 0
            self.animation_frame = 1 - self.animation_frame

    def jump(self):

        if self.on_ground:
            self.velocity_y = self.jump_power
            self.on_ground = False

    def draw(self):

        # animation for walking
        if keyboard.left or keyboard.right:

            if self.animation_frame == 0:
                image = "player_walk_1"
            else:
                image = "player_walk_2"

        # Idle animation
        else:

            if self.animation_frame == 0:
                image = "player_idle_1"
            else:
                image = "player_idle_2"

        screen.blit(image, (self.x, self.y))

class Enemy:
    # Enemy movement and collision detection

    def __init__(self, x, y, width, height, speed,
                 left_limit, right_limit, color):

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.speed = speed

        self.left_limit = left_limit
        self.right_limit = right_limit

        self.direction = 1
        self.color = color
        self.can_damage = True
        
        self.animation_frame = 0
        self.animation_timer = 0

    def move(self):
        # Move in the current direction and reverse if hitting walls
        self.x += self.speed * self.direction

        if self.x <= self.left_limit:
            self.direction = 1

        elif self.x >= self.right_limit:
            self.direction = -1

    def update_animation(self):
    # Switch between two animation frames

        self.animation_timer += 1

        if self.animation_timer >= 12:
            self.animation_timer = 0
            self.animation_frame = 1 - self.animation_frame

    def draw(self):

        # Brown enemy = wolf
        if self.color == (139, 69, 19):

            if self.animation_frame == 0:
                image = "wolf_walk_1"
            else:
                image = "wolf_walk_2"

        # Purple enemy = bat
        else:

            if self.animation_frame == 0:
                image = "bat_fly_1"
            else:
                image = "bat_fly_2"

        screen.blit(image, (self.x, self.y))

    def collides_with(self, player):

        enemy_rect = Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

        player_rect = Rect(
            player.x,
            player.y,
            player.width,
            player.height
        )

        return enemy_rect.colliderect(player_rect)

class Coin:
    # Collectible coin

    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.size = 20
        self.collected = False

    def draw(self):

        if not self.collected:

            screen.draw.filled_circle(
                (self.x, self.y),
                self.size // 2,
                "yellow"
            )

    def collect(self, player):

        if self.collected:
            return False

        player_rect = Rect(
            player.x,
            player.y,
            player.width,
            player.height
        )

        coin_rect = Rect(
            self.x - 10,
            self.y - 10,
            20,
            20
        )

        if player_rect.colliderect(coin_rect):
            self.collected = True
            return True

        return False

class Button:
    #button used in the main menu.

    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = Rect(x, y, width, height)

    def draw(self):
        # Draw the button
        screen.draw.filled_rect(self.rect, (40, 80, 40))
        screen.draw.rect(self.rect, "white")

        screen.draw.text(
            self.text,
            center=self.rect.center,
            fontsize=40,
            color="white"
        )

    def clicked(self, pos):
        # Check if the mouse clicked this button
        return self.rect.collidepoint(pos)


# Main menu buttons
start_button = Button("Start Game", 350, 220, 300, 60)
music_button = Button("Music: ON", 350, 320, 300, 60)
exit_button = Button("Exit", 350, 420, 300, 60)

# Creat the player
player = Player()

# Create two enemies with different  areas and colors
wolf = Enemy(500,HEIGHT - 105, 45, 45, 2, 450, 700,(139, 69, 19))

bat = Enemy(700, HEIGHT - 220, 40, 30, 3,650,900,(128, 0, 128))

coins = [
    Coin(300, HEIGHT - 80),
    Coin(420, HEIGHT - 80),
    Coin(540, HEIGHT - 80),
    Coin(760, HEIGHT - 80),
    Coin(880, HEIGHT - 80)
]


def draw():
    # Draw the current screen

    if current_state == MENU:

        screen.fill((34, 139, 34))

        screen.draw.text(
            "FOREST ESCAPE",
            center=(WIDTH // 2, 120),
            fontsize=70,
            color="yellow"
        )

        start_button.draw()
        music_button.draw()
        exit_button.draw()

    elif current_state == PLAYING:

        # Sky
        screen.fill((135, 206, 235))

        # Ground
        screen.draw.filled_rect(
            Rect(0, HEIGHT - 60, WIDTH, 60),
            (50, 180, 70)
        )

        player.draw()
        wolf.draw()
        bat.draw()

        for coin in coins:
            coin.draw()

        screen.draw.text(
            f"Health: {player.health}",
            (20, 20),
            fontsize=35,
            color="white"
        )

        screen.draw.text(
            f"Score: {player.score}",
            (20, 60),
            fontsize=35,
            color="yellow"
        )

    elif current_state == GAME_OVER:

        screen.fill((120, 0, 0))

        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=70,
            color="white"
        )

    elif current_state == WIN:

        screen.fill((0, 120, 0))

        screen.draw.text(
            "YOU WIN!",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=70,
            color="white"
        )     

def on_mouse_down(pos):
    # Handle menu clicks
    global current_state
    global music_on

    if current_state != MENU:
        return

    if start_button.clicked(pos):
        current_state = PLAYING

        if music_on:
            music.play("music_loop")

    elif music_button.clicked(pos):

        music_on = not music_on

        if music_on:
            music_button.text = "Music: ON"
            music.play("music_loop")
        else:
            music_button.text = "Music: OFF"
            music.stop()

    elif exit_button.clicked(pos):
        music.stop()
        sys.exit()

def on_key_down():

    if current_state != PLAYING:
        return

    if keyboard.space:
        sounds.jump.play()
        player.jump()

def check_collisions():
    global current_state

    for enemy in [wolf, bat]:

        if enemy.collides_with(player):

            if enemy.can_damage:
                player.health -= 1
                sounds.hit.play()
                enemy.can_damage = False

                if player.health <= 0:
                    music.stop()
                    current_state = GAME_OVER

        else:
            enemy.can_damage = True

def collect_coins():
    global current_state

    for coin in coins:

        if coin.collect(player):
            sounds.coin.play()
            player.score += 1

    if player.score == len(coins):
        music.stop()
        sounds.win.play()
        current_state = WIN
        clock.schedule(return_to_menu, 3.0)

def return_to_menu():
    global current_state, player, wolf, bat, coins

    current_state = MENU

    player = Player()
    wolf = Enemy(500, HEIGHT - 105, 45, 45, 2, 450, 700, (139, 69, 19))
    bat = Enemy(700, HEIGHT - 220, 40, 30, 3, 650, 900, (128, 0, 128))

    coins = [
        Coin(300, HEIGHT - 80),
        Coin(420, HEIGHT - 80),
        Coin(540, HEIGHT - 80),
        Coin(760, HEIGHT - 80),
        Coin(880, HEIGHT - 80)
    ]


def update():

    if current_state == PLAYING:
        player.move()
        player.update_animation()

        wolf.move()
        wolf.update_animation()

        bat.move()
        bat.update_animation()

        check_collisions()
        collect_coins()