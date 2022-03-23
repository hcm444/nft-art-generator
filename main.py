from generate import generate
from itertools import product


def create():
    if __name__ == "__main__":
        layer1 = [1, 2, 3, 4, 5]
        layer2 = [1, 2, 3, 4, 5]
        layer3 = [1, 2, 3, 4, 5]
        layer4 = [1, 2, 3, 4, 5]
        layer5 = [1, 2, 3, 4, 5]
        # five arrays for every attribute
        M = (list(product(layer1, layer2, layer3, layer4, layer5)))
        # M is a list of every possible tuple
        for counter in range(M.__len__()):
            # parse through these tuples
            attr0 = M[counter][0]
            attr1 = M[counter][1]
            attr2 = M[counter][2]
            attr3 = M[counter][3]
            attr4 = M[counter][4]
            # save every respective place of the tuple for generate()
            generate(attr0, attr1, attr2, attr3, attr4)
            # remember how many permutations you have! ex: 5x5x5x5x5 = 3125 files!


"""TEST CLASSES"""
# create()
# This function will generate all possible permutations
generate(1, 1, 1, 1, 1)
generate(2, 2, 2, 2, 2)
generate(3, 3, 3, 3, 3)
generate(4, 4, 4, 4, 4)
generate(5, 5, 5, 5, 5)
