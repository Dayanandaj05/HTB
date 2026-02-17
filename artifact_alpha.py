#!/usr/bin/env python3
"""
Artifact Alpha Generator
Creates a JPEG with hidden EXIF metadata containing the Caesar cipher flag
"""

from PIL import Image
import piexif

def create_defaced_grade_image():
    """
    Create a JPEG image with hidden EXIF metadata containing the flag:
    EVENT{HACKER_IP_FOUND} -> Caesar +7 -> LCLUA{OHJRLY_PW_MVBUK}
    """
    
    # The Caesar cipher flag to hide in EXIF
    hidden_flag = "LCLUA{OHJRLY_PW_MVBUK}"
    
    # Create a new image simulating a "defaced" grade screen
    # Dark red/black theme to indicate compromise
    width, height = 1024, 768
    image = Image.new('RGB', (width, height), color=(20, 10, 10))
    
    # Save temporarily to add EXIF
    temp_path = '/tmp/temp_grade.jpg'
    image.save(temp_path, 'jpeg')
    
    # Create EXIF data with the hidden flag
    exif_dict = {
        "0th": {
            piexif.ImageIFD.Make: b"University_System",
            piexif.ImageIFD.Model: b"Registrar_Terminal",
            piexif.ImageIFD.ImageDescription: b"System Screenshot - DO NOT DISTRIBUTE",
        },
        "Exif": {
            piexif.ExifIFD.DateTimeOriginal: b"2026:02:16 02:15:00",
            piexif.ExifIFD.UserComment: hidden_flag.encode('utf-8'),
        },
        "GPS": {}
    }
    
    exif_bytes = piexif.dump(exif_dict)
    
    # Save with EXIF data
    image.save('defaced_grade.jpg', 'jpeg', exif=exif_bytes)
    
    print("✓ Artifact Alpha created: defaced_grade.jpg")
    print(f"  Hidden flag in EXIF metadata: {hidden_flag}")
    print("  Location: UserComment field")
    print("  To extract: Use exiftool or PIL to read EXIF UserComment")
    
    return 'defaced_grade.jpg'


def verify_exif():
    """Verify the EXIF data was written correctly"""
    try:
        exif_dict = piexif.load('defaced_grade.jpg')
        user_comment = exif_dict["0th"][piexif.ImageIFD.UserComment]
        print(f"\n✓ Verification: EXIF UserComment = {user_comment}")
    except Exception as e:
        print(f"Note: EXIF verification requires PIL/piexif: {e}")


if __name__ == "__main__":
    try:
        create_defaced_grade_image()
        verify_exif()
    except ImportError:
        print("Installing required package: piexif...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'piexif', '-q'])
        create_defaced_grade_image()
        verify_exif()
