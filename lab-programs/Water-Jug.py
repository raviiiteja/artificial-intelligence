from collections import deque

def water_jug():
    jug1_capacity = 5
    jug2_capacity = 3
    goal = 2

    visited = set()
    queue = deque()
    queue.append((0, 0, [(0, 0)]))

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        if jug1 == goal or jug2 == goal:
            print("\nSolution Found!\n")
            for i, state in enumerate(path):
                print(f"Step {i}: Jug1 = {state[0]}L, Jug2 = {state[1]}L")
            print("\nGoal Achieved!")
            return

        next_states = [
            (jug1_capacity, jug2),
            (jug1, jug2_capacity),
            (0, jug2),
            (jug1, 0),
            (jug1 - min(jug1, jug2_capacity - jug2),
             jug2 + min(jug1, jug2_capacity - jug2)),
            (jug1 + min(jug2, jug1_capacity - jug1),
             jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path + [state]))

water_jug()

print("\nProgram Executed Successfully.")