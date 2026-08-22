from collections import deque


class Solution:
    def lastSubstring(self, s: str) -> str:
        # import pudb
        #
        # pu.db
        if not s:
            return ""
        if len(s) == 1:
            return s
        left = 0
        right = 1
        offset = 0
        while (left + offset) < len(s) and (right + offset) < len(s):
            if s[left + offset] == s[right + offset]:
                # keep going
                offset += 1
                continue
            # new substring is 'higher', pull up left to right
            elif s[left + offset] < s[right + offset]:
                left = max(left + offset + 1, right)
                right = left + 1
            else:
                right += 1
            offset = 0
        return "".join(s[left:])


s = "jlidhumidloagrlvvxdqscegbeaybfhhyaeilzxdpyvvxixrjytdalknkospradmumysbkizziltzjwsxkteykblcvkfivzmtvnsyrfgvojhyzkouscymixrdfmehiwijntzqptqaxgalygtzvwxnsgcnygbjzeqmbactgmckvssvkentpxcnznrbbnkttnzpvlzfmdvvsozaiycumzlizbfxvyucyagclrifczcvzvrkiqiajindjjyxgxflnjcgckruujsbppxtwgwvrrxgniqplynvboqyvrsxnmbjhgoybqophbxmjhhrznezstujjuucvrrvofktxldxfaioyijoayggmvjmgzjflzxmkwxmxnyizampdcfntdfkxxprgfxjduiwrmgdfuprpljgnbzbedqbzhqsbmohbhlszvdzcgbimfurmkwqaignxbeevevonmdgupugcjxvqglqkwqzrlqequliwmfrvidtpprodcbhgkt"
expected = "zziltzjwsxkteykblcvkfivzmtvnsyrfgvojhyzkouscymixrdfmehiwijntzqptqaxgalygtzvwxnsgcnygbjzeqmbactgmckvssvkentpxcnznrbbnkttnzpvlzfmdvvsozaiycumzlizbfxvyucyagclrifczcvzvrkiqiajindjjyxgxflnjcgckruujsbppxtwgwvrrxgniqplynvboqyvrsxnmbjhgoybqophbxmjhhrznezstujjuucvrrvofktxldxfaioyijoayggmvjmgzjflzxmkwxmxnyizampdcfntdfkxxprgfxjduiwrmgdfuprpljgnbzbedqbzhqsbmohbhlszvdzcgbimfurmkwqaignxbeevevonmdgupugcjxvqglqkwqzrlqequliwmfrvidtpprodcbhgkt"
result = Solution().lastSubstring(s)
print("output: ", result)
print("*" * 10)
print("expected: ", expected)
assert expected == result
