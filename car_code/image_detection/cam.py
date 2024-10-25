import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time 
# define the lower and upper bounds of the yellow color in HSV
lower_yellow = (0, 100, 100)
upper_yellow = (35, 255, 255)

# initialize the video capture
cap = cv2.VideoCapture(0)


def get_fram_data():
    difference_x = 0 
    difference_y = 0 
    ret, flipped_frame = cap.read()
    # Flip the frame upside down
    frame = cv2.flip(flipped_frame, -1)
    # convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # threshold the frame to get the yellow color
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # find contours in the thresholded frame
    contours, hierarchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # draw a bounding box around the detected yellow object
    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # draw a text box with the label 'box'
        cv2.rectangle(frame, (x, y - 20), (x + 50, y), (0, 255, 0), -1)
        cv2.putText(frame, 'Box', (x + 5, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # Calculate the center of the contour
        center_contour_x = x + (w // 2)
        center_contour_y = y + (h // 2)

        # Draw a small green dot at the center of the contour
        cv2.circle(frame, (center_contour_x, center_contour_y),
                2, (0, 255, 0), -1)

        # Print the position of the center of the contour
        # print("Center of contour position: ({}, {})".format(
        #     center_contour_x, center_contour_y))

    #############################
    # decode QR code if present #
    #############################
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        # Draw a blue contour around the detected QR code
        qr_contour = np.array([obj.polygon], dtype=np.int32)
        cv2.drawContours(frame, qr_contour, -1, (255, 0, 0), 2)
        # Calculate the center of the QR code contour
        qr_center_x = int(obj.rect.left + (obj.rect.width / 2))
        qr_center_y = int(obj.rect.top + (obj.rect.height / 2))

        # Draw a blue small dot at the center of the QR code contour
        cv2.circle(frame, (qr_center_x, qr_center_y), 2, (255, 0, 0), -1)

        # Print the position of the center of the QR code contour
        # print("Center of QR code contour position: ({}, {})".format(
        #     qr_center_x, qr_center_y))

    ######################
    #### center frame ####
    ######################
    # Get the dimensions of the frame
    height, width, _ = frame.shape

    # Calculate the coordinates for the center point
    center_x = int(width / 2)
    center_y = int(height / 2)

    # Draw a small red point at the center
    cv2.circle(frame, (center_x, center_y), 2, (0, 0, 255), -1)

    # Print the position of the center point
    # print("Center point position: ({}, {})".format(center_x, center_y))
    if len(contours) > 0:
        difference_x = center_x - center_contour_x
        difference_y = center_y - center_contour_y
        print("Difference: ({}, {} )".format(difference_x, difference_y))
    
    return (frame,difference_x,difference_y ,decodedObjects)

def scan_box():
    while True:
        # read a frame from the video capture
        frame, difference_x ,difference_y ,decodedObjects =get_fram_data()
        print(difference_x ,difference_y )
        cv2.imshow('frame', frame)
        # break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Done")
    print("Difference: ({}, {})".format(difference_x, difference_y))



# release the video capture and close all windows
if __name__ == '__main__':
    scan_box()