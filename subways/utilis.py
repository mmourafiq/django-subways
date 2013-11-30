# -*- coding: utf-8 -*-
def shortest_path_search(start, goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if start == goal:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for successor in s.get_successors():            
            successor_stop = successor.successor_stop
            successor_line = successor.successor_line
            if successor_stop not in explored:
                explored.add(successor_stop)
                path2 = path + [successor_line, successor_stop]
                if successor_stop == goal:
                    return path2
                else:
                    frontier.append(path2)
    return []

def ride_path(here, there):
    "Return a path on the subway system from here to there."
    path = shortest_path_search(here, there)
    stops = path_stops(path)    
    return stops

def longest_ride_path(stops):
    """"Return the longest possible 'shortest path' 
    ride between any two stops in the system."""    
    return max([ride_path(a, b) for a in stops for b in stops], key=len)

def path_stops(path):
    "Return a list of stops in this path."
    return path[0::2]
    
def path_lines(path):
    "Return a list of lines in this path."
    return path[1::2]
