class Solution:
    def defangIPaddr(self, address):
        defanged = ""
        for char in address:
            defanged += char if char.isdigit() else '[.]'
        return defanged
		
# Official solution given

class Solution:
    def defangIPaddr(self, address):
        ans = []
        for ch in address:
            if ch.isdigit():
                ans.append(ch)
            else:
                ans.append("[.]")
        return "".join(ans)
