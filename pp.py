def greedy_search(problem, heuristic):
    current_state = problem.initial_state()
    path = [current_state]
    while not problem.is_goal(current_state):
        neighbors = problem.get_neighbors(current_state)
        best_neighbor = None
        best_cost = float('inf')
        for neighbor in neighbors:
            cost = heuristic(neighbor)
            if cost < best_cost:
                best_neighbor = neighbor
                best_cost = cost
        current_state = best_neighbor
        path.append(current_state)
    return path

# مثال على استخدام الخوارزمية:
class Problem:
    def initial_state(self):
        return 'A'

    def is_goal(self, state):
        return state == 'G'

    def get_neighbors(self, state):
        neighbors = {'A': ['B', 'C'],
                     'B': ['D'],
                     'C': ['E', 'F'],
                     'D': ['G'],
                     'E': [],
                     'F': [],
                     'G': []}
        return neighbors[state]

def heuristic(state):
    heuristic_values = {'A': 10, 'B': 8, 'C': 7, 'D': 6, 'E': 5, 'F': 3, 'G': 0}
    return heuristic_values[state]

problem = Problem()
path = greedy_search(problem, heuristic)
print("المسار الأمثل:", path)