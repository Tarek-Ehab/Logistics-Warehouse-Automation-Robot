from decimal import Decimal
RR = Decimal('0.0')
UU = Decimal('0.0')
DD = Decimal('0.0')
LL = Decimal('0.0')
RU = Decimal('-1.1')
UR = Decimal('1.1')
UL = Decimal('0.9')
LU = Decimal('-0.9')
DL = Decimal('1.0')
LD = Decimal('-1.0')
RD = Decimal('-1.2')
DR = Decimal('1.2')
RL = Decimal('-0.2')
LR = Decimal('0.2')
UD = Decimal('-0.1')
DU = Decimal('0.1')

num = {
    'R':Decimal('2.2'),
    'L':Decimal('2.4'),
    'U':Decimal('3.3'),
    'D':Decimal('3.4')
}

Cost = 50
goal = ''
start = ''
car_orientaion = 'R'
#sub or add two (x,y) points.
class Point:
    def __init__(self,x,y) -> None:
        self.x = x  
        self.y = y
    
    def __add__(self,o):
        return (self.x+o.x,self.y+o.y)
    
    def __sub__(self,o):
        return (self.x-o.x,self.y-o.y)



#7awlt el grid ll points from class point ely fo2
Grid = {
    'A':Point(1,1),
    'B':Point(1,2),
    'C':Point(1,3),
    'D':Point(2,1),
    'E':Point(2,3),
    'F':Point(3,1),
    'G':Point(3,2),
    'H':Point(3,3),
    'I':Point(4,1),
    'J':Point(4,3),
    'K':Point(5,1),
    'L':Point(5,2),
    'M':Point(5,3),
}


Graph = {
    'A':[('B',Cost),('D',Cost)],
    'B':[('A',Cost),('C',Cost)],
    'C':[('B',Cost),('E',Cost)],
    'D':[('A',Cost),('F',Cost)],
    'E':[('C',Cost),('H',Cost)],
    'F':[('D',Cost),('I',Cost),('G',Cost)],
    'G':[('F',Cost),('H',Cost)],
    'H':[('E',Cost),('J',Cost),('G',Cost)],
    'I':[('F',Cost),('K',Cost)],
    'J':[('H',Cost),('M',Cost)],
    'K':[('I',Cost),('L',Cost)],
    'L':[('K',Cost),('M',Cost)],
    'M':[('J',Cost),('L',Cost)],
}


#direction of next
def dirction(current:str,gole:str) ->str:
    d = Grid[gole]-Grid[current]
    if d[0] ==0 and d[1]<0:
        return 'L'
    elif d[0]==0 and d[1]>0:
        return 'R'
    elif d[0] <0 and d[1]==0:
        return 'U'
    elif d[0]>0 and d[1]==0:
        return 'D'
    else :
        return 'Error'

#Manhattan distance hueristic
#ba3ml minus ml goal l kol point wa2fa 3aleha w ba2es leha el hueristic bta3ha
def hueristic (curent:Point,final_gole:Point):
    d =final_gole-curent
    Distance = abs(d[0])+abs(d[1])
    return Distance

#btakhod path l sou w ba3ml pop l 1st 3ashan ma3mltsh check marten bayen
# l kol node fl path ba3tha l direction   
def get_comands(sou:list)->list:
    sol = sou.copy()
    start_node = sol.pop(0)[0]
    directions =[]
    for (node,Cost) in sol:
        directions.append(dirction(start_node,node))
        start_node = node
    return directions

def Path_Cost(path):
    g_cost = 0
    global goal
    for (node, cost) in path:
        g_cost += cost
    last_node = path[-1][0]
    h_cost = hueristic(Grid[last_node],Grid[goal])
    f_cost = g_cost + h_cost
    return f_cost, last_node

def a_star_search(graph, start_point, goal_point):
    global start ,goal
    start = start_point
    goal = goal_point
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=Path_Cost)
        path = queue.pop(0)
        node = path[-1][0]
       

        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)

#All are substract with direction taken into consideration
def run(first:str,next:str) ->str:
    ID=Decimal(num[first]-num[next])
    if ID in (RR, DD, UU, LL):
       return ['F']  
    elif ID in (RU, LD, DR, UL):
        return ['TL']
    elif ID in (UR, DL, RD, LU):
        return ['TR']
    elif ID in (RL, LR, UD, DU):
        return ['TRR']


def get_data(STRAT,GOAL) ->list:
    global start, goal,car_orientaion
    start = STRAT
    goal = GOAL
    solution = a_star_search(Graph, start, goal)
    turn = get_comands(solution)
    print(solution)
    
    turn.insert(0,car_orientaion)
    car_orientaion = turn[-1]
    print(turn)
    comandes = []
    for i in range(len(turn)-1):
        code=run(turn[i],turn[i+1])
        comandes.extend([code]) 
    return sum(comandes, [])

if __name__ =="__main__":
    Move = get_data('A', 'H')
    print(Move)
    
    
    
