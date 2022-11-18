from chatterbot import ChatBot


import time
time.clock = time.time

bot = ChatBot('Amazebot',
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )


# run and get response from user.
name = input('Enter Your Name: ')

print ('Hello, I am Trevelyan House Surgery Amazebot. How can I help you today?')

while True:

    request = input(name+': ')

    if request=="Bye" or request=='bye':
        print('Bot: Bye')
        break
    else:
        response=bot.get_response(request)
        print('Bot: ', response)