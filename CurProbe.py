input strings
emails_list = ['vasya@mail.ru', 
          'akakiy@yandex.ru', 
          'spyderman@yandex.ru', 
          'XFiles@gmail.com', 
          'hello@mail.ru', 
          'noname@gmail.com', 
          'DonaldTrump@mail.ru', 
          'a768#af@yandex.ru', 
          'Ivan_Ivanovich@yandex.ru', 
          'thebestmail@yandex.ru']
domains=[]
quantities=[]
domain_dict={}
CountAddresses=0
CountUniqueDomains=0
for email in emails_list:
    CountAddresses=CountAddresses+1
    domain=email[email.find('@')+1:]
    print(CountAddresses,') ',email, domain)
    if CountAddresses==1:
        CountUniqueDomains=CountUniqueDomains+1
        domains.append(domain)
        quantities.append(1)
        domain_dict[domain]=1
        print('Erst. Domains','\n',domains,' \n quantities:',quantities,'dict:',domain_dict)
    else:
        N=0
        FoundN=0
        for domainPresent in domains:
            N=N+1
            if domain==domainPresent:
                FoundN=N
                print(domain,'=',domainPresent,' it is in N ',FoundN)
        if FoundN==0: 
            CountUniqueDomains=CountUniqueDomains+1
            print('new unique domain! N ',CountUniqueDomains,' : ',domain)
            domains.append(domain)
            quantities.append(1)
            domain_dict[domain]=1
            print(CountUniqueDomains, domain,domain_dict[domain])
            domain_dict[domain]=quantities[CountUniqueDomains-1]
            print(CountUniqueDomains, domain,domain_dict[domain])
        else:
            quantities[FoundN-1]=quantities[FoundN-1]+1
            domain_dict[domain]=domain_dict[domain]+1
            domain_dict[domain]=quantities[FoundN-1]
            print('this domain is already present at N ',FoundN,' and occurs already ',quantities[FoundN-1],' times')
            #print('this domain is already present. Now quantities:\n',quantities)
        #print(domains)
        #print(quantities)
        print(domain_dict)
print('Finally:')
#print(domains)
#print(quantities)
stro=''
print(domain_dict)
print('Or better')
CountDictItems=0
NLen=len('N ')
DomainLen=len('Domain ')
QuantityLen=len('Quantity')
for domain, quantity in domain_dict.items():
    CountDictItems=CountDictItems+1
    if len(str(CountDictItems))>NLen:
       NLen=len(str(CountDictItems))
    if len(domain)>DomainLen:
        DomainLen=len(domain)
    if QuantityLen<len(str(quantity)):
        QuantityLen=len(str(quantity))
#print('N','Domain','Quantity')
print(('N',NLen), stro.ljust('Domain',DomainLen), stro.ljust('Quantity',QuantityLen))
CountDictItems=0
for domain, quantity in domain_dict.items():
    CountDictItems=CountDictItems+1
    print(stro.ljust(CountDictItems,NLen), stro.ljust(domain,DomainLen), stro.ljust(quantity,QuantityLen))
