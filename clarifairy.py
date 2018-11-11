#!/usr/bin/python3

from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='57ab074b98b3476c8fcc2b4c3ab95a56')
model = app.public_models.general_model


def get_concepts(image):
    if image[:4].lower() == 'http':
        response = model.predict_by_url(image)
    else:
        response = model.predict_by_filename(image)
    concepts = response['outputs'][0]['data']['concepts']
    return [{c['name']: c['value']} for c in concepts]


def list_concepts(image):
    return [list(d)[0] for d in get_concepts(image)]


def is_pic_of(image_url, thing):
    table = get_concepts(image_url)
    return True if (thing in [list(d)[0] for d in table]) else False

