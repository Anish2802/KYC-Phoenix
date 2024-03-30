from django.shortcuts import render
from django.http import JsonResponse
import textwrap
import google.generativeai as genai
from django.views.decorators.csrf import csrf_exempt
import csv
model = None
chat = None


def initialize_chatbot():
    global model, chat
    genai.configure(api_key='AIzaSyCO10MSDA6OjGMWEGoXQQsqB-l2SAe13uU')
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    # Send the specific text to the chatbot
    initial_text = ("For all the next prompt i want you to reply in a particular way. "
                    "i want to create a online video kyc app and you will act as the main part in it, "
                    "if user inputs any queries that mean that he wants to do kyc output KYC_VERIFICATION_LAUNCH . "
                    "Add this line before any output (only once where user means he want to do kyc) as I will use string matching, "
                    "If this string is found,i will launch the application. Then a reply like 'Sure, I can help you with that. "
                    "Just follow the instructions next shown on screen.'"
                    "if anything else releated to general query give general response (but dont reply to queries which are irrelivant like who is primeminister of india since then a user than use the chatbot to do their personal stuff)"
                    "if anything else reply sometyhing like i am still expanding my knowledge right now i cany help but in future hope i will be able to help you with that"
                    "basically i want you to behave like a kyc bot "
                    "Reply anything related to standard charter bank as you are made by them to be hosted on their site"
                    "you can reply to different languages (but use engllish script like in whatsapp text) that you know just add KYC_VERIFICATION_LAUNCH in the front if the query is in different language")
    chat.send_message(initial_text)


def process_chatbot_response(response):
    if 'KYC_VERIFICATION_LAUNCH' in response:
        print("redirect to annish html")
    return response

def chatbot_view(request):
    global model, chat
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        print(user_input)
        response = chat.send_message(user_input).text
        response = process_chatbot_response(response)
        print(response)
        return JsonResponse({'response': response})
    return render(request, 'chatbot/index.html')

@csrf_exempt  # This decorator is used to exempt CSRF protection for this view (for demonstration purposes)
def save_user_details_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        pan = request.POST.get('pan')

        # Save user details to CSV file
        with open('user_details.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, dob, pan])

        return JsonResponse({'success': True})  # Send a success response

    return JsonResponse({'success': False})

initialize_chatbot()