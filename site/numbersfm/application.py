import os, commands
from flask import Flask, render_template, request, session, url_for, \
    redirect
from auth import session_key_required


app = Flask(__name__)
app.config.from_object('settings')

# ---------------------
# Utils
# ---------------------    

def start_archives():
    if commands.getoutput('pidof ices'):
        return

    commands.getoutput('start_ices.sh')
    
def stop_archives():
    commands.getoutput('stop_ices.sh')
    
def archive_stream_is_running():
    try:
        ices_pid = int(commands.getoutput('pidof ices'))
        return True
    except ValueError:
        return False

    
# ---------------------
# Views
# ---------------------    
    
@app.route("/secrets/stream", methods=['POST', 'GET'])
@session_key_required('admin_logged_in', True, '/secrets/login')
def stream_index():
    if request.method == 'POST':
        archive_action = request.form['archive-action']
        
        if archive_action == 'stop':
            stop_archives()
        elif archive_action == 'start':
            start_archives()
    return render_template('stream_control.html',
                           archives_playing=archive_stream_is_running())

@app.route("/secrets/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and \
                request.form['password'] == app.config['ADMIN_PASSWORD']:
            session['admin_logged_in'] = True
            if request.form.get('from'):
                return redirect(request.form['from'])
            else:
                return redirect('/secrets')
        else:
            error = "Invalid credentials"

    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)

