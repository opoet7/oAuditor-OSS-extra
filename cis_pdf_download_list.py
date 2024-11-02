import requests,re

cookies = {
    'workbench_session': 'put your session'
}
dl = ""
for i in range(1, 99):
    params = {
        'q': 'windows', #searcg query
        'tags': '11', #benchmark taq
        'page': i, #page number
    }
    response = requests.get('https://workbench.cisecurity.org/files', params=params, cookies=cookies)
    ids = re.findall(".*href=\"https:\/\/workbench\.cisecurity\.org\/files\/(\d+)\"", response.text)
    for id in ids:
        dl += "https://workbench.cisecurity.org/files/" + id + "/download\n"
    if not ids:
        break
print(dl)
