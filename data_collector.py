import os
import cv2
import time
import uuid
import logging
IMAGE_PATH="CollectedImages"

labels=['Hello','Yes','Luv U','Please']



num_images = 5

for label in labels:
    img_path=os.path.join(IMAGE_PATH,label)
    os.makedirs(img_path,exist_ok=True)


    cap=cv2.VideoCapture(0)  #opening camera
    logging.info(f"opening camera")
    time.sleep(3)


    for imgnum in range(num_images):
        ret,frame =  cap.read()
        imagename=os.path.join(IMAGE_PATH,label,label + '.' + '{}.jpg' .format(str(uuid.uuid1())))
        cv2.imwrite(imagename,frame)
        cv2.imshow('frame',frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break

    cap.release()