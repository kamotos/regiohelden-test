from django.contrib.auth.mixins import UserPassesTestMixin


class UserCreatedByAdminMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        return self.request.user.can_modify(self.get_object())
