import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['API_KEY']
URL = os.environ['URL']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)
LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
