# Project: Minimax Algorithm with Alpha-Beta Pruning

## Project Description

This project implements the **Minimax algorithm with Alpha-Beta pruning**, an optimization technique used in decision-making and game-playing AI. Minimax is a recursive algorithm that evaluates the best move for a player assuming the opponent also plays optimally. The Alpha-Beta pruning enhances Minimax by eliminating unnecessary branches, reducing computation time.

### Algorithm Logic

Minimax operates by evaluating possible game states to determine the best move:

1. **Players alternate turns:**
   - **Maximizing Player (Max):** Tries to get the highest score.
   - **Minimizing Player (Min):** Tries to get the lowest score.

2. **Tree traversal:**
   - The algorithm explores all possible moves to a given depth.
   - It assigns scores to terminal nodes (win, loss, draw, or heuristic values for ongoing states).

3. **Backpropagation of values:**
   - Max chooses the highest value from child nodes.
   - Min chooses the lowest value from child nodes.

4. **Alpha-Beta pruning:**
   - **Alpha** represents the best already found for Max.
   - **Beta** represents the best already found for Min.
   - If a node’s value is worse than a previously found option, that branch is skipped.

## Code Explanation

The implementation of the Minimax algorithm with Alpha-Beta pruning is structured as follows:

1. **Function Definition**

   ```python
   def minimax(position, depth, alpha, beta, maximizingPlayer):
   ```
   - Defines the recursive function that implements Minimax with Alpha-Beta pruning.

2. **Base Case: Evaluating Terminal Nodes**

   ```python
   if depth == 0 or is_terminal(position):
       return evaluate(position)
   ```
   - If the maximum depth is reached or a terminal state occurs, return the evaluated score.

3. **Maximizing Player’s Turn**

   ```python
   if maximizingPlayer:
       maxEval = float('-inf')
       for child in get_children(position):
           eval = minimax(child, depth - 1, alpha, beta, False)
           maxEval = max(maxEval, eval)
           alpha = max(alpha, eval)
           if beta <= alpha:
               break
       return maxEval
   ```
   - Explores all child nodes, updating the best value.
   - Updates alpha and prunes branches where further exploration is unnecessary.

4. **Minimizing Player’s Turn**

   ```python
   else:
       minEval = float('inf')
       for child in get_children(position):
           eval = minimax(child, depth - 1, alpha, beta, True)
           minEval = min(minEval, eval)
           beta = min(beta, eval)
           if beta <= alpha:
               break
       return minEval
   ```
   - Similar to Max’s turn, but chooses the lowest value and updates beta.

## How to Run the Project

### Requirements

- 🐍 Python 3.x installed

### Running the Code

1. 📥 Clone this repository:
   ```sh
   git clone https://github.com/oarthurfc/minimax.git
   cd minimax-alpha-beta
   ```
2. ▶️ Run the script:
   ```sh
   python minimax.py
   ```
3. 🕹️ Play against the AI or analyze game moves.

## Asymptotic Complexity

| Case         | Complexity       |
|-------------|-----------------|
| ⚡ Best case | \(O(b^{d/2})\)  |
| ⚡ Worst case | \(O(b^d)\)      |

Where:
- **b** = branching factor (number of moves per state)
- **d** = depth of the search tree

The Alpha-Beta pruning helps **reduce** the number of nodes evaluated compared to the standard **O(b^d)** complexity of Minimax, making it much more efficient in deep searches.

## References

- 📚 [Minimax Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Minimax)
- 📚 [Alpha-Beta Pruning - GeeksforGeeks](https://www.geeksforgeeks.org/alpha-beta-pruning/)
- 🎮 [Game AI Techniques](https://www.redblobgames.com/)

