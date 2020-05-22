from __future__ import unicode_literals

import uuid
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from django.conf import settings


class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=True) 
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.CharField(_('website name'), max_length=250, blank=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_created_by', null=True, blank=True)
    created_on = models.DateTimeField(_('user created on'), auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_updated_by', null=True, blank=True)
    updated_on = models.DateTimeField(_('user updated on'), auto_now=True)
    user_is_deleted = models.BooleanField(default=False)
    user_deleted_at = models.DateTimeField(blank=True, null=True)

    role = models.ForeignKey(Role, related_name="role", on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs) 
    

