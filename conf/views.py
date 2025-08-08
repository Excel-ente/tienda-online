from django.views.generic import TemplateView
from .models import Empresa, Landing

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empresa = Empresa.objects.first()
        landing = Landing.objects.filter(empresa=empresa).first()
        sections = landing.sections.filter(is_active=True) if landing else []
        context.update({'empresa': empresa, 'landing': landing, 'sections': sections})
        return context
