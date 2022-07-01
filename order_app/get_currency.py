
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup as Bs


def get_currency(date: datetime):
    """
    Получаем стоимость доллара
    """

    url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
    params = {
        'date_req': date.strftime("%d/%m/%Y")
    }

    try:
        request = requests.get(url, params)
        soup = Bs(request.content, 'xml')
        find_usd = soup.find(ID='R01235').Value.string
        result = float(find_usd[:6].replace(',', '.'))
    except AttributeError:
        result = get_currency(date - timedelta(days=1))

    return result
