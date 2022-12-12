from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = "SPOTIPY_CLIENT_ID"
SPOTIPY_CLIENT_SECRET = "SECRET"
SPOTIPY_REDIRECT_URI = "http://example.com"


print("Welcome to Tyler's awesome Spotify time-machine.")
chosen_date = input("When would you like to travel to? Type the date in this format, YYYY-MM-DD: ")
year = chosen_date[:4]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{chosen_date}")
billboard_page = response.text
soup = BeautifulSoup(billboard_page, "html.parser")
song_names = soup.select("li h3", id="title-of-a-story")

song_list = [song_name.getText().strip() for song_name in song_names]
song_list_trim = song_list[:100]

song_artist = soup.select("ul li ul li span")
artist_list = [artist.getText().strip() for artist in song_artist]
artists = artist_list[0::7]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(

        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-private",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

uri_list = []
for num in range(0, 100):
    result = (sp.search(q=f"track: {song_list_trim[num]} artists{artists[num]}", type="track"))
    try:
        uri = result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{song_list_trim[num]} by {artists[num]} cannot be found in Spotify. I have skipped this song.")


create_playlist = sp.user_playlist_create(user_id, f"{chosen_date}s top 100", public=False, collaborative=False, description=f"The top 100 songs on {chosen_date}. A project by Tyler.")
playlist_id = create_playlist["id"]
sp.playlist_add_items(playlist_id, uri_list, position=None)