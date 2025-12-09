"""Generate the alien sprite image."""
import struct
import os

def create_alien_bmp():
    """Create a simple 20x20 BMP alien sprite."""
    width, height = 20, 20
    bytes_per_row = ((width * 24 + 31) // 32) * 4

    # BMP file header
    bmp_data = b'BM'  # Signature
    file_size = 54 + bytes_per_row * height
    bmp_data += struct.pack('<I', file_size)  # File size
    bmp_data += struct.pack('<HH', 0, 0)  # Reserved
    bmp_data += struct.pack('<I', 54)  # Offset to pixel data

    # DIB header (BITMAPINFOHEADER)
    bmp_data += struct.pack('<I', 40)  # Header size
    bmp_data += struct.pack('<i', width)  # Width
    bmp_data += struct.pack('<i', height)  # Height
    bmp_data += struct.pack('<HH', 1, 24)  # Planes and bits per pixel
    bmp_data += struct.pack('<I', 0)  # Compression
    bmp_data += struct.pack('<I', 0)  # Image size
    bmp_data += struct.pack('<i', 0)  # X pixels per meter
    bmp_data += struct.pack('<i', 0)  # Y pixels per meter
    bmp_data += struct.pack('<I', 0)  # Colors used
    bmp_data += struct.pack('<I', 0)  # Important colors

    # Pixel data (BGR format, bottom-up)
    for y in range(height):
        row = b''
        for x in range(width):
            # Green background
            r, g, b = 0, 255, 0
            # Black eyes
            if (3 <= x <= 6 and 3 <= y <= 6) or (13 <= x <= 16 and 3 <= y <= 6):
                r, g, b = 0, 0, 0
            row += struct.pack('BBB', b, g, r)
        # Pad row to 4-byte boundary
        padding = bytes_per_row - (width * 3)
        row += b'\x00' * padding
        bmp_data += row

    # Write to file
    os.makedirs('images', exist_ok=True)
    with open('images/alien.bmp', 'wb') as f:
        f.write(bmp_data)
    print('Alien sprite image created: images/alien.bmp')


if __name__ == '__main__':
    create_alien_bmp()

