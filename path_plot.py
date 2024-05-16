from environment import path_view

def main():
    """
    The function `main()` creates a grid instance with specified dimensions and states, displays it, and
    saves it to a text file.
    """
    states = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 4), (2, 4), (3, 4), (4,4)] #test
    grid_instance = path_view(6, 6, 50, 50, states=states)
    grid_instance.main()
    grid_instance.save('environment/maps/path.txt')

if __name__== "__main__":
    main()