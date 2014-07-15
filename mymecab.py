#!/usr/bin/python
# -*- coding: utf-8 -*-

import MeCab

# 品詞
MECAB_FEATURE_POS = 0
# 品詞細分類1
MECAB_FEATURE_SUBCLASS1 = 1
# 品詞細分類2
MECAB_FEATURE_SUBCLASS2 = 2
# 品詞細分類3
MECAB_FEATURE_SUBCLASS3 = 3
# 活用形
MECAB_FEATURE_CONJUGATION = 4
# 活用型（未然形などの活用の種類）
MECAB_FEATURE_CONJUGATE_TYPE = 5
# 原形
MECAB_FEATURE_BASE = 6
# 読み
MECAB_FEATURE_READING = 7
# 発音
MECAB_FEATURE_PRONUNCE = 8

# MeCabクラス
class mecab:

    def __init__(self, param=""):
        self.t = MeCab.Tagger (" ".join(param))

    def getVersion(self):
        return MeCab.VERSION

    def getParseData(self, sentence):
        return self.t.parse(sentence)

    # 原型を取得
    def getSurface(self, sentence):
        results = []
        try:
            m = self.t.parseToNode(sentence)
            while m:
                if m.surface != "":
                    results.append(m.surface)
                m = m.next
            return results
        except RuntimeError, e:
            print "RuntimeError:", e;

    # 指定位置を取得
    def getFeature(self, sentence, feature_type):
        try:
            m = self.t.parseToNode(sentence)
            while m:
                if m.surface != "":
                    yield m.feature.split(",")[feature_type]
                m = m.next
        except RuntimeError, e:
            print "RuntimeError:", e;

    # 指定位置を取得
    def getFeatures(self, sentence):
        try:
            m = self.t.parseToNode(sentence)
            while m:
                if m.surface != "":
                    yield m.feature.split(",")
                m = m.next
        except RuntimeError, e:
            print "RuntimeError:", e;


# x = mecab()
# for i in x.getFeature("こんにちは．私は太郎ですよ．", MECAB_FEATURE_BASE):
#     print i