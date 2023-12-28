# Grains 

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    grains_on_square = 2 ** (number - 1)
    return grains_on_square

def total():
    grains_on_chessboard = 2 ** 64 - 1
    return grains_on_chessboard
