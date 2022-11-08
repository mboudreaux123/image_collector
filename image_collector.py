# Michael Boudreaux
# 11/7/2022
# Capture a series of images at a specified time interval

# Credit:
# Python | OpenCV program to read and save an Image
# https://www.geeksforgeeks.org/python-opencv-program-to-read-and-save-an-image/
# How to change a datetime format in python?
# https://stackoverflow.com/questions/64137532/how-to-change-a-datetime-format-in-python

import cv2, time, argparse
from datetime import datetime
  
TIME_INTERVAL = 0.25 # Interval is in seconds
SHOW_FRAME_ENABLED = False

WINDOW_NAME = "Gathering images... Rate: " + str(1 / TIME_INTERVAL) + " per sec"

def printBorder():
    print("-" * 64) 

def printSummary(camera, counter):
    printBorder()
    print()
    print("Summary:")
    print()
    print("Images Captured: " + str(counter -1))
    print("Time Interval: " + str(TIME_INTERVAL) + " per sec")
    print("Frame Width: " + str(int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))))
    print("Frame Width: " + str(int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    print("Camera FPS: " + str(camera.get(cv2.CAP_PROP_FPS)))
    print()
    printBorder()

def generateFilename():
    filename = str(datetime.now())
    filename = filename.replace(" ", "-")
    filename = filename.replace(".", "-")
    filename = filename.replace(":", "-")
    filename = filename + ".png"

    return filename

def main():
    try:
        # define a video capture object
        camera = cv2.VideoCapture(0)

        counter = 1
        while True:
            
            # Read the frame data
            ret, frame = camera.read()
        
            # Display the image if enabled
            if SHOW_FRAME_ENABLED:
                cv2.imshow(WINDOW_NAME, frame)
            
            # Generate photo to file and print feedback
            filename = generateFilename()
            cv2.imwrite(filename, frame)
            print("File " + str(counter) + ": " + filename)

            # the 'q' button is set as the
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Increment counter and wait at the interval time
            counter = counter + 1
            time.sleep(TIME_INTERVAL)
        
        # Cleanup after exit
        printSummary(camera, counter)
        camera.release()
        cv2.destroyAllWindows()
    
    except KeyboardInterrupt:
        printSummary(camera, counter)
        camera.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()