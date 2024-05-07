import random
from selenium.webdriver.common.by import By

# Get free proxies for rotating


async def get_free_proxies(selected_web_browser):
    selected_web_browser.get('https://sslproxies.org')

    table = selected_web_browser.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)

    random_position = random.randint(0, 99)

    return {
        'ip': proxies[random_position]['IP Address'],
        'port': proxies[random_position]['Port']
    }
