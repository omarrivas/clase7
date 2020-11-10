import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3, ToneAnalyzerV3

def analyze_tone(text):
    authenticator1 = IAMAuthenticator('GpbsKvgqXeGH2JFudq05I1ospPeSvhRrQDhdAnkkLJqu')
    tone_analyzer = ToneAnalyzerV3(
        version='2019-09-26',
        authenticator=authenticator1
    )
    tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/c67764e7-aa06-4e6c-b972-782056a7adc1')

    authenticator2 = IAMAuthenticator('QXz49Lpq5BXFTi6mO_DPAnupyB8IUAr2792eYwmolJRC')
    language_translator = LanguageTranslatorV3(
        version='2019-09-26',
        authenticator=authenticator2)

    language_translator.set_service_url('https://api.us-south.language-translator.watson.cloud.ibm.com/instances/4b86824c-2516-48d5-82cf-4f82fd264002')

    '''
    # Translate Document
    with open('en.pdf', 'rb') as file:
        result = language_translator.translate_document(
            file=file,
            file_content_type='application/pdf',
            filename='en.pdf',
            model_id='en-fr').get_result()
        print(json.dumps(result, indent=2))
    de https://github.com/watson-developer-cloud/python-sdk/blob/master/examples/language_translator_v3.py
    '''

    text_to_translate = [text]
    translation = language_translator.translate(
        text=text_to_translate,
        model_id='es-en').get_result()

    text= str(translation['translations'][0]['translation'])
    tone_analysis = tone_analyzer.tone(
        {'text': text}
    ).get_result()

    return json.dumps(tone_analysis, indent=2)


result= analyze_tone('estoy muy triste')
print(result)
