import csv

genre = set()

with open("gross movies.csv", "r", encoding='UTF8') as file:
    flicksread = csv.reader(file)
    next(flicksread)

    for flick in sorted(flicksread):
        genre.add(flick[1].lower())

    for flick in sorted(genre):
        print(flick)
