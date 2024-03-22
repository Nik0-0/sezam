from PIL import Image
import os

# Function to add image to A4 page and save as PNG
def add_image_to_page_and_save():
    # Get the absolute path to the image file
    current_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_directory, "add.png")

    # Load the image
    try:
        image = Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: Could not find the image file: {image_path}")
        return

    # Open or create the A4 page
    try:
        a4_page = Image.open("a4_page.png")
    except FileNotFoundError:
        a4_page = Image.new("RGB", (2480, 3508), color="white")

    # Load or initialize the counter
    counter_file = os.path.join(current_directory, "counter.txt")
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            counter = int(f.read())
    else:
        counter = 0

    # If the counter is 5, clear the page and reset the counter
    if counter == 5:
        a4_page = Image.new("RGB", (2480, 3508), color="white")
        counter = 0

    # Calculate the position for the new image
    row = counter // 2
    col = counter % 2
    position = (50 + col * 1240, 50 + row * 1754)

    # Paste the image onto the A4 page
    a4_page.paste(image, position)

    # Save the updated A4 page
    a4_page.save("a4_page.png")

    # Increment the counter and save it
    counter += 1
    with open(counter_file, "w") as f:
        f.write(str(counter))

# Test the function
add_image_to_page_and_save()