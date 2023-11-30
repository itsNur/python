from yandexfreetranslate import YandexFreeTranslate
import requests

response = requests.get("https://favqs.com/api/qotd")

quote = response.json()["quote"]["body"]
yt = YandexFreeTranslate()
# yt = YandexFreeTranslate(api = "web")
yt = YandexFreeTranslate(api = "ios")

print(yt.translate("en", "ru", quote))