from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CommentForm
from .models import Book
# Create your views here.
class Home(LoginView):
    template_name = 'home.html'
def about(request):
    return render(request, 'about.html')

@login_required
def book_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book= Book.objects.get(id=book_id)
    comment_form = CommentForm()
    return render(request, 'books/detail.html',
     {'book' : book,
     'comment_form': comment_form,
     })

class BookCreate(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['name','image', 'review', 'age', 'recommend']
    success_url = '/books/'

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the book
        return super().form_valid(form)

class BookUpdate(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['image', 'review','age', 'recommend']

class BookDelete(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = '/books/'

@login_required
def add_comment(request, book_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.book_id = book_id
        new_comment.save()

    return redirect('book_detail', book_id=book_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)