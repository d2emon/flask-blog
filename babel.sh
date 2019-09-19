pybabel extract -F /babel.cfg -k _l -o /app/app/translations/messages.pot .
pybabel init -i /app/app/translations/messages.pot -d /app/app/translations -l ru
pybabel update -i /app/app/translations/messages.pot -d /app/app/translations
pybabel compile -d /app/app/translations
