# Ghost_Platform_Game

[![Ask DeepWiki](https://img.shields.io/badge/Ask-DeepWiki-4B32C3?logo=read-the-docs&logoColor=white)](https://deepwiki.com/Drakonosinc/Ghost_Platform_Game)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pygame-CE](https://img.shields.io/badge/Pygame--CE-2.5%2B-00A86B.svg)](https://pyga.me/)
[![PyForgeUI](https://img.shields.io/badge/UI-PyForgeUI-orange.svg)](https://pypi.org/project/pyforgeui/)
[![PyForgeAI](https://img.shields.io/badge/AI-PyForgeAI-EE4C2C.svg)](https://pypi.org/project/pyforgeai-engine/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0.html)

**Ghost_Platform_Game** is an object-oriented vertical platform jumping game built with **Pygame** and **PyTorch**. It integrates a multi-agent AI training and inference system powered by [**PyForgeAI**](https://github.com/Drakonosinc/PyForgeAI) (`pyforgeai-engine` on PyPI) supporting both Neuroevolution (Genetic Algorithms) and Deep Q-Learning (`DQNAgent`), and a modular menu interface built with [**PyForgeUI**](https://github.com/Drakonosinc/PyForgeUI) (`pyforgeui` on PyPI).

---

## Features

- **Playable & Autonomous Modes**:
  - **Player Mode**: Manual platform jumping while dodging meteorites and collecting health potions and shields.
  - **AI Mode**: Watch a pre-trained 26-input neural network track platforms, hazards, and power-ups in real time.
  - **Training AI Mode**: Simultaneous multi-agent neuroevolution (`genetic_algorithm`) and Deep Q-Network (`DQNAgent`) training.
- **Modular Ecosystem Integration**:
  - **UI Layer (`pyforgeui`)**: Interactive menus, dynamic buttons, and real-time audio/visual/key configuration screens.
  - **AI Layer (`pyforgeai-engine`)**: Multi-agent batch evaluation, `DQNAgent` + `ReplayMemory`, and automatic PyTorch checkpoint serialization.
- **Customizable Visuals, Audio & Controls**: Persistent JSON settings (`Config/config.json`) for platforms, meteorites, potions, shields, flyers, audio toggles, and key bindings.

---

## Installation & Quick Start

```bash
# 1. Install dependencies (including pyforgeui and pyforgeai-engine from PyPI)
pip install -r requirements.txt

# 2. Launch the game
python src/Main.py
```

---

## License

This project is licensed under the [GNU GPL v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## Author

Developed by [Drakonosinc](https://github.com/Drakonosinc)
