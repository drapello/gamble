# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from website.utils import *
from website.models import *
from optparse import make_option
import time
import unicodedata

class Command(BaseCommand): 
    # option_list = BaseCommand.option_list + (
    #     make_option('--sentenca',
    #         default='',
    #         help='features'),
    #     )
    
    def normalize(self, text):
        if type(text) != unicode:
            try: 
                text = str(text).decode("UTF-8")
            except:
                text = str(text).decode("iso8859-1")
        text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore")
        return text
    
    def handle(self, *args, **options):
        # options['sentenca']
        
        contas = [account for account in Account.objects.all()]
        
        for account in contas:        
            
            print "Crawling user %s" % account.username
            github_profile = profile(account.username)
            github_profile.get_info()
            
            #projetos = []
            #for projeto in github_profile.projetos:
            #    proj = Projeto.objects.get_or_create(nome=projeto['nome'], linguagem=projeto['language']) 
            #    projetos.append(proj[0])

            linguagens = []
            for projeto in github_profile.projetos:
                linguagem = projeto['language'].lower()
                if linguagem not in linguagens:
                    try:
                        int(linguagem)
                    except: 
                        linguagens.append(linguagem)
            
            for username in github_profile.amigos:
                try:
                    Profile.objects.get(username=username)
                except (Profile.DoesNotExist):
                    acc = Account.objects.get_or_create(username=username)
                    contas.append(acc[0]) 

            #print github_profile.username, github_profile.name, github_profile.email, github_profile.location, github_profile.company

            #tratamento para estados
            
            estadosesiglas = [('acre', 'AC'), ('alagoas', 'AL'), ('amapa', 'AP'), ('amazonas', 'AM'), ('bahia', 'BA'), 
            ('ceara', 'CE'), ('distrito federal', 'DF'), ('espirito santo', 'ES'), ('goias', 'GO'), ('maranhao', 'MA'), 
            ('mato grosso', 'MT'), ('mato grosso do sul', 'MS'), ('minas gerais', 'MG'), ('para', 'PA'), ('paraiba', 'PB'), 
            ('parana', 'PR'), ('pernambuco', 'PE'), ('piaui', 'PI'), ('rio de janeiro', 'RJ'), ('rio grande do norte', 'RN'),
            ('rio grande do sul', 'RS'), ('rondonia', 'RO'), ('roraima', 'RR'), ('santa catarina', 'SC'), ('sao paulo', 'SP'), 
            ('sergipe', 'SE'), ('tocantins', 'TO')]
            
            local = ""
            for (estado, sigla) in estadosesiglas:
                if estado in self.normalize(github_profile.location).lower():
                    local = estado
                    break
                    
            if not local:
                if "brasil" in self.normalize(github_profile.location).lower():
                    local = "brasil"
                    for (estado, sigla) in estadosesiglas:
                        if sigla in github_profile.location:
                            local = estado
                            break
            
            if local and len(github_profile.projetos) > 0 and self.normalize(github_profile.company).lower() != "globo.com" and len(linguagens)>0:    
                user = Profile.objects.get_or_create(
                    username = github_profile.username,
                    nome = self.normalize(github_profile.name),
                    link = github_profile.link,
                    email = github_profile.email,
                    company = self.normalize(github_profile.company).lower(),
                    location = local,
                    linguagens = ", ".join(linguagens),
                    projetos = len(github_profile.projetos),
                    )

            contas.remove(account)
            user = Account.objects.get(username = github_profile.username)
            user.delete()
            time.sleep(1)
            

