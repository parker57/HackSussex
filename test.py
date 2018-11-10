from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='57ab074b98b3476c8fcc2b4c3ab95a56')
model = app.public_models.general_model
response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

def mostLikely(image_url):
    response = model.predict_by_url(image_url)
    return response['outputs'][0]['data']['concepts'][0]['name']


'''
concepts = response['outputs'][0]['data']['concepts']
for concept in concepts:
	print(concept['name'], concept['value'])
'''
