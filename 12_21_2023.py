# Maximum Edge of a Triangle
# Examples
# nextEdge(8, 10) ➞ 17
# nextEdge(5, 7) ➞ 11
# nextEdge(9, 2) ➞ 10

def next_edge(side1, side2):
    max_edge = side1 + side2 - 1
    return(max_edge)
