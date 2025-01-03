## Нomework 24.1 Вьюсеты и дженерики

### Задание 1

Создайте новый Django-проект, подключите DRF в настройках проекта.

### Задание 2

Создайте следующие модели:

#### Пользователь:

все поля от обычного пользователя, но авторизацию заменить на email;
телефон;
город;
аватарка.
Модель пользователя разместите в приложении users

#### Курс:

название,
превью (картинка),
описание.

#### Урок:

название,
описание,
превью (картинка),
ссылка на видео.
Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков.
Реализуйте связь между ними.

### Задание 3

Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока -
Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.

Для работы контроллеров опишите простейшие сериализаторы.

Работу каждого эндпоинта необходимо проверять с помощью Postman.

## 24.2 Сериализаторы

### Задание 1

Для модели курса добавьте в сериализатор поле вывода количества уроков. Поле реализуйте с помощью
SerializerMethodField()

### Задание 2

Добавьте новую модель Платежи в приложение users с полями:
пользователь,
дата оплаты,
оплаченный курс или урок,
сумма оплаты,
способ оплаты: наличные или перевод на счет.

### Задание 3

Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод реализуйте с помощью сериализатора для связанной
модели.
Один сериализатор должен выдавать и количество уроков курса и информацию по всем урокам курса одновременно.

### Задание 4

Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
менять порядок сортировки по дате оплаты,
фильтровать по курсу или уроку,
фильтровать по способу оплаты.

## 25.1 Права доступа в DRF

### Задание 1

Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, настройте в проекте использование
JWT-авторизации и закройте каждый эндпоинт авторизацией.

Эндпоинты для авторизации и регистрации должны остаться доступны для неавторизованных пользователей.

### Задание 2

Заведите группу модераторов и опишите для нее права работы с любыми уроками и курсами, но без возможности их удалять и
создавать новые. Заложите функционал такой проверки в контроллеры.

### Задание 3

Опишите права доступа для объектов таким образом, чтобы пользователи, которые не входят в группу модераторов, могли
видеть, редактировать и удалять только свои курсы и уроки.

## 26.2. Celery
### Задание 1
Настройте проект для работы с Celery. Также настройте приложение на работу с celery-beat для выполнения периодических
задач.

### Задание 2
Добавьте асинхронную рассылку писем пользователям об обновлении материалов курса.

### Задание 3
С помощью celery-beat реализуйте фоновую задачу, которая будет проверять пользователей по дате последнего входа по полю
last_login
и, если пользователь не заходил более месяца, блокировать его с помощью флага
is_active

