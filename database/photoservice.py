from database import get_db
from database.models import PostPhoto

# Получени фотографии
def get_all_or_photo_db(photo_id, user_id):

    db = next(get_db())

    # Если нужны все фотографии определлонного ползователя
    if user_id:
        exact_user_photos = db.query(PostPhoto).filter_by(id=user_id).all

        return {'status': 1, 'message': exact_user_photos}

    elif photo_id:
        exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

        return {'status': 1, 'message': exact_photo}


# Изменить фото профиля
def change_photo_db(photo_id, new_photo_path):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        exact_photo.photo_path = new_photo_path
        db.commit()

        return True
    return False

# Удаление фото
def delete_photo_db(photo_id):
    db = next(get_db())

    exact_photo = db.query(PostPhoto).filter_by(id=photo_id).first()

    if exact_photo:
        db.delete(exact_photo)
        db.commit()