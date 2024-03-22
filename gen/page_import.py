from PIL import Image
import os


def page_for_print():

    laptop_image_path = "add.png"
    laptop_image = Image.open(laptop_image_path)


    try:
        a4_page = Image.open("a4_page.png")
    except FileNotFoundError:
        a4_page = Image.new("RGB", (2480, 3508), color="white")

    # Load or initialize the counter
    counter_file = "counter.txt"
    if os.path.exists(counter_file):
        with open(counter_file, "r") as f:
            counter = int(f.read())
    else:
        counter = 0

    # If the counter is 4, clear the page and reset the counter
    if counter == 4:
        a4_page = Image.new("RGB", (2480, 3508), color="white")
        counter = 0

    # Calculate the position for the new image
    row = counter // 2
    col = counter % 2
    position = (50 + col * 1240, 50 + row * 1754)

    # Paste the laptop image onto the A4 page
    a4_page.paste(laptop_image, position)

    # Save the updated A4 page
    a4_page.save("a4_page.png")

    # Increment the counter and save it
    counter += 1
    with open(counter_file, "w") as f:
        f.write(str(counter))


page_for_print()
