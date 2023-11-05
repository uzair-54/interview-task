data = [['A', 'B'],
        ['B', 'C'],
        ['D', 'C'],
        ['D', 'E'],
        ['F', 'G'],
        ['H', 'G'],
        ['A', 'G'],
        ['A', 'X'],
        ['Y', 'X'],
        ['Y', 'Z'],]

# Function for getting neighbours list
def getNeighbours(node):
    
    listOfNeigbour = [node] # Initializing list to keep track of neighbours, adding the starting node itself as well   
    
    for pair in data: # Looping through node pairs in the data list
        if node in pair: # Checking if the given node is in the pair

            neighbour = pair[0] if node != pair[0] else pair[1] # Getting neighbour from the pair by checking it is not the given node
            listOfNeigbour.append(neighbour) # Appending the node the list

    return listOfNeigbour # Returning the list of neightbours 

# Function for getting path through iterative method

def getPathIterative(startingNode, endingNode, depth):
    visited = [] # Initializing a list for keeping track of visited nodes
    stack = [(startingNode, [startingNode])] # Initializing a stack with a tuple where at 0 index is the node and at 1 index the path to that node 

    while stack: # Looping till the stack is not empty
        node, path = stack.pop() # Getting the top tuple in the stack
        if node == endingNode: # Checking if the node is the final node in our path/route
            return path

        if node not in visited and len(path) <= depth: # Checking if the node is not visited and the specified depth nas not been reached 
            visited.append(node)
            neighbors = getNeighbours(node) # Getting neighbours of the node
            for neighbor in neighbors: # Iterating through the neighbours
                if neighbor not in visited: # Checking if the neighbour has not been visited 
                    newPath = path + [neighbor] # Creating a new path by extending the current path with the neighbor
                    stack.append((neighbor, newPath)) # Adding the neighbour and the tuple into the stack

    return "Path does not exist" # Returning string when stack is empty and path has not been found

# function for getting path through recursive method

def getPathRecursive(startingNode, endingNode, depth, currentDepth = 0, path = []):
        
        if currentDepth > depth: # Checking if the specified depth has not been reached
            return "Path does not exist" # Returning string depth has exceded the specified depth 
        
        path.append(startingNode) # Adding the node to the path 
        if startingNode == endingNode: # Checking if we have reached at our specified node (destination)
            return path 

        for neighbor in getNeighbours(startingNode): #Iterating through the neighbors of the current node
            if neighbor not in path: # Checking if the neighbour is not already been visited

                # Recursively attempt to find a path from the neighbor to the ending node, increasing the depth 
                newPath = getPathRecursive(neighbor, endingNode, depth, currentDepth + 1, path.copy())
                if type(newPath) == list: # Checking if the returned path is of type list
                    return newPath
                
        return "Path does not exist" # Returning string when path has not been found

print(getPathIterative("A","Z",6))


