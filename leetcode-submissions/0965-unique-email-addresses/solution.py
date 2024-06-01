class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """     
        
        """ 
        Time: O(n)
        Space: 
        Intuition: 
        # Iterate from left to right
        # Take an email and extract it's unique local name
        # Hash that unique name with a list of related domain names(use set for these) """

        def filter_local_name(email):
            k = len(email)
            email_copy = ""
            for i in range(k):
                if email[i] != ".":
                    email_copy = email_copy + email[i]                 
                elif email[i] == "+":
                    break
            try:
                x = email_copy.index("+")
            except ValueError:
                x = k
            
            return email_copy[:x]
                 

        length = len(emails)
        unique_emails = set()

        for i in range(length):
            email = emails[i]
            separator = email.index("@")
            unfiltered_local_name = email[:separator]
            filtered_local_name = filter_local_name(unfiltered_local_name)
            domain_name = email[separator+1:]
            unique_emails.add((filtered_local_name, domain_name))         
         

        return len(unique_emails)
