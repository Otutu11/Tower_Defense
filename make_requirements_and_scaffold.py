#!/usr/bin/env python3
"""Create a Tower_Defense scaffold with requirements.txt and core folders."""
import argparse, pathlib

FOLDERS = ["enemies", "main_menu", "menu", "towers"]
REQUIREMENTS = "# Runtime\npygame>=2.5.0\nnumpy>=1.24\npyyaml>=6.0.1\nloguru>=0.7.2\n\n# Optional (uncomment if you use them)\n# pillow>=10.0\n# pysdl2>=0.9.16\n# screeninfo>=0.8.1\n\n# Dev tools (optional)\n# black>=24.0\n# isort>=5.13\n# mypy>=1.10\n# pytest>=8.0\n"
STARTER_MAIN = "import pygame\nimport sys\n\nWIDTH, HEIGHT = 960, 540\nFPS = 60\n\ndef main():\n    pygame.init()\n    screen = pygame.display.set_mode((WIDTH, HEIGHT))\n    pygame.display.set_caption(\"Tower Defense \u2014 Starter\")\n    clock = pygame.time.Clock()\n\n    running = True\n    while running:\n        for event in pygame.event.get():\n            if event.type == pygame.QUIT:\n                running = False\n\n        screen.fill((20, 24, 28))\n        pygame.display.flip()\n        clock.tick(FPS)\n\n    pygame.quit()\n    sys.exit()\n\nif __name__ == \"__main__\":\n    main()\n"

def write(base: pathlib.Path, rel: str, content: str):
    p = base / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return p

def make(base: pathlib.Path):
    base.mkdir(parents=True, exist_ok=True)
    for name in FOLDERS:
        (base / name).mkdir(parents=True, exist_ok=True)
        write(base, f"{name}/__init__.py", "# package\n")
    write(base, "requirements.txt", REQUIREMENTS)
    write(base, "main.py", STARTER_MAIN)
    print(f"✓ Created scaffold at: {base}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--path", default="./Tower_Defense")
    args = ap.parse_args()
    make(pathlib.Path(args.path).resolve())

if __name__ == "__main__":
    main()
