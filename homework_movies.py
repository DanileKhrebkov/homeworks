import json
import os 


    

class Movies:
    def __init__(self, file):
        self.filename = file
        try:
            if os.path.exists(file):
                with open(self.filename, 'r', encoding='UTF-8') as file:
                    self.file = json.load(file)
            else:
                self.file = []
        except json.JSONDecodeError:
            self.file = []

    def search_movie(self, nameMovie):
        for movie in self.file:
            if movie["name"] == nameMovie:
                return movie
            
    def add_movie(self, nameMovie, yearMovie):
        self.file.append({"name":nameMovie, "year":yearMovie})

    def del_movie(self, movieName):
        for movie in self.file:
            if movie["name"] == movieName:
                self.file.remove(movie)

    def save_file(self):
        with open(self.filename, 'w', encoding='UTF-8') as file:
            json.dump(self.file, file, indent=4)

FILE = 'movies.json'
myMovies = Movies(FILE)
myMovies.del_movie('Lion King 2')
myMovies.add_movie('Shrek 5', '2027')
myMovies.save_file()