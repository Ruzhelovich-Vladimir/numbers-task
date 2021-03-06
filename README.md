# Numbers-task

# Статус выполнения и комментарии:

1. Документ: https://docs.google.com/spreadsheets/d/1-Ro_CzYc9RGktqdUC00P30LbWNv1XVaEs-zAerZ_KAo/edit#gid=0 - копия документа
2. Реализована п.1-3,4.b часть задания. запуск процесса обновления происходит по команде:
   ```python3 manage.py update_run_processing``` были разные идеи как это реализовать, но запуска параллельного процесса использование модуля расписания, хотя можно было без него обновляются данные каждые 15 минут
   автоматически рассчитываются курс валюты, обновляются только те записи которые изменились.
3. Не удалось собрать докер-контейнер, но текущие файлы прикладываю. 
4. К сожалению я потратил очень много времени на настройку docker-контейнера, в ближайшее время я разберусь с этим, из-за этого остальное не успел сделать
5. Создал простую страницу с пагинации вывода таблицы, сделал её за пару часов, но конечно - это не окончательный вариант который хотелось сдать.
6. К сожалению также не успел сделать систему нотификацию, но я могу дать пример реализованной мною системы нотификации, которая работает. https://github.com/Ruzhelovich-Vladimir/API_Notification_System.git принцип работы примерно будет тот же, просто данный скрипт запускается cron`ном

## 1. Требования:

python 3.8+

## 2. Установка (linux):

* ```python3.[номер версии] -m venv venv``` - создаём виртуальное огружение [номер версии] - см. п.1
* ```source venv/bin/activate``` - активируем виртуальное окружение
* ```pip3 freeze -r requirements.txt``` - устанавливаем требуемые модули
* осуществляем настройки проекта см. п.3.
  * настройка базы posgress. установите библиотеку 
    замените параметры в ```config/setting.yaml```
   ```Параметры для PostgresSQL
        DATABASES:
           default:
           ENGINE: django.db.backends.postgresql
           NAME: 'имя базы данных',
           USER: 'имя пользователя',
           PASSWORD: 'пароль пользователя',
           HOST: 'хост',
           PORT: 'порт'
    ```
* запустите создание миграции ```python manage.py makemigrations```
* примените миграции миграции ```python manage.py migrate```
* запуск процесса обновления таблиц с заказами ```python3 manage.py update_run_processing```
* запуск сервера ```python3 manage.py runserver 0.0.0.0:8000```

# 3. Настройка проекта

Настройка проекта осуществляется в каталоге /config корневого каталога проекта, все параметры соответствую параметрами проекта django, в формате yaml

В каталоге могу содержаться следующие файлы:
* settings.yaml - хранятся базовые настройки проекта (обязательный файл)
* .secrets.yaml - хранятся настройки для локальной отладки и тестирования (не обязательный файл)

Некоторые настройки могут повторяться в файлах. Требуется знать, что вначале применяется настройки, которые находятся в файла "settings.yaml", затем ".secrets.yaml"
Т.е. настройки в файле ".secrets.yaml", переопределяют существующие настройки в "settings.yaml" 

# 4. Тестовое задание (developer)

Необходимо разработать скрипт на языке Python 3, который будет выполнять следующие функции:

1. Получать данные с документа при помощи Google API, сделанного в [Google Sheets](https://docs.google.com/spreadsheets/d/1LTejK-Oo7L1bFreBIIcEZnF1W1RCC1s_jos3EuIP0jI/edit?usp=sharing) (необходимо копировать в свой Google аккаунт и выдать самому себе права).
2. Данные должны добавляться в БД, в том же виде, что и в файле –источнике, с добавлением колонки «стоимость в руб.»
    
    a. Необходимо создать DB самостоятельно, СУБД на основе PostgreSQL.
    
    b. Данные для перевода $ в рубли необходимо получать по курсу [ЦБ РФ](https://www.cbr.ru/development/SXML/).
    
3. Скрипт работает постоянно для обеспечения обновления данных в онлайн режиме (необходимо учитывать, что строки в Google Sheets таблицу могут удаляться, добавляться и изменяться).

Дополнения, которые дадут дополнительные баллы и поднимут потенциальный уровень оплаты труда:

4. Упаковка решения в docker контейнер
    
    a. Разработка функционала проверки соблюдения «срока поставки» из таблицы. В случае, если срок прошел, скрипт отправляет уведомление в Telegram.
    b. Разработка одностраничного web-приложения на основе Django или Flask. Front-end React.
    
5. Решение на проверку передается в виде ссылки на проект на Github. В описании необходимо указать ссылку на ваш Google Sheets документ (открыть права чтения и записи для пользователя sales@numbersss.com ), а также инструкцию по запуску разработанных скриптов.