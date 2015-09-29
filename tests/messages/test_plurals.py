# -*- coding: utf-8 -*-
#
# Copyright (C) 2008-2011 Edgewall Software
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution. The terms
# are also available at http://babel.edgewall.org/wiki/License.
#
# This software consists of voluntary contributions made by many
# individuals. For the exact contribution history, see the revision
# history and logs, available at http://babel.edgewall.org/log/.

from babel import Locale
from babel.messages import plurals


def test_get_plural():
    assert plurals.get_plural(locale='en') == (2, '(n != 1)')
    assert plurals.get_plural(locale='ga') == (3, '(n==1 ? 0 : n==2 ? 1 : 2)')

    tup = plurals.get_plural("ja")
    assert tup.num_plurals == 1
    assert tup.plural_expr == '0'
    assert tup.plural_forms == 'npurals=1; plural=0'
    assert str(tup) == 'npurals=1; plural=0'

    for locale, num_plurals, plural_expr in [
        (Locale('en'), 2, '(n != 1)'),
        (Locale('en', 'US'), 2, '(n != 1)'),
        (Locale('zh'), 1, '0'),
        (Locale('zh', script='Hans'), 1, '0'),
        (Locale('zh', script='Hant'), 1, '0'),
        (Locale('zh', 'CN', 'Hans'), 1, '0'),
        (Locale('zh', 'TW', 'Hant'), 1, '0'),

    ]:
        tup = plurals.get_plural(locale)
        assert tup.num_plurals == num_plurals
        assert tup.plural_expr == plural_expr


def test_get_plural_falls_back_to_default():

    assert plurals.get_plural('aa') == (2, '(n != 1)')