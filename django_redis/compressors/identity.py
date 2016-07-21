# -*- coding: utf-8 -*-

from .base import BaseCompressor

class IdentityCompressor(BaseCompressor):
    def compress(self, value):
        print 'compressing'
        return value + 'test'

    def decompress(self, value):
        return value
