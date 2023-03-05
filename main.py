from flask import *  
from datetime import datetime
app = Flask(__name__)

# save downloaded files to user list
users = {
    
}

def get_size(fobj):
    if fobj.content_length:
        return fobj.content_length

    try:
        pos = fobj.tell()
        fobj.seek(0, 2)  #seek to end
        size = fobj.tell()
        fobj.seek(pos)  # back to original position
        return size
    except (AttributeError, IOError):
        pass

    # in-memory file object that doesn't support seeking or tell
    return 0  #assume small enough


# datetime object containing current date and time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/upload/<user>', methods=['POST'])
def upload(user):  
    if request.method == 'POST':  
        for fobj in request.files.getlist('f[]'):
            if get_size(fobj) > 300 * (1024 ** 2):
                abort(413)  # request entity too large
        f = request.files['file']
        #LOG
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print(f"{dt_string}| [{user}] File uploaded: {f.filename}")

        f.save("Files\\" + f.filename)  
        users[user] = f.filename      
        return 200

@app.route('/api/getfilename/<user>', methods=['GET'])
def getfilename(user):
    if request.method == 'GET':
        return users[user]


@app.route('/api/download/<user>', methods=['GET'])
def download(user):  
    if request.method == 'GET':  
        print(users[user])
        # return file to user
        return send_file(users[user], as_attachment=True)


if __name__ == '__main__':
    app.run(port=7979)

