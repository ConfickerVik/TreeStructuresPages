
# Древовидная структура страниц неограниченного уровня вложенности

Было создано приложение, которое позволяет при помощи Django Admin создавать, редактировать и удалять страницы.

Так же было реализовано API на Django Rest Framework для получения страницы и его потомков (полное дерево) по полному URL.

## Установка

Склонируйте репозиторий:

```bash
  git clone https://github.com/ConfickerVik/TreeStructuresPages.git
```

Создайте виртуальное окружение Python:

```bash
  python -m venv venv
```

Чтобы начать пользоваться виртуальным окружением, необходимо его активировать:

```bash
  venv\Scripts\activate.bat  - для Windows
  source venv/bin/activate - для Linux и MacOS
```

Установите зависимости из файла requirements.txt:

```bash
  pip install -r requirements.txt
```

Чтобы программа заработала, необходимо применить миграции:

```bash
  python manage.py migrate
```

Теперь можно запусть Django сервер и пользоваться приложением:

```bash
  python manage.py runserver
```
## Работа с Django Admin

Форма добавления выглядит следующим образом:

![addpages](https://github.com/ConfickerVik/TreeStructuresPages/assets/43670422/b74cdef8-cf7a-4e75-bee5-df20456005f4)

Поле url было скрыто из форм создания и изменения страницы, так как оно генерируется при помощи пагинации родительского url и созданного объекта

Заполним необходимые поля и сохраним запись:

![addpagesAbout](https://github.com/ConfickerVik/TreeStructuresPages/assets/43670422/6630002c-f056-4fc8-b67a-f127788aaf05)

В результате получаем:

![createAbout](https://github.com/ConfickerVik/TreeStructuresPages/assets/43670422/000b2429-3958-4c46-a984-f8b482cc5e54)

Добавим страницы Контакты и Реквизиты по такому же принципу и получим следующее: 

![addContacts](https://github.com/ConfickerVik/TreeStructuresPages/assets/43670422/b5db6b11-e5c9-415e-8b0c-7e96aca34557)

В итоге получаем записи в бд и можем убедиться, что url были сгенерированы.

## Документация API

#### Получение потомков для всех страниц

```bash
  GET /api/pages/?url=
```

| Параметр  | Тип      | Описание                   |
| :-------- | :------- | :------------------------- |
|   `url`   | `string` |  Пустое значене            |



#### Получение потомков для страницы, например, /catalog/shoes/

```bash
  GET /api/pages/?url=/catalog/shoes/
```

| Параметр  | Тип      | Описание                          |
| :-------- | :------- | :-------------------------------- |
| `url`     | `string` | Полный URL-адрес из базы данных   |



## Результат работы API

Для следующей структуры страниц:

- Главная страница `(slug: "", url: "/")`
- О компании `(slug: "about", url: "/about/")`
    - Реквизиты `(slug: "req", url: "/about/req/")`
    - Контакты `(slug: "contacts", url: "/about/contacts/")`
- Каталог `(slug: "catalog", url: "/catalog/")`
    - Обувь `(slug: "shoes", url: "/catalog/shoes/")`
        - Тапки `(slug: "slipper", url: "/catalog/shoes/slipper/")`
        - Сандали `(slug: "sandals", url: "/catalog/shoes/sandals/")`
    - Одежда `(slug: "clothes", url: "/catalog/clothes/")`
        - Штаны `(slug: "pants", url: "/catalog/clothes/pants/")`
        - Кофты `(slug: "sweatshirts", url: "/catalog/clothes/sweatshirts/")`

Получение потомков для всех страниц будет выглядеть так:

```bash
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "name": "Главная страница",
        "url": "/",
        "children": []
    },
    {
        "name": "О компании",
        "url": "/about/",
        "children": [
            {
                "name": "Реквизиты",
                "url": "/about/req/",
                "children": []
            },
            {
                "name": "Контакты",
                "url": "/about/contacts/",
                "children": []
            }
        ]
    },
    {
        "name": "Реквизиты",
        "url": "/about/req/",
        "children": []
    },
    {
        "name": "Контакты",
        "url": "/about/contacts/",
        "children": []
    },
    {
        "name": "Каталог",
        "url": "/catalog/",
        "children": [
            {
                "name": "Обувь",
                "url": "/catalog/shoes/",
                "children": [
                    {
                        "name": "Тапки",
                        "url": "/catalog/shoes/slipper/",
                        "children": []
                    },
                    {
                        "name": "Сандали",
                        "url": "/catalog/shoes/sandals/",
                        "children": []
                    }
                ]
            },
            {
                "name": "Одежда",
                "url": "/catalog/clothes/",
                "children": [
                    {
                        "name": "Штаны",
                        "url": "/catalog/clothes/pants/",
                        "children": []
                    },
                    {
                        "name": "Кофты",
                        "url": "/catalog/clothes/sweatshirts/",
                        "children": []
                    }
                ]
            }
        ]
    },
    {
        "name": "Обувь",
        "url": "/catalog/shoes/",
        "children": [
            {
                "name": "Тапки",
                "url": "/catalog/shoes/slipper/",
                "children": []
            },
            {
                "name": "Сандали",
                "url": "/catalog/shoes/sandals/",
                "children": []
            }
        ]
    },
    {
        "name": "Тапки",
        "url": "/catalog/shoes/slipper/",
        "children": []
    },
    {
        "name": "Сандали",
        "url": "/catalog/shoes/sandals/",
        "children": []
    },
    {
        "name": "Одежда",
        "url": "/catalog/clothes/",
        "children": [
            {
                "name": "Штаны",
                "url": "/catalog/clothes/pants/",
                "children": []
            },
            {
                "name": "Кофты",
                "url": "/catalog/clothes/sweatshirts/",
                "children": []
            }
        ]
    },
    {
        "name": "Штаны",
        "url": "/catalog/clothes/pants/",
        "children": []
    },
    {
        "name": "Кофты",
        "url": "/catalog/clothes/sweatshirts/",
        "children": []
    }
]
```

Получение потомков для страницы /catalog/shoes/ будет следующим:

```bash
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "name": "Обувь",
        "url": "/catalog/shoes/",
        "children": [
            {
                "name": "Тапки",
                "url": "/catalog/shoes/slipper/",
                "children": []
            },
            {
                "name": "Сандали",
                "url": "/catalog/shoes/sandals/",
                "children": []
            }
        ]
    }
]
```
