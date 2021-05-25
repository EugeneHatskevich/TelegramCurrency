from config import BOT_TOKEN
from config import MENU, INFO, CONVERTER, CONVERTER_SECOND, CONVERTER_END
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import ConversationHandler, CallbackQueryHandler
from telegram.ext import Updater
from telegram.ext import CommandHandler
from handlers import command_handlers, message_handlers, callback_handlers
from models.bd_connection import *
import peewee


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    update_handler = (CommandHandler('update', command_handlers.update_bd))
    create_handler = (CommandHandler('create', command_handlers.create_bd))
    help_handler = (CommandHandler('help', command_handlers.helps))
    other_handlers = (CallbackQueryHandler(callback_handlers.other))
    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('start', command_handlers.start)],
        states={
            MENU: [
                CallbackQueryHandler(callback_handlers.menu),
            ],
            INFO: [
                CallbackQueryHandler(callback_handlers.converter, pattern='^converter$'),
                CallbackQueryHandler(callback_handlers.info),
            ],
            CONVERTER: [
                CallbackQueryHandler(callback_handlers.converter),
            ],
            CONVERTER_SECOND: [
                CallbackQueryHandler(callback_handlers.converter_second),
            ],
            CONVERTER_END: [
                MessageHandler(Filters.text, message_handlers.convert_end),
            ],
        },
        fallbacks=[MessageHandler(Filters.regex('^Done$'), command_handlers.done)]
    )
    dispatcher.add_handler(update_handler)
    dispatcher.add_handler(create_handler)
    dispatcher.add_handler(help_handler)
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_handler(other_handlers)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    try:
        db.connect()
        Currency.create_table()
    except peewee.InternalError as px:
        print(str(px))
    main()
