import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlineInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = Group()
        self.aliens = Group()

        self._create_fleet()

        # Game statistics
        self.game_active = True
        self.score = 0
        self.lives = 3

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._handle_keydown(event)
            elif event.type == pygame.KEYUP:
                self._handle_keyup(event)

    def _handle_keydown(self, event):
        """Handle key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_p:
            if not self.game_active:
                self._restart_game()

    def _handle_keyup(self, event):
        """Handle key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed and self.game_active:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Draw all bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw all aliens
        self.aliens.draw(self.screen)

        # Display score and lives
        self._draw_stats()

        # Display game over message if game is inactive
        if not self.game_active:
            self._draw_game_over()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def _draw_stats(self):
        """Draw current score and lives on the screen."""
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        lives_text = font.render(f"Lives: {self.lives}", True, (0, 0, 0))

        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (self.settings.screen_width - 200, 10))

    def _draw_game_over(self):
        """Draw game over message."""
        font = pygame.font.SysFont(None, 72)
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        restart_text = pygame.font.SysFont(None, 36).render("Press P to Play Again or Q to Quit", True, (255, 0, 0))

        game_over_rect = game_over_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2 - 50))
        restart_rect = restart_text.get_rect(center=(self.settings.screen_width // 2, self.settings.screen_height // 2 + 50))

        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(restart_text, restart_rect)

    def _update_bullets(self):
        """Update position of bullets and remove off-screen bullets."""
        # Update bullet positions
        self.bullets.update()

        # Remove bullets that have gone off the top of the screen
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens that fit on a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * ship_height) - alien_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the fleet."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond if any aliens have hit an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_collisions(self):
        """Check for collisions between bullets and aliens, and between aliens and the ship."""
        # Check if any bullets have hit aliens
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens_hit in collisions.values():
                self.score += len(aliens_hit) * 10

        # Check if aliens have hit the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break

        # Check if all aliens have been destroyed
        if not self.aliens:
            self._start_new_level()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.lives > 1:
            self.lives -= 1
            self._reset_positions()
        else:
            self.game_active = False

    def _reset_positions(self):
        """Reset the positions of the ship and aliens."""
        # Clear all bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

    def _start_new_level(self):
        """Start a new level by increasing difficulty and resetting positions."""
        self.settings.increase_difficulty()
        self._reset_positions()

    def _restart_game(self):
        """Restart the game."""
        self.game_active = True
        self.score = 0
        self.lives = 3
        self.settings.speedup_scale = 1.1
        self.settings.alien_speed = 1.0
        self.settings.fleet_direction = 1
        self._reset_positions()


if __name__ == '__main__':
    # Make a game instance and run the game.
    ai = AlineInvasion()
    ai.run_game()
