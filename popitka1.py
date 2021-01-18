import random
import speech_recognition as sr
import pyttsx3

kek = pyttsx3.init()
kek.say('Как тебя зовут?')
kek.runAndWait()

mic = sr.Microphone()
r = sr.Recognizer()
def recog():
    with mic:
            audio = r.listen(mic)
            try:
                text = r.recognize_google(audio, language = "ru-RU")
            except:
                text = 'Аноним'
    return text
rcg = recog()
kek.say('вау! тебя правда зовут'+rcg +'? Отличное имя!')
print('Я думаю, что Вас зовут '+rcg)
kek.runAndWait()

kek.say('Ладно,хватит болтовни,задавай свой вопрос')
kek.runAndWait()

text = recog()
mas = {1: 'Тепло', 2 : 'Полегче', 3: 'В одежду покемона'}
mas2 = ['в ближайшие дни', 'в ближайшие два месяца', 'в этом году', 'в следующем году', 'в ближайшие несколько лет',
        'более, чем через 10 лет', 'никогда']
mas3 = {1 : (' более, чем вероятно', ' весьма возможно'), 2 : (' невозможно','едва ли вероятно')}

print(text)
text = text.lower()

if (('как' and 'одеься')) in text:
    keys = random.choice([1, 2, 3])
    answer = 'Я думаю, тебе сегодня стоит одеться ' + mas[keys]
    kek.say(answer)
elif 'когда' in text :
    keys = random.randrange(1,7)
    answer = 'Я думаю, это будет ' + mas2[keys]
    kek.say(answer)
else:
    keys = random.choice([1, 2])
    answer = 'Я думаю, это ' + random.choice(mas3[keys])
    kek.say(answer)
answer = answer.lower()
print(answer)
kek.runAndWait()