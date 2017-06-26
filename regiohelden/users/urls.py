from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^~update/$',
        view=views.OwnUserUpdateView.as_view(),
        name='update'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/delete$',
        view=views.UserDeleteView.as_view(),
        name='delete'
    ),
]
