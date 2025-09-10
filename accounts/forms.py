from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="ایمیل")
    phone_number = forms.CharField(
        max_length=11, required=False, label="شماره تلفن"
    )
    birthday = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="تاریخ تولد"
    )
    sex = forms.ChoiceField(
        choices=User.SEX_CHOICES, required=False, label="جنسیت"
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "phone_number",
            "birthday",
            "sex",
            "password1",
            "password2",
        ]
        labels = {
            "username": "نام کاربری",
            "password1": "رمز عبور",
            "password2": "تکرار رمز عبور",
        }

    # اگر بخوای می‌تونی اعتبارسنجی اضافه هم بذاری
    def clean_phone_number(self):
        phone = self.cleaned_data.get("phone_number")
        if phone and len(phone) != 11:
            raise forms.ValidationError("شماره تلفن باید 11 رقم باشد")
        return phone
