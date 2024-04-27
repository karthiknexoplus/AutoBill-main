import cv2
def capture_image(output_file):
    # Open the camera
    camera = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not camera.isOpened():
        print("Error: Unable to open camera")
        return

    # Capture frame-by-frame
    ret, frame = camera.read()

    # Release the camera
    camera.release()

    # Check if the frame is captured successfully
    if not ret:
        print("Error: Unable to capture frame")
        return

    # Save the captured frame to the output file
    cv2.imwrite(output_file, frame)
    print("Image captured and saved to", output_file)

if __name__ == "__main__":
    output_file = "image.jpg"  # Specify the output file name
    capture_image(output_file)
