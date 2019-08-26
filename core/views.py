import random

from django.shortcuts import render

# Create your views here.
from core.forms import InvestigacaoForm
from core.models import Investigacao
from utils.investigacao.identificarCulpado import listarOpcoesView
from utils.investigacao.opcoes import suspeitos, armas, locais, respostas


def home(request):
    form = InvestigacaoForm(request.POST or None)

    print(Investigacao.objects.exists())

    if (not Investigacao.objects.exists()):
        investigacao = Investigacao()
        investigacao.criarCenaDoCrime()
        investigacao.save()
        print(investigacao)

    else:
        investigacao = Investigacao.objects.first()

    context = {}
    context['form'] = form
    context['suspeitos'] = listarOpcoesView(suspeitos)
    context['armas'] = listarOpcoesView(armas)
    context['locais'] = listarOpcoesView(locais)

    if request.method == "POST":
        try:
            if form.is_valid():

                if (investigacao.local == form.cleaned_data['local'] and
                        investigacao.arma == form.cleaned_data['arma'] and
                        investigacao.suspeito == form.cleaned_data['suspeito']):

                    context['mensagemSucesso'] = respostas[0]
                    Investigacao.objects.all().delete()

                elif (investigacao.suspeito != form.cleaned_data['suspeito']):
                    context['mensagemErro'] = respostas[1]

                elif (investigacao.arma != form.cleaned_data['arma']):
                    context['mensagemErro'] = respostas[2]

                elif (investigacao.local != form.cleaned_data['local']):
                    context['mensagemErro'] = respostas[3]

                else:
                    context['mensagemErro'] = respostas[random.choice(1, len(respostas))]

                return render(request, 'home.html', context)

        except (KeyError, Exception):
            context['falhaDeExecucao'] = 'Ocorreu um erro durante a submissão. Favor, tente novamente.'
            return render(request, 'home.html', context)
    return render(request, 'home.html', context)
