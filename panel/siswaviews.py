from django.shortcuts import render, get_object_or_404

def index(request) :
    data = {
        'judul':"SISWA Said Alamin",
        'judulhalaman':'Siswa Said Alamain',
    }
    
    return render(request, 'siswa/index.html', data)
