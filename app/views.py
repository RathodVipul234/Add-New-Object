from django.apps import apps
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from .forms import *
from .models import *

class Manytomany3ModelView(CreateView):
    model = manytomany3
    template_name =  "manytomany3.html"
    form_class = Manytomany3ModelForm
    success_url = "/"



class AddNewObjectView(CreateView):
    model = None
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        app_name = request.path.split("/")[2]
        model_name = request.path.split("/")[3]
        self.model = apps.get_model(app_label=app_name, model_name=model_name)
        self.object = None
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        print(self.object,"========")
        new_id = self.object.id
        new_value = self.object.__str__()
        data = {
            "id":new_id,
            "value":new_value
        }
        return JsonResponse({"status":200, "data":data})

    def form_invalid(self, form):
        """If the form is valid, save the associated model."""
        return JsonResponse({"status":403})
