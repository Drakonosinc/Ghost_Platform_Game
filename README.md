# Ghost_Platform_Game

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Pygame](https://img.shields.io/badge/Engine-Pygame--CE-green)
![PyForgeUI](https://img.shields.io/badge/UI-PyForgeUI-blueviolet)
![PyForgeAI](https://img.shields.io/badge/AI-PyForgeAI-orange)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Drakonosinc/Ghost_Platform_Game)

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
