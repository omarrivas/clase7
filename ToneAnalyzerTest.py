import json
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

def analyze_tone(text):
    authenticator = IAMAuthenticator('GpbsKvgqXeGH2JFudq05I1ospPeSvhRrQDhdAnkkLJqu')
    tone_analyzer = ToneAnalyzerV3(
        version='2019-09-26',
        authenticator=authenticator
    )

    tone_analyzer.set_service_url('https://api.us-south.tone-analyzer.watson.cloud.ibm.com/instances/c67764e7-aa06-4e6c-b972-782056a7adc1')

    tone_analysis = tone_analyzer.tone(
        {'text': text}
    ).get_result()

    return json.dumps(tone_analysis, indent=2)


data = input("Ingresa algo:\n")
result= analyze_tone(data)
print(result)
