import re
import sys
import argparse
import csv
from patterns import WHOISPATTERNS, get_error, get_provider

rx_get_domain_date_rest = re.compile(r"^(.+?)\n(.+?)\n+((?:.+\n)+)", re.MULTILINE)
pattern_dict = WHOISPATTERNS['fields']
rx_list = [(field, re.compile('(' + pattern + r")\.*(:|])+[^\S\n]*(?P<val>.+?)\n", re.DOTALL))
            for (field, pattern) in pattern_dict.items()]


def search_rest_pattern(rest, rx):
    m = rx.search(rest, re.IGNORECASE)
    if m:
        return m.group('val')
    else:
        return ''


def generate_dict(path, sep):
    f = open(path, 'r', encoding="utf8")
    text = f.read()

    for match in rx_get_domain_date_rest.finditer(text):
        res_dict = {}
        domain, date, rest = match.groups()
        domain = domain.strip()
        rest = rest.replace(sep, '')

        error = get_error(rest)

        res_dict['domain'] = domain
        res_dict['date'] = date
        res_dict['error'] = error

        for field, rx in rx_list:
            if error != '':
                res = ''
            else:
                res = search_rest_pattern(rest, rx)
            res_dict[field] = res

        if error != '':
            provider = ''
        else:
            provider = get_provider(rest)

        res_dict['provider'] = provider
        res_dict['rest'] = rest
        yield res_dict
        
    f.close()


def main(path_in, path_out):

    sep = ','
    g =  generate_dict(path_in, sep)

    header = True
    with open(path_out, 'w', encoding="utf8", newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for d in g:
            if header:
                keys = d.keys()
                writer.writerow(keys)
                header = False
            values = d.values()
            writer.writerow(values)
         
if __name__ == "__main__":
    parser = argparse.ArgumentParser()   
    parser.add_argument('-i', '--input', default='Data/results_all.tsv')
    parser.add_argument('-o', '--output', default='output.csv')
    args = parser.parse_args()
    main(args.input, args.output)
