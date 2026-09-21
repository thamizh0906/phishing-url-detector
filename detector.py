import re
def check_url(url):
    red_flags = 0
    if len(url) > 75:
        red_flags += 1
    if '@' in url:
        red_flags +=1
    if not url.startswith('https'):
        red_flags +=1
        ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        if re.search(ip_pattern, url):
            red_flags +=1
    suspicious_words = ['login','verify','account','secure','update']
    for word in suspicious_words:
        if word in url.lower():
            red_flags +=1
            break
    if red_flags >=2:
        print("WARNING: idhu phishing URL ah irukalam!")
    else:
        print("idhu safe URL ah therithu")
test_url = input("URL ah type pannunga:")
check_url(test_url)