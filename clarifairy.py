#!/usr/bin/python3

#from clarifai.rest import ClarifaiApp

#new key: 4c7f557436744091a230a2b4675324b0

def validate_api_key(api_key):
    """Check that an API key is valid, if yes return the app."""
    try:
        from clarifai.rest import ClarifaiApp, ApiError
        app = ClarifaiApp(api_key=api_key)
        return app
    except ApiError as exc:
        error = json.loads(exc.response.content)
        _LOGGER.error(
            "%s error: %s", CLASSIFIER, error['status']['details'])
        return None


app = validate_api_key(api_key='d1e1cf2d912445b5a155f0eb4f8d83ab')
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


