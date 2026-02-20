celebs = ("Taylor Swift", "Lionel Messi", "The Weeknd", "Keanu Reeves", "Angelina Jolie")
ages = (36, 38, 36, 61, 50)

celebs_list = []
ages_list = []

for celeb in celebs:
    celebs_list.append(celeb)

ages_list = [age for age in ages]

celebs_dict = {"Celebrties": celebs_list, "Ages": ages_list}

print(celebs_dict)