# User Polling System
#### Настройка
Первое, что нужно сделать, это клонировать репозиторий:

```
$ git clone https://github.com/AkrisMoon/PollingSystem.git
$ cd userPollingSystem
```
Создайте виртуальную среду для установки зависимостей и ее активации:
```
$ virtualenv2 --no-site-packages venv
$ source venv/bin/activate
```
Затем установите зависимости:
```
(venv) $ pip install -r requirements.txt
```
Обратите внимание на (venv) перед командой. Это указывает на то, что данный терминальный сеанс работает в виртуальной среде, созданной virtualenv2.

После завершите загрузки зависимостей:
```
(venv) $ cd userPollingSystem
(venv) $ python manage.py runserver
```
И перейдите на http://127.0.0.1:8000/.

#### Документация
http://127.0.0.1:8000/swagger/

#### URL приложения

Base URL: 127.0.0.1:8000/api/v1/

Вывод всех активных опросов:
```
URL: /polls/active/
```

Вывод всех опросов:
```
URL: /polls/list/
```

Вывод всех ответов по текущему ID пользователя:
```
URL: /user_answers/list/
```

Вывод всех ответов по указанному ID пользователя:
```
URL: /user_answers/{id}/
```

Вывод всех вопросов:
```
URL: /questions/list/
```

Создание ответа пользователя:
```
URL: /user_answers/create/
```

Создание опросов:
```
URL: /polls/create/
```

Редактирование/удаление опроса:
```
URL: /poll/detail/{id}/
```

Создание ответа на вопрос:
```
URL: /answers/create/
```

Редактирование/удаление ответа на вопрос:
```
URL: /answer/detail/{id}/
```

Создание вопросов:
```
URL: /questions/create/
```

Редактирование/удаление вопросов:
```
URL: /questions/detail/{id}/
```
