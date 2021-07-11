from django.core.exceptions import ValidationError


def val_email(value) :
    email_input = value
    if email_input == "jpashter@gmail.com" :
        pesan = "Email "+ email_input + " sudah digunakan"
        raise ValidationError(pesan)