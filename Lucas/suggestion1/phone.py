import pygame
import os
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 700
ICON_SIZE = 80
BUTTON_SIZE = 60
BUTTON_BAR_HEIGHT = 70

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

# Paths
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
BG_PATH = os.path.join(CURRENT_DIR, 'background.png')
BACK_BUTTON_PATH = os.path.join(PARENT_DIR, 'icons', 'button_back.png')
HOME_BUTTON_PATH = os.path.join(PARENT_DIR, 'icons', 'button_home.png')
OPTIONS_BUTTON_PATH = os.path.join(PARENT_DIR, 'icons', 'button_options.png')
ICON_1_PATH = os.path.join(PARENT_DIR, 'icons', 'icon_1_1.png')
ICON_2_PATH = os.path.join(PARENT_DIR, 'icons', 'icon_1_2.png')

# App class - base class for all apps
class App:
    def __init__(self, name, color=(100, 100, 100)):
        self.name = name
        self.color = color
        
    def draw(self, screen):
        # Create a rectangle filling most of the screen
        app_rect = pygame.Rect(20, 20, SCREEN_WIDTH - 40, SCREEN_HEIGHT - BUTTON_BAR_HEIGHT - 40)
        pygame.draw.rect(screen, self.color, app_rect)
        
        # Draw app name
        font = pygame.font.SysFont('Arial', 30)
        text = font.render(self.name, True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(text, text_rect)
        
    def handle_event(self, event):
        pass

# Example apps
class App1(App):
    def __init__(self):
        super().__init__('App 1', RED)

class App2(App):
    def __init__(self):
        super().__init__('App 2', BLUE)

# Selection UI - Main menu with app icons
class Selection_UI:
    def __init__(self):
        self.apps = [App1(), App2()]
        
        # Load icon images
        self.icon_images = [
            pygame.image.load(ICON_1_PATH).convert_alpha(),
            pygame.image.load(ICON_2_PATH).convert_alpha()
        ]
        
        # Scale icons if needed
        for i in range(len(self.icon_images)):
            self.icon_images[i] = pygame.transform.scale(self.icon_images[i], (ICON_SIZE, ICON_SIZE))
        
        # Create icon rectangles
        self.icon_rects = [
            pygame.Rect(80, 200, ICON_SIZE, ICON_SIZE),
            pygame.Rect(240, 200, ICON_SIZE, ICON_SIZE)
        ]
        
    def draw(self, screen):
        # Draw app icons
        for i, rect in enumerate(self.icon_rects):
            screen.blit(self.icon_images[i], rect)
            
            # Draw app name under icon
            font = pygame.font.SysFont('Arial', 20)
            text = font.render(self.apps[i].name, True, BLACK)
            text_rect = text.get_rect(center=(rect.centerx, rect.bottom + 20))
            screen.blit(text, text_rect)
    
    def handle_click(self, pos):
        for i, rect in enumerate(self.icon_rects):
            if rect.collidepoint(pos):
                return self.apps[i]
        return None

# Main UI class
class Phone_UI:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Phone Simulation')
        
        # Load images
        self.bg_image = pygame.image.load(BG_PATH).convert()
        self.bg_image = pygame.transform.scale(self.bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.back_button = pygame.image.load(BACK_BUTTON_PATH).convert_alpha()
        self.back_button = pygame.transform.scale(self.back_button, (BUTTON_SIZE, BUTTON_SIZE))
        
        self.home_button = pygame.image.load(HOME_BUTTON_PATH).convert_alpha()
        self.home_button = pygame.transform.scale(self.home_button, (BUTTON_SIZE, BUTTON_SIZE))
        
        self.options_button = pygame.image.load(OPTIONS_BUTTON_PATH).convert_alpha()
        self.options_button = pygame.transform.scale(self.options_button, (BUTTON_SIZE, BUTTON_SIZE))
        
        # Create button rectangles
        self.back_rect = pygame.Rect(50, SCREEN_HEIGHT - BUTTON_BAR_HEIGHT + 5, BUTTON_SIZE, BUTTON_SIZE)
        self.home_rect = pygame.Rect(SCREEN_WIDTH // 2 - BUTTON_SIZE // 2, SCREEN_HEIGHT - BUTTON_BAR_HEIGHT + 5, BUTTON_SIZE, BUTTON_SIZE)
        self.options_rect = pygame.Rect(SCREEN_WIDTH - 50 - BUTTON_SIZE, SCREEN_HEIGHT - BUTTON_BAR_HEIGHT + 5, BUTTON_SIZE, BUTTON_SIZE)
        
        # Initialize UI elements
        self.selection_ui = Selection_UI()
        self.current_app = None
        self.clock = pygame.time.Clock()
        
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click
                        if self.back_rect.collidepoint(event.pos):
                            self.current_app = None
                        elif self.home_rect.collidepoint(event.pos):
                            self.current_app = None
                        elif self.options_rect.collidepoint(event.pos):
                            pass  # Options functionality could be added here
                        elif self.current_app is None:
                            # Check if app icon was clicked
                            app = self.selection_ui.handle_click(event.pos)
                            if app:
                                self.current_app = app
            
            self.draw()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()
    
    def draw(self):
        # Draw background
        self.screen.blit(self.bg_image, (0, 0))
        
        # Draw current UI
        if self.current_app:
            self.current_app.draw(self.screen)
        else:
            self.selection_ui.draw(self.screen)
        
        # Draw navigation bar background
        nav_bar_rect = pygame.Rect(0, SCREEN_HEIGHT - BUTTON_BAR_HEIGHT, SCREEN_WIDTH, BUTTON_BAR_HEIGHT)
        pygame.draw.rect(self.screen, GRAY, nav_bar_rect)
        
        # Draw navigation buttons
        self.screen.blit(self.back_button, self.back_rect)
        self.screen.blit(self.home_button, self.home_rect)
        self.screen.blit(self.options_button, self.options_rect)

# Run the phone UI
if __name__ == '__main__':
    phone = Phone_UI()
    phone.run()
