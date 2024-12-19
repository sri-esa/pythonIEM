from collections import deque
import matplotlib.pyplot as plt

# Function to solve the Water Jug Problem using BFS
def water_jug_problem(jug1_capacity, jug2_capacity, target):
    # Queue to store states (current state, path to state)
    queue = deque()
    visited = set()
    
    # Initial state: Both jugs are empty
    initial_state = (0, 0)
    queue.append((initial_state, []))
    visited.add(initial_state)

    # List to store visited states for visualization
    visited_states = [initial_state]

    while queue:
        (jug1, jug2), path = queue.popleft()

        # Check if we've reached the target
        if jug1 == target or jug2 == target:
            return path + [(jug1, jug2)], visited_states

        # Generate all possible next states
        next_states = [
            (jug1_capacity, jug2),  # Fill Jug1
            (jug1, jug2_capacity),  # Fill Jug2
            (0, jug2),              # Empty Jug1
            (jug1, 0),              # Empty Jug2
            # Pour Jug1 -> Jug2
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)),
            # Pour Jug2 -> Jug1
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state, path + [(jug1, jug2)]))
                visited_states.append(state)

    # If no solution is found
    return None, visited_states

# Function to plot visited states
def plot_states(visited_states):
    jug1_values = [state[0] for state in visited_states]
    jug2_values = [state[1] for state in visited_states]

    plt.figure(figsize=(8, 6))
    plt.scatter(jug1_values, jug2_values, c='blue', label='Visited States')
    plt.xlabel('Jug1 (Liters)')
    plt.ylabel('Jug2 (Liters)')
    plt.title('States Visited During Solution')
    plt.legend()
    plt.grid()
    plt.show()

# Main Program
if __name__ == "__main__":
    print("Welcome to the Water Jug Problem Solver!")
    try:
        jug1_capacity = int(input("Enter the capacity of Jug1 (in liters): "))
        jug2_capacity = int(input("Enter the capacity of Jug2 (in liters): "))
        target = int(input("Enter the target amount of water (in liters): "))

        # Solve the problem
        solution, visited_states = water_jug_problem(jug1_capacity, jug2_capacity, target)

        if solution:
            print("\nSolution Found!")
            print("Steps to achieve the target:")
            for step, (jug1, jug2) in enumerate(solution, start=1):
                print(f"Step {step}: Jug1 = {jug1}L, Jug2 = {jug2}L")
            
            # Ask if the user wants to visualize the states
            visualize = input("\nDo you want to visualize the visited states? (yes/no): ").strip().lower()
            if visualize == "yes":
                plot_states(visited_states)
        else:
            print("\nNo solution exists for the given input.")
    except ValueError:
        print("Invalid input! Please enter positive integers for capacities and target.")
