# ParticlesPy

## Overview

This is a Pygame-based particle simulation inspired by the popular particles.js library. The project creates a dynamic visualization of particles moving across the screen, drawing connection lines between nearby particles.

## Features

- Randomly generated particles with unique velocities
- Particles wrap around screen edges
- Dynamic line connections between close particles
- Smooth color interpolation based on particle depth
- Customizable particle and screen parameters

## Prerequisites

- Python 3.7+
- Pygame
- NumPy (optional, but recommended for scientific computing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/particle-simulation.git
   cd particle-simulation
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install pygame
   ```

## Project Structure

```
particle-simulation/
│
├── main.py           # Main program entry point
├── particle.py       # Particle class definition
├── particle_utilities.py  # Utility functions for particle manipulation
└── settings.py       # Configuration and constants
```

## Configuration

Modify `settings.py` to customize the simulation:

- `BACKGROUND_COLOR`: Background color
- `PARTICLE_COLOR`: Particle color
- `SCREEN_WIDTH` & `SCREEN_HEIGHT`: Screen dimensions
- `MAX_PARTICLES`: Number of particles
- `PARTICLE_SIZE`: Size of each particle
- `SPEED_SCALAR`: Velocity multiplier

## How It Works

1. Particles are initialized with random positions and velocities
2. Each particle moves independently across the screen
3. Lines are drawn between particles within a certain distance
4. Particle color fades based on its depth (z-coordinate)
5. Particles wrap around screen edges when they reach boundaries

## Running the Simulation

```bash
python main.py
```

## Performance Considerations

- Increase `MAX_PARTICLES` for more complex simulations
- Adjust `SPEED_SCALAR` to control particle movement
- Modify distance threshold in `drawLines()` to change connection behavior

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Choose an appropriate license, e.g., MIT License]

## Acknowledgments

- Inspired by particles.js
- Created using Pygame

## Todo

- [ ] Add mouse interaction
- [ ] Implement particle acceleration
- [ ] Create configurable particle behaviors
- [ ] Add performance optimizations
```
