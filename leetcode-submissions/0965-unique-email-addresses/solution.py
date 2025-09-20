class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        number_of_emails = {}
        for email in emails:
            email_components = email.split("@")
            
            local = email_components[0]
            domain = email_components[1]
            
            new_local = ""
            
            instance_of_plus = local.find("+")
            
            if instance_of_plus != -1:
                new_local = local[0:instance_of_plus]
            else:
                new_local = local
                
            new_local = new_local.replace(".", "")
            
            trimmed_email = new_local + "@" + domain
            
            if trimmed_email not in number_of_emails:
                number_of_emails[trimmed_email] = 0
            else:
                number_of_emails[trimmed_email] += 1
        return len(number_of_emails)
                
