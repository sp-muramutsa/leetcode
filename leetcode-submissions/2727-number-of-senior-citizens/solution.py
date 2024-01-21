class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([person for person in details if int(person[11:13]) > 60])
        
