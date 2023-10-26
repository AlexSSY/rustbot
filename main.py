from telegram.ext import ApplicationBuilder

from . import config


def main():
    app = ApplicationBuilder().token(token=config.BOT_API_KEY).build()


if __name__ == '__main__':
    main()
