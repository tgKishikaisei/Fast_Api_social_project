from fastapi import FastAPI
from database import Base, engine

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)


app = FastAPI()

from  social_project.comments_api import comments
from  social_project.hashtag_api import hashtags
from  social_project.posts_api import posts
from  social_project.photo_api import photos
from  social_project.users_api import users



# @app.get('/hello')
# async def hello():
#     return {'hello': 'Fastapi'}
#
#
#
# @app.post('/hello')
# async def post_home(name: str):
#     return {'message': f'hello {name}'}