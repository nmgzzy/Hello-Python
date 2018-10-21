import requests
from bs4 import BeautifulSoup
import time

today = time.strftime("%Y-%m-%d")
info = []

def getHTMLText(url):
    try:
        #修改标识 503
        kv = {'user-agent':'Mozilla/5.0'}
        r=requests.get(url, headers = kv, timeout = 10)
        
        #百度搜索 [key_words]
        #kv = {'wd':'[key_words]'}
        #r=requests.get(url, params = kv)
        
        #r=requests.get(url, timeout = 10)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'

def compare_time(time1,time2):
    s_time = time.mktime(time.strptime(time1,'%Y-%m-%d'))
    e_time = time.mktime(time.strptime(time2,'%Y-%m-%d'))
    return round((int(e_time) - int(s_time))/86400)

def getTJUinfo():#天津大学
    url = 'http://yzb.tju.edu.cn/'
    info.append('天津大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('#objcontent4')[0].select('.newslink')
        date = soup.select('#objcontent4')[0].select('.font_10_time')
        info.append('  校级公告：\n')
        for i in range(0,10):
            if compare_time(date[i].text[1:-1], today) <= 5:
                info.append('!' + date[i].text + '\t' + news[i].text + '\n')
            else:
                info.append(' ' + date[i].text + '\t' + news[i].text + '\n')
        news = soup.select('#objcontent5')[0].select('.newslink')
        date = soup.select('#objcontent5')[0].select('.font_10_time')
        info.append('  学院通知：\n')
        for i in range(0,10):
            if compare_time(date[i].text[1:-1], today) <= 5:
                info.append('!' + date[i].text + '\t' + news[i].text + '\n')
            else:
                info.append(' ' + date[i].text + '\t' + news[i].text + '\n')
        news = soup.select('#objcontent1')[0].select('.newslink')
        date = soup.select('#objcontent1')[0].select('.font_10_time')
        info.append('  学历硕士：\n')
        for i in range(0,10):
            if compare_time(date[i].text[1:-1], today) <= 5:
                info.append('!' + date[i].text + '\t' + news[i].text + '\n')
            else:
                info.append(' ' + date[i].text + '\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getNKUinfo():#南开大学
    url = 'http://yzb.nankai.edu.cn/5508/list.htm'
    info.append('南开大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('#wp_news_w9')[0].select('.col_news_title')
        date = soup.select('#wp_news_w9')[0].select('.col_news_date')
        for i in range(0,20):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getSEUinfo():#东南大学
    url = 'http://yzb.seu.edu.cn/6676/list.htm'
    info.append('东南大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('#wp_news_w3')[0].select('a')
        date = soup.select('#wp_news_w3')[0].select('div')
        for i in range(0,14):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getNJUinfo():#南京大学
    url = 'http://grawww.nju.edu.cn/910/list.htm'
    info.append('南京大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.wp_article_list')[0].select('.Article_Title')
        date = soup.select('.wp_article_list')[0].select('.Article_PublishDate')
        for i in range(0,14):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getZJUinfo():#浙江大学 .snews  .qnews
    url = 'http://grs.zju.edu.cn/redir.php?catalog_id=17212'
    info.append('浙江大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        info.append('  最新公告：\n')
        news = soup.select('.zsw-news-con')[0].select('a')
        for i in range(0,len(news)):
            info.append('\t\t' + news[i].text.strip() + '\n')
        info.append('  硕士生招生：\n')
        news = soup.select('.snews')[0].select('a')
        date = soup.select('.snews')[0].select('.art-date')
        for i in range(0,8):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i+1].text + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i+1].text + '\n')
        info.append('  其他消息：\n')
        news = soup.select('.qnews')[0].select('a')
        date = soup.select('.qnews')[0].select('.art-date')
        for i in range(0,5):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i+1].text + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i+1].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getBUPTinfo():#北京邮电大学
    url1 = 'https://yzb.bupt.edu.cn/list/list.php?p=2_1_1'
    url2 = 'https://yzb.bupt.edu.cn/list/list.php?p=8_4_1'
    info.append('北京邮电大学：'+url1+'\n')
    try:
        html = getHTMLText(url1)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.lh28')
        date = soup.select('.cor3')
        info.append('  通知公告：\n')
        for i in range(0,10):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text[10:] + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text[10:] + '\n')
        html = getHTMLText(url2)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.lh28')
        date = soup.select('.cor3')
        info.append('  招生简章：\n')
        for i in range(0,5):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text[10:] + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text[10:] + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getBUAAinfo():#北京航空航天大学
    url = 'http://yzb.buaa.edu.cn/zxsd/dtxx.htm'
    info.append('北京航空航天大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.newslist')[0].select('a')
        date = soup.select('.newslist')[0].select('span')
        for i in range(0,20):
            if compare_time(date[i].text, today) <= 5:
                info.append('![' + date[i].text + ']\t' + news[i].text.replace('\n','').replace('\r','').replace(' ','') + '\n')
            else:
                info.append(' [' + date[i].text + ']\t' + news[i].text.replace('\n','').replace('\r','').replace(' ','') + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')

def getHITinfo():#哈尔滨工业大学
    url = 'http://yzb.hit.edu.cn/8822/list.htm'
    info.append('哈尔滨工业大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.wp_article_list_table')[0].select('a')
        date = soup.select('.wp_article_list_table')[0].select('.tt2')
        date2 = []
        for i in range(0,10):
            date2.append(date[i].text.replace('年','-').replace('月','-').replace('日',''))
            if compare_time(date2[i], today) <= 5:
                info.append('![' + date2[i] + ']\t' + news[i].text.replace('\n','').replace('\r','').replace(' ','') + '\n')
            else:
                info.append(' [' + date2[i] + ']\t' + news[i].text.replace('\n','').replace('\r','').replace(' ','') + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')
    
def getSJTUinfo():#上海交通大学
    url = 'http://yzb.sjtu.edu.cn/index/zkxx/sszs.htm'
    info.append('上海交通大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.Newslist')[0].select('a')
        date = soup.select('.Newslist')[0].select('span')
        for i in range(0,13):
            if compare_time(date[2*i].text.strip(), today) <= 5:
                info.append('![' + date[2*i].text.strip() + ']\t' + news[i].text + '\n')
            else:
                info.append(' [' + date[2*i].text.strip() + ']\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')
'''
def getWHUinfo():
    url = 'http://www.gs.whu.edu.cn/tzgg/zs.htm'
    info.append('武汉大学：'+url+'\n')
    try:
        html = getHTMLText(url)
        soup = BeautifulSoup(html, "html.parser")
        news = soup.select('.r_con')[0].select('a')
        date = soup.select('.ny_con')[0].select('span')
        for i in range(0,15):
            if compare_time(date[i].text, today) <= 5:
                info.append('!' + date[i].text + '\t' + news[i].text + '\n')
            else:
                info.append(' ' + date[i].text + '\t' + news[i].text + '\n')
    except:
        info.append('\t获取失败...\n')
    info.append('\n')
'''
def getBITinfo():#北京理工大学
    url1 = 'http://grd.bit.edu.cn/zsgz/ssyjs/index.htm'
    url2 = 'http://ac.bit.edu.cn/tzgg/index.htm'
    html = getHTMLText(url)
    soup = BeautifulSoup(html, "html.parser")

def saveInfo():
    with open('C:\\Users\\Joey Zhao\\Desktop\\test.txt', 'w', encoding = 'utf-8') as f:
        f.write('  \n--------------------'+ today +'--------------------\n\n')
        for i in info:
            f.write(i)
   
def main():
    getTJUinfo()
    getNKUinfo()
    getSEUinfo()
    getNJUinfo()
    getBUPTinfo()
    getZJUinfo()
    getBUAAinfo()
    getHITinfo()
    getSJTUinfo()
    saveInfo()
        


if __name__ == "__main__":
    main()