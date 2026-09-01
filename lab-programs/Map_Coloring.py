regions = ['A', 'B', 'C', 'D']

colors = ['Red', 'Green', 'Blue']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
def is_valid(region, color, assignment):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(assignment):
    if len(assignment) == len(regions):
        return assignment

    for region in regions:
        if region not in assignment:
            break

    
    for color in colors:
        if is_valid(region, color, assignment):
            assignment[region] = color

            result = solve(assignment)

            if result:
                return result

            
            del assignment[region]

    return None


solution = solve({})

print("Map Coloring using CSP")
print("----------------------")

if solution:
    print("Solution found:")
    for region in regions:
        print(region, "->", solution[region])
else:
    print("No solution exists.")