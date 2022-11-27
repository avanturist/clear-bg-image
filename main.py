from flask import Flask
from rembg import remove
from PIL import Image
from pathlib import Path

app = Flask(__name__)

def remove_bg():
    image_types = ['*.png','*.jpg','*.jpeg','*.webp']
    files = []
    path = Path(__file__).parent.resolve()
    for type in image_types:
        files.extend((path/'input').glob(type));

    for img in files:
        input = Path(img)
        file_name = input.stem

        output_name = f'{path}/output/{file_name}_clearbg.png'

        input_image = Image.open(input)
        output_image = remove(input_image)
        output_image.save(output_name)
        print(file_name + ' - DONE.')


if __name__ == '__main__':
    # app.run(debug=True)
    remove_bg();