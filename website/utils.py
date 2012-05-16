# -*- coding: utf-8 -*-
from lxml import html as lhtml

import urllib, urllib2

class profile(object):

    def __init__(self, username):
        url = 'https://github.com/'
        self.username = username
        self.link = url + username
        self.followers_link = self.link + '/followers'
        self.following_link = self.link + '/following'
        self.amigos = []
        self.projetos = []
        self.name = ""
        self.email = ""
        self.company = ""
        self.location = ""
        
    def get_data(self,link):
        response = urllib2.urlopen(link)
        if not response:
            return ''
        return lhtml.fromstring(response.read())

    def get_basicinfo(self):
        html = self.get_data(self.link)

        name = [e.text_content().strip() for e in html.cssselect('.avatared em span')]
        if name:        
            self.name = name[0]
            
        email = [e.get('data-email') for e in html.cssselect('.js-obfuscate-email')]
        if email:
            self.email = "".join([unichr(int(s,16)) for s in email[0].split('%') if s])
        
        company = [e.text_content().strip() for e in html.cssselect('.vcard dd') if 'worksFor' in e.values()]
        if company:        
            self.company = company[0]
        
        location = [e.text_content().strip() for e in html.cssselect('.vcard dd') if 'homeLocation' in e.values()]
        if location:        
            self.location = location[0]

        repositories = [e for e in html.cssselect('.repositories .public')]
        for repo in repositories:
            projeto =  {
                'nome' : repo.cssselect('h3 a')[0].text_content().strip(),
                'language' : repo.cssselect('ul li')[0].text_content().strip(),
            } 
            self.projetos.append(projeto) 

    def get_friends(self,url):
        html = self.get_data(url)
        amigos = [e for e in html.cssselect('.members li')]
        for amigo in amigos:
            nomeamigo = amigo.cssselect('a')[1].text_content().strip()
            if nomeamigo not in self.amigos:
                self.amigos.append(nomeamigo)
            
    def get_followers(self):
        self.get_friends(self.followers_link)

    def get_following(self):
        self.get_friends(self.following_link)    
    
    def get_info(self):
        self.get_basicinfo()
        self.get_followers()
        self.get_following()




