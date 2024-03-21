import os
from PIL import Image, ImageDraw, ImageFont

def generate_image_from_text_files(text_files, output_image, lines_y, image_mapping, image_data):
    # Set up image parameters
    image_width = 400
    image_height = 200
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

        # Check if the current text file is the one to apply image mapping
        if text_file == "text_file1.txt" and text in image_mapping:
            # Get the filename of the corresponding PNG image
            png_image_file = os.path.join(os.path.dirname(__file__), image_mapping[text])

            # Open and paste the PNG image onto the image
            png_image = Image.open(png_image_file)
            image.paste(png_image, (text_x + 150, text_y))  # Adjust position as needed

    # Paste PNG images specified in the image_data dictionary
    for image_file, image_properties in image_data.items():
        # Get the absolute path to the image file
        image_file = os.path.join(os.path.dirname(__file__), image_file)
        
        # Open the PNG image
        png_image = Image.open(image_file)
        
        # Resize the PNG image if specified
        if 'scale' in image_properties:
            scale = image_properties['scale']
            png_image = png_image.resize((int(png_image.width * scale), int(png_image.height * scale)))

        # Get the position for pasting the PNG image
        image_x = image_properties.get('x', 0)
        image_y = image_properties.get('y', 0)

        # Paste the PNG image onto the image
        image.paste(png_image, (image_x, image_y), png_image)

    # Draw multiple horizontal lines
    for line_y in lines_y:
        draw.line([(0, line_y), (image_width, line_y)], fill=(0, 0, 0), width=2)  # Adjust line properties as needed

    # Save image
    image.save(output_image)
    print("Image generated successfully!")

# Example usage:
text_files = {
    "title.txt": {"x": 70, "y": 70, "font_size": 80, "text_color": (0, 0, 0), "font_file": "arial.ttf"},
    "desc.txt": {"x": 70, "y": 160, "font_size": 30, "text_color": (255, 0, 0), "font_file": "arial.ttf"},
    
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

lines_y = [175]  # List of y-coordinates for the lines

image_mapping = {
    "HP": "HP.png",  # Mapping text content to PNG image filename
    "SAMSUNG": "SAMSUNG.png",  # Add more mappings as needed
}  # Dictionary containing text content and corresponding PNG image filenames

image_data = {
    "logo.png": {"x": 550, "y": 100, "scale": 1},
}  # Dictionary containing PNG image file paths and their properties

output_image_path = "laptop.png"  # Replace with the desired output image filename
generate_image_from_text_files(text_files, output_image_path, lines_y, image_mapping, image_data)
