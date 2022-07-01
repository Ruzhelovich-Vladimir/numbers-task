import os.path
from datetime import datetime
from googleapiclient.discovery import build
from google.oauth2 import service_account

# Определение расположения файла полномочий
CREDENTIALS_FILE = 'credentials.json'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SERVICE_ACCOUNT_FILE = os.path.join(BASE_DIR, CREDENTIALS_FILE)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# Определение документа
SPREADSHEET_ID = '1-Ro_CzYc9RGktqdUC00P30LbWNv1XVaEs-zAerZ_KAo'
# Определение диапазона
RANGE_NAME = 'Лист1!A:D'


def get_data():
    """ Получение данных из google документа"""

    # Подключению к боту
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=credentials)

    # Обращение к документу через API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()

    values = result.get('values', [])
    values.pop(0)

    result = [
        {
            'id': int(_id),
            'order_no': int(_order_no),
            'usd_cost': float(_cust_cost),
            'delivery_day': datetime.strptime(_delivery_day, "%d.%m.%Y")
         } for [_id, _order_no, _cust_cost, _delivery_day] in values
    ]

    return result


if __name__ == '__main__':

    print(get_data())
