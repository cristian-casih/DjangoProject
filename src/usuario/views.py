
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from actstream.models import user_stream, target_stream



from usuario.forms import RegistroForm

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class RegistroUsuario (LoginRequiredMixin,CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy("gestion:personal_list")

class UserDetailView(DetailView):

    model = User
    login_required = True
    template_name = 'usuario/detalleusuario.html'

    def get_context_data(request, self, **kwargs):
        user_stream(request.user, with_user_activity=True)
        context = super().get_context_data(**kwargs)
        context['last_activity'] = user_stream(self.get_object())[:20]
        return context

