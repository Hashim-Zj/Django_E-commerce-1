from django import forms


class OrderDetailsForm(forms.Form):
  options=(
    ("dispached","dispached"),
    ("deliverd","deliverd"),
    ("outofstock","outofstock")
    )
  status=forms.ChoiceField(choices=options,widget=(forms.Select(attrs={"class":"form-control my-3"})))
  expected_date=forms.DateField(widget=(forms.DateInput(attrs={"class":"form-control","type":"date"})))