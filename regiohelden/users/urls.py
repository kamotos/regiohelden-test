from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^create/$',
        view=views.UserCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=views.UserUpdateView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.OwnUserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<pk>\d+)/delete$',
        view=views.UserDeleteView.as_view(),
        name='delete'
    ),
]
