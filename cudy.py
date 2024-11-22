#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url_api = 'https://support.cudy.com/emulator/LT500-Outdoor/cgi-bin/luci/admin/network/gcom/status/detail/1/iface/4g'

data = requests.get(url_api, timeout=2).text
soup = BeautifulSoup(data, 'html.parser')

cell_id = soup.find(id="cbi-table-13-data").find('p','visible-xs').string.strip()
band = soup.find(id="cbi-table-15-data").find('p','visible-xs').string.strip()
rsrp = soup.find(id="cbi-table-18-data").find('p','visible-xs').string.strip()
rsrq = soup.find(id="cbi-table-19-data").find('p','visible-xs').string.strip()
rssi = soup.find(id="cbi-table-3-data").find('p','visible-xs').string.strip()
sinr = soup.find(id="cbi-table-20-data").find('p','visible-xs').string.strip()

print(f'cell {cell_id}  band {band}  RSRP {rsrp}dBm  RSRQ {rsrq}dB  RSSI {rssi}dBm  SINR {sinr}dB')
