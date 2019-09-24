import locale


try:
    locale.setlocale(locale.LC_ALL, 'russian')
except locale.Error:
    locale.setlocale(locale.LC_ALL, 'ru_RU.utf8')
