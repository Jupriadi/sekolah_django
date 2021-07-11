from django import forms
from .models import Guru

class FormGuru(forms.ModelForm) :
    class Meta:
        model = Guru
        fields = [
            'nipguru',
            'namaguru',
            'kelaminguru',
            'alamatguru',
            'tanggallahir',
            'hpguru',
            'email',
            'photoguru',
            'jenjang',
            'jurusan',
        ]
        labels = {
            'nipguru': 'NIP Guru',
            'namaguru' : 'Nama Lengkap Guru',
            'kelaminguru' : 'Jenis Kelamin',
            'alamatguru' : 'Alamat',
            'tanggallahir' : 'Tanggal Lahir',
            'hpguru' : 'Nomor HP / WA',
            'email' : 'Email',
            'photoguru' : 'Photo',
            'jenjang' : 'Jenjang Pendidikan',
            'jurusan' : 'jurusan' 
        }

        widgets ={
            'nipguru' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control rounded-pill'
                }
            ),
            'namaguru' : forms.TextInput(
                attrs = {
                    'class' : 'form-control rounded-pill'
                }
            ),
            'kelaminguru' : forms.Select(
                attrs = {
                    'class' : 'form-control rounded-pill'
                }
            ),
            'alamatguru' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'rows':'3',
                }
            ),
            'tanggallahir' : forms.DateInput(
                attrs = {
                    'type':'date',
                    'class' : 'form-control rounded-pill',
                }
            ),
            'hpguru' : forms.NumberInput(
                attrs = {
                    'class' : 'form-control rounded-pill',
                }
            ),
            'email' : forms.EmailInput(
                attrs = {
                    'class' : 'form-control rounded-pill',
                }
            ),
            'photoguru' : forms.TextInput(
                attrs = {
                    'class' : 'form-control rounded-pill',
                }
            ),
            'jenjang' : forms.TextInput(
                attrs = {
                    'class' : 'form-control rounded-pill',
                }
            ),
            'jurusan' : forms.TextInput(
                attrs = {
                    'class' : 'form-control rounded-pill',
                }
            ),
        }

# class FormGuru(forms.Form) :
#     nipguru = forms.IntegerField(
#         max_value = 999999999999,
#         label = "NIP Guru",
#         widget = forms.NumberInput(
#             attrs ={
#                 'class':'form-control mb-3 rounded-pill'
#             }  
#         )
#     )
#     namaguru =forms.CharField(
#         max_length = 50,
#         label = 'Nama Lengkap Guru ',
#         widget = forms.TextInput(
#             attrs={
#                 'class':'form-control mb-3 rounded-pill'
#             }
#         )
#     )
#     kelaminguru = forms.BooleanField(
#         label = "Jenis Kelamin",
#         widget = forms.NumberInput(
#             attrs ={
#                 'class':'form-control mb-3 rounded-pill'
#             }  
#         )
#     )
#     tanggallahir= forms.DateField(
#         widget=forms.DateInput(
#         attrs={
#             'type': 'date',
#             'class' : 'form-control mb-3 rounded-pill'
            
#             }    
#         )
#     )
#     alamatguru  = forms.CharField(
#         label = "Alamat Lengkap",
#         widget = forms.Textarea(
#             attrs ={
#                 'class':'form-control mb-3',
#                 'rows':'3',
#             }  
#         )
#     )
#     hpguru = forms.CharField(
#         label = "Nomor HP / WA",
#         widget = forms.TextInput(
#             attrs = {
#                 'class':'form-control mb-3 rounded-pill'
#             }
#         )
#     )
#     email = forms.EmailField(
#         label = "Email",
#         widget = forms.EmailInput(
#             attrs = {
#                 'class':'form-control mb-3 rounded-pill'
#             }
#         )
#     )
#     jenjang = forms.CharField(
#         label = "Pendidkan Terahir",
#         widget = forms.TextInput(
#             attrs = {
#                 'class':'form-control mb-3 rounded-pill'
#             }
#         )
#     )
#     jurusan = forms.CharField(
#         label = "Jurusa",
#         widget = forms.TextInput(
#             attrs = {
#                 'class' : 'form-control mb-3 rounded-pill'
#             }
#         )
#     )


#     def clean_email(self):
#         email_input = self.cleaned_data.get('email')

#         if email_input == "jpashter@gmail.com" :
#             raise forms.ValidationError("Email Sudah Ada")
#         return email_input