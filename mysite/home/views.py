from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import  User_Action, User_input,Score
from django.contrib import messages
# Create your views here.
import random
import os

def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)

def create_log(user_obj):
    current_date = datetime.date(datetime.now())
    current_time = datetime.time(datetime.now())
    current_time = str(current_time).replace(':', '-')
    
    if os.path.exists('game_logs/') == False:
        os.mkdir('game_logs/')
        print('game_logs directory created')

    log = open(f"game_logs/{user_obj}__{current_date}__{current_time}.log", "a")

    return log


import logging
logger = logging.getLogger(__name__)
def play_game(request):
    context={}
    possible_actions = ["rock", "paper", "scissor"]
    computer_action = random.choice(possible_actions)
    user_score = Score.objects.values_list('user_score',flat=True)
    bot_score = Score.objects.values_list('bot_score',flat=True)
    tie = Score.objects.values_list('tie',flat=True)
    for score in user_score:
        user_score=score
    for score in bot_score:
        bot_score= score 
    for score in tie:
        tie= score 
    print(user_score)    
    print(bot_score)    
       
    if request.method == 'POST' and 'user_name' in request.POST:
        user_name = request.POST['user_name']
        user_obj = User_input( name= user_name)
        log = create_log(user_obj)
        log.write("\nUser created: "+ str(user_obj))
        # logger.debug(f'Player name: {user_obj}')
        user_obj.save()
        Score.objects.create(user_score=0,bot_score=0,tie=0)
       
    if request.method == 'POST' and 'rock' in request.POST:
        
        rock = request.POST['rock']
        select_obj = User_Action()
        user_action = rock
        select_obj.role = rock
        select_obj.save()

        user_obj = User_input.objects.all().values_list('name', flat=True).last()
        
        if user_action == computer_action:
            tie = int(tie) +1
        elif user_action == "rock":
            if computer_action == "scissor":
                user_score = int(user_score) +1
            else:
                bot_score = int(bot_score) +1
        log = create_log(user_obj)
        log.write("\nUser Action: "+ str(user_action))
        log.write("\nBot Action: "+ str(computer_action))
        log.write("\nUser Score: "+ str(user_score))
        log.write("\nBot Score: "+ str(bot_score))
                
        Score.objects.all().update(user_score=user_score,bot_score=bot_score,tie=tie)        
        context["user_action"] = user_action
        context["computer_action"] = computer_action
    
    
    if request.method == 'POST' and 'paper' in request.POST:
        paper = request.POST['paper']
        select_obj = User_Action()
        user_action = paper
        select_obj.role = paper
        user_obj = User_input.objects.all().values_list('name', flat=True).last()
        
        if user_action == computer_action:
            tie = int(tie) +1
        elif user_action == "paper":
            if computer_action == "rock":
                user_score = int(user_score) +1
            else:
                bot_score = int(bot_score) +1
                
        select_obj.save() 
        log = create_log(user_obj)
        log.write("\nUser Action: "+ str(user_action))
        log.write("\nBot Action: "+ str(computer_action))
        log.write("\nUser Score: "+ str(user_score))
        log.write("\nBot Score: "+ str(bot_score))
        
        Score.objects.all().update(user_score=user_score,bot_score=bot_score,tie=tie)        
        context["user_action"] = user_action
        context["computer_action"] = computer_action
    
    if request.method == 'POST' and 'scissor' in request.POST:
        scissor = request.POST['scissor']
        select_obj = User_Action()
        user_action = scissor
       
        select_obj.role = scissor
        user_obj = User_input.objects.all().values_list('name', flat=True).last()
        
        if user_action == computer_action:
           
            tie = int(tie) +1
        elif user_action == "scissor":
            if computer_action == "paper":
                user_score = int(user_score) +1
                
            else:
                bot_score = int(bot_score) +1
                
        select_obj.save() 
        log = create_log(user_obj)
        log.write("\nUser Action: "+ str(user_action))
        log.write("\nBot Action: "+ str(computer_action))
        log.write("\nUser Score: "+ str(user_score))
        log.write("\nBot Score: "+ str(bot_score))
         
        Score.objects.all().update(user_score=user_score,bot_score=bot_score,tie=tie)        
        context["user_action"] = user_action
        context["computer_action"] = computer_action

    
    
        
    user_name = User_input.objects.all().last()
    user_name = user_name.name
    round_count = User_Action.objects.all().count()
   
    context['user_name'] = user_name
    context['round_count'] = round_count
    context['user_score'] = user_score
    context['bot_score'] = bot_score
    context['tie'] = tie
    if round_count == 3:
        User_Action.objects.all().delete()
        Score.objects.all().delete()
        Score.objects.create(user_score=0,bot_score=0,tie=0)
    if int(user_score) > int(bot_score):
        context['best_3']='Win'
    elif int(user_score)< int(bot_score):
        context['best_3']='Lose'
    else:
        context['best_3']='Tie'
                    
    return render(request, 'play_game.html',context)
