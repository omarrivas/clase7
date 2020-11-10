import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('tZ8FBk5KL4yVyXTxMkyjxHJay8jF0tC4VzwkXd0q_y3V')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://api.us-south.discovery.watson.cloud.ibm.com/instances/3a89bbd0-a32b-4db2-b1f8-453f1eb9279e')

#print(discovery.list_environments())
#print(discovery.list_collections('f83cc839-b87b-4df3-8a37-b8e10abeeab6'))

consulta= discovery.query('f83cc839-b87b-4df3-8a37-b8e10abeeab6', '1775f01d-446a-4173-b330-445346f8c5b1', natural_language_query='que es el SAE')
print (consulta)
