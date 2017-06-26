from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from regiohelden.users.permissions import UserCreatedByAdminMixin
from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = ['first_name', 'last_name', 'iban']

    # we already imported User in the view code above, remember?
    model = User


class OwnUserUpdateView(UserUpdateView):

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User


class UserDeleteView(LoginRequiredMixin, UserCreatedByAdminMixin, DeleteView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    success_url = reverse_lazy('users:list')
