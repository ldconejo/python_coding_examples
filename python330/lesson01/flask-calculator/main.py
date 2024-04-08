import os
import base64

from flask import Flask, render_template, request, session, redirect, url_for

from model import SavedTotal

app = Flask(__name__)

app.secret_key = "do_not_use_this_secret_key"

@app.route('/add', methods=['GET', 'POST'])
def add():
    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number

    return render_template('add.jinja2', session=session)

@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()

    return render_template('save.jinja2', code=code)

# 3QO2DXZCVGV6Y
@app.route('/retrieve')
def retrieve():
    code = request.args.get('code', None)
    if code is None:
        return render_template('retrieve.jinja2')
    else:
        try:
            saved_total = SavedTotal.get(SavedTotal.code == code)
            session['total'] = saved_total.value
        except SavedTotal.DoesNotExist:
            return render_template('retrieve.jinja2', error="Code not found.")
        
        return redirect(url_for('add'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="127.0.0.1", port=port, debug=True)