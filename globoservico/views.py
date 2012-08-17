from django.http import HttpResponse
from lxml import html as lhtml
import urllib, urllib2

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time


def incidentes(request):
    
    # import pdb; pdb.set_trace();
    # 
    # browser = webdriver.Firefox() # Get local session of firefox
    # browser.get("http://www.yahoo.com") # Load page
    # assert "Yahoo!" in browser.title
    # elem = browser.find_element_by_name("p") # Find the query box
    # elem.send_keys("seleniumhq" + Keys.RETURN)
    # time.sleep(0.2) # Let the page load, will be added to the API
    # try:
    #     browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
    # except NoSuchElementException:
    #     assert 0, "can't find seleniumhq"
    # browser.close()
    
    
    req1 = urllib2.Request('https://globo.service-now.com/login.do?user_name=cadunsocial%40corp.globo.com&user_password=globocom&language_select=pb&ni.noecho.user_name=true&ni.noecho.user_password=true&ni.nolog.user_password=true&not_important=&screensize=1280x800&sys_action=sysverb_login')
    response = urllib2.urlopen(req1)
    import pdb; pdb.set_trace();
    cookie = response.headers.get('Set-Cookie')

    # Use the cookie is subsequent requests
    req2 = urllib2.Request('https://globo.service-now.com/task_list.do?sysparm_userpref_module=b8c0a2bb0a0a3ca101b9f519ae7f49d7&sysparm_query=sys_class_name=incident^state=3^assignment_group=javascript:getMyGroups()%20^NQsys_class_name=change_request^state=9^assignment_group=javascript:getMyGroups()%20^NQsys_class_name=sc_req_item^state=3^assignment_group=javascript:getMyGroups()%20^NQsys_class_name=incident^state=2^assignment_group=javascript:getMyGroups()%20^NQsys_class_name=sc_task^state=1^assignment_group=javascript:getMyGroups()%20^NQsys_class_name=problem^state=2^assignment_group=javascript:getMyGroups()%20^EQ')
    req2.add_header('cookie', cookie)
    response = urllib2.urlopen(req2)
    
    
    html = "running"
        
        
    return HttpResponse(html)
