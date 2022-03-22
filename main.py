from random import randint

from generate import generate

# test classes here
# generate 10000 of them and crash your computer!
body_array = []

eyes_array = []

mouth_array = []

nose_array = []

background_array = []

NFT_array = []

counter = 0

amount = 3

while 0 <= counter < amount:
    v = randint(1, 5)
    body_array.append(v)
    w = randint(1, 5)
    eyes_array.append(w)
    x = randint(1, 5)
    mouth_array.append(x)
    y = randint(1, 5)
    nose_array.append(y)
    z = randint(1, 5)
    background_array.append(z)
    NFT_array = [[v,w,x,y,z]]
    generate(v, w, x, y, z)
    NFT_array.append(NFT_array)
    counter += 1

stat_body = [body_array.count(1), body_array.count(2), body_array.count(3), body_array.count(4), body_array.count(5)]
stat_eyes = [eyes_array.count(1), eyes_array.count(2), eyes_array.count(3), eyes_array.count(4), eyes_array.count(5)]
stat_mouth = [mouth_array.count(1), mouth_array.count(2), mouth_array.count(3), mouth_array.count(4), mouth_array.count(5)]
stat_nose = [nose_array.count(1), nose_array.count(2), nose_array.count(3), nose_array.count(4), nose_array.count(5)]
stat_background = [background_array.count(1), background_array.count(2), background_array.count(3), background_array.count(4),
                   background_array.count(5)]

print(amount, "NFT's generated")
print(stat_body)
print(stat_eyes)
print(stat_mouth)
print(stat_nose)
print(stat_background)


