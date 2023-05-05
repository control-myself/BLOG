
from typing import Any
from django.http import HttpRequest, HttpResponse
import markdown
from django.conf import settings
from django.shortcuts import render
from markdownx.utils import markdownify
from django.views.generic import CreateView, DetailView
from blog.apps.article.models import Article
from blog.apps.account.models import User
from django.shortcuts import redirect


def home(request):
    content = {}
    can_click = False
    if request.user.is_authenticated:
        if request.user.user_type == 'author':
            can_click = True

    author = User.objects.get(email=settings.AUTHOR_EMAIL)
    content['author'] = author
    content['can_click'] = can_click

    return render(request, 'home.html', {'content': content})
        
class CreateNewArticle(CreateView):
    template_name = 'add_article.html'
    model = Article
    fields = ('content', 'title', 'author')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login/?next=%s' % request.path_info)
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        user = request.user
        content = request.POST['content']
        title = request.POST['title']
        self.model.objects.create(title=title, content=content, author=user)

        return super().post(request)


class EditArticle(CreateView):
    template_name = 'b.html'
    model = Article
    fields = ('content',)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        content = self.model.objects.first()
        ctx['content'] = content.content
        return ctx

    def post(self, request):
        content = request.POST['content']
        self.model.objects.filter().update(content=content)
        return render(request, 'b.html', {'content': content})
    

class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    model = Article

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        article = self.model.objects.get(id=kwargs['pk'])
        context['article'] = markdown.markdown(article.content)
        return self.render_to_response(context)