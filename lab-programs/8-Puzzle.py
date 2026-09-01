from queue import PriorityQueue

goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def print_board(state):
    for i in range(0, 9, 3):
        row = [" " if val == 0 else str(val) for val in state[i:i+3]]
        print(" | ".join(row))
    print("-" * 9)

def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            tile = state[i*3 + j]
            if tile != 0:
                x, y = (tile - 1) // 3, (tile - 1) % 3
                distance += abs(x - i) + abs(y - j)
    return distance

def successors(state):
    result = []
    i = state.index(0)

    if i % 3 != 0:  # Move Left
        s = list(state)
        s[i], s[i-1] = s[i-1], s[i]
        result.append(tuple(s))

    if i % 3 != 2:  # Move Right
        s = list(state)
        s[i], s[i+1] = s[i+1], s[i]
        result.append(tuple(s))

    if i // 3 != 0:  # Move Up
        s = list(state)
        s[i], s[i-3] = s[i-3], s[i]
        result.append(tuple(s))

    if i // 3 != 2:  # Move Down
        s = list(state)
        s[i], s[i+3] = s[i+3], s[i]
        result.append(tuple(s))

    return result

def solve(initial):
    frontier = PriorityQueue()
    # Now storing path history: (f_score, g_score, state, path)
    frontier.put((heuristic(initial), 0, initial, [initial]))
    explored = set()

    while not frontier.empty():
        _, g, state, path = frontier.get()

        # GOAL FOUND: Return the list of states (path)
        if state == goal_state:
            return path

        if state in explored:
            continue

        explored.add(state)

        for s in successors(state):
            if s not in explored:
                new_g = g + 1
                f = new_g + heuristic(s)
                frontier.put((f, new_g, s, path + [s]))

    return None


initial_state = (1, 2, 3, 
                 5, 0, 7, 
                 6, 4, 8)

path = solve(initial_state)

if path:
    print(f"Solved in {len(path) - 1} moves!\n")
    for step, board in enumerate(path):
        print(f"Step {step}:")
        print_board(board)
else:
    print("Unsolvable puzzle.")