from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "Walk for 20 minutes every day",
    "march": "Lear Django for 20 minutes every day",
    "april": "Walk for 20 minutes every day",
    "may": "Eat no meat for the entire month",
    "june": "Lear Django for 20 minutes every day",
    "july": "Walk for 20 minutes every day",
    "august": "Lear Django for 20 minutes every day",
    "september": "Walk for 20 minutes every day",
    "october": "Eat no meat for the entire month",
    "november": "Lear Django for 20 minutes every day",
    "december": "Walk for 20 minutes every day",
}

def index(request):
    response_html = '<ul>'
    for month in monthly_challenges:
        month_path = reverse('month-challenge', args=[month])
        response_html += f'<li><a href="{month_path}">{month.capitalize()}</a>'
    response_html += '</ul>'
    return HttpResponse(response_html)


def monthly_challenge_by_number(request, month):
    if 1 <= month <= 12:
        redirect_month = list(monthly_challenges.keys())[month - 1]
        redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenges/january
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound('<h1>HttpResponseNotFound: This is not a correct month</h1>')


def monthly_challenge(request, month):
    if month in monthly_challenges:
        challenge_text = month.capitalize() + ': ' + monthly_challenges[month]
        #response_data = render_to_string('challenges/challenge.html')
        #return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html',{
            'challenge_text' : challenge_text,
            'month': month.capitalize(),
        })
    else:
        return HttpResponseNotFound('<h1>HttpResponseNotFound: This is not a correct month</h1>')
    
