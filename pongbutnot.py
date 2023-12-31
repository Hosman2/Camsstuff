import simpleGE
import pygame
import random

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setCaption("2 Player Projectile Dodger")
        self.background = pygame.image.load("sky.png")
        self.background = pygame.transform.scale(self.background, (640, 480))

        self.projectile = Projectile(self)
        self.player1 = Player(self)
        self.player2 = Player2(self)

        self.lblLives = simpleGE.Label()
        self.lblLives.text = "Lives: 5"
        self.lblLives.center = (50, 15)
        self.Lives = 5

        self.lblLives2 = simpleGE.Label()
        self.lblLives2.text = "Lives: 5"
        self.lblLives2.center = (600, 15)
        self.Lives2 = 5

        self.sprites = [self.projectile, self.lblLives, self.lblLives2, self.player1, self.player2]

    def update(self):
        self.lblLives.text = f"lives: {self.Lives}"
        self.lblLives2.text = f"lives: {self.Lives2}"



class Player(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cat.gif")
        self.setSize(100, 100)
        self.moveSpeed = 5
        self.lives = 3
        self.x = 35
        self.y = 240



    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_w):
            self.y -= 20
        if self.scene.isKeyPressed(pygame.K_s):
            self.y += 20


class Player2(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("cat2.gif")
        self.setSize(100, 100)
        self.moveSpeed = 5
        self.lives = 3
        self.x = 605
        self.y = 240


    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_UP):
            self.y -= 20
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.y += 20


class Projectile(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("fireball.gif")
        self.setSize(100, 100)
        self.moveSpeed = 5
        self.x = 320
        self.y = 240
        self.moveSpeed = 10
        self.x = 320
        self.y = 240
        self.dx = 5
        self.dy = 5


    def update(self):
        super().update()

        self.x += self.dx
        self.y += self.dy

        if self.x <= 1:
            self.dx += 0
            self.dy += 0
            self.dx = -self.dx

        if self.x >= 640:
            self.dx += 0
            self.dy += 0
            self.dx = -self.dx


        if self.y <= 1:
            self.dx += 0
            self.dy += 0
            self.dy = -self.dy

        if self.y >= 460:
            self.dx += 0
            self.dy += 0
            self.dy = -self.dy


    def checkEvents(self):
        if self.collidesWith(self.scene.player1):
            self.scene.Lives -= 1
            self.moveSpeed = 10
            self.reset()
        if self.collidesWith(self.scene.player2):
            self.scene.Lives2 -= 1
            self.moveSpeed = 10
            self.reset()
        if self.scene.Lives <= 0:
            self.scene.stop()
            pygame.quit()
        if self.scene.Lives2 <= 0:
            self.scene.stop()
            pygame.quit()
    def reset(self):
        self.x = 320
        self.y = 240


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
