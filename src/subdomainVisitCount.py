from collections import Counter

def subdomainVisits(cpdomains):


    domain_counts = Counter()

    for domain in cpdomains:

        count,subdomain = domain.split(" ")
        # print(count,subdomain)

        

        splits = subdomain.split(".") #either 3 or 2
        # print(splits)

        for i in range(len(splits)):
            domain_counts[".".join(splits[i:])] += int(count)


    # print(domain_counts)

    return [str(value)+ " " + key for key,value in domain_counts.items()]

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
print(subdomainVisits(["9001 discuss.leetcode.com"]))
 



