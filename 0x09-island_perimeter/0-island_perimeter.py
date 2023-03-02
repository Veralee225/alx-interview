#!/usr/bin/python3
""" module to define the island_perimeter function """


def island_perimeter(grid):
    """ functin to find perimeter of an island
    Arguments:
        gird : the given grid
    Returns:
        the peremeter of an island
    """
    width = len(grid[0])
    height = len(grid)
    per = 0

    for y in range(height):
        for x in range(width):
            if grid[y][x] == 1:
                if y - 1 >= 0:
                    if grid[y - 1][x] == 0:
                        per += 1
                else:
                    per += 1
                if x - 1 >= 0:
                    if grid[y][x - 1] == 0:
                        per += 1
                else:
                    per += 1
                if y + 1 < height:
                    if grid[y + 1][x] == 0:
                        per += 1
                else:
                    per += 1
                if x + 1 < width:
                    if grid[y][x + 1] == 0:
                        per += 1
                else:
                    per += 1
    return per
