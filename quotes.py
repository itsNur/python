import pandas as pd
from yandexfreetranslate import YandexFreeTranslate 
import requests


def get_quotes(num_quotes):
     '''get quotes from API'''
    quotes = []
    for _ in range(num_quotes):
        response = requests.get("https://favqs.com/api/qotd")
        quote = response.json()["quote"]["body"]
        yt = YandexFreeTranslate(api = "ios")
        rus_quote = yt.translate("en", "ru", quote)
        quotes.append(rus_quote)
    return quotes


def save_quotes_to_excel(data, file_path):
     '''write quotes to excel file'''
    df = pd.DataFrame(data)
    df.to_excel(file_path, index=False, header=False)


def save_quotes_to_csv(data, file_path):
     '''write quotes to csv file'''
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, header=False, encoding='utf-8-sig')


def save_quotes_to_txt(data, file_path):
     '''write quotes to txt file'''
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, header=False)


if __name__ == "__main__":
    try:
        num_quotes = 10  '''quotes quantity'''
        quotes = get_quotes(num_quotes)
        
         '''file paths'''
        file_path_excel = 'C:/NURSULTAN/Python/wb_tech/50_quotes/pandas_quotes/ex_result.xlsx' 
        file_path_csv = 'C:/NURSULTAN/Python/wb_tech/50_quotes/pandas_quotes/csv_result.csv'
        file_path_txt = 'C:/NURSULTAN/Python/wb_tech/50_quotes/pandas_quotes/txt_result.txt'
        
        save_quotes_to_excel(quotes, file_path_excel)
        save_quotes_to_csv(quotes, file_path_csv)
        save_quotes_to_txt(quotes, file_path_txt)
    
    except Exception as e:
        print(e)
