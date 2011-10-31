import os, commands
from flask import Flask, render_template, request


app = Flask(__name__)

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

@app.route("/control/stream", methods=['POST', 'GET'])
def stream_control_index():
    if request.method == 'POST':
        archive_action = request.form['archive-action']
        
        if archive_action == 'stop':
            stop_archives()
        elif archive_action == 'start':
            start_archives()
        
    return render_template('stream_control.html',
                           archives_playing=archive_stream_is_running())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000, debug=True)
