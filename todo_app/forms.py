from django import  forms

from todo_app.models import Task


class TaskForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field.widget, forms.CheckboxSelectMultiple):
                field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Task
        exclude = ['created_at','updated_at','slug']
        widgets = {
            'type': forms.CheckboxSelectMultiple(),
        }