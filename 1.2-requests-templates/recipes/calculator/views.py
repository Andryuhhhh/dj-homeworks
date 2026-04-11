from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def omlet(request):
    servings = int(request.GET.get('serving', 1))
    count_eggs = int(DATA["omlet"]["яйца, шт"]) * servings
    count_milk = float(DATA["omlet"]["молоко, л"]) * servings
    count_salt = float(DATA["omlet"]["соль, ч.л."]) * servings


    context = {
        'recipe': {
            'яйца': f'{count_eggs} шт',
            'молоко': f'{count_milk:.1f} л',
            'соль': f'{count_salt:.2f} ч.л.',

        }
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get('serving', 1))

    count_pasta = float(DATA["pasta"]["макароны, г"]) * servings
    count_cheese = float(DATA["pasta"]["сыр, г"]) * servings



    context = {
        'recipe': {
            'макароны': f'{count_pasta:.2f} г',
            'сыр': f'{count_cheese:.2f} г',

        }
    }
    return render(request, 'calculator/index.html', context)

def buter(request):
    servings = int(request.GET.get('serving', 1))

    count_bread = int(DATA["buter"]["хлеб, ломтик"]) * servings
    count_sausage = int(DATA["buter"]["колбаса, ломтик"]) * servings
    count_cheese = int(DATA["buter"]["сыр, ломтик"]) * servings
    count_tomato = int(DATA["buter"]["помидор, ломтик"]) * servings


    context = {
        'recipe': {
            'хлеб': f'{count_bread} ломтик',
            'колбаса': f'{count_sausage} ломтик',
            'сыр': f'{count_cheese} ломтик',
            'помидор': f'{count_tomato} ломтик',

        }
    }
    return render(request, 'calculator/index.html', context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
