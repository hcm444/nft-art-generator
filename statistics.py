from main import body_array, eyes_array, mouth_array, nose_array, background_array, amount

def statictics(NFT_array):

    # statistics arrays show a heatmap of the rarity of the NFTs
    stat_body = [body_array.count(1), body_array.count(2), body_array.count(3), body_array.count(4), body_array.count(5)]
    stat_eyes = [eyes_array.count(1), eyes_array.count(2), eyes_array.count(3), eyes_array.count(4), eyes_array.count(5)]
    stat_mouth = [mouth_array.count(1), mouth_array.count(2), mouth_array.count(3), mouth_array.count(4),
                  mouth_array.count(5)]
    stat_nose = [nose_array.count(1), nose_array.count(2), nose_array.count(3), nose_array.count(4), nose_array.count(5)]
    stat_background = [background_array.count(1), background_array.count(2), background_array.count(3),
                       background_array.count(4),
                       background_array.count(5)]

    print(amount, "NFT's generated")
    print(stat_body)
    print(stat_eyes)
    print(stat_mouth)
    print(stat_nose)
    print(stat_background)