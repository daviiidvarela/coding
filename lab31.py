## --- TASK 1 ---##
def string_to_seconds(t): # function to convert mm:ss to ss
    """Returns seconds from time."""
    m, s = t.split(':')
    if int(s) >= 60 or len(t) != 2:
        return int(m) * 60 + int(s)
# Test for task 1
#print(string_to_seconds('4:50'))

## --- TASK 2 ---##
## A ##
def read_library(file): #simple function to open the file 80s_library.txt
    lib = open(file, 'r')
    lib.close()
    
#Test for task 2.a
# read_library('80s_library.txt')

## B ##
def print_library(lib):
    lib = open('80s_library.txt', 'r')
    songs = {}
    total_songs = 0 #sets initial value of all variables to 0 so we can add to them later
    total_length = 0
    
    for line in lib: # in this case every line is a song with extra information about its artist and length
        artist, title, length = line.strip().split(',') # splits each key in each line to get artist, song and length on their own
        length_minutes, length_seconds = map(int, length.split(":")) # splits the minutes and seconds for each song so that the totals can be calculated
        length_total = length_minutes * 60 + length_seconds
        
        if artist not in songs: # this function creates a new dictionary space for every artist
            songs[artist] = [] 
        
        songs[artist].append((title, length)) # further, this adds song title and length to each artists' dictionary space
        total_songs += 1
        total_length += length_total
    
    for artist in sorted(songs.keys()): # this function finds the length of each artists discography and yields the total length for each artist
        artist_songs = songs[artist]
        artist_songs_count = len(artist_songs)
        artist_length = sum(map(lambda x: int(x[1].split(":")[0]) * 60 + int(x[1].split(":")[1]), artist_songs))
        
        print(f"{artist} ({artist_songs_count} songs, {int(artist_length / 60)}:{artist_length % 60:02d})") # prints the length of each artists' discography
        
        for title, length in artist_songs: # finally, this prints each song's title and length line by line until the whole library is accounted for
            print(f"- {title} ({length})") 
    
    print(f"Total: {total_songs} songs, {int(total_length / 60)}:{total_length % 60:02d}") # prints total library song count and length

# Test for task 2.b
#lib = read_library('80s_library.txt')
#print_library(lib)

## --- TASK 3 ---##
## A ##
def make_playlist(file, theme):
    library = {}
    with open('80s_library.txt', 'r') as file:
        for line in file:
            artist, song, length = line.strip().split(',')
            library[song] = (artist, length)
    playlist = []
    for song in library:
        if theme in song:
            artist, length = library[song]
            length_minutes, length_seconds = map(int, length.split(":")) 
            length_total = length_minutes * 60 + length_seconds
            playlist.append((artist, song, length_total))
    return playlist
    if not playlist:
        raise ValueError('No songs match the theme')
    

# Test for task 3.a
#lib = read_library('80s_library.txt')
#make_playlist(lib, "Rock")

## B ##

def write_playlist(playlist, filename):
    with open(filename, 'w') as f:
        for artist, song, length in playlist:
            length_minutes = length // 60
            length_seconds = length % 60
            f.write(f"{artist},{song},{length_minutes}:{length_seconds:02}\n")
    return f

# Test for task 3.b
#lib = read_library('80s_library.txt')
#house = make_playlist(lib, "House")
#write_playlist(house, "house_music.txt")

## --- TASK 4 ---##
def main():
    library_filename = input("Enter a music library filename: ")
    library = read_library(library_filename)
    print("Library:")
    print_library(library)
    theme = input("Enter a playlist theme: ")
    playlist = make_playlist(library, theme.casefold())
    print("Playlist:")
    print(playlist)
    playlist_filename = input("Enter a filename to save the playlist: ")
    write_playlist(playlist, playlist_filename)

main()