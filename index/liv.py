from nltk.chat.util import Chat, reflections

pairs = [
    ['hi', ['hello', 'hi there', 'hey']],
    ['what is your name', ['My name is Chatbot', 'I am Chatbot']],
    ['who created you', ['mr kelvin', 'kelvin', 'my master']]
]

chatbot = Chat(pairs, reflections)
response = chatbot.respond("hi")
print(response)
