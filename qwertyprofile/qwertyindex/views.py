from django.shortcuts import render
from django.views import View

from qwertyindex.forms import SubscriberForm
from qwertyindex.models import qwertyindex, Subscibemodel

# Create your views here.


def index(request):
    template_name = "base.html"
    return render(request, template_name)


class IndexView(View):
    def get(self, request):
        name = "belt"
        github_url = "https://github.com/balabeltmimi"
        github_project_url = "https://github.com/balabeltmimi/qwerty-belt"
        template_name = "base.html"
        return render(
            request,
            template_name,
            {
                "name": name,
                "github_url": github_url,
                "github_project_url": github_project_url,
            },
        )

    def post(self, request):
        template_name = "base.html"
        form = SubscriberForm(request.POST)
        profile = qwertyindex.objects.get(id=1)

        if form.is_valid():
            email = form.cleaned_data.get("email")

            Subscibemodel.objects.create(email=email)
            form = SubscriberForm()

        return render(
            request,
            template_name,
            {
                "name": profile.name,
                "form": form,
                "github_url": profile.github_url,
                "github_project_url": profile.github_project_url,
            },
        )

        return render(request, "base.html")
