from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlZTZjZTc1NjcxMDdmODg3OWM1MWRkOTk0OWMzMjllNCIsInN1YiI6IjYxMTAzMjBiNGE1MmY4MDA0NTQ0YjY5ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.EN72uVMWl8EZZCA-DEvJHkKvZwCqt0-4ONOw6RbV8zk'}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

@app.route('/')
def homepage():
    movies = get_popular_movies()
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)