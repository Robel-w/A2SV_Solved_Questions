class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapp = defaultdict(int)

        for item in cpdomains:
            count_str, domain = item.split()
            count = int(count_str)

            parts = domain.split('.')

            for i in range(len(parts)):
                subdomain = '.'.join(parts[i:])
                mapp[subdomain] += count

        res = [f"{v} {k}" for k, v in mapp.items()]
        return res
                   






            
        

        
