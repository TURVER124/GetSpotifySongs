import shutil, os, csv


title = []
artist = []
album = []
link = []

with open('KSongLinks.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='`', quotechar='|')
    for row in reader:
        title.append(row[0])
        artist.append(row[1])
        album.append(row[2])
        link.append(row[3])

for i in range (0, len(title)):   
    shutil.copy(f'Songs/{i}.mp3', f'NamedSongs/{title[i]} by {artist[i]}.mp3')
    # shutil.copy(f'Songs/{i}.mp3', f'NamedSongs/{title[i]}.mp3')