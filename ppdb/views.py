from django.shortcuts import render

def index(request):
    data = {
        'judul':"PPDB Said Alamin",
        'kreator':'Jupriadi',
        'menu' :[
            ['/','Home'],
            ['/panel','Admin']
        ]
    }
    return render(request, 'index.html', data)