from youtubesearchpython import VideosSearch
import csv, time

title = []
artist = []
album = []
link = []

with open('KSongs.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='`', quotechar='|')
    for row in reader:
        title.append(row[0])
        artist.append(row[1])
        album.append(row[2])


for i in range(0, len(title)):
    videosSearch = VideosSearch(f'{title[i]} by {artist[i]}', limit = 1)
    results = videosSearch.result()
    link.append(results['result'][0]['link'])
    print(f'{title[i]} by {artist[i]}: {link[i]}')
    # time.sleep(1)


with open('KSongLinks.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter='`')

    for j in range(0, len(title)):
        row = [title[j], artist[j], album[j], link[j]]
        writer.writerow(row)