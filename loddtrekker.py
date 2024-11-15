fullscreen = False

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import secrets

# Initialize Pygame
pygame.init()

# Detect screen resolution
info_object = pygame.display.Info()
screen_width, screen_height = info_object.current_w, info_object.current_h
if not fullscreen:
    screen_width, screen_height = 1280, 720

# Set up display
if fullscreen:
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Loddtrekkern 3000")


class enkeltlodd():
    def __init__(self, color=None, letter=None, number=None):
        self.color_name_to_rgb = {
            "rød": (200, 0, 0),
            "grønn": (0, 200, 0),
            "blå": (100, 100, 255),  # Lighter blue
            "gul": (200, 200, 0),
            "oransje": (200, 130, 0),
            "lilla": (100, 0, 100),
            "lyseblå": (140, 180, 200),
            "rosa": (200, 80, 140),  # Less bright pink
            "fersken": (200, 170, 150)
        }
        self.letter = letter
        self.number = number
        self.color = self.color_name_to_rgb[color] if color else (255, 255, 255)  # Default to white if color is None
    def __str__(self):
        color_name = next((name for name, rgb in self.color_name_to_rgb.items() if rgb == self.color), "ukjent farge")
        return f"Farge: {color_name}, Bokstav: {self.letter}, Nummer: {self.number}"
    


alle_lodd  = []

def legg_til_loddserie(farge, bokstav, tallserie):
    for tall in tallserie:
        alle_lodd.append(enkeltlodd(farge, bokstav, tall))




# Font settings
font = pygame.font.Font(None, int(screen_width*0.12))

# Function to draw slot machine result
def draw_result(winner=None, color_picked=False, letter_picked=False, number_picked=False):
    screen.fill((0, 0, 0))
    
    totalt_lodd = len(alle_lodd)


    random_lodd = secrets.choice(alle_lodd)
    color = random_lodd.color
    letter = random_lodd.letter
    number = random_lodd.number

    if color_picked:
        color = winner.color
        letter = secrets.choice([lodd.letter for lodd in alle_lodd if lodd.color == color])
        number = secrets.choice([lodd.number for lodd in alle_lodd if lodd.color == color and lodd.letter == letter])
    if letter_picked: 
        letter = winner.letter
        number = secrets.choice([lodd.number for lodd in alle_lodd if lodd.color == color and lodd.letter == letter])
    if number_picked: 
        number = winner.number

    rect_width, rect_height = screen_width*0.4, screen_height*0.7
    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2
    
    pygame.draw.rect(screen, color, (rect_x, rect_y, rect_width, rect_height))
    
    combined_text = letter + " " + "{:02d}".format(number)
    combined_text_rendered = font.render(combined_text, True, (0, 0, 0))
    combined_rect = combined_text_rendered.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
    
    screen.blit(combined_text_rendered, combined_rect)

    pygame.display.flip()



def main():
    running = True
    color_picked = False
    number_picked = False
    letter_picked = False
    winner = secrets.choice(alle_lodd)
    print(winner)

    while running:
        delay = 150
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

                if event.key == pygame.K_PAGEDOWN or event.key == pygame.K_PAGEUP or event.key == pygame.K_SPACE: # Neste steg
                    if not color_picked and not letter_picked and not number_picked:
                        color_picked = True
#                        delay = 400
                    elif color_picked and not letter_picked:
                        letter_picked = True
 #                       delay = 400
                    elif letter_picked and not number_picked:
                        number_picked = True
  #                      delay = 400

                if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE: # Start på nytt
                    # Same cannot win twice in a row
                    new_winner = secrets.choice(alle_lodd)
                    while new_winner == winner:
                        new_winner = secrets.choice(alle_lodd)
                    winner = new_winner
                    print(winner)
                    
                    color_picked = False
                    number_picked = False
                    letter_picked = False


        draw_result(winner, color_picked, letter_picked, number_picked)
        pygame.time.delay(delay)

    pygame.quit()

superlodd_serie_a = [
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]
superlodd_serie_b = [
     1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50
]
x_lodd = superlodd_serie_a + [x + 50 for x in superlodd_serie_b]

# LEGG TIL LODDSERIER HER

# Pakkeserie A
legg_til_loddserie("gul",     "C", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("gul",     "J", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("gul",     "B", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("rosa",    "H", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("rosa",    "V", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("grønn",   "Q", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("grønn",   "W", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("blå",     "Y", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("blå",     "I", superlodd_serie_a + list(range(51, 51)))
legg_til_loddserie("blå",     "R", superlodd_serie_a + list(range(51, 51)))


# Pakkeserie B
legg_til_loddserie("gul",     "A", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("gul",     "L", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("rosa",    "D", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("rosa",    "O", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("rosa",    "K", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("grønn",   "V", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("grønn",   "E", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("blå",     "F", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("blå",     "P", superlodd_serie_b + list(range(51, 51)))
legg_til_loddserie("blå",     "M", superlodd_serie_b + list(range(51, 51)))


# Superlodd
legg_til_loddserie("blå", "X", x_lodd )

#legg_til_loddserie("blå", "Z", range(51, 51))
#legg_til_loddserie("grønn", "E", range(51, 51))
#legg_til_loddserie("fersken", "Y", [5,6,91,92,93,94,95,96,97,98,99])
print("Totalt antall lodd:", len(alle_lodd))
print("Sannsynlighet for å vinne:", "{:.2%}".format(1/len(alle_lodd)))

if __name__ == "__main__":
    main()
