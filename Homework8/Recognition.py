import os
import face_recognition
import cv2
import matplotlib.pyplot as plt

# make a list of available images
knownimages = os.listdir('KnownImages')
testimages = os.listdir('WhoAreThese')

# load your image (this is the image wish to identify)
# iterate over each image (known)
for image in knownimages:
    print('*************** Testing new image ***************')
    image_to_be_matched = face_recognition.load_image_file('KnownImages/' + image)
    image_to_be_matched_encoded = face_recognition.face_encodings(image_to_be_matched)[0]
    for testimage in testimages:
        # load the image
        current_image = face_recognition.load_image_file('WhoAreThese/' + testimage)
        # encode the loaded image into a feature vector
        current_image_encoded = face_recognition.face_encodings(current_image)[0]
        # do they match
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        print('Checking image with this image:', testimage)
        if result[0] == True:
            print('Matched:' + image)
        else:
            print('Not matched:' + image)
    print('\n\n')
print('End')
