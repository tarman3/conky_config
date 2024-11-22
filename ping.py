from ping3 import ping

url='google.com'
ip = '8.8.8.8'
timeout = 1


try:
    response_url = round(ping(url, timeout=timeout, unit='ms'))
    # print(response_url)
except Exception:
    response_url = None

if not response_url:
    try:
        response_ip = round(ping(ip, timeout=timeout, unit='ms'))
        # print(f'IP {round(response_ip)}')
    except Exception:
        response_ip = None

if response_url:
    if response_url > 500:
        print(f'${{color red}}{str(response_url).rjust(4)} ms$color')
    elif response_url > 200:
        print(f'${{color yellow}}{str(response_url).rjust(4)} ms$color')
    else:
        print(f'{str(response_url).rjust(4)} ms')
elif response_ip:
    print(f'${{color red}}IP {str(response_ip).rjust(4)} ms$color')
else:
    print(f'${{color red}}No connection$color')
