import os
from PIL import Image, ImageDraw, ImageFont

def generate_image_from_text(text_file, output_image):
    # Get the absolute path to the text file
    text_file = os.path.join(os.path.dirname(__file__), text_file)
    # Get the absolute path to the font file
    font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")

 
    
    # Read text from file
    with open(text_file, 'r') as file:
        text = file.read().strip()
    
    # Set up image parameters
    image_width = 400
    image_height = 200
    background_color = (255, 255, 255)  # White
    text_color = (0, 0, 0)  # Black
    font_size = 20
    #font = ImageFont.truetype("arial.ttf", font_size)
    font = ImageFont.truetype(font_path, font_size)
    
    # Create new image
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)
    
    # Fixed position for the text
    text_x = 50  # Replace with the desired X-coordinate
    text_y = 50  # Replace with the desired Y-coordinate
    
    # Draw text on image
    draw.text((text_x, text_y), text, fill=text_color, font=font)
    
    # Save image
    image.save(output_image)
    print("Image generated successfully!")

# Example usage:
text_file_path = "text_file.txt"  # Replace with the filename of your text file
output_image_path = "output_image.png"  # Replace with the desired output image filename
generate_image_from_text(text_file_path, output_image_path)
