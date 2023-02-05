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
    
    for line in lib:
        artist, title, length = line.strip().split(',')
        length_minutes, length_seconds = map(int, length.split(":"))
        length_total = length_minutes * 60 + length_seconds
        
        if artist not in songs:
            songs[artist] = []
        
        songs[artist].append((title, length))
        total_songs += 1
        total_length += length_total
    
    for artist in sorted(songs.keys()):
        artist_songs = songs[artist]
        artist_songs_count = len(artist_songs)
        artist_length = sum(map(lambda x: int(x[1].split(":")[0]) * 60 + int(x[1].split(":")[1]), artist_songs))
        
        print(f"{artist} ({artist_songs_count} songs, {int(artist_length / 60)}:{artist_length % 60:02d})")
        
        for title, length in artist_songs:
            print(f"- {title} ({length})")
    
    print(f"Total: {total_songs} songs, {int(total_length / 60)}:{total_length % 60:02d}")

# call the functions
lib = read_library('80s_library.txt')
print_library(lib)



