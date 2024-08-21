import os
import html
from PIL import Image, ImageDraw, ImageFont
import barcode

ean_input_file = os.path.join(os.path.dirname(__file__), "ean_input.txt")
with open(ean_input_file, 'r') as file:
 ean_code = file.read().strip()

ean_image = barcode.get_barcode_class('ean13')(ean_code, writer=barcode.writer.ImageWriter())
temp_ean_file = os.path.join(os.path.dirname(__file__), "temp_ean")
ean_image.save(temp_ean_file)  # Save EAN code as an image



def generate_image_from_text_files(text_files, output_image, lines_y, image_mapping, image_data, ean_code):
    # Set up image parameters
    image_width = 870
    image_height = 1235
    background_color = (255, 255, 255)  # White

    # Create new image
    image = Image.new("RGB", (image_width, image_height), background_color)
    draw = ImageDraw.Draw(image)

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

    # Iterate over text files
    for text_file, properties in text_files.items():
        # Get the absolute path to the text file
        text_file = os.path.join(os.path.dirname(__file__), text_file)

        # Read text from file with utf-8 encoding
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read().strip()
        # Escape html chars if theres one
        text = html.unescape(text)
        # Remove the leftover symbols
        text = text.replace('\\"', '"')

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
        if "title.txt" in os.path.basename(text_file):
            print(f"Text read from title.txt: {text}")  # Debug
            # Convert everything to lowercases
            image_mapping_lower = {key.lower(): value for key, value in image_mapping.items()}
            if text.lower() in image_mapping_lower:
                print(f"Detected {text} in {text_file}, applying image mapping...")  # Debug
                # Get the filename of the corresponding PNG image
                png_image_file = os.path.join(os.path.dirname(__file__), image_mapping_lower[text.lower()])
                # Open and paste the PNG image onto the image
                png_image = Image.open(png_image_file)
                image.paste(png_image, (35, 35))  # Adjust position as needed  | text_x + 150, text_y)

    # Draw multiple horizontal lines
    for line_y in lines_y:
        draw.line([(0, line_y), (image_width, line_y)], fill=(0, 0, 0), width=2)  # Adjust line properties as needed








    # Open the EAN image
    ean_image = Image.open(os.path.join(os.path.dirname(__file__), "temp_ean.png"))

    # Define the scale factor
    scale_factor = 0.5  # Adjust this value as needed

    # Calculate the new size of the EAN image based on the scale factor
    new_width = int(ean_image.width * scale_factor)
    new_height = int(ean_image.height * scale_factor)

    # Resize the EAN image
    ean_image = ean_image.resize((new_width, new_height))

    # Paste the resized EAN image onto the main image at position (5, 0)
    image.paste(ean_image, (590, 1000))



    # Draw outline for better cutting etc...
    draw.rectangle([(0, 0), (image_width - 1, image_height - 1)], outline=(0, 0, 0))


    # Save image
    image.save(output_image)
    print("Image generated successfully!")

# Example usage:
text_files = {
    "title.txt": {"x": 170, "y": 35, "font_size": 85, "text_color": (0, 0, 0), "font_file": "us_heavy.otf"},
    "desc.txt": {"x": 170, "y": 110, "font_size": 40, "text_color": (0, 0, 0), "font_file": "us_thin.otf"},

    "sub1.txt": {"x": 100, "y": 190, "font_size": 55, "text_color": (0, 0, 0), "font_file": "fonts/Ubuntu-L.ttf"},
    "text1.txt": {"x": 100, "y": 270, "font_size": 35, "text_color": (0, 0, 0), "font_file": "us_thin.otf"},

    "sub2.txt": {"x": 100, "y": 390, "font_size": 55, "text_color": (0, 0, 0), "font_file": "fonts/Ubuntu-L.ttf"},
    "text2.txt": {"x": 100, "y": 470, "font_size": 35, "text_color": (0, 0, 0), "font_file": "us_thin.otf"},

    "sub3.txt": {"x": 100, "y": 590, "font_size": 55, "text_color": (0, 0, 0), "font_file": "fonts/Ubuntu-L.ttf"},
    "text3.txt": {"x": 100, "y": 670, "font_size": 35, "text_color": (0, 0, 0), "font_file": "us_thin.otf"},

    "text4.txt": {"x": 100, "y": 805, "font_size": 25, "text_color": (0, 0, 0), "font_file": "us_thin.otf"},


    "zl_brutto.txt": {"x": 650, "y": 1150, "font_size": 50, "text_color": (0, 0, 0), "font_file": "fonts/Ubuntu-M.ttf"},
    "price.txt": {"x": 50, "y": 1050, "font_size": 150, "text_color": (0, 0, 0), "font_file": "fonts/Ubuntu-M.ttf"},



}  # Dictionary containing text file paths and their properties

lines_y = [175,375,575,775]  # List of y-coordinates for the lines

image_mapping = {
    "HP": "HP.png",  # Mapping text content to PNG image filename
    "SAMSUNG": "SAMSUNG.png",
    "XIAOMI": "XIAOMI.png",
    "PHILIPS": "PHILIPS.png",
    "FINLUX": "FINLUX.png",
    "TOSHIBA": "TOSHIBA.png",
    "LG": "LG.png",
    "TELEFUNKEN": "TELEFUNKEN.png",
    "NIKO": "NIKO.png",
    "HISENSE": "HISENSE.png", 
    "LENOVO": "LENOVO.png",
}  # Dictionary containing text content and corresponding PNG image filenames

image_data = {
    "logo.png": {"x": 525, "y": 42, "scale": 0.4},
    "tlo1.png": {"x": 35, "y": 33, "scale": 1},
    "tlo.png": {"x": 35, "y": 1040, "scale": 10},


    "check.png": {"x": 17, "y": 197, "scale": 0.5},
    "check2.png": {"x": 17, "y": 397, "scale": 0.5},
    "check3.png": {"x": 17, "y": 597, "scale": 0.5},
    "question.png": {"x": 17, "y": 797, "scale": 0.5},
}  # Dictionary containing PNG image file paths and their properties



    


output_image_path = "laptop.png"  # Replace with the desired output image filename


generate_image_from_text_files(text_files, output_image_path, lines_y, image_mapping, image_data, ean_code)
