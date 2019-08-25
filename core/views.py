from django.shortcuts import render, redirect

# Create your views here.
from core.forms import InvestigacaoForm


def home(request):
    form = InvestigacaoForm(request.POST or None)

    context = {}
    context['form'] = form

    if request.method == "POST":
        try:
            if form.is_valid():

                return render(request, 'home.html', context)

        except (KeyError, Exception):
            context['errorMessage'] = 'Ocorreu um erro durante a submissão. Favor, tente novamente.'
            return render(request, 'home.html', context)
    return render(request, 'home.html', context)

