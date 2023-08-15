from database.models import User
from datetime import datetime

from database import get_db


# Регистрации пользователя
def register_user_db(name, email, phone_number, password, user_city):
    db = next(get_db())


    new_user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        password=password,
        user_city=user_city,
        reg_date=datetime.now()
)
    # добовляем в базу
    db.add(new_user)


    # сохрони в базе
    db.commit()


    return new_user


# проверка на ниличие в базу ползователя
def check_user_data_db(phone_number, email):

    # генератор связи базы данных
    db = next(get_db())

    # Проверка данных на наличие записи в базе
    checker = db.query(User).filter_by\
        (phone_number=phone_number,
         email=email).first()


    # Если есть совподения
    if checker:
        return False

    # А если нет совподение
    return True

# Проверка пароля при выходе в аккаунт
def check_user_password_db(email, password):

    # генератор связи базы данных
    db = next(get_db())

    # Попробуем найти ползователя
    checker = db.query(User).fileter_by(email=email).first()


    # Если нашел такой мейл проверим правилность пароля
    if checker:
        # Начинаем сверку пароля
        if checker.password == password:
            return checker.id

        else:
            return 'Неверный пароль'

    # если не находит данные в базе
    return 'Неверная почта'


# Получить информацию о ползователя
def profile_info_db(user_id):


    # генератор связи базы данных
    db = next(get_db())

    # Проверка полбьзователя через id
    exact_user = db.query(User).filter_by(id=user_id).first()


    # если нашел пользователя передаю все инфармацию про него
    if exact_user:
        return exact_user.email, \
               exact_user.phone_number, \
               exact_user.id, \
               exact_user.reg_date,\
               exact_user.user_city, \
               exact_user.name



    return 'Ползователь не найден'


# Изменение данных ползователя
def change_user_data(user_id, change_info, new_date):


    # генератор связи базы данных
    db = next(get_db())


    # Нвходим пользователя в базе
    exact_user = db.query(User).filter_by(id=user_id).first()

    # Если есть ползователь в базе
    if exact_user:
        # Проверка того какую информацию хочет изменить ползователь
        if change_info == 'email':
            exact_user.email = new_date


        elif change_info == 'number':
            exact_user.phone_number = new_date


        elif change_info == 'name':
            exact_user.name = new_date


        elif change_info == 'city':
            exact_user.user_city = new_date


        elif change_info == 'password':
            exact_user.password = new_date


        # сохроняем изменение в базе
        db.commit()


        return 'Данные успешно изменены'


    # а если не находим в базе ползователя
    return 'не находим в базе ползователя'