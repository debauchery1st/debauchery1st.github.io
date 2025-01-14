import json
import requests
from flask_babel import _
from flask import current_app

def translate(text, fromLang, toLang):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY']}
    url = 'https://api.microsofttranslator.com/v2/Ajax.svc/Translate?text={}&from={}&to={}'.format(text, fromLang, toLang)
    r = requests.get(url, headers=auth)
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
