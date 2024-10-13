from environs import Env

env = Env()
env.read_env()

ADMINS = env.list("ADMINS")
BOT_TOKEN = env.str("BOT_TOKEN")

DB_NAME = env.str("DB_NAME")
DB_PASS = env.str("DB_PASS")
DB_USER = env.str("DB_USER")
DB_HOST = env.str("DB_HOST")
DB_PORT = env.str("DB_PORT")
