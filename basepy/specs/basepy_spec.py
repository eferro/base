# -*- coding: utf-8 -*-

from expects import *
from hamcrest import *
from doublex import *


with describe('foo1'):
    with describe('bar'):
        with it('borr'):
            expect(True).to(equal(True))
