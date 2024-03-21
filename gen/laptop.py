import os
from PIL import Image, ImageDraw, ImageFont

def generate_image_from_text_files(text_files, output_image):
    # Set up image parameters
    image_width = 870
    image_height = 1235
    background_color = (255, 255, 255)  # White

    # Create new image
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

    for text_file, properties in text_files.items():
        # Get the absolute path to the text file
        text_file = os.path.join(os.path.dirname(__file__), text_file)

        # Read text from file
        with open(text_file, 'r') as file:
            text = file.read().strip()

        # Set text properties
        font_size = properties.get('font_size', 20)
        font_color = properties.get('text_color', (0, 0, 0))  # Default: black
        text_x = properties.get('x', 0)
        text_y = properties.get('y', 0)
        
        # Load font if specified
        font = None
        font_file = properties.get('font_file')
        if font_file:
            font_path = os.path.join(os.path.dirname(__file__), font_file)
            font = ImageFont.truetype(font_path, font_size)

        # Draw text on image
        draw.text((text_x, text_y), text, fill=font_color, font=font)

    # Save image
    image.save(output_image)
    print("Image generated successfully!")

# Example usage:
text_files = {
    "title.txt": {"x": 70, "y": 70, "font_size": 80, "text_color": (0, 0, 0), "font_file": "arial.ttf"}
   # "desc.txt": {"x": 100, "y": 100, "font_size": 30, "text_color": (255, 0, 0), "font_file": "arial.ttf"},
    
   # "sub1.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
   # "size.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},

   # "sub2.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
   # "res.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
   # "rest.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},

   # "desc1.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
   # "info1.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},

   # "desc2.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
   # "info2.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},

   # "price.txt": {"x": 150, "y": 150, "font_size": 25, "text_color": (0, 0, 255), "font_file": "arial.ttf"},
    
}  # Dictionary containing text file paths and their properties
output_image_path = "laptop.png"  # Replace with the desired output image filename
generate_image_from_text_files(text_files, output_image_path)
