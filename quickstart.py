#!/usr/bin/env python
"""
Quick Start Guide for Alien Invasion Game

This script provides an interactive setup and quick start for the game.
"""

import os
import sys
import subprocess


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def check_python_version():
    """Check if Python version is 3.7 or higher."""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7+ required!")
        print(f"   Current version: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor} OK")
    return True


def check_pygame():
    """Check if pygame is installed."""
    try:
        import pygame
        print(f"✅ pygame {pygame.version.ver} installed")
        return True
    except ImportError:
        print("❌ pygame not found")
        return False


def install_dependencies():
    """Attempt to install pygame."""
    print("Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "pygame"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        print("   Try: pip install pygame")
        return False


def create_alien_image():
    """Create the alien sprite image."""
    if os.path.exists("images/alien.bmp"):
        print("✅ Alien sprite already exists")
        return True

    print("Creating alien sprite...")
    try:
        subprocess.check_call([sys.executable, "create_alien_image.py"])
        print("✅ Alien sprite created")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to create alien sprite")
        return False


def start_game():
    """Start the game."""
    print("\n🚀 Starting Alien Invasion...")
    print("Controls: LEFT/RIGHT arrows to move, SPACE to shoot, P to restart, Q to quit\n")
    try:
        subprocess.call([sys.executable, "alien_invasion.py"])
    except KeyboardInterrupt:
        print("\n\nGame interrupted by user")


def main():
    """Main setup and launch."""
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    print_header("ALIEN INVASION - Quick Start")

    # Check Python version
    if not check_python_version():
        sys.exit(1)

    # Check pygame
    if not check_pygame():
        print("\n📦 Would you like to install pygame? (y/n): ", end="")
        if input().lower() == 'y':
            if not install_dependencies():
                sys.exit(1)
        else:
            print("Cannot run game without pygame")
            sys.exit(1)

    # Create alien image if needed
    if not create_alien_image():
        print("Warning: Alien sprite might not load correctly")

    print_header("Ready to Play!")
    print("Press ENTER to start the game...")
    input()

    start_game()

    print_header("Thanks for Playing!")
    print("For more information, see README.md")


if __name__ == "__main__":
    main()

