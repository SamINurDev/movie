from flask import Flask , request , jsonify
from bs4 import BeautifulSoup
from flask_cors import CORS, cross_origin
import requests
import re

app = Flask(__name__)
cors = CORS(app)

@app.route('/latest-movies',methods=['GET'])
def API():
    if request.method == 'GET':
        '''
        url = "https://topcinema.cam/movies/"

        content = requests.get(url).content
        soup = BeautifulSoup(content, "html.parser")

        movies = soup.find_all('div', {"class":"Small--Box"})

        l = []
        for i in range(1,5):
            if i == 1:
                for i,movie in enumerate(movies):
                    d = {}
                    movie = movies[i].find('a')
                    movie_title = str(movie['title'])
                    title = re.sub(r"[^'a-zA-Z0-9:-]", " ", movie_title).strip()


                    d["movie_title"] = title
                    d["image_url"] = movie.img['src']
                    d["href"] = str(movie['href'])

                    l.append(d)

            else:
                pages_url = "https://topcinema.cam/movies/page/" + str(i)
                content = requests.get(pages_url).content
                soup = BeautifulSoup(content, "html.parser")
                movies = soup.find_all('div', {"class":"Small--Box"})
                for i,movie in enumerate(movies):
                    d = {}
                    movie = movies[i].find('a')
                    movie_title = str(movie['title'])
                    title = re.sub(r"[^a-zA-Z0-9:-]", " ", movie_title).strip()
                    d['movie_title'] = title
                    d["image_url"] = movie.img['src']
                    d["href"] = str(movie['href'])
                    l.append(d)

            '''        

        m = []
        for i in range(1,5):
            url = ""
            if(i == 1):
                url = "https://topcinema.cam/movies/"
            else:
                url = "https://topcinema.cam/movies/page/" + str(i)

            content = requests.get(url).content
            soup = BeautifulSoup(content, "html.parser")

            movies = soup.find_all('div', {"class":"Small--Box"})
            for i,movie in enumerate(movies):
                d = {}
                movie_title = movies[i].find('a')['title']
                movie_title = re.sub(r"[^'a-zA-Z0-9:-]", " ", movie_title).strip()
                movie_image = movies[i].find('a').img['src']
                movie_href = movies[i].find('a')['href']



                d["movie_title"] = movie_title
                d["movie_image_url"] = movie_image
                d["movie_href"] = movie_href

                m.append(d)

        return jsonify(m)



@app.route('/movie', methods=["GET"])
def TEST():
    if request.method == "GET":
        movie_url = request.args.get('url')

        content = requests.get(movie_url).content
        soup = BeautifulSoup(content, 'html.parser')

        movie_iframe = soup.find('iframe')['src']

        return jsonify(movie_iframe)



if __name__ == '__main__':
    app.run()