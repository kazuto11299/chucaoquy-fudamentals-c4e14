from flask import Flask, render_template, redirect
app = Flask(__name__)
@app.route('/about_me')
def about_me():
    info = {
        'Name': 'Quy',
        'Work': 'Student',
        'School': 'Luong The Vinh High School',
        'Hobbies': 'Reading, Listening to music, Playing games',
        'Pet': 'None',
        'Crush': 'Nope :D'
    }
    return render_template('about_me.html', me = info)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
  app.run(debug=True)
