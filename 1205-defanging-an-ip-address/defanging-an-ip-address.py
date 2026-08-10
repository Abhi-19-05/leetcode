class Solution:
    def defangIPaddr(self, address: str) -> str:
        k=address.replace(".","[.]")
        return k