from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot('Aither')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo',
			'Você gosta de programar?', 'Sim, eu programo em Python','Sua Gostosa','Para billy...','Bora sair na porrada','Você não aguentaria','Aither','Oii..']
trainer = ListTrainer(bot)
trainer.train(conversa)

def Aither(perg):
    perg = perg.replace('-',' ')
    resposta = bot.get_response(perg)
    if float(resposta.confidence) > 0.5:
            return resposta
    else:
       return 'Não sei responder'
