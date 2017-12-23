from flask import Flask, render_template, redirect, url_for
from Models.service import Service

from mlab import mlab_connect

app = Flask(__name__)
mlab_connect()

@app.route('/admin')
def admin():
    return render_template('admin.html', services = Service.objects())

@app.route("/delete/<service_id>")
def delete(service_id):
    service = Service.objects().with_id(service_id)
    if service is None:
        return "Not found"
    else:
        service.delete()
        return redirect(url_for('admin'))


@app.route('/info/<service_id>')
def info(service_id):
    info_service = Service.objects().with_id(service_id)
    info_pic = info_service.game + '.jpg'
    info_account = info_service.account
    info_game = info_service.game
    info_price = info_service.price
    info_contact = info_service.contact
    info_occupied = info_service.occupied
    return render_template('info.html', info_pic = info_pic, info_account = info_account, info_game = info_game, info_price = info_price, info_contact = info_contact, info_occupied = info_occupied)

if __name__ == '__main__':
  app.run(debug=True)
