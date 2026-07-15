class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        closetoopen = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closetoopen:
                if stck and stck[-1] == closetoopen[c]:
                    stck.pop()
                else:
                    return False
            
            else:
                stck.append(c)

        return True if not stck else False