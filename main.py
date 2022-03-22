from random import randint
# need randint because to lazy to use seeds
from generate import generate

# generate.py
# test classes here
# generate 10000 of them and crash your computer!
# created self explainatory arrays for values
body_array = []

eyes_array = []

mouth_array = []

nose_array = []

background_array = []

NFT_array = []

counter = 0

amount = 3

while 0 <= counter < amount:
    # while not at max amount of generated nfts
    # fill respective values with random ints
    v = randint(1, 5)
    # append ints to int arrays
    body_array.append(v)
    w = randint(1, 5)
    eyes_array.append(w)
    x = randint(1, 5)
    mouth_array.append(x)
    y = randint(1, 5)
    nose_array.append(y)
    z = randint(1, 5)
    background_array.append(z)
    # make an array of arrays representing every NFT
    # could do analysis here
    NFT_array = [[v, w, x, y, z]]
    # send the data to the generator
    generate(v, w, x, y, z)
    # apent NFT array after generation
    NFT_array.append(NFT_array)
    # increment counter
    counter += 1

