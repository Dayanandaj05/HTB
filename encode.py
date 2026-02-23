from PIL import Image

def create_stego():
    # Load your base image
    img = Image.open("boot-screen.jpg")
    
    # The Caesar +7 shifted flag
    cipher_text = "catalyst Hyperion Nexus node Xenon 3layer vector delta Vector 9phase hacker cipher matrix Vector flux Yield 2axis xeno vector cipher 2unit Unity equals \n"

    
    # Add to UserComment (EXIF tag 0x9286)
    exif = img.getexif()
    exif[0x9286] = cipher_text
    
    img.save("boot-after-hack.jpg", exif=exif)
    print("Success! File created: boot-after-hack.jpg")

create_stego()