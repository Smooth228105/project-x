.
├── README.md
├── requirements.txt
├── client
│   ├── main.py                # Главный файл для клиента (запуск)
│   ├── model.py               # Модель (работа с API)
│   ├── controller.py          # Контроллер (связь модели и представления)
│   ├── view.py                # Представление (GUI с Tkinter)
│   └── __init__.py            # Инициализация пакета client
│
├── server
│   ├── serverapp.py           # Главный файл сервера (Flask)
│   ├── routes.py              # Маршруты (обработчики API)
│   ├── models.py              # Модели для работы с базой данных (SQLAlchemy)
│   ├── database.sql           # SQL-скрипт для создания базы данных
│   ├── config.py              # Конфигурация для сервера и базы данных
│   └── __init__.py            # Инициализация пакета server
│
├── tests
│   ├── test_client.py         # Юнит-тесты для клиентской модели
│   ├── test_server.py         # Юнит-тесты для серверного API
│   └── __init__.py            # Инициализация пакета tests
│
├── ZapuskClienta.md           # Инструкция по запуску клиента
├── ZapuskTestov.md            # Инструкция по запуску тестов
├── Zavisimosti.md             # Инструкция по установке зависимостей
├── serverModels.py            # Дополнительная модель, если требуется
└── test_client.py             # Пример тестов клиента
