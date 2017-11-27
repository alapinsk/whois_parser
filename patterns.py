WHOISPATTERNS = {
    'fields': {
        'name': r'name|person|registrar',
        'country': r'country',
        'city': r'city',
        'created': r'created|Created|Created Date|Created On|Created on|Creation Date|Creation Date \(dd/mm/yyyy\)|Registration Date|Registered On|Registered on|Registered|Registered Date|registration|registered|requested on|record activated'
    }
}
def get_error(rest):
    if 'No whois information found.'  in rest:
        error = 'NA' 
    elif 'no entries found'  in rest:
        error = 'NA'     
    elif 'No entries found for the selected source(s).'  in rest:
        error = 'NA'     
    elif 'Status: connect'  in rest:
        error = 'SC'
    elif 'connection attempt failed' in rest:
        error = 'SF' 
    elif 'no data of the requested type was found' in rest:
        error = 'NO'
    elif 'host has failed to respond' in rest:
        error = 'HF'
    elif 'Lookup refused.' in rest:
        error = 'LR'
    elif 'excessive access' in rest:
        error = 'EA'
    elif 'limit exceeded' in rest:
        error = 'EA'
    elif 'many simulataneous connections' in rest:
        error = 'EA'
    elif 'You have exceeded this limit' in rest:
        error = 'EA'   
    elif 'You have exceeded the query limit' in rest:
        error = 'EA' 
    elif 'blacklisted' in rest:
        error = 'EA' 
    elif 'Invalid pattern' in rest:
        error = 'IP' 
    elif 'No such host is known.' in rest:
        error = 'UH'    
    elif 'Failure to abide'  in rest:
        error = 'FA'   
    elif 'NOT FOUND'  in rest:
        error = 'NF'   
    elif len(rest) < 120:
        error = 'NA'
    else:
        error = ''
    return error

def get_provider(rest):
    if 'icann' in rest:
        provider = 'icann'
    elif 'ICANN' in rest:
        provider = 'icann'
    elif 'nominet' in rest:
        provider = 'nominet'
    elif 'nic.it' in rest:
        provider = 'nic.it'
    elif 'SIDN' in rest:
        provider = 'SIDN'
    elif 'eurid' in rest:
        provider = 'eurid'
    elif 'dns.pl' in rest:
        provider = 'dns.pl'
    elif 'godaddy' in rest:
        provider = 'godaddy'
    elif '% Rights to the data above are restricted by copyright.' in rest:
        provider = 'ripencc'
    elif 'nic.it' in rest:
        provider = 'nicit' 
    elif 'ripe.net' in rest:
        provider = 'ripenet'
    elif '[Domain]' in rest:
        provider = 'brackets' 
    elif 'DOMREG' in rest:
        provider = 'domreg'
    elif 'domain.hu' in rest:
        provider = 'domain.hu' 
    elif 'FRNIC' in rest:
        provider = 'frnic' 
    elif 'DNS Belgium' in rest:
        provider = 'dnsbelgium'
    elif 'networksolutions' in rest:
        provider = 'networksolutions'
    elif 'rotld.ro' in rest:
        provider = 'rotld.ro' 
    elif 'DK Hostmaster' in rest:
        provider = 'dkhostmaster'
    elif 'cxDA' in rest:
        provider = 'cxDA' 
    elif 'Afilias' in rest:
        provider = 'afilias'
    elif 'norid.no' in rest:
        provider = 'norid.no'
    elif 'wildwestdomains' in rest:
        provider = 'wildwestdomains'
    elif 'registry.si' in rest:
        provider = 'registry.si'
    elif 'RESTENA' in rest:
        provider = 'RESTENA'
    elif 'internet.ee' in rest:
        provider = 'internet.ee' 
    elif 'NIC Chile' in rest:
        provider = 'nicchile'
    elif 'cointernet.co' in rest:
        provider = 'cointernet.co'
    elif 'registro.br' in rest:
        provider = 'registro.br'
    elif 'whois.sk-nic.sk' in rest:
        provider = 'whois.sk-nic.sk'
    elif 'RIPN' in rest:
        provider = 'ripn'
    elif 'dnc.org' in rest:
        provider = 'dnc.org'
    elif 'PT.whois-servers.net' in rest:
        provider = 'PT.whois-servers.net'
    else:
        provider = ''
    return provider
