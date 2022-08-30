from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from blog.models import Post
from blog.forms import PostForm, EditPostForm, CommentForm
from django.urls import reverse_lazy, reverse

# def home(request):
#  return render(request, 'home.html', {})

class HomeView(ListView):
 model = Post
 ordering= ['-created_date']
 template_name = 'home.html'
 paginate_by = 5
 
class PostDetailView(FormMixin, DetailView):
 model = Post
 template_name = 'post_details.html'
 form_class = CommentForm
 
 def get_success_url(self):
  return reverse('post-detail', args=(str(self.object.id)) )
 
 def get_context_data(self, **kwargs):
   context = super(PostDetailView, self).get_context_data(**kwargs)
   context['form'] = CommentForm(initial={'post': self.object})
   return context

 def post(self, request, *args, **kwargs):
     self.object = self.get_object()
     form = self.get_form()
     if form.is_valid():
         return self.form_valid(form)
     else:
         return self.form_invalid(form)

 def form_valid(self, form):
     form.save()
     return super(PostDetailView, self).form_valid(form)
 
 
class AddPostView(CreateView):
 model = Post
 form_class = PostForm
 template_name = 'add_post.html'
 
class UpdatePostView(UpdateView):
 model = Post
 form_class = EditPostForm
 template_name = 'update_post.html'
 # fields = ['title', 'title_tag', 'body']
 
class DeletePostView(DeleteView):
 model = Post
 template_name = 'delete_post.html'
 success_url = reverse_lazy('home')