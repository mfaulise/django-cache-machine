from django.db import models

import mock

from caching.base import CachingMixin, CachingManager, cached_method


# This global call counter will be shared among all instances of an Addon.
call_counter = mock.Mock()


call_secondary_counter = mock.Mock()


class User(CachingMixin, models.Model):
    name = models.CharField(max_length=30)

    objects = CachingManager()


class Addon(CachingMixin, models.Model):
    val = models.IntegerField()
    author1 = models.ForeignKey(User)
    author2 = models.ForeignKey(User, related_name='author2_set')

    objects = CachingManager()

    def calls(self, arg=1):
        """This is a docstring for calls()"""
        call_counter()
        return arg, call_counter.call_count
    calls = cached_method(calls, objects)


class Secondary(CachingMixin, models.Model):
    val = models.IntegerField()

    objects = CachingManager('secondary')
    
    def calls(self, arg=1):
        call_secondary_counter()
        return arg, call_secondary_counter.call_count
    calls = cached_method(calls, objects)
