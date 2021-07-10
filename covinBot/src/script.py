import requests
import telebot,os
API_KEY=os.environ.get('TOKEN')
bot=telebot.TeleBot(API_KEY)
from datetime import datetime
#from flask import request
import re,textwrap
now=datetime.now()
today_date=now.strftime("%d-%m-%Y")
base_url="https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict"
API_URL="https://api.telegram.org/bot1860319551:AAEyIIxWRuEbYhN3_pF5zKU1EnMniadP5RU/getUpdates"
TOKEN="1860319551:AAEyIIxWRuEbYhN3_pF5zKU1EnMniadP5RU"
district={622: 'Agra', 623: 'Aligarh', 625: 'Ambedkar Nagar', 626: 'Amethi', 627: 'Amroha', 628: 'Auraiya', 646: 'Ayodhya', 629: 'Azamgarh', 630: 'hathrus'}

def availability_data(response):
  response_json=response.json()
  message=""
  for center in response_json["centers"]:
    for session in center["sessions"]:
      if(session["available_capacity_dose1"]>0):
        message+="PinCode:{} \nDate :{} \nCenter Name :{} \nMin Age :{} \nVaccine Type :{} \nCapacity :{}\n---\n".format(center["pincode"],
          session["date"],center["name"],session["min_age_limit"],session["vaccine"],session["available_capacity_dose1"])
  return message
def fetch_data_from_covin(dist_id):
  query="?district_id={}&date={}".format(dist_id,today_date)
  final_url=base_url+query
  response=requests.get(final_url)
  return availability_data(response)
#print(fetch_data_from_covin(622

if __name__=="__main__":
    
  try:
        
      @bot.message_handler(commands=['start'])  
      def start_message(message):
            text="i will help you to find vaccine slots in your district just type districts then enter your district code:) "
            bot.send_message(message.chat.id,text)
            #bot.reply_to(message,"somthing went wrong :-{")
            
      @bot.message_handler(content_types=['text'])
      def send_text(message):
        try:
            txt=message.text
            if(len(txt)==0):
              bot.reply_to(message,"NOT available")
            if txt.lower()=="district":
              districts=""
              for a,b in district.items():
                districts+="{} - {}\n".format(a,b)
              bot.reply_to(message,districts)
            elif txt.isnumeric() and int(txt)>0:
              dist_id=int(txt)
              slots=fetch_data_from_covin(dist_id)
              split_text=textwrap.wrap(slots,width=4096,break_long_words=False)
              #bot.sendMessage(chat_id=chat_id, text=slots, reply_to_message_id=msg_id)
              if len(slots)>=4095:
                for text in split_text:
                  text=text+"\n--" 
                  bot.send_message(message.chat.id,text.upper())
              else:
                bot.send_message(message.chat.id,slots)  
            else:
              bot.send_message(message.chat.id,"INVALID CODE! TRY AGAIN")
            # elif message.text.lower() =='Bye':
            #   bot.send_message(message.chat.id,'see you soom' )
            # elif message.text.lower() == 'I love you':
            #   bot.send_sticker(message.chat.id, 'API')
            # bot.send_message(message.chat.id,'Wrong code ' )  
        except Exception as e:
            print(e)
            bot.reply_to(message,"slots are not available :-{")
      bot.polling(none_stop=True)
  except Exception as e:
    print(e)
    bot.polling(none_stop=True)
