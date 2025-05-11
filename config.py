import os

class Config:
    SECRET_KEY = os.urandom(24)  # or another method to set a secret key
    SQLALCHEMY_DATABASE_URI = 'postgresql://neondb_owner:npg_ZFUJzHv3iDK8@ep-silent-poetry-a4mzoyjf-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    