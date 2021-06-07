from django.shortcuts import render
from django.views import View
# Create your views here.


def index(request):
    template_name = 'base.html'
    return render(request, template_name)

class IndexView(View):
    def get(self, request):

        name = 'belt'
        github_url = 'https://github.com/balabeltmimi'
        github_project_url = 'https://github.com/balabeltmimi/qwerty-belt'
        template_name = 'base.html'
        return render(
            request,
            template_name,
            {
               'name': name,
               'github_url': github_url,
               'github_project_url': github_project_url,
            },
        )

    def post(self, request):
        print(request.POST)
        print(request.POST.get('email'))

        form = SubscriberForm(request.POST)
        if form_is_valid():
            print(form.cleaned_data)
            print(form.cleaned_data.get('email'))

        profile = qwertyindex.objects.get(id=1)

        name = 'belt'
        github_url = 'https://github.com/balabeltmimi'
        github_project_url = 'https://github.com/balabeltmimi/qwerty-belt'
        template_name = 'base.html'
        return render(
            request,
            template_name,
            {
               'name': name,
               'form': form,
               'github_url': github_url,
               'github_project_url': github_project_url,
            },
        )

        return render(request, 'base.html')