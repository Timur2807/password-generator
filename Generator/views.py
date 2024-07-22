from django.http import HttpResponse
from django.shortcuts import render
from random import choice, sample


def home(request):
    context = {
        'name': 'Тимур Валиев',
        'name2': 'Ренат Галипов'
    }
    return render(request, 'Generator/home.html', context=context)


def about_me(request):
    return render(request, 'Generator/about-me.html')


def generate(request):
    symbols_list = 'abcdefghijklmnoprqstuvwxyz'
    numbers_list = '0123456789'
    super_symbols_list = '!@#$%^%*(){}.,'
    password = ''

    count = request.GET.get('count')
    # print(count)
    upper = request.GET.get('upper')
    # print(upper)
    lower = request.GET.get('lower')
    # print(lower)
    numbers = request.GET.get('numbers')
    # print(numbers)
    super_symbols = request.GET.get('super_symbols')
    # print(super_symbols)

    if count:
        all_simbols = ''
        if upper:
            for char in range(int(count)):
                all_simbols += "".join(sample(symbols_list, len(symbols_list) - int(count))).upper()
        if lower:
            for char in range(int(count)):
                all_simbols += "".join(sample(symbols_list, len(symbols_list) - int(count))).lower()
        if numbers:
            for char in range(int(count)):
                all_simbols += "".join(sample(numbers_list, len(numbers_list)))
        if super_symbols:
            for char in range(int(count)):
                all_simbols += "".join(sample(super_symbols_list, len(super_symbols_list)))

        if all_simbols:
            while True:
                if len(password) == int(count):
                    break
                else:
                    password += choice(all_simbols)
        else:
            password = 'Нужно увеличить длину пароля'

    context = {
        'symbols': symbols_list,
        'numbers': numbers_list,
        'super_symbols': super_symbols_list,
        'password': password,
    }
    return render(request, 'Generator/generate.html', context)

def backward(request):

    return render(request, 'Generator/backward.html')

def backward_result(request):
    full_name = request.GET.get('FIO')
    result = "".join(reversed(full_name))
    context = {
        'result': result
    }
    return render(request, 'Generator/backward_result.html', context=context)

