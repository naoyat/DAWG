# -*- coding: utf-8 -*-
import pytest
import dawg

class TestPrediction(object):
    DATA = [
      u'日本電気',
      u'山本電気', u'坂本電気', u'日本電器', u'日本電機', u'日本電熱', u'日立電気',
    ]

    SUITE = [
        ((u'日本電気', 0),
           [u'日本電気']),
        ((u'日本電気', 1, True),
           [u'日本電気', u'日本電器', u'日本電機', u'日本電熱', u'日立電気']),
        ((u'日本電気', 1, False),
           [u'日本電気', u'山本電気', u'坂本電気', u'日本電器', u'日本電機', u'日本電熱', u'日立電気']),
    ]

    @pytest.mark.parametrize(("params", "expected"), SUITE)
    def test_dawg_prediction_with_edit_distance(self, params, expected):
        d = dawg.DAWG(self.DATA)
        actual = d.similar_keys_with_edit_distance(*params)
        assert frozenset(actual) == frozenset(expected)