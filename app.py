from flask import Flask, request, jsonify
app = Flask(__name__)

movies_list = [
    {
        "id": 1,
        "title": "interstellar",
        "director": "christopher nolan",
        "language": "english"
    },
    {
        "id": 2,
        "title": "irishman",
        "director": "martin scorsese",
        "language": "english"
    },
    {
        "id": 3,
        "title": "pulp fiction",
        "director": "quentin tarantino",
        "language": "english"
    },
    {
        "id": 4,
        "title": "vada chennai",
        "director": "vetrimaaran",
        "language": "tamil"
    },
    {
        "id": 5,
        "title": "RRR",
        "director": "rajamouli",
        "language": "telugu"
    },
    {
        "id": 6,
        "title": "karnan",
        "director": "mari selvaraj",
        "language": "tamil"
    },

]


@app.route('/movies', methods=['GET', 'POST'])
def movies():
    if request.method == 'GET':
        if len(movies_list) > 0:
            return jsonify(movies_list)
        else:
            'Nothing Found 404'

    if request.method == 'POST':
        new_title = request.form['title']
        new_director = request.form['director']
        new_language = request.form['language']
        id = movies_list[-1]['id']+1

        new_obj = {
            'id': id,
            'title': new_title,
            'director': new_director,
            'language': new_language
        }
        movies_list.append(new_obj)
        return jsonify(movies_list), 201


@app.route('/movie/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_movie(id):
    if request.method == 'GET':
        for movie in movies_list:
            if movie['id'] == id:
                return jsonify(movie)
            pass
    if request.method == 'PUT':
        for movie in movies_list:
            if movie['id'] == id:
                movie['title'] = request.form['title']
                movie['director'] = request.form['director']
                movie['language'] = request.form['language']
                updated_movie = {
                    'id': id,
                    'title': movie['title'],
                    'director': movie['director'],
                    'language': movie['language']
                }
                return jsonify(updated_movie)
    if request.method == 'DELETE':
        for index, movie in enumerate(movies_list):
            if movie['id'] == id:
                movies_list.pop(index)
                return jsonify(movies_list)


if __name__ == '__main__':
    app.run()




