from braces.views import FormValidMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, DeleteView, CreateView

from django.contrib.auth.mixins import LoginRequiredMixin

from regiohelden.users.permissions import UserCreatedByAdminMixin, UserHasGoogleAccountMixin
from .models import User


class UserCreateView(LoginRequiredMixin,
                     FormValidMessageMixin,
                     UserHasGoogleAccountMixin,
                     CreateView):
    model = User
    fields = ('username', 'first_name', 'last_name', 'iban')
    form_valid_message = "User successfully created"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        return super().form_valid(form)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'pk': self.request.user.pk})


class UserUpdateView(LoginRequiredMixin,
                     UserCreatedByAdminMixin,
                     FormValidMessageMixin,
                     UpdateView):
    fields = ['first_name', 'last_name', 'iban']
    model = User
    form_valid_message = "User successfully updated"


class OwnUserUpdateView(UserUpdateView):

    def get_success_url(self):
        return self.request.user.get_absolute_url()

    def get_object(self):
        # Only get the User record for the user making the request
        return self.request.user


class UserListView(LoginRequiredMixin, ListView):
    model = User


class UserDeleteView(LoginRequiredMixin, UserCreatedByAdminMixin, DeleteView):
    model = User
    success_url = reverse_lazy('users:list')
