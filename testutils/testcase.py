# coding: utf-8
import os
import shutil
import simplejson
from lxml import html as lhtml
from lxml import etree  
from unittest import TestCase
from django.test.client import Client
from django.conf import settings
from django.http import HttpResponse
from django.template import Context, Template

class _TestCase(TestCase):
    
    def setUp(self):
        pass
        
    def before(self):
        pass
    
    def tearDown(self):
        self.after()
        
    def after(self):
        pass
        
    def browser(self):
        if '_browser' in self.__dict__:
            return self._browser 
        self._browser = Client()
        return self._browser
    
    def login(self):
        self.browser().login(username='test',password='test')
    
    def get_redirect(self,url):
        return self.get_301(url)
    
    def get_404(self,url):
        response = self.browser().get(url)
        assert 404 == response.status_code
        return response

    def get_301(self,url):
        response = self.browser().get(url)
        assert 301 == response.status_code
        return response
    
    def get(self,url):
        response = self.browser().get(url)
        assert 200 == response.status_code, "status_code=[%s] - %s" % (response.status_code, url)
        return response
    
    def to_html(self,response):
        if type(response) == HttpResponse:
            return lhtml.fromstring(response.content.decode('utf-8'))
        else:
            return lhtml.fromstring(response)
    
    def to_json(self,response):
        return simplejson.loads(response.content.decode('utf-8'))
        
    def get_html(self,url):
        response = self.get(url)
        return self.to_html(response)
    
    def get_json(self,url):
        response = self.get(url)
        return self.to_json(response)
    
    def get_xml(self,url):
        response = self.get(url)
        return etree.fromstring(response.content)
        
    def tag_test(self, template, context, modulo):
        return self.render(('{%% load %s %%}' % modulo)+template,context)
    
    def render(self,template,context):
        t = Template(template)
        c = Context(context)
        return t.render(c)

    def contents_by_css(self,html,css):
        return [ h.text_content() for h in html.cssselect(css) ]
    
    def striped_contents_by_css(self,html,css):
        return [ h.text_content().strip() for h in html.cssselect(css) ]
    
    def attr(self,el,attr):
        return el.attrib[attr] if attr in el.attrib else None
    
    def attr_by_css(self,html,css,attr):
        return [ self.attr(h,attr) for h in html.cssselect(css) ]