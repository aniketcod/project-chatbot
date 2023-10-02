import random

hello = ["hi", "is anyone there", "hello aniket", "hello there", "can you help me", "hello"]
bye = ["cya", "see you later", "bye", "goodbye", "have a good day", "i am leaving"]
howare = ["how are you", "what's up","how are you doing", ]
name = ["what's your name", "what is your name","do you have anytime","what should i call you"]
menu = [" i want to tell my symptom","what disease do i suffering from", "what do you recommend?",]

print("********************************************")

while True:
    a = input('user said -')
    

    if a.lower() in  hello:
        botans = ["hello!", "hi there", "welcome"]
        print('bot said- '+random.choice(botans)+ '\n')
    elif a.lower() in bye:
        botans = ["sad to see you go :(","bye","miss you","come back soon"]    
        print('bot said -' +random.choice(botans)+'\n')
    elif a.lower() in howare:
        botans = ["I am fine, thanks","happy", "i am good"]
        print('bot said -' +random.choice(botans)+'\n')
    elif a.lower() in name:
        botans = ["My name is Aniket's assistant bot","you can cll me aniket's assistant","aniket's assistant in your service"]    
        print('bot said -' +random.choice(botans)+'\n')
    elif a.lower() in bye:
        botans = ["sad to see you go:(","talk to you later", "goodbye!","have a nice day"]    
        print('bot said -' +random.choice(botans)+'\n')
    elif a.lower() in menu:
        botans = ["tell you symptoms","ask your symptoms", "common symptoms are illness and cold"]    
        print('bot said -' +random.choice(botans)+'\n')
    else:
         print('bot said - Sorry could not get what you said try to make your queastion more understandable''\n')




            