from PIL import Image

def create_stego():
    # Load your base image
    img = Image.open("boot-screen.jpg")
    
    # The Caesar +7 shifted flag
    cipher_text = "OIA{wzn_8960}"
    
    # Add to UserComment (EXIF tag 0x9286)
    exif = img.getexif()
    exif[0x9286] = cipher_text
    
    img.save("boot_after_hack.jpg", exif=exif)
    print("Success! File created: boot_after_hack.jpg")

create_stego()