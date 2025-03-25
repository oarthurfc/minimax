import math

def minimax(node, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or isinstance(node, int):
        return node  

    if maximizingPlayer:
        maxEval = -math.inf
        for child in node:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  
        return maxEval
    else:
        minEval = math.inf
        for child in node:
            eval = minimax(child, depth - 1, alpha, beta, True)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return minEval

tree = [
    [[3, 5], [6, 9]],  
    [[1, 2], [0, -1]]  
]

result = minimax(tree, 3, -math.inf, math.inf, True)
print("Minimax Alpha-Beta result:", result)