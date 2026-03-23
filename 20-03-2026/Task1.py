from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get(r'file:///Users/dakshjain/PycharmProjects/20-03-2026/playlist.html')
driver.maximize_window()

# songs_list = driver.find_element(By.ID, 'songs')
# select = Select(songs_list)
#
# if select.is_multiple:
#     for i in select.options:
#         if 'Girl' in i.text or 'Love' in i.text:
#             select.select_by_visible_text(i.text)
#
# print([i.text for i in select.all_selected_options])
#
# driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

songs_list = driver.find_element(By.XPATH, '//select[@id="songs"]')
select = Select(songs_list)

if select.is_multiple:
    fav_songs = driver.find_elements(By.XPATH, '//optgroup[2]/option')
    for i in fav_songs:
        select.select_by_visible_text(i.text)

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, '//button[text()="Add to Playlist"]').click()

sleep(5)
driver.quit()