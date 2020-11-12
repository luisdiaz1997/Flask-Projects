from google.cloud import vision
from google.cloud import datastore

datastore_client = datastore.Client()

def get_text_from_image(image_file):
    client = vision.ImageAnnotatorClient()
    content = image_file.read()
    image = vision.Image(content=content)
    response = client.document_text_detection(image=image)
    image_text_list = []
    image_text=' '
    for page in response.full_text_annotation.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text = ''.join([
                        symbol.text for symbol in word.symbols
                    ])
                    image_text_list.append(word_text)                    
    image_text = image_text.join(image_text_list)
    print(image_text)
    entity = datastore.Entity(key=datastore_client.key("proj3_files"))
    entity.update({
        'CloudStorage_url' : "No URL",
        'Transcribed Text' : image_text
    })
    datastore_client.put(entity)
    return image_text