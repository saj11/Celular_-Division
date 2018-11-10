from flask import Flask, request, render_template, send_from_directory
import os
from Controller import Controller

app = Flask(__name__)
controller = Controller()
## @package Web
# Documentation for the backend and frontend
# FrameWork; Flask, Bootstrap, 
#  More details.

@app.route("/")
def index():
    """
    Function that gives the start html.
    """
    return render_template("upload.html")

@app.route("/upload", methods=["POST"])
def upload():
    """
    Function that take the image from the picker and save it into a folder where later can be search to display it.
    """
    
    controller.create_folder()
             
    #print("Image Name {}".format(image_names))
    for upload in request.files.getlist("file"):    #Loop through all the images to be uploaded
        #print("{} is the file name".format(upload.filename))
        filename = upload.filename
        print("FILENAME")
        print(filename)
        print(filename.split('/'))
        part1= filename.split('/')[0] 
        part2= filename.split('/')[1]
        print("nombre archivo")
        print(part1+"\\"+part2)
        filename2= part2
        print(filename2)
        if filename:    #Validate if there are no images to be upload
            destination = "/".join([controller.images_path[:], filename2])            
            if filename not in controller.list_images and filename != ".DS_Store": #Validate if the image to be upload is not uploaded yet
                upload.save(destination)
                controller.create_Image(destination[destination.rfind("/")+1:])
                #controller.list_images.append(destination[destination.rfind("/")+1:])
    
    if ".DS_Store" in controller.list_images: # Delete if there is a strange file
        print("borrando..")
        controller.list_images = controller.list_images[1:]
        
    return render_template("upload.html", image_names=controller.list_images)  #Return the same page with the images

@app.route("/process_all", methods=["POST"])  
def process_all():
    controller.process_images()
    
    return render_template("upload.html", image_names=controller.list_images)
                      
@app.route('/upload<filename>')
def send_image(filename):
    """
    Function that save the file given into a folder.
    """
    return render_template("upload.html", image_names=controller.list_images)

if __name__ == "__main__":
    app.run(port=4555, debug=True)