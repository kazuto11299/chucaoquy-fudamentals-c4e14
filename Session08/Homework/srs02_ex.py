
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    items = [
        {
            'game': 'League of Legends',
            'rank': 'Challenger',
            'price': '1000/h',
            'status': 'Available',
            'game_pic': 'https://www.bleedingcool.com/wp-content/uploads/2017/02/League-of-Legends.png'
        },
        {
            'game': 'Couter-Strike: Global Offensive',
            'rank': 'Global Elite',
            'price': '1500/h',
            'status': 'Available',
            'game_pic': 'http://cdn.edgecast.steamstatic.com/steam/apps/730/header.jpg?t=1512411779'
        },
        {
            'game': "PLAYERUNKNOWN'S BATTLEGROUNDS",
            'rank': 'No ranking system',
            'price': '2000/h',
            'status': 'Available',
            'game_pic': 'http://media.game8.vn/Media/files/PUBG(3).jpg'
        }
    ]
    return render_template('srs02_ex.html', items = items )

if __name__ == '__main__':
    app.run(debug=True)
