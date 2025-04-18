# 🐾 Digital Pet Simulator 

A modular Python-based virtual pet simulator built with Object-Oriented Programming principles.

![Pet Simulator Screenshot](screenshot.png) *(Example screenshot placeholder)*

## 🌟 Features

- **Fully modular architecture** with separated concerns
- **Realistic pet attributes** (hunger, energy, happiness)
- **Trick training system** with duplicate prevention
- **Interactive menu-driven interface**
- **Visual status indicators** (star ratings)
- **Responsive pet behaviors** with conditional logic

## 📦 Project Structure
__pyche__/
├── main.py # Program entry point
├── game.py # Game interface and flow control
├── pet.py # Main Pet class
├── attributes.py # Attribute management system
└── tricks.py # Trick training system
## game controls
1. Feed your pet      - Decreases hunger
2. Play with pet      - Increases happiness (costs energy)
3. Put pet to sleep   - Restores energy
4. Teach a trick      - Add to pet's repertoire
5. View tricks        - Show learned tricks
6. Check status       - Display all stats
7. Quit               - Exit the program
## example session 
Welcome to Digital Pet Simulator!
What would you like to name your pet? Whiskers

What would you like to do?
1. Feed your pet
2. Play with your pet
3. Put pet to sleep
4. Teach a trick
5. View tricks
6. Check status
7. Quit
Enter your choice (1-7): 1
Whiskers eats happily. Hunger decreases, happiness increases!

Enter your choice (1-7): 4
What trick would you like to teach? roll over
Whiskers learned a new trick: roll over!

Enter your choice (1-7): 6

Whiskers's Status:
Hunger: ★★☆☆☆☆☆☆☆☆ (2/10)
Energy: ★★★★★☆☆☆☆☆ (5/10)
Happiness: ★★★★★★☆☆☆☆ (6/10)
Whiskers is full and satisfied.
