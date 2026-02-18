#!/usr/bin/env python3
"""
Artifact Alpha Generator
Creates a JPEG with hidden EXIF metadata containing the flag
Real flag: HTB{psg_grade_swap} -> Caesar +13 (ROT13) -> UGO{cft_tenqr_fjnc}
"""

from PIL import Image
import piexif

def create_defaced_grade_image():
    """
    Create a JPEG image with hidden EXIF metadata containing the Caesar cipher flag.
    Real flag: HTB{psg_grade_swap}
    Encoded (ROT13): UGO{cft_tenqr_fjnc}
    """
    
    # The Caesar cipher flag to hide in EXIF (ROT13 encoded)
    hidden_flag = "UGO{cft_tenqr_fjnc}"
    
    # Create a new image simulating a "defaced" grade screen
    width, height = 1024, 768
    image = Image.new('RGB', (width, height), color=(20, 10, 10))
    
    # Save temporarily to add EXIF
    temp_path = '/tmp/temp_grade.jpg'
    image.save(temp_path, 'jpeg')
    
    # Create EXIF data with the hidden flag
    exif_dict = {
        "0th": {
            piexif.ImageIFD.Make: b"University_System",
            piexif.ImageIFD.Model: b"REGISTRAR-PROD-01",
            piexif.ImageIFD.ImageDescription: b"System Screenshot - CONFIDENTIAL",
            piexif.ImageIFD.Software: b"ScreenCapture v2.1.4",
        },
        "Exif": {
            piexif.ExifIFD.DateTimeOriginal: b"2026:02:16 02:15:33",
            piexif.ExifIFD.UserComment: hidden_flag.encode('utf-8'),
        },
        "GPS": {}
    }
    
    exif_bytes = piexif.dump(exif_dict)
    
    # Save with EXIF data
    image.save('defaced_grade.jpg', 'jpeg', exif=exif_bytes)
    
    print("✓ Artifact Alpha created: defaced_grade.jpg")
    print(f"  Hidden flag in EXIF metadata: {hidden_flag}")
    print("  Real flag (ROT13 decoded): HTB{psg_grade_swap}")
    print("  Location: EXIF UserComment field")
    print("  To extract: exiftool defaced_grade.jpg | grep 'User Comment'")
    print("  To decode: Apply ROT13 cipher")
    
    return 'defaced_grade.jpg'


def verify_exif():
    """Verify the EXIF data was written correctly"""
    try:
        exif_dict = piexif.load('defaced_grade.jpg')
        user_comment = exif_dict["Exif"][piexif.ExifIFD.UserComment].decode('utf-8')
        print(f"\n✓ Verification: EXIF UserComment = {user_comment}")
    except Exception as e:
        print(f"Note: EXIF verification error: {e}")


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
