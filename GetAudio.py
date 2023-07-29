import pytube, time, csv, music_tag

title = []
artist = []
album = []
link = []

with open('Aftermath.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter='`', quotechar='|')
    for row in reader:
        title.append(row[0])
        artist.append(row[1])
        album.append(row[2])
        link.append(row[3])

print(len(title))

#Create the Youtube object
for i in range (0, len(title)):
    youtube = pytube.YouTube(link[i])
    audio = youtube.streams.filter(only_audio=True)
    desire_audio = audio[0]

    print(f'{i}: {title[i]}')

    desire_audio.download(filename=(f'Aftermath/{title[i]}.mp3'))


    f = music_tag.load_file(f'Aftermath/{title[i]}.mp3')
    f['title'] = title[i]
    f['artist'] = artist[i]
    f['album'] = album[i]
    f.save()