def subdomainVisits(cpdomains):
    dict = {}
    for i in cpdomains:
        nums, web = i.split(' ')
        domins = web.split('.')

        print(domins)
        if len(domins) == 2:
            domin_list = [web, domins[1]]
            for i in domin_list:
                if i in dict:
                    dict[i] += int(nums)
                else:
                    dict[i] = int(nums)
        else:
            domin_list = [web, domins[2], domins[1]+'.'+domins[2]]
            for i in domin_list:
                if i in dict:
                    dict[i] += int(nums)
                else:
                    dict[i] = int(nums)
    m = []
    for key, value in dict.items():
        m.append(str(value)+' '+key)
    return m

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))




