from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)


def db_connection():
    connection = None
    try:
        connection = sqlite3.connect('movies.sqlite')
    except sqlite3.error as e:
        print(e)
    return connection


@app.route('/movies', methods=['GET', 'POST'])
def movies(row=None):
    connection = db_connection()
    cursor = connection.cursor()

    if request.method == 'GET':
        cursor = connection.execute("SELECT *FROM movie")
        movies = [
            dict(id=row[0], title=row[1], director=row[2], language=row[3])
            for row in cursor.fetchall()
        ]
        if movies is not None:
            return jsonify(movies)

    if request.method == 'POST':
        new_title = request.form['title']
        new_director = request.form['director']
        new_language = request.form['language']
        sql = """INSERT INTO movie (title, director, language)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_title, new_director, new_language))
        connection.commit()
        return f"movie with the id: {cursor.lastrowid} created successfully", 201


@app.route('/movie/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def single_movie(id):
    connection = db_connection()
    cursor = connection.cursor()
    movie = None
    if request.method == 'GET':
        cursor.execute("SELECT * FROM movie WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            movie = r
        if movie is not None:
            return jsonify(movie), 200
        else:
            return "something wrong", 404
    if request.method == 'PUT':
        sql = """UPDATE movie
                SET title=?,
                    director=?,
                    language=?
                WHERE id=?"""

        title = request.form['title']
        director = request.form['director']
        language = request.form['language']
        updated_movie = {
                    'id': id,
                    'title': movie['title'],
                    'director': movie['director'],
                    'language': movie['language']
                }
        connection.execute(sql, (title, director, language, id))
        connection.commit()
        return jsonify(updated_movie)
    if request.method == 'DELETE':
        sql = """DELETE FROM movie WHERE id=?"""
        connection.execute(sql, (id,))
        connection.commit()
        return "The movie with id: {} has been deleted".format(id), 200


if __name__ == '__main__':
    app.run()
