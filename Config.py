import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = '29698700'
    API_HASH = 'c08d5af866792c7f96e2de2b35ad5a34'
    BOT_TOKEN = '6005321257:AAFytdaPgqN8Q6ECsB9V9dQKnTGk2DB5q1M'
    DATABASE_URL = 'postgres://yoqdgotu:D2BaXqX7e4VBZQRrLoGzevz3UqFiQPf9@lallah.db.elephantsql.com/yoqdgotu'
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ''
    if MUST_JOIN.startswith("@solotreee"):
        MUST_JOIN = MUST_JOIN[1:]
