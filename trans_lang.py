# Importing necessary libraries
import os
from google.cloud import translate_v2

# Making a Cloud Translation Client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"translate.json"
client = translate_v2.Client()


# To print all the supported languages with the target language name
def supp_languages(language):
    response = client.get_languages(target_language= language)

    for language in response:
        print("{name} ({language})".format(**language))
    return response

supp_languages("en")


# To tranlsate a text into target language
def trans_late(text, target_language):
    output = client.translate(text, target_language = target_language)
    print(output["translatedText"])

# Text to translate
text = "My name is Raghav Saini"  
# target language_code to which you want to translate
target = "hi"  
              
trans_late(text, target)


