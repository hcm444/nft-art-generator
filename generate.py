from PIL import Image


def generate(body, eyes, mouth, nose, background):
    # generates NFT art and saves in it Output file

    # if else statements below match number of image to corresponding attribute for description
    body_value = ""

    if body == 1:
        body_value = "white"
    elif body == 2:
        body_value = "green"
    elif body == 3:
        body_value = "yellow"
    elif body == 4:
        body_value = "pink"
    elif body == 5:
        body_value = "teal"

    eyes_value = ""

    if eyes == 1:
        eyes_value = "alert"
    elif eyes == 2:
        eyes_value = "red"
    elif eyes == 3:
        eyes_value = "sus"
    elif eyes == 4:
        eyes_value = "tired"
    elif eyes == 5:
        eyes_value = "sunglasses"

    mouth_value = ""

    if mouth == 1:
        mouth_value = "pursed"
    elif mouth == 2:
        mouth_value = "smirk"
    elif mouth == 3:
        mouth_value = "frown"
    elif mouth == 4:
        mouth_value = "teeth"
    elif mouth == 5:
        mouth_value = "smile"

    nose_value = ""

    if nose == 1:
        nose_value = "crooked"
    elif nose == 2:
        nose_value = "round"
    elif nose == 3:
        nose_value = "fat"
    elif nose == 4:
        nose_value = "small"
    elif nose == 5:
        nose_value = "big"

    background_value = ""

    if background == 1:
        background_value = "beach"
    elif background == 2:
        background_value = "hell"
    elif background == 3:
        background_value = "sunset"
    elif background == 4:
        background_value = "snow"
    elif background == 5:
        background_value = "morning"

    # numer array and description array
    num_array = [body, eyes, mouth, nose, background]
    desc_array = [body_value, eyes_value, mouth_value, nose_value, background_value]
    # print both arrays to console
    print(str(desc_array))
    print(num_array)
    # Open the images including the body
    attr0 = Image.open('NFT/' + "Body/" + str(body) + ".png")
    attr1 = Image.open('NFT/' + "Eyes/" + str(eyes) + ".png")
    attr2 = Image.open('NFT/' + "Mouth/" + str(mouth) + ".png")
    attr3 = Image.open('NFT/' + "Nose/" + str(nose) + ".png")
    attr4 = Image.open('NFT/' + "Background/" + str(background) + ".png")
    # Paste/Merge Required images, everything pasted on body
    attr0.paste(attr1, (0, 0), attr1)
    attr0.paste(attr2, (0, 0), attr2)
    attr0.paste(attr3, (0, 0), attr3)
    attr0.paste(attr4, (0, 0), attr4)
    # Resize image
    resized_img = attr0.resize((300, 300), Image.NEAREST)  # opensea size
    # save name as attributes number _ properties.png so I can easily perform data analysis.
    resized_img.save('NFT/{0}{1}{2}{3}{4}_{5}_{6}_{7}_{8}_{9}.png'.format(str(num_array[0]), str(num_array[1]),
                                                                                 str(num_array[2]), str(num_array[3]),
                                                                                 str(num_array[4]), body_value,
                                                                                 eyes_value, mouth_value, nose_value,
                                                                                 background_value), "PNG")

    return
