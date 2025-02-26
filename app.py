from flask import Flask, render_template, request, jsonify
from encode import encode_message_in_image, encode_message_in_audio, encode_message_in_video
from decode import decode_message_from_image, decode_message_from_audio, decode_message_from_video

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    # Get data from form
    image_file = request.files.get('image')
    audio_file = request.files.get('audio')
    video_file = request.files.get('video')
    message = request.form.get('message')

    # Check if only one type of file is selected and a message is entered
    file_count = sum(1 for file in [image_file, audio_file, video_file] if file)
    if file_count != 1 or not message:
        return jsonify({'error': 'Please select exactly one type of file (image, audio, or video) and enter a message.'}), 400

    # Encode message into files based on the selected type
    if image_file:
        encode_message_in_image(image_file, message, 'encoded_image.png')
    elif audio_file:
        encode_message_in_audio(audio_file, message, 'encoded_audio.mp3')
    elif video_file:
        encode_message_in_video(video_file, message, 'encoded_video.mp4')

    return jsonify({'message': 'Message encoded successfully'})

@app.route('/decode', methods=['POST'])
def decode():
    # Get data from form
    image_file = request.files.get('image')
    audio_file = request.files.get('audio')
    video_file = request.files.get('video')

    # Decode message from files
    decoded_messages = {}
    if image_file:
        decoded_messages['image'] = decode_message_from_image(image_file)
    if audio_file:
        decoded_messages['audio'] = decode_message_from_audio(audio_file)
    if video_file:
        decoded_messages['video'] = decode_message_from_video(video_file)

    return jsonify(decoded_messages)

if __name__ == '__main__':
    app.run(debug=True)
