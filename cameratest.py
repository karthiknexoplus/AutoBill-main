import subprocess

def capture_image(output_file):
    # Use the libcamera command-line tool to capture an image
    try:
        subprocess.run(["raspistill", "-o", output_file])
        print("Image captured and saved to", output_file)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    output_file = "image.jpg"  # Specify the output file name
    capture_image(output_file)
