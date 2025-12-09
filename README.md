# Alien Invasion Game

A fun 2D space shooter game built with Python and Pygame. Defend your ship from waves of invading aliens!

## Game Overview

**Alien Invasion** is a classic arcade-style shooter where you:
- Control a ship at the bottom of the screen using **LEFT** and **RIGHT** arrow keys
- Shoot aliens with the **SPACE** bar
- Survive waves of aliens that move horizontally and descend toward you
- Earn points for each alien destroyed
- Lose when aliens reach the bottom or hit your ship
- Progress through increasingly difficult levels

## Features

✅ **Player Controls**
- Arrow keys for smooth left/right movement
- Space bar to fire bullets (max 3 on screen)
- Press P to restart after game over
- Press Q to quit

✅ **Game Mechanics**
- Fleet of aliens that move horizontally and drop down when hitting screen edges
- Collision detection for bullets hitting aliens
- Collision detection for aliens hitting the ship
- Game over when all lives are lost
- Level progression with increasing difficulty
- Score tracking and lives display

✅ **Visual Elements**
- Sky blue background
- Ship sprite at the bottom
- Green alien sprites in formation
- Black bullet indicators
- Game over screen with restart instructions
- On-screen score and lives counter

## Installation

### Prerequisites
- Python 3.7 or higher
- `uv` package manager

#### Installing uv

If you don't have `uv` installed, follow the [official uv installation guide](https://docs.astral.sh/uv/getting-started/installation/):

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or install via Homebrew (macOS):
```bash
brew install uv
```

For other installation methods, see the [uv documentation](https://docs.astral.sh/uv/).

### Setup

1. **Navigate to the project directory:**
```bash
cd alien_invasion
```

2. **Install dependencies:**
```bash
uv pip install pygame
```


3. **Generate the alien sprite image** (if not already created):
```bash
python create_alien_image.py
```

## Running the Game

```bash
python alien_invasion.py
```

The game window will open at 1200x800 resolution.

## Game Controls

| Key | Action |
|-----|--------|
| **LEFT Arrow** | Move ship left |
| **RIGHT Arrow** | Move ship right |
| **SPACE** | Fire bullet |
| **P** | Play again (when game over) |
| **Q** | Quit game |

## Game Settings

You can customize game parameters in `settings.py`:

- **Screen resolution**: `screen_width`, `screen_height`
- **Ship speed**: `ship_speed`
- **Bullet settings**: `bullet_speed`, `bullet_width`, `bullet_height`, `bullets_allowed`
- **Alien settings**: `alien_speed`, `fleet_drop_speed`
- **Difficulty scaling**: `speedup_scale` (multiplier for speed increase per level)

### Example: Making the game harder
```python
self.ship_speed = 2.0          # Faster ship
self.alien_speed = 2.0         # Faster aliens
self.speedup_scale = 1.2       # More aggressive difficulty scaling
```

## Project Structure

```
alien_invasion/
├── alien_invasion.py       # Main game loop and controller
├── ship.py                 # Ship sprite class
├── bullet.py               # Bullet sprite class
├── alien.py                # Alien sprite class
├── settings.py             # Game configuration and settings
├── create_alien_image.py   # Script to generate alien sprite
├── images/
│   ├── ship.bmp           # Ship sprite image
│   └── alien.bmp          # Alien sprite image
└── README.md              # This file
```

## How the Game Works

### Game Loop
1. **Check Events**: Handle player input (keyboard)
2. **Update**: Move ship, bullets, and aliens
3. **Detect Collisions**: Check for bullet-alien hits, alien-ship hits, and aliens reaching bottom
4. **Render**: Draw all sprites and UI elements
5. **Refresh**: Update display at 60 FPS

### Scoring
- **+10 points** for each alien destroyed
- **Lives**: Start with 3
- **Game Over**: When you lose all lives

### Difficulty Progression
- Each completed level (all aliens destroyed) triggers:
  - Speed increase for aliens
  - Speed increase for bullets (optional)
  - New fleet generated at original positions
- Game continues until all lives are lost

## Class Overview

### AlineInvasion (Main Game)
Manages the overall game flow, sprite groups, collisions, and game state.

**Key Methods:**
- `run_game()` - Main game loop
- `_check_events()` - Handle user input
- `_update_bullets()` - Update bullet positions
- `_update_aliens()` - Update alien positions
- `_check_collisions()` - Detect all collisions
- `_create_fleet()` - Generate alien formation
- `_ship_hit()` - Handle ship collision
- `_start_new_level()` - Progress to next level

### Ship
Player-controlled sprite that fires bullets.

**Key Methods:**
- `update()` - Move ship based on input flags
- `center_ship()` - Reset ship position
- `blitme()` - Draw ship on screen

### Bullet
Projectile fired by the ship.

**Key Methods:**
- `update()` - Move bullet upward
- `draw_bullet()` - Draw bullet on screen

### Alien
Enemy sprite in the invading fleet.

**Key Methods:**
- `update()` - Move alien horizontally
- `check_edges()` - Detect screen boundary collision

### Settings
Configuration class for all game parameters.

**Key Methods:**
- `increase_difficulty()` - Scale up game speed

## Tips & Tricks

1. **Don't waste bullets** - You can only have 3 bullets on screen at once
2. **Position matters** - Try to intercept aliens early before they descend too far
3. **Don't get cornered** - Move to the center when large groups approach
4. **Each level gets harder** - Aliens move faster with each completed level
5. **Keyboard response** - Game runs at 60 FPS for smooth, responsive controls

## Troubleshooting

### Game won't start
- Ensure pygame is installed: `uv pip list | grep pygame`
- Check Python version: `python --version` (requires 3.7+)

### Alien images not loading
- Run `python create_alien_image.py` to generate the alien sprite
- Ensure `images/` directory exists

### Game is too slow/fast
- Adjust `ship_speed`, `alien_speed` in `settings.py`
- Modify `speedup_scale` for difficulty progression

## Future Enhancement Ideas

Here are some ideas to expand the game:

- 🎵 **Sound Effects** - Add explosion and shooting sounds
- 💥 **Power-ups** - Extra lives, rapid fire, shields
- 🎨 **Better Graphics** - Improved sprite artwork
- 🎯 **Obstacles** - Bunkers/shields for strategic gameplay
- 📊 **High Scores** - Persistent leaderboard
- 🌙 **Boss Battles** - Special enemy waves with unique patterns
- 🏆 **Achievements** - Complete challenges for badges

## Learning Objectives

This project teaches:
- Object-oriented programming in Python
- Game loop structure and timing
- Sprite management with Pygame
- Collision detection algorithms
- Event-driven programming
- Game state management
- Difficulty scaling mechanics

## License

Free to use and modify for educational purposes.

## Author

Created as a learning project using Python and Pygame.

---

**Enjoy the game! 🚀👽**

