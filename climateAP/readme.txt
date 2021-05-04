scrapy startproject myproject  终端创建项目
cd myproject                   进入项目
scrapy genspider mydomain mydomain.com  使用 scrapy 工具来对其进行控制和管理

scrapy crawl mydomain -o scraped_data.json   #终端运行mydomain 的name方法  返回scraped_data.json文件

测试常用命令：
scray shell "www.baidu.com"            #下载该页面，返回多个文件，可直接调用，相当于创建变量环境
response.xpath("//div").extract()      #取出该页面的所有div
item_list=response.xpath("//div").extract()
for item in item_list:
     print(item)

climateAP网站爬取的难点分为三点个1.抓包表单的真实请求形式 2.scrapy的post请求的改写 3.动态改变请求的表单

1.抓包表单的真实请求形式
   这个可以暂时通过抓包软件fidder获取，暂不破解
   请求体格式application/x-www-form-urlencoded
   可以通过_urlencode(items, self.encoding) #items是字典格式
   来直接格式化表单形式

2.scrapy的post请求的改写
因为我是抓包获取的表单形式，不需要它对表单的格式化，也不能限定formdata是字典，所以改写scrapy.FormRequest方法
# items = formdata.items() if isinstance(formdata, dict) else formdata
# querystr = _urlencode(items, self.encoding)
querystr   =formdata

3.动态改变请求的表单
这个改变不好改写主要取决于对class类的理解不深，self.name 是栈的形式，也就是说这里如果使用self那么它便是循环定义的最后一个值
因此我们需要gloabl  var   来对动态变化的变量进行覆写，并在class的函数循环时使用变化的值，这里的机制还不了解。暂时写下

scrapy步骤梳理
1）编写mydomain.py爬虫程序
#爬虫主程序
class MydomainSpider(scrapy.Spider):
    name = 'mydomain'           #关于调用哪个爬虫程序
    # allowed_domains = ['climateap.net']
    start_urls = ['http://climateap.net']

    el = 859

    def detail(self, response):
    #该函数为页面处理函数，处理parse请求返回的页面
        html = response.text
        html = etree.HTML(html)
        Annual_variables = html.xpath("//td[@style='width:133px;']/select[@id='ListBox1']/option/text()")
        item1 = ClimateapItem1()
        List1=equ_to_dic(Annual_variables)
        lat              =html.xpath('//tr/td/input[@name="txt_lat"]/@value')[0]
        lng              =html.xpath('//tr/td/input[@name="txt_lng"]/@value')[0]
        time             =html.xpath("//td/select[@id='DropD_hist']/option[@selected='selected']/text()")[0]

    def parse(self, response):
    #该函数为url爬取函数，header在setting.py设置，
       url = 'http://climateap.net'
       data = data.format(i[0], i[1], el, Year, gcm)
       result=scrapy.FormRequest(url, method='POST', formdata=data, callback=self.detail)
       yield result

1）定义items.py
import scrapy
class ClimateapItem1(scrapy.Item):
    x_lan   = scrapy.Field()
    y_lai   = scrapy.Field()
    year    = scrapy.Field()

2）编写管道 pipelines.py
class ClimateapPipeline:
    def open_spider(self, spider):
    #打开要写入的文件
    def process_item(self,item,spider):
    #写入过程，包含mydomain返回的item1、item2、item3的处理
    #使用函数if isinstance(item,ClimateapItem1):
                return item
            elif isinstance(item,ClimateapItem2):
                return item
            elif isinstance(item,ClimateapItem3):
                return item
    #这系列函数可以区分不同的item来写入
    def close_spider(self,spider):
    #关闭文件


我发现这个scrapy的mydomain.py、items.py、piplines.py以及piplines.py返回的item的关系十分不清晰
不过大致总结下
  mydomain.py中  from ..items import ClimateapItem1,ClimateapItem2,ClimateapItem3   联系items.py

  piplines.py中  from .items import ClimateapItem1,ClimateapItem2,ClimateapItem3    联系items.py
                 class ClimateapPipeline：              #这个类中的__int__直接接收mydomain.py返回的item
                    ...。                               #但是这个 __int__ 函数不显示
                  def process_item(self,item,spider)
                    return item                        #这个返回的item不知是什么用途/猜测数据库可能会用到
