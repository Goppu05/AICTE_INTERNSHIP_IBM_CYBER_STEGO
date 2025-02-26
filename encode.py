from PIL import Image

def encode_message_in_image(image_file, message, output_file):
    try:
        img = Image.open(image_file)
    except IOError:
        print("Error: Unable to open image file.")
        return False

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)

    # Check if the image size is large enough to accommodate the message
    width, height = img.size
    if len(binary_message) > width * height:
        print("Error: Message is too large to be encoded in the image.")
        return False

    # Get the red channel of the image
    red_channel = img.split()[0]

    # Encode the message into the least significant bit (LSB) of each pixel value
    encoded_pixels = []
    binary_index = 0
    for pixel in red_channel.getdata():
        # Ensure we have more bits to encode
        if binary_index < len(binary_message):
            # Clear the least significant bit and set it to the next bit of the message
            new_pixel = (pixel & 0xFE) | int(binary_message[binary_index])
            encoded_pixels.append(new_pixel)
            binary_index += 1
        else:
            # No more bits to encode, append the original pixel value
            encoded_pixels.append(pixel)

    # Create a new image with the encoded pixel data
    encoded_img = Image.new('RGB', img.size)
    encoded_img.putdata([(r, g, b) for r, g, b in zip(encoded_pixels, img.split()[1].getdata(), img.split()[2].getdata())])

    # Save the encoded image to the output file
    encoded_img.save(output_file)
    return True

def encode_message_in_audio(audio_file, message, output_file):
    # Placeholder implementation for encoding message into audio file
    pass

def encode_message_in_video(video_file, message, output_file):
    # Placeholder implementation for encoding message into video file
    pass
