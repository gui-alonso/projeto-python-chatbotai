# Importar as bibliotecas necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Criar uma instância do chatbot
chatbot = ChatBot(
    'ExampleBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Treinar o chatbot com o corpus em inglês
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Função para iniciar uma conversa com o chatbot
def start_chat():
    print("Oi! Sou um chatbot. Pergunte-me algo.")
    while True:
        try:
            user_input = input("Você: ")
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

# Iniciar a conversa
if __name__ == '__main__':
    start_chat()