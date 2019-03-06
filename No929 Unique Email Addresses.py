class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for i in emails:
            local_name, domain_name = i.split('@')
            local_name = local_name.split('+')[0].split('.')
            result.add(''.join(local_name)+domain_name)
        return len(result)