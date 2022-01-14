from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Transacao
from .form import TransacaoForm
from django.http import JsonResponse
# Create your views here.

# from django.http import HttpResponse
import datetime

from .serializers import ControleGastosListViewSerializer, ControleGastosViewSerializer


def home(request):
    data = {}
    data['transacoes'] = ['t1', 't2', 't3']
    data['now'] = datetime.datetime.now()
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # return HttpResponse(html)
    return render(request, 'contas/home.html', data)


def listagem(request):
    data = {}
    # manager
    data['transacoes'] = Transacao.objects.all()
    return render(request, 'contas/listagem.html', data)


def nova_transacao(request):
    # data = {}
    # form = TransacaoForm()
    # data['form'] = form
    # return render(request, 'contas/form.html', data)
    # --- a mesma coisa acima de um jeito diferente abaixo
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        # return listagem(request)
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form})


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)

    if form.is_valid():
        form.save()
        # return listagem(request)
        return redirect('url_listagem')

    return render(request, 'contas/form.html', {'form': form, 'transacao': transacao})


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    transacao.delete()
    return redirect('url_listagem')


class ControleGastosListView(APIView):
    def get(self, request):
        try:
            lista = Transacao.objects.all()
            serial = ControleGastosListViewSerializer(lista, many=True)
            return Response(serial.data)
        except Exception:
            return JsonResponse({'mensagem': 'Falha ao listar os status dos itens'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ControleGastosView(APIView):
    def post(self, request):
        try:
            serial = ControleGastosViewSerializer(data=request.data, many=True)
            if serial.is_valid():
                serial.save()
                return Response(serial.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'mensagem': str(serial.errors)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'mensagem': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, id):
        try:
            registro = Transacao.objects.get(id=id)
            registro.data = request.data['data']
            registro.valor = request.data['valor']
            registro.descricao = request.data['descricao']
            registro.save()
            return JsonResponse({'mensagem': 'Altrado comsucesso'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'mensagem': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, id):
        try:
            registro = Transacao.objects.get(id=id)
            registro.delete()
            return JsonResponse({'mensagem': 'Excluído com sucesso'}, status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return JsonResponse({'mensagem': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
