#from astreamBotHandler import *
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'I\'m only bot after all')

if __name__ == '__main__':
     bot.polling(none_stop=True)


# greet_bot = BotHandler(token)  
# greetings = ('hello', 'hi', 'greetings', 'sup')  
# now = datetime.datetime.now()

# def main():  
#     new_offset = None
#     today = now.day
#     hour = now.hour
# 
#     while True:
#         greet_bot.get_updates(new_offset)
# 
#         last_update = greet_bot.get_last_update()
# 
#         last_update_id = last_update['update_id']
#         last_chat_text = last_update['message']['text']
#         last_chat_id = last_update['message']['chat']['id']
#         last_chat_name = last_update['message']['chat']['first_name']
#         
#         greet_bot.send_message(last_chat_id, 'I\'m only bot after all')
# 
#         if last_chat_text.lower() in greetings and today == now.day and 6 <= hour < 12:
#             greet_bot.send_message(last_chat_id, 'Good Morning  {}'.format(last_chat_name))
#             today += 1
# 
#         elif last_chat_text.lower() in greetings and today == now.day and 12 <= hour < 17:
#             greet_bot.send_message(last_chat_id, 'Good Afternoon {}'.format(last_chat_name))
#             today += 1
# 
#         elif last_chat_text.lower() in greetings and today == now.day and 17 <= hour < 23:
#             greet_bot.send_message(last_chat_id, 'Good Evening  {}'.format(last_chat_name))
#             today += 1
# 
#         new_offset = last_update_id + 1
# 
# if __name__ == '__main__':  
#     try:
#         main()
#     except KeyboardInterrupt:
#         exit()