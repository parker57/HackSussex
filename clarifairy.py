from os import listdir
from os.path import isfile, join
import imghdr
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='57ab074b98b3476c8fcc2b4c3ab95a56')
model = app.public_models.general_model

directory = '.'

image_extensions = ['jpeg', 'bmp', 'jpg', 'png']

files_in_dir = [f for f in listdir(directory) if isfile(join(directory, f))]

images = [f for f in files_in_dir if str(imghdr.what(f)).lower() in image_extensions]

img = model.predict_by_filename(images[0])


def get_concepts(image):
    if image[:4].lower() == 'http':
        response = model.predict_by_url(image)
    else:
        response = model.predict_by_filename(image)
    concepts = response['outputs'][0]['data']['concepts']
    return [{c['name']: c['value']} for c in concepts]


def is_pic_of(image_url, thing):
    table = get_concepts(image_url)
    return True if (thing in [list(d)[0] for d in table]) else False


print(get_concepts('https://www.hakaimagazine.com/wp-content/uploads/header-humpbacks-and-grays.jpg'))

