'''
translator module using watson translate
translate english to french
'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

#set up watson language translator environment
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''
    translate english to french
    '''

    if englishText == "":
        return ""
    translation = language_translator.translate(
        text=englishText,
        model_id='en-fr').get_result()
#    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    '''
    translate french to english
    '''

    if frenchText == "":
        return ""
    translation = language_translator.translate(
        text=frenchText,
        model_id='fr-en').get_result()
#    print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation["translations"][0]["translation"]

print(f"hello->{englishToFrench('hello')}")
print(f"bonjour->{frenchToEnglish('bonjour')}")
