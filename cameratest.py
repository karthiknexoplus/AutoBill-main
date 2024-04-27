import time
import picamera

def capture_image(output_file):
    with picamera.PiCamera() as camera:
        # Adjust camera settings if necessary
        # For example:
        # camera.resolution = (1920, 1080)  # Set resolution
        # camera.rotation = 180  # Rotate the image

        # Wait for the camera to warm up
        time.sleep(2)

        # Capture an image and save it to the specified output file
        camera.capture(output_file)

if __name__ == "__main__":
    output_file = "image.jpg"  # Specify the output file name
    capture_image(output_file)
    print("Image captured and saved to", output_file)
