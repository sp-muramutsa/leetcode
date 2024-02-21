class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Time O(n * m * k)
        Space O(n)
        """
        valids = []
        for email in emails: # O(n)
            local, domain = email.split("@")  #O(m) where m is the email length

            if "." in local:
                local = local.replace(".", "") #O(m) where m is the email length
            
            if "+" in local:
                plus_index = local.index("+") #O(m) where m is the email length
                local = local[:plus_index] #O(m) where m is the email length
            
            valid_email = local + "@" + domain #O(m) where m is the email length
            if valid_email not in valids: #O(k) where k is the valids list length
                valids.append(valid_email)
        
        return len(valids)
           
        
        
