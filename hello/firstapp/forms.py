from django import forms

# class UserForm(forms.Form):
#     name = forms.CharField(label="Имя клиента")
#     age = forms.IntegerField(label="Возраст клиента")
# class UserForm(forms.Form):
#     basket = forms.BooleanField(label="Положить товар в корзину", required=False)
# class UserForm(forms.Form):
#     vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")
# class UserForm(forms.Form):
#     name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИO не более 15 символов")
# class UserForm(forms.Form):
#   ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text=" Пример формата 192.0.2.0")
# class UserForm(forms.Form):
#     reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")
# class UserForm(forms.Form):
#  slug_text = forms.SlugField(label="Введите текст")
# class UserForm(forms.Form):
#  url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")
# class UserForm(forms.Form):
#  uuid_text = forms.UUIDField(label="Введите UUID", help_text="Формат xxxxxxxx-xxxx-xxxx-xxxxxxxxxxxxxxxx")
# class UserForm(forms.Form):
#     combo_text = forms.ComboField(label="Введите URL",
#     fields=[forms.URLField(), forms.CharField(max_length=20)])
class UserForm(forms.Form):
 file = forms.FileField(label="Файл")