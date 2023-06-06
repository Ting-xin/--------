import csv
import time
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException


def open_page(driver, institu_name):
    # 打开知网高级检索页面
    driver.get("https://kns.cnki.net/kns8/AdvSearch?dbprefix=CFLS&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN")
    # 点击学术期刊栏目
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[3]/div[1]/div/ul[1]/li[1]/a/span'))).click()
    # 选择作者单位
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[1]/span'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[2]/ul[2]/li[5]/a'))).click()
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id = "gradetxt"]/dd[2]/div[2]/input').send_keys(institu_name)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[2]/div/span'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[2]/ul/li[1]/a'))).click()
    time.sleep(3)
    # 选择年份
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/input'))).click()
    time.sleep(3)
    time0_element = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul')
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", time0_element)
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul/li[45]/a'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/input'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/a'))).click()
    time.sleep(3)

    # 点击检索
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input'))).click()
    time.sleep(10)
    # 获取中文总文献数
    ch_num = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '''//*[@id="countPageDiv"]/span[1]/em'''))).text
    ch_num = int(ch_num.replace(",", ''))
    return ch_num
    # # 获取外文总文献数
    # WebDriverWait(driver, 100).until(
    #     EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div/div/div/a[2]'))).click()
    # time.sleep(10)
    # en_num = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
    #     (By.XPATH, '''//*[@id="countPageDiv"]/span[1]/em'''))).text
    # en_num = int(en_num.replace(",", ''))
    # return [ch_num, en_num]


def open_page_author(driver, institu_name, res):
    # 打开知网高级检索页面
    driver.get("https://kns.cnki.net/kns8/AdvSearch?dbprefix=CFLS&&crossDbcodes=CJFQ%2CCDMD%2CCIPD%2CCCND%2CCISD%2CSNAD%2CBDZK%2CCCJD%2CCCVD%2CCJFN")
    # 点击学术期刊栏目
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[3]/div[1]/div/ul[1]/li[1]/a/span'))).click()
    # 选择作者单位
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[1]/span'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[1]/div[2]/ul[2]/li[5]/a'))).click()
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id = "gradetxt"]/dd[2]/div[2]/input').send_keys(institu_name)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[2]/div/span'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="gradetxt"]/dd[2]/div[2]/div[2]/ul/li[1]/a'))).click()
    time.sleep(3)
    # 选择年份
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div/input'))).click()
    time.sleep(3)
    time0_element = driver.find_element_by_xpath(
        '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul')
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight", time0_element)
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/ul/li[45]/a'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div/input'))).click()
    time.sleep(3)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/ul/li[3]/a'))).click()
    time.sleep(3)

    # 点击检索
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/input'))).click()
    time.sleep(10)

    while True:
        # 找到table中的所有tr元素
        table = driver.find_element_by_xpath(
            '/html/body/div[3]/div[2]/div[2]/div[2]/form/div/table')
        rows = table.find_elements_by_xpath('.//tr')

        # 遍历每个tr元素
        for row in rows[1:]:
            # 找到该行中的所有td元素
            cells = row.find_elements_by_xpath('.//td')
            article = {}
            # 遍历每个td元素，并将它们的文本值存储在一个字典对象中
            article['单位'] = institu_name
            article['名称'] = cells[1].text
            article['作者'] = cells[2].text
            article['刊名'] = cells[3].text
            article['时间'] = cells[4].text
            res.append(article)

        try:
            # 找到下一页元素，并单击它
            next_page = driver.find_element_by_css_selector('#PageNext')
            next_page.click()

            # 等待页面加载完成
            driver.implicitly_wait(10)

            # 找到table元素
        except NoSuchElementException:
            # 如果没有下一页数据，则退出循环
            break
    # 循环获取每一页的数据


# if __name__ == "__main__":
#     # get直接返回，不再等待界面加载完成
#     desired_capabilities = DesiredCapabilities.CHROME
#     desired_capabilities["pageLoadStrategy"] = "none"

#     # 设置谷歌驱动器的环境
#     options = webdriver.ChromeOptions()
#     # 设置chrome不加载图片，提高速度
#     options.add_experimental_option(
#         "prefs", {"profile.managed_default_content_settings.images": 2})
#     # # 设置不显示窗口
#     # options.add_argument('--headless')
#     # 创建一个谷歌驱动器
#     driver = webdriver.Chrome(options=options)
#     # 爬取每个机构发表的中英文论文期刊数
#     # with open('./data/长三角科研机构清单.json', encoding='utf-8') as f:
#     with open('./失败清单.json', encoding='utf-8') as f:
#         institu_list = json.load(f)
#     fail_institu_list = []
#     success_num = 0
#     fail_num = 0
#     for institu in institu_list:
#         try:
#             temp_num = open_page(driver, institu['科研机构名称'])
#             institu['中文文献数'] = temp_num
#             # institu['英文文献数'] = temp_num[1]
#             time.sleep(15)
#             success_num += 1
#         except Exception as e:
#             fail_num += 1
#             print('fail: ', fail_num, '\t success: ', success_num)
#             print('fail_name: ', institu)
#             print(institu)
#             fail_institu_list.append(institu)

#     with open('./长三角科研机构知网论文数.json', 'w', encoding='utf-8') as file:
#         json.dump(institu_list, file)
#     with open('./失败清单.json', 'w', encoding='utf-8') as file:
#         json.dump(fail_institu_list, file)
#     # 关闭浏览器
#     driver.close()

if __name__ == "__main__":
    # get直接返回，不再等待界面加载完成
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    # 设置谷歌驱动器的环境
    options = webdriver.ChromeOptions()
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option(
        "prefs", {"profile.managed_default_content_settings.images": 2})
    # # 设置不显示窗口
    # options.add_argument('--headless')
    # 创建一个谷歌驱动器
    driver = webdriver.Chrome(options=options)
    result = []
    institu_list = json.loads(open('./长三角科研机构知网论文数.json').read())
    # open_page_author(driver, "江苏省建筑科学研究院有限公司", result)
    for institu in institu_list:
        if '中文文献数' in institu:
            open_page_author(driver, institu['科研机构名称'], result)
    with open('./长三角论文.json', 'w', encoding='utf-8') as file:
        json.dump(result, file)
    driver.close()
