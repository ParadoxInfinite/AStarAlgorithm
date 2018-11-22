from tkinter import *
class Node():
    """A node class for A* Pathfinding"""
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)

def main():
    start = (0,0)
    end = (9,9)
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    root = Tk()
    root.title('A Star Algorithm')
    frameMaze = Frame(root, width = 500, height = 500, padx=30, pady=30)
    frameMaze.pack(fill = None, expand = False)
    grid = []
    for i in range(10) :
        row = []
        for j in range(10) :
            if maze[i][j]==1:
                button = Button(frameMaze, width = 3, height = 1, borderwidth = 1, background = 'grey',relief = 'flat')
                button.grid(row = i, column = j)
                button.position = (i, j)
                row.append(button)
            else :
                button = Button(frameMaze, width = 3, height = 1, borderwidth = 1)
                button.grid(row = i, column = j)
                button.position = (i, j)
                row.append(button)
        grid.append(row)
    def update_buttons():
        path = astar(maze, start, end)
        for x in path :
            i = x[0]
            j = x[1]
            grid[i][j].config(bg = "black")
            if(x == path[0]):
                grid[i][j].config(bg = "blue")
            if(x==path[len(path)-1]) :
                grid[i][j].config(bg = "red")
    frameIndex = Frame(root)
    frameIndex.pack()
    labelIndex = Label(frameIndex, text = "INDEX :")
    labelIndex.pack()
    labelBlue = Label(frameIndex, text = 'Start Node : ' )
    labelBlue.pack()
    buttonBlue = Button(frameIndex, width = 3, height = 1, borderwidth = 1, bg = 'Blue')
    buttonBlue.pack()
    labelRed = Label(frameIndex, text = 'End Node : ' )
    labelRed.pack()
    buttonBlue = Button(frameIndex, width = 3, height = 1, borderwidth = 1, bg = 'Red')
    buttonBlue.pack()
    labelBlack = Label(frameIndex, text = 'Path : ' )
    labelBlack.pack()
    buttonBlue = Button(frameIndex, width = 3, height = 1, borderwidth = 1, bg = 'Black')
    buttonBlue.pack()
    frameButton = Frame(root)
    frameButton.pack(side = BOTTOM)
    startButton = Button(frameButton, text='Start!', width = 15, command = update_buttons)
    quitButton = Button(frameButton, text='Quit!', width = 15, command = root.destroy)
    startButton.pack(side = LEFT)
    quitButton.pack(side = LEFT)
    root.mainloop()


if __name__ == '__main__':
    main()
