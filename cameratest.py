import subprocess
import cv2

def capture_image(output_file):
    try:
        # Use the libcamera command-line tool to capture an image
        subprocess.run(["raspistill", "-o", output_file])
        print("Image captured and saved to", output_file)
    except Exception as e:
        print("Error:", e)

def process_image(input_file):
    try:
        # Read the image using OpenCV
        img = cv2.imread(input_file)

        # Process the image as needed
        # For example, you can display it using imshow
        cv2.imshow("Captured Image", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    output_file = "image.jpg"  # Specify the output file name
    capture_image(output_file)
    process_image(output_file)
