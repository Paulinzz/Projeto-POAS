from dotenv import load_dotenv
from os import getenv

load_dotenv()

KITSU_API_URL = "https://kitsu.io/api/edge"
TMDB_API_URL = "https://api.themoviedb.org/3"
TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYzliMTUwNGQ1MDBkMzE3MTU0ZWU3MDRhZjg0ZjQzNiIsIm5iZiI6MTc4MDMwODk3MS4yNTIsInN1YiI6IjZhMWQ1YmViYjBhZmE0YzNlZTgyYTZjMSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nYDbSi_34xgj5EX5xstqGoF0GFUD_9v7TbpCFXnBZ1E"
TMDB_KEY = getenv("TMBD_API_KEY")

PARAMS_TMDB = {
    "language": "pt-BR"
}
HEADERS_TMDB = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_KEY}"
}

HEADERS_KITSU = {
    "Accept": "application/vnd.api+json",
    "Content-Type": "application/vnd.api+json"
}