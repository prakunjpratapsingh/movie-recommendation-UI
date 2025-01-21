from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Movie data with poster_path
    movies = [
        {"title": "BUSHS BRAIN", "poster_path": "/xkc6Q3zRj2vELOe1fKKIRevcSGt.jpg"},
        {"title": "WEREWOLF OF LONDON", "poster_path": "/78kD3Fpvgd8qubKMbhS5dKofjR8.jpg"},
        {"title": "THE GUNFIGHTER", "poster_path": "/5696EpyH0tB8DtKvwNGABMRWknX.jpg"},
        {"title": "BUSHS BRAIN", "poster_path": "/xkc6Q3zRj2vELOe1fKKIRevcSGt.jpg"},
        {"title": "WEREWOLF OF LONDON", "poster_path": "/78kD3Fpvgd8qubKMbhS5dKofjR8.jpg"},
        {"title": "THE GUNFIGHTER", "poster_path": "/5696EpyH0tB8DtKvwNGABMRWknX.jpg"},
        # Add more movie objects here
    ]

    # Base URL for the movie images
    base_url = "https://image.tmdb.org/t/p/original/"

    # Render the HTML template and pass the movie data
    return render_template('index.html', movies=movies, base_url=base_url)


if __name__ == '__main__':
    app.run(debug=True)