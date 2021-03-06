import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATOR_KEY' not in current_app.config or not current_app.config['YANDEX_TRANSLATOR_KEY']:
        return _('Error: the translation service is not configured.')
    r = requests.post(
        "https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&lang={}".format(
            current_app.config['YANDEX_TRANSLATOR_KEY'],
            "{}-{}".format(source_language, dest_language),
        ),
        data={'text': text},
    )
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    data = json.loads(r.content.decode('utf-8-sig'))
    return "".join(data.get('text', [])) or _('Error: the translation service failed.')
