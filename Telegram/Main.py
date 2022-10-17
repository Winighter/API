import os,telegram
from img import *
from emoji import emojize
from telegram.ext import *


token = '5600507635:AAH1HdyylnDYaCpLLMkGm85u0VHG0AR11Ik'
chat_id = '5555783580'
bot = telegram.Bot(token) #bot을 선언합니다.
updates = bot.getUpdates() #업데이트 내역을 받아옵니다.
'''
for i in updates: # 내역중 메세지를 출력합니다.
    print(i.message) # ""
'''
# os 모듈을 불러온 뒤 dir_now라는 경로를 만들어 줍니다. 이는 받은 사진이 저장될 경로입니다.
dir_now = os.path.dirname(os.path.abspath(__file__)) # Real Path to dirname

# start reply function
def start_command(update, context):
    update.message.reply_text("I'm a bot, please talk to me!")


# Message reply function
def get_message(update, context): # get_message 함수는 MessageHandler에 의해 호출
    # 지정된 Message O
    update.message.reply_text("got text") # 호출되었을 경우 지정된 Message를 답장
    # 내가 보낸 지정된 Message X
    update.message.reply_text(update.message.text) # 호출되었을 경우 Me 가 보낸 메세지를 답장


# help reply function
def help_command(update, context):# help_command라는 CommandHandler에 의해 호출될 함수를 만들어 줍니다.
    update.message.reply_text("무엇을 도와드릴까요?")


# photo reply function
def get_photo(update, context):# get_photo 함수를 보면 경로 생성 - 받은 사진의 id값 받아오기 - id값을 이용하여 파일 받기의 순서로 동작합니다.
    file_path = os.path.join(dir_now, 'from_telegram.png')
    photo_id = update.message.photo[-1].file_id  # 제일 마지막 사진이 화질이 제일 좋으므로 -1을 넣어서 마지막 사진을 저장합니다. photo 번호가 높을수록 화질이 좋음
    photo_file = context.bot.getFile(photo_id)
    photo_file.download(file_path)
    update.message.reply_text('사진 저장 완료')


# file reply function
def get_file(update, context): # 사진과 마찬가지로 경로 생성 - 파일의 id값 받아오기 - id값을 이용하여 파일 받기의 순서로 동작합니다.
    file_id_short = update.message.document.file_id
    file_url = os.path.join(dir_now, update.message.document.file_name)
    context.bot.getFile(file_id_short).download(file_url)
    update.message.reply_text('파일 저장 완료')


# echo reply function
def echo_command(update, context): # 자문자답
    user_text = update.message.text
    if '모해' in user_text:
        bot.send_message(chat_id=chat_id, text='오빠 생각 ㅎㅎ')
    '''
    elif '아잉' in user_text:
        bot.send_message(chat_id=chat_id, text=emojize('아잉:heart_eyes:', use_aliases=True))
    '''
    if '몇시' in user_text:
        bot.send_message(chat_id=chat_id, text='7시에 보자')
    elif '민정사진' in user_text:
        bot.send_photo(chat_id=chat_id, photo=open('Desktop\Emma\img\Rhee Min-Jung\mj.jpg','rb'))

    if '민정' in user_text:
        bot.send_message(chat_id=chat_id, text='왱?')

    elif '이유사진' in user_text:
        bot.send_photo(chat_id=chat_id, photo=open('Desktop\Emma\img\IU\IU.jpg','rb'))
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')  

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')   

    elif '뭐해' in user_text:
        bot.send_message(chat_id=chat_id, text='아무것도 안 합니다')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')  

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '뭐해' in user_text:
        bot.send_message(chat_id=chat_id, text='아무것도 안 합니다')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')  

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')   

    elif '뭐해' in user_text:
        bot.send_message(chat_id=chat_id, text='아무것도 안 합니다')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')  

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')
    
    elif '엠마' in user_text:
        bot.send_message(chat_id=chat_id, text='네, 대답하세요.')

updater = Updater(token, use_context=True) # updater는 봇의 업데이트 사항이 있으면 이를 가져오는 클래스입니다.

### Commands ###

# start handler
start_handler = CommandHandler('start', start_command)
updater.dispatcher.add_handler(start_handler)
'''
#Filters.text는 텍스트에 대해 응답하며 이때 get_message 함수를 호출합니다.
message_handler = MessageHandler(Filters.text & (~Filters.command), get_message) # Handler는 각종 메세지들을 다루기 위한 클래스입니다.
updater.dispatcher.add_handler(message_handler) # updater의 dispatcher.add_handler를 이용하여 handler를 추가해 줍니다.
'''
# 텔레그램에서 Command는 맨 앞에 / 혹은 @(설정했을 경우)가 붙은 메세지를 말합니다.
help_handler = CommandHandler('help', help_command) # # 메세지중에서 command 제외
updater.dispatcher.add_handler(help_handler) # 실행시킨 뒤 /help를 보내봅니다.

# MessageHandler와 Filters.photo를 이용하여 사진에 대해 응답하는 Handler를 추가해 줍니다.
photo_handler = MessageHandler(Filters.photo, get_photo)
updater.dispatcher.add_handler(photo_handler)

# Handler를 보면 파일의 경우 Filters.document 형식으로 주의해 주시기 바랍니다.
file_handler = MessageHandler(Filters.document, get_file)
updater.dispatcher.add_handler(file_handler)

echo_handler = MessageHandler(Filters.text, echo_command)
updater.dispatcher.add_handler(echo_handler)

updater.start_polling() # start_polling을 이용하여 polling을 시작합니다.
updater.idle() # idle은 updater가 종료되지 않고 계속 실행되어 있도록 하는 함수입니다.