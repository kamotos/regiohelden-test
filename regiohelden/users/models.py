from django.contrib.auth.models import AbstractUser
from localflavor.generic.models import IBANField
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    created_by = models.ForeignKey('self', null=True, editable=False)
    iban = IBANField(null=True)

    def __str__(self):
        return self.get_full_name()

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'pk': self.pk})

    def can_modify(self, user):
        """

        :type user: regiohelden.users.models.User
        :param user: User to be modified
        :rtype: bool
        """
        return self.has_google_account() and (user.created_by == self or user == self)

    def has_google_account(self):
        return self.socialaccount_set.filter(provider="google").exists()
