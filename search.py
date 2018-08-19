#!/usr/bin/env python3
import requests
import sys
from terminaltables import AsciiTable
from datetime import datetime

default_limit = 3
if len(sys.argv) == 3:
    default_limit = sys.argv[2]

data = requests.get('https://portal.mnemonic.no/web/api/pdns/v3/{0}?limit={1}'.format(sys.argv[1], default_limit)).json()

pdns_table = data['data']


table_data = [
    ['Type', 'Query', 'Answer', 'First', 'Last', 'Count'],
]

for result in data['data']:

	last = datetime.fromtimestamp(int(result['firstSeenTimestamp']) / 1000).strftime('%d.%m.%Y %H:%M')
	first = datetime.fromtimestamp(int(result['lastSeenTimestamp']) / 1000).strftime('%d.%m.%Y %H:%M')
	table_data.append([result['rrtype'], result['query'], result['answer'], first, last, result['times']])

table = AsciiTable(table_data)
print(table.table)