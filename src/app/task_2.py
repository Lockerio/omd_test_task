import re

# Пример строки стиля background-image с image-set
style_string = ('background-image:image-set(url("https://img.detmir.st/ztpREaZYy8TzxIq429f1SVgKx_F9gg_-zg8wopnA_y8/rs:fill:7680:180/g:ce/aHR0cHM6Ly9nby5kZXRtaXIuc3QvaW1hZ2VzL2Jhbm5lcnMvNTY4ZGM4M2NlMjM4YzNkNjg5MWI3NjhmYjJlYTczYjBkNzc3YzNjNS5qcGVn.webp") 3x, url("https://img.detmir.st/O1Auifqi4bBiYhIigaGWQuUHPP4cDyt5U7thko0g5kc/rs:fill:5120:120/g:ce/aHR0cHM6Ly9nby5kZXRtaXIuc3QvaW1hZ2VzL2Jhbm5lcnMvNTY4ZGM4M2NlMjM4YzNkNjg5MWI3NjhmYjJlYTczYjBkNzc3YzNjNS5qcGVn.webp") 2x, url("https://img.detmir.st/qEuHrpLgSk7oJg11Pu68tYSiFhITlHSfjRyLRnSrRfw/rs:fill:2560:60/g:ce/aHR0cHM6Ly9nby5kZXRtaXIuc3QvaW1hZ2VzL2Jhbm5lcnMvNTY4ZGM4M2NlMjM4YzNkNjg5MWI3NjhmYjJlYTczYjBkNzc3YzNjNS5qcGVn.webp") 1x)')

# Регулярное выражение для поиска всех ссылок URL в image-set
urls = re.findall(r'url\("([^"]+)"\)', style_string)
urls_list = ";".join(urls)
# Вывод всех найденных URL
print(urls_list)