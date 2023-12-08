from yandexfreetranslate import YandexFreeTranslate 
import requests

file = open("quotes.txt", "w", encoding='utf-8')

try:
    for _ in range(10):
        response = requests.get("https://favqs.com/api/qotd")
        quote = response.json()["quote"]["body"]
        yt = YandexFreeTranslate(api = "ios")
        rus_quote = yt.translate("en", "ru", quote)

        file.write(rus_quote)
        file.write('\n')

finally:
    file.close()