from flask import jsonify, request
from flask_login import login_required
from . import blueprint
from .translate import translate


@blueprint.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(
        request.form.get('text'),
        request.form.get('source_language'),
        request.form.get('dest_language'),
    )})
