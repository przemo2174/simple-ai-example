from simpleai.search import SearchProblem, astar, breadth_first

class Connection:
    def __init__(self, src, dest, cost):
        self.src = src
        self.dest = dest
        self.cost = cost

class Graph:
    def __init__(self):
        self.connections = []

    def add_connection(self, node1, node2, cost):
        self.connections.append(Connection(node1, node2, cost))
        self.connections.append(Connection(node2, node1, cost))

    def print(self):
        for connection in self.connections:
            print(connection.src + ' -> ' + connection.dest + ' (' + str(connection.cost) + ')')
            # print(connection.node2 + ' -> ' + connection.node1 + ' (' + str(connection.cost) + ')')


g = Graph()
g.add_connection('Kraków', 'Warszawa', 293)
g.add_connection('Kraków', 'Wrocław', 272)
g.add_connection('Warszawa', 'Wrocław', 348)
g.add_connection('Warszawa', 'Gdańsk', 339)
g.add_connection('Gdańsk', 'Szczecin', 370)
g.add_connection('Wrocław', 'Szczecin', 415)
g.print()

class DistanceProblem(SearchProblem):
    def __init__(self, init_state, goal, graph):
        self.initial_state = init_state
        self.goal = goal
        self.graph = graph

    def actions(self, state):
        if self.goal not in state:
            possible_cities = [c.dest for c in self.graph.connections if c.src == state.split(',')[-1]]
            # print('Possible cities:', possible_cities)
            return possible_cities
        else:
            return []

    def result(self, state, action):
        return state + ',' + action
    
    def is_goal(self, state):
        # print('State:', state)
        return self.goal in state

    def cost(self, state, action, state2):
        src = state.split(',')[-1]
        dest = action
        cost = [c.cost for c in self.graph.connections if c.src == src and c.dest == dest][0]
        return cost

    # def heuristic(self, state):
    #     # how far are we from the goal?
    #     wrong = sum([1 if state[i] != self.goal[i] else 0
    #                 for i in range(len(state))])
    #     missing = len(self.goal) - len(state)
    #     return wrong + missing


# Znajdz najkrotsza drogę z Krakowa do Szczecina

initial_state = 'Kraków'
goal = 'Szczecin'

problem = DistanceProblem(initial_state, goal, g)
result = breadth_first(problem)

print('Final state:', result.state)
print('Path:', result.path())
print('Cost:', result.cost)

    

