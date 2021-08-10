import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZTZjZTc1NjcxMDdmODg3OWM1MWRkOTk0OWMzMjllNCIsInN1YiI6IjYxMTAzMjBiNGE1MmY4MDA0NTQ0YjY5ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EN72uVMWl8EZZCA-DEvJHkKvZwCqt0-4ONOw6RbV8zk'}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(path, size="w342"):
    return "https://image.tmdb.org/t/p/"+size+path
