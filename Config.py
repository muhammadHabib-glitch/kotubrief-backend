from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import os

Base = declarative_base()

# ✅ Get the database URL from Railway environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL environment variable not found!")

# ✅ Create engine and session
engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)

# Upload folder setup (unchanged)
UPLOAD_FOLDER = "uploads/profile_images"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Mail settings (unchanged)
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'kotubriefapp@gmail.com'
MAIL_PASSWORD = 'vstpbouwbnacdwem'
MAIL_DEFAULT_SENDER = ('KotuBrief', MAIL_USERNAME)

JWT_SECRET = os.environ.get("JWT_SECRET", "change-this-in-production")
JWT_ALGO = "HS256"
JWT_EXPIRES_MIN = 60
DEV_BYPASS_AUTH = True


# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import create_engine
# import os
#
# Base = declarative_base()
#
#
#
# DATABASE_URI = r"mssql+pyodbc://sa:habibfarooq12345@DESKTOP-8TUN3M3\SQLEXPRESS/KotuBrief?driver=ODBC+Driver+17+for+SQL+Server"
#
# engine = create_engine(DATABASE_URI, echo=True)
# Session = sessionmaker(bind=engine)
#
# # config.py
# UPLOAD_FOLDER = "uploads/profile_images"
# UPLOAD_FOLDER = "uploads/profile_images"
# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
#
# # Upload folder
# UPLOADFOLDER = 'uploads/BookImage'
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)
#
#
#
# MAIL_SERVER = 'smtp.gmail.com'
# MAIL_PORT = 587
# MAIL_USE_TLS = True
# MAIL_USE_SSL = False
# MAIL_USERNAME = 'kotubriefapp@gmail.com'        # must match sender
# MAIL_PASSWORD = 'vstpbouwbnacdwem'               # the 16-char App Password
# MAIL_DEFAULT_SENDER = ('KotuBrief', MAIL_USERNAME)
#
#
#
# JWT_SECRET = os.environ.get("JWT_SECRET", "change-this-in-production")
# JWT_ALGO = "HS256"
# JWT_EXPIRES_MIN = 60  # token lifetime
# # add a flag
# DEV_BYPASS_AUTH = True
#
