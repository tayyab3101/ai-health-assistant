from google import genai

client = genai.Client(api_key="AIzaSyDKI_G_zeY5R-OMkw2yAdU0i8-VMIYaEuU")

models = client.models.list()

for m in models:
    print(m.name)