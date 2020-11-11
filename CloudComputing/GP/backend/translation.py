"""Translates text into the target language.

Target must be an ISO 639-1 language code.
See https://g.co/cloud/translate/v2/translate-reference#supported_languages
"""
from google.cloud import translate_v2 as translate
import six
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'proj3-ml-api-2ba7a1a87cba.json'
translate_client = translate.Client()

def translate_text(target, text):
    # [START translate_translate_text]
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """

    if isinstance(text, six.binary_type):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print(u"Text: {}".format(result["input"]))
    print(u"Translation: {}".format(result["translatedText"]))
    print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    # [END translate_translate_text]
    return result["translatedText"]

#target = "Spanish (es)"

def list_languages():
    # [START translate_list_codes]
    """Lists all available languages."""

    results = translate_client.get_languages()

    for language in results:
        print(u"{name} ({language})".format(**language))
    # [END translate_list_codes]