import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened correctly
if not cap.isOpened():
    print("Camera is not opened")
    exit()

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to grab frame")
        break 

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        print("Exiting...")
        break

    # Display the current frame
    cv2.imshow("Frame", frame)

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
