from PIL import Image

def create_stego():
    # Load your base image
    img = Image.open("input_image.jpg")
    
    # The Caesar +7 shifted flag
    cipher_text = "LCLUA{wzn_8960}"
    
    # Add to UserComment (EXIF tag 0x9286)
    exif = img.getexif()
    exif[0x9286] = cipher_text
    
    img.save("warehouse_dispatch.jpg", exif=exif)
    print("Success! File created: warehouse_dispatch.jpg")

create_stego()