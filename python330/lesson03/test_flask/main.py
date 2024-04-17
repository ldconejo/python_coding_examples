import os

from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Added in "Add numbers"
app.secret_key = b'$W\x0f\xa4,\x8b\x03&\xe2g[\xb2>\xf8\xe8\xda\xe2\x83\xdc\xa1~&\xaf\xb7'

# Added in "Save progress"
from model import SavedTotal

# Added later in "Save progress"
import base64

@app.route('/add', methods=['GET', 'POST'])
def add():
    # Added in "Add numbers"
    if 'total' not in session:
        session['total'] = 0

    if request.method == 'POST':
        number = int(request.form['number'])
        session['total'] += number

    #return render_template('add.jinja2')

    # Added in "Add numbers"
    return render_template('add.jinja2', session=session)

# Added in "Add numbers"
@app.route('/save', methods=['POST'])
def save():
    total = session.get('total', 0)
    code = base64.b32encode(os.urandom(8)).decode().strip("=")

    saved_total = SavedTotal(value=total, code=code)
    saved_total.save()

    return render_template('save.jinja2', code=code)

# Added in "Retrieve totals"
@app.route('/retrieve')
def retrieve():
    # Using request.args because we're using the GET method
    code = request.args.get('code', None)

    if code is None:
        return render_template('retrieve.jinja2')
    else:
        try:
            saved_total = SavedTotal.get(SavedTotal.code == code)
            session['total'] = saved_total.value
        except SavedTotal.DoesNotExist:
            return render_template('retrieve.jinja2', error="Code not found.")

        session['total'] = saved_total.value
        
        return redirect(url_for('add'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='127.0.0.1', port=port)
