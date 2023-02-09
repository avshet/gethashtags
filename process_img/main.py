
from google.cloud import vision
from flask import Flask,render_template,request,redirect
import os
import io

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = 'static\Images'

@app.route("/home",methods=['POST','GET'])
def upload_image():
    print(request)
    if request.method == "POST":
        image = request.files['file']
        
        if image.filename == '':
            print("File is invalid")
            return redirect(request.url)
        
        filename = image.filename
        basedir = os.path.abspath(os.path.dirname(__file__))

        image_path = os.path.join(basedir,app.config['IMAGE_UPLOADS'],filename)
        image.save(image_path)

        
        #send saved file to google vision
        with io.open(image_path,'rb') as image_file:
            content = image_file.read()
        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=content)

        response = client.label_detection(image=image)
        labels = response.label_annotations
        tags = []

        #get tags from labels
        for label in labels:
            temp = label.description.split()
            temp = "#"+"".join(temp)
            tags.append(temp)

        if response.error.message:
            raise Exception(
                    '{}\nFor more info on error messages, check: '
                    'https://cloud.google.com/apis/design/errors'.format(
                        response.error.message))

        return render_template("main.html",filename=filename,tags=tags)
        
    return render_template("main.html")

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static',filename = '/Images/'+filename),code=301)
app.run(port=5000)