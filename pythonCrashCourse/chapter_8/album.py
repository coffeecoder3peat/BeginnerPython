def make_album(artist_name, album_title, number_of_songs=None):
    album_info = {
        'Artist Name': artist_name.title(),
        'Album Title': album_title.title(),
    }
    
    if number_of_songs:
        album_info['Number of Songs'] = number_of_songs

    return album_info

while True:
    print("Enter 'q' at any time to quit")
    artist_name = input("Who is the album artist? ")
    if artist_name == 'q':
        break
    album_name = input("What is the album title? ")
    if album_name == 'q':
        break
    
    answer = input('Do you know how many songs there are? Please enter Y/N')
    if answer == 'q':
        break
    while answer != 'Y' and answer != 'N':
        answer = input(f"{answer} is not a valid answer. Please enter Y or N")

    if answer == 'Y':
        number_of_songs = input("Great! How many songs are on this album? ")
        album = make_album(artist_name, album_name, number_of_songs)
    else:
        album = make_album(artist_name, album_name)
    
    print(album)
