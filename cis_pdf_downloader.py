import requests,re,time
cookies = {
    'workbench_session': '#put your session id here'
}
dls = []
for i in range(1, 99):
    params = {
        'q': 'windows', #searcg query
        'tags': '11', #benchmark taq
        'page': i, #page number
    }
    response = requests.get('https://workbench.cisecurity.org/files', params=params, cookies=cookies)
    ids = re.findall(".*href=\"https:\/\/workbench\.cisecurity\.org\/files\/(\d+)\"", response.text)
    dls += ids
    if not ids:
        break
for id in dls:
    response = requests.get(f"https://workbench.cisecurity.org/files/{id}/download",cookies=cookies)
    if response.status_code == 200:
        content_disposition = response.headers.get('Content-Disposition')
        if content_disposition:
            match = re.search('filename="(.+)"', content_disposition)
            if match:
                file_name = match.group(1)
            else:
                file_name = f"{id}.pdf"
        else:
            file_name = f"{id}.pdf"
        with open(file_name, 'wb') as file:
            file.write(response.content)
            print(f"Downloaded file saved as: {file_name}")
    else:
        print("Failed to download the file. Status code:", response.status_code)
    time.sleep(5)