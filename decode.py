from PIL import Image

def decode_message_from_image(image_file):
    try:
        img = Image.open(image_file)
    except IOError:
        print("Error: Unable to open image file.")
        return ""

    # Get the red channel of the image
    red_channel = img.split()[0]

    # Initialize an empty string to store the extracted message
    extracted_message = ''

    # Extract the LSB (Least Significant Bit) from each pixel value
    width, height = img.size
    for y in range(height):
        for x in range(width):
            pixel_value = red_channel.getpixel((x, y))
            extracted_bit = pixel_value & 1  # Extract the LSB
            extracted_message += str(extracted_bit)

    # Convert the binary string to ASCII characters
    decoded_message = ''
    for i in range(0, len(extracted_message), 8):
        byte = extracted_message[i:i+8]
        decoded_message += chr(int(byte, 2))

    return decoded_message

def decode_message_from_audio(audio_file):
    # Placeholder implementation for decoding message from audio file
    pass

def decode_message_from_video(video_file):
    # Placeholder implementation for decoding message from video file
    pass
