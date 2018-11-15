from flask import Flask, request, render_template, send_from_directory
import os
from Controller import Controller

app = Flask(__name__)
controller = Controller()

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

## @package Web
# Documentation for the backend and frontend
# FrameWork; Flask, Bootstrap, 
#  More details.

@app.route("/")
def IND8dex():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'Resources/images/')
    image_names = os.listdir('./Resources/images')
    print(target)
    print("Image Name {}".format(image_names))
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(request.files.getlist("file"))
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename.split('/')[1]
        print(filename)
        destination = "/".join([target, filename])
        print("destinatiooon:",destination)
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        upload.save(destination)
        image_names.append(destination[destination.rfind("/") + 1:])
    if ".DS_Store" in image_names:
        image_names = image_names[1:]
    # return send_from_directory("images", filename, as_attachment=True)
    # return render_template("complete.html", image_name=filename)
    print("IM: {}".format(destination))
    print("IM: {}".format(image_names))
    return render_template("upload.html", image_names=image_names)

#@app.route("/upload", methods=["POST"])
# def upload():
#     """
#     Function that take the image from the picker and save it into a folder where later can be search to display it.
#     """
#     
#     controller.create_folder()
#              
#     #print("Image Name {}".format(image_names))
#     for upload in request.files.getlist("file"):    #Loop through all the images to be uploaded
#         #print("{} is the file name".format(upload.filename))
#         filename = upload.filename.split('/')[1]
#         print("FILENAME")
#         print(filename)
#         print(request.files.getlist("file"))
#         #part1= filename.split('/')[0] 
#         #part2= filename.split('/')[1]
#         #filename2= part2
#         #print(filename2)
#         if filename:    #Validate if there are no images to be upload
#             destination = "\\".join([controller.images_path[:-1], filename])
#             print(controller.images_path[:])      
#             print(filename)
#             print("destination::::",destination)      
#         if filename not in controller.list_images and filename != ".DS_Store": #Validate if the image to be upload is not uploaded yet
#             upload.save(destination)
#             controller.create_Image(destination[destination.rfind("/")+1:])
#             #controller.list_images.append(destination[destination.rfind("/")+1:])
#     
#     if ".DS_Store" in controller.list_images: # Delete if there is a strange file
#         print("borrando..")
#         controller.list_images = controller.list_images[1:]
#         
#     return render_template("upload.html", image_names=controller.list_images)  #Return the same page with the images

@app.route("/process_all", methods=["POST"])  
def process_all():
    controller.process_images()
    
    return render_template("upload.html", image_names=controller.list_images)
                      
@app.route('/upload<filename>')
def send_image(filename):
    """
    Function that save the file given into a folder.
    """
    return send_from_directory("Resources\\images", filename)

if __name__ == "__main__":
    app.run(port=4555, debug=True)