from django.shortcuts import render
from django.http import JsonResponse
from hugchat import hugchat
from demo.settings import HUGGING_CHAT_SESSION
def hello_world(request):

    cookies = HUGGING_CHAT_SESSION

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    question = "Hello, can you describe about yourself, what is HuggingChat?"
    answer = chatbot.query(question)

    print("answer")
    print(answer)

    data = {'question': question, 'response': answer.get_final_text()}
    return JsonResponse(data)