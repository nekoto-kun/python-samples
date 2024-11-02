import dns.resolver

def dns_enumerate(domain):
    records = ["A", "AAAA", "MX", "NS", "TXT"]
    for record in records:
        try:
            answers = dns.resolver.resolve(domain, record)
            for answer in answers:
                print(f"{record} record: {answer}")
        except dns.resolver.NoAnswer:
            pass

domain = input("Enter domain: ")
dns_enumerate(domain)