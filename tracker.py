import os
import json
from datetime import datetime, timezone
from urllib.parse import quote
from urllib.request import Request, urlopen

PLAYER_TAG = '#G9UPL22PQ'


def main():
    token = os.getenv('COC_API_TOKEN')
    if not token:
        raise SystemExit('Set COC_API_TOKEN before running')
    url = 'https://api.clashofclans.com/v1/players/' + quote(PLAYER_TAG, safe='')
    request = Request(url, headers={'Authorization': 'Bearer ' + token})
    with urlopen(request, timeout=20) as response:
        player = json.load(response)
    with open('player_latest.json', 'w', encoding='utf-8') as output:
        json.dump({'fetched_at': datetime.now(timezone.utc).isoformat(), 'player': player}, output, indent=2)
    print('Fetched player:', player.get('name'))


if __name__ == '__main__':
    main()
