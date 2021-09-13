import pygame
import random


class Pane:

    def __init__(self):
        pygame.init()
        self.b1 = pygame.Rect(50, 200, 80, 40)
        self.b2 = pygame.Rect(270, 200, 80, 40)
        self.text_style = pygame.font.SysFont('Arial', 20)
        self.dis = pygame.display.set_mode((400, 400))
        self.cards = []
        self.card_style = ["spades", "club", "heart", "diamond"]
        self.show_cards = []
        self.player1 = []
        self.player2 = []
        self.player2_card = "  "
        self.player1_card = "  "

    def add(self, game_over, num1, num2, white, black, player_one_cards, player_two_cards):
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.b1.collidepoint(event.pos):
                            self.dis.fill(black, (50, 100, 200, 80))
                            self.dis.blit(self.text_style.render(str(self.player1[num1]), True, white), (50, 100))
                            self.player1_card = str(self.player1[num1])
                            num1 += 1
                            player_one_cards -= 1
                            self.dis.fill(black, (50, 300, 300, 50))
                            self.dis.blit(
                                self.text_style.render("Number of cards for p1: {}".format(player_one_cards), True,
                                                       white), (50, 300))
                            if self.player1_card[0:2] == self.player2_card[0:2]:
                                player_one_cards = 52 - player_two_cards
                                self.dis.fill((0, 0, 0), (50, 300, 300, 50))
                                self.dis.blit(
                                    self.text_style.render("Number of cards for p1: {}".format(player_one_cards), True,
                                                           (255, 255, 255)), (50, 300))
                        if self.b2.collidepoint(event.pos):
                            self.dis.fill(black, (270, 100, 300, 80))
                            self.dis.blit(self.text_style.render(str(self.player2[num2]), True, white), (270, 100))
                            self.player2_card = str(self.player2[num2])
                            num2 += 1
                            player_two_cards -= 1
                            self.dis.fill(black, (50, 350, 300, 50))
                            self.dis.blit(
                                self.text_style.render("Number of cards for p2: {}".format(player_two_cards), True,
                                                       white), (50, 350))
                            if self.player2_card[0:2] == self.player1_card[0:2]:
                                player_two_cards = 52 - player_one_cards
                                self.dis.fill((0, 0, 0), (50, 350, 300, 50))
                                self.dis.blit(
                                    self.text_style.render("Number of cards for p2: {}".format(player_two_cards), True,
                                                           (255, 255, 255)), (50, 350))
            pygame.draw.rect(self.dis, (0, 0, 255), self.b1)
            pygame.draw.rect(self.dis, (255, 0, 0), self.b2)
            self.dis.blit(self.text_style.render("Player 1", True, (0, 0, 0)), (50, 200))
            self.dis.blit(self.text_style.render("Player 2", True, (0, 0, 0)), (270, 200))
            pygame.display.set_caption("Let's play card game!")
            pygame.display.update()
        pygame.quit()

    def create_cards(self):
        for card in range(1, 53):
            self.cards.append(card)

        for style in range(0, 4):
            for num in range(0, 13):
                self.show_cards.append(str(self.cards[num]) + " of " + self.card_style[style])
        random.shuffle(self.show_cards)

        for x in range(0, 26):
            self.player1.append(self.show_cards[x])

        for y in range(26, 52):
            self.player2.append(self.show_cards[y])


if __name__ == "__main__":
    pane = Pane()
    pane.create_cards()
    pane.add(False, 0, 0, (255, 255, 255), (0, 0, 0), 26, 26)

