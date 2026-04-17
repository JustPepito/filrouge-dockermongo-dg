from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
import pymysql
import os

app = FastAPI()

MONGO_URL = os.getenv("MONGO_URL")
MONGO_DATABASE = os.getenv("MONGO_DATABASE", "blog_db")

MYSQL_HOST = os.getenv("MYSQL_HOST", "db_mysql")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongo_db = mongo_client[MONGO_DATABASE]


def get_mysql_connection():
    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        cursorclass=pymysql.cursors.DictCursor
    )


@app.get("/")
def root():
    return {"message": "API hybride Docker OK"}


@app.get("/posts")
async def get_posts():
    try:
        cursor = mongo_db.posts.find({}, {"_id": 0})
        posts = await cursor.to_list(length=100)
        return posts
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MongoDB error: {str(e)}")


@app.get("/users")
def get_users():
    try:
        connection = get_mysql_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nom, email FROM utilisateurs")
            users = cursor.fetchall()
        connection.close()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"MySQL error: {str(e)}")
