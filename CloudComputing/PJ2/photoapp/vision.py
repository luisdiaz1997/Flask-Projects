import io
import os
import sys
from google.cloud import vision


def process_file(im_path):
    client = vision.ImageAnnotatorClient()
    with io.open(im_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    print('Labels:')
    for label in labels:
        print(label.description)
    return [label.description for label in labels]


if __name__ == '__main__':
    process_file(sys.argv[1])

