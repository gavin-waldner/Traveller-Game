# Traveller Game

A simple text-based dice-rolling adventure game where a traveller journeys down a road, facing challenges and trying to reach the end before running out of health.

## Files

### `main.py`
This is the main game script. It:
- Initializes the game environment (`road` and `health` files)
- Accepts a random seed as a command-line argument
- Begins the game loop where the player rolls a die to move forward, take damage, or trigger special events
- Accepts user inputs:  
  - `r` to roll the dice  
  - `p` to consume a potion (placeholder, no defined mechanics yet)  
  - `q` to quit the game  

### `traveller_functions.py`
A helper module that manages health and movement:
- `getHealth()` – Reads and displays current health
- `saveHealth(currentHealth)` – Updates health in file
- `takeDamage(dmg)` – Reduces health and checks for game over
- `getRoad()` – Reads and returns current road state
- `printRoad()` – Displays the current road
- `saveRoad(cRoad)` – Saves the current road layout
- `moveForward()` / `moveBackward()` – Moves the traveller symbol (`'X'`) along the road

## How to Run

```bash
python main.py <seed>
```

- Replace `<seed>` with any integer to initialize the random number generator.
- The game state is stored in two files: `health` and `road`.

## Notes
- Winning condition: Reach the end of the road (position 9).
- Losing condition: Health reaches 0.
- The special event on rolling a 3 offers a 1 in 10 chance of instant victory.
