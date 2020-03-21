# -*- coding:utf-8 -*-
import itertools
class Solution:
    def Permutation(self, ss):
        if not ss:
            return []
        ans = []
        for i in itertools.permutations(list(ss), len(ss)):
            ans.append("".join(i))
        return sorted(list(set(ans)))