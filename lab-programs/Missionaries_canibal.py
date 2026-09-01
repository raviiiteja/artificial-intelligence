from collections import deque


def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    
    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False

    
    if m_left > 0 and c_left > m_left:
        return False

    if m_right > 0 and c_right > m_right:
        return False

    return True



def missionaries_cannibals():
    
    start = (3, 3, 'L')
    goal = (0, 0, 'R')

    
    moves = [
        (2, 0),  
        (0, 2),  
        (1, 1),  
        (1, 0), 
        (0, 1)   
    ]

    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        m, c, boat = state

        for dm, dc in moves:

            if boat == 'L':
                new_state = (m - dm, c - dc, 'R')
            else:
                new_state = (m + dm, c + dc, 'L')

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    queue.append((new_state, path + [new_state]))

    return None


# Main Program
solution = missionaries_cannibals()

if solution:
    print("Missionaries and Cannibals Solution using BFS\n")
    print("Step\tMissionaries Left\tCannibals Left\tBoat")

    for i, state in enumerate(solution):
        print(f"{i}\t{state[0]}\t\t\t{state[1]}\t\t{state[2]}")

else:
    print("No solution found.")