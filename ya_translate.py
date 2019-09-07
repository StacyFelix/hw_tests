import requests

API_KEY = "trnsl.1.1.20190710T190047Z.726d9f9bd5e955ba.ceb044300bdbd5ebca4ddac1f4098a745a40e2dc"
URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"

# https://translate.yandex.net/api/v1.5/tr.json/translate
#  ? [key=<API-ключ>]
#  & [text=<переводимый текст>]
#  & [lang=<направление перевода>]
#  & [format=<формат текста>]
#  & [options=<опции перевода>]
#  & [callback=<имя callback-функции>]


def translate(text_untranslate, lang, to_lang='ru'):

    params = {
        "key": API_KEY,
        "text": text_untranslate,
        "lang": f"{lang}-{to_lang}"
    }

    try:
        response = requests.get(URL, params=params)
        text_translate = response.json()["text"]
    except:
        print("Невалидные данные")
        text_translate = ''
        status_code = 0
    else:
        status_code = response.status_code
        text_translate = ''.join(text_translate)

    return status_code, text_translate


if __name__ == '__main__':
    print(translate("hello, World", 'en'))
    print(translate("hello", 'йц'))
    print(translate("dgjskgsfjgo", 'en'))
