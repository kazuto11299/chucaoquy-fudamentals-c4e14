from flask import Flask, render_template
app = Flask(__name__)


@app.route('/') # When users access homepage
def index(): # Call this function
    post_list = [
        "Two little lizards",
        "Very unlucky",
        "What do you want",
        "Link"
    ]
    return render_template('index.html', article_title="A duck", posts=post_list)

@app.route('/blog')
def blog():
    posts = [
        {
            "content": "Two little lizzards",
            "author": "Thanh"
        },
        {
            "content": "Very unlucky",
            "author": "Quan"
        },
        {
            "content": "What do you want",
            "author": "Huong"
        },
        {
            "content": "Link",
            "author": "Son Tung"
        },
    ]
    return render_template('blog.html', posts=posts)

@app.route('/hello')
def hello():
    return "Hello C4E"


@app.route('/hello_me')
def hello_me():
    return "Hello Quy"


@app.route('/hello_me/hello_Duy')
def hello_Duy():
    return "U piece of shit"


@app.route('/sayhi/<name>')
def sayhi(name):
    return "Son of a bitch " + name


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return "Ahihi " + str(a + b)

@app.route('/heading')
def heading():
    return "<h1>Chữ cực to và đậm</h1>"


if __name__ == '__main__':
  app.run(debug=True)
