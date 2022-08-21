# Площадка для продавцов цветами

#### Функционал:

- Деление юзеров на продавцов и покупателей (продавцы не могут быть покупателями)
- Создание продавцам лотов с информацией о виде цветка(ромашка/тюльпан и т.п.), его оттенка(перечень оттенков ограничен и известен заранее), количестве товара этого вида, цене за один товар
- Продавец может выбирать: отображать выбранный лот покупателям или нет
- Покупатели могу оставлять отзывы на лоты и продавца 
- Отслеживание сделки
- Cкрипт, который возвращает информацию в виде списка продавцов с перечнем покупателей, которые делали покупку у этого продавца и общей суммой покупок. Реализовано через Django Signals


## Инструкция по запуску:

Склонируйте проект:
```
https://github.com/Ramil2003/Frosty.git
```

Создайте виртуальное окружение:
```
python3 -m venv venv
```

Активируйте вирт. окружение:
```
source venv/bin/activate
```

Установите зависимости:
```
pip install -r requirements.txt
```

Запустите приложение и создайте супер юзера
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
```
python3 manage.py createsuperuser
```
```
python3 manage.py runserver 
```

Открыть сайт по ссылке: **http://127.0.0.1:8000/admin**
