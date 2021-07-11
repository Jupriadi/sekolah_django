from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django import forms

from .models import Guru
from .form import FormGuru


# Create your views here.
def index(request) :
    data = {
        'judul':"PPDB Said Alamin",
        'judulhalaman':'PPDB Said Alamain',
        'menu' :[
            ['/','Home'],
            ['/panel','Admin']
        ]
    }
    return render(request, 'index.html', data)


def profsek(request) :
    data = {
        'judul':"Profil Sekolah",
        'judulhalaman' : "Profil Sekolah",
    }
    return render(request, 'profsek.html', data)


def editprofsek(request) :
    data = {
        'judul':"Edit Profil",
         'judulhalaman' : "Edit Profil Sekolah",
    }
    return render(request, 'editprofsek.html', data)

def guru(request) :

    #query set
    dataguru = Guru.objects.all()
    # print(dataguru)
    data = {
        'judul' : "Data Guru",
        'judulhalaman' : "Data Guru",
        'guru' : dataguru,
    }
    return render(request, 'guru/index.html', data)


def tambahguru(request) :

    form = FormGuru(request.POST or None) 

    if request.method == 'POST' :
        if form.is_valid():
            form.save()

            messages.success(request, 'Berhasil Menyimpan Data')
            return HttpResponseRedirect("/panel/guru")
    else :
        print("ini adalah method get")    
    


    data = {
        'judul':"Tambah Guru",
        'judulhalaman' : "Form Tambah Guru",
        'form' : form
    }

    return render(request, 'guru/formguru.html', data)


def editguru(request, id) :

    dataguru = Guru.objects.get(id=id) 
    guru = {
        'nipguru' : dataguru.nipguru,
        'namaguru' : dataguru.namaguru,
        'kelaminguru' : dataguru.kelaminguru,
        'alamatguru' : dataguru.alamatguru,
        'tanggallahir' : dataguru.tanggallahir,
        'hpguru' : dataguru.hpguru,
        'email' : dataguru.email,
        'photoguru' : dataguru.photoguru,
        'jenjang' : dataguru.jenjang,
        'jurusan' : dataguru.jurusan,
    }

    form = FormGuru(request.POST or None,initial=guru, instance=dataguru)
    if request.method == 'POST' :
        if form.is_valid():
            form.save()

            messages.success(request, 'Berhasil Mengubah Data')
            return HttpResponseRedirect("/panel/guru")
    else :
        print("ini adalah method get")    
    

    data = {
        'judul':"Edit Guru",
        'judulhalaman' : "Form Edit Guru",
        'form' : form,
    }

    return render(request, 'guru/formguru.html', data)



def hapusguru(request, id) :
    Guru.objects.filter(id = id).delete()
    return HttpResponseRedirect("/panel/guru")