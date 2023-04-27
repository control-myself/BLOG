
from django.http import HttpResponse
import markdown
from django.views.generic import ListView, DetailView, CreateView
from blog.apps.article.models import text
# Create your views here.


class test(CreateView):
    template_name = 'text_form.html'
    model = text
    fields = ('t',)
    # s = "## hello-world"

    def post(self, request):
        action = request.POST.get('action')
        if action == 'preview':
            text = request.POST.get('text')
            text = text.replace("</br>","\n")
            print(text)
            return HttpResponse(markdown.markdown(text))
