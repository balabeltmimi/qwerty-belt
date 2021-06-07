from django.shortcuts import render
from django.views import View
# Create your views here.


def index(request):
    template_name = 'base.html'
    return render(request, template_name)

class IndexView(View):
    def get(self, request):
        github_url = 'https://github.com/balabeltmimi'
        template_name = 'base.html'
        return render(
            request,
            template_name,
            {
               'github_url': github_url
            },
        )

    def post(self, request):
        pass