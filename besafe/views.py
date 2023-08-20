from django.views.generic import TemplateView

from subscription.models import SubscriptionModel


class Index(TemplateView):
    template_name = "index.html"


class ConsultingComplete(TemplateView):
    template_name = "consultingComplete_07.html"


class Introduce(TemplateView):
    template_name = "introduce_02.html"


class Portfolio(TemplateView):
    template_name = "portfolio_04.html"


class Program(TemplateView):
    template_name = "program_03.html"


class ServiceCenter(TemplateView):
    template_name = "serviceCenter_05.html"


class Subscription(TemplateView):
    template_name = "subscription.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["subscription_models"] = SubscriptionModel.objects.all()

        return context_data
