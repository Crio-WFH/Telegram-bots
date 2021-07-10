from telegram.ext import Updater, InlineQueryHandler, CommandHandler,  MessageHandler, Filters
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url


def dog(update, context):
    print("reached dog")
    url = get_image_url()
    
    # gives  a call to the function 'get_image_url()' in order to recieve image url as return message
    context.bot.send_photo(chat_id=update.effective_chat.id, photo = url)


def start(update, context):
    print("conversation started")
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Bot Quirky welcomes you!")
    
    # on recieving /start command prints the message "Bot Quirky welcomes you!" on the telegram chat 
    # and prints "conversation started" message where the source code is running

def end(update, context):
    print("conversation ended")
    context.bot.send_message(chat_id = update.effective_chat.id,
            text="Bye! See you Again.")
    
    # on recieving /bye command prints the message "Bye! See you Again." on the telegram chat 
    # and prints "conversation ended" message where the source code is running
    

def unknown(update, context):
    print("retry")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command. Try another command.")
    
    # on recieving any unknown command prints the message "Sorry, I didn't understand that command. Try another command." on the telegram chat 
    # and prints "retry" message where the source code is running


def main():
    token='{{ YOUR TOKEN HERE }}'
    #replace the curly braces with your bot token
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher
    unknown_handler = MessageHandler(Filters.command, unknown)
    start_handler = CommandHandler('start', start)
    
    dispatcher.add_handler(CommandHandler('dog',dog))
    
    # handles the command /dog and on being called takes to function dog defined above
    
    dispatcher.add_handler(CommandHandler('bye',end))
    
    # handles the command /bye and on being called takes to function end defined above
    
    dispatcher.add_handler(start_handler)
    
    # handles the command /start and on being called takes to function start defined above
    
    dispatcher.add_handler(unknown_handler)
    
    # handles any command which is not listed and on being called takes to function unknown defined above
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
    # calls the main function if namespace is main
