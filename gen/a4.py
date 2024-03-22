from PIL import Image

def upscale_image(input_image_path, output_image_path, target_size):
    # Open the input image
    input_image = Image.open(input_image_path)
    
    # Resize the image while maintaining or improving quality
    resized_image = input_image.resize(target_size, Image.LANCZOS)
    
    
    resized_image.save(output_image_path)
  

input_image_path = "laptop.jpg"
output_image_path = "a4.jpg"
target_size = (800, 600)

upscale_image(input_image_path, output_image_path, target_size)
