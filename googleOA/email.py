class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        email_set = set()
        for email in emails:
            local, domain = email.split("@")
            local = local.split("+")[0].replace(".", "")
            email_set.add((local,domain))
        
        return len(email_set)