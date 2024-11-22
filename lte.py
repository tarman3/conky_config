#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------- Импорт библиотек ---------------------------

import requests
import xml.etree.ElementTree as ET
import re

# ---------------------------- Параметры -------------------------------

url_api = 'http://192.168.9.1/api/device/signal'

output_len = 49
rsrp_low = -110
rsrq_low = -19
rssi_low = -80
sinr_low = 0

# ----------------------------- Сенарий --------------------------------

'''
RSSI
Received Signal Strength Indicator and is a measure of cellular signal strength.
RSSI is used when measuring the strength of 3G networks.

RSRP
Reference Signal Received Power, used when measuring 4G LTE networks
measured 0dBm (best signal) to -110dBm (weakest/no signal).
An RSRP of -95dBm would be a strong signal whereas -115dBm would be very weak.

RSRQ is Reference Signal Received Quality.
This again only applies to 4G LTE networks and is a measure of the signal quality of a cellular connection.
from 0dB (highest quality) to -20dB (lowest quality).

SINR
Signal to Interference-plus Noise Ratio
'''

def color(string, low_level):
    value = int(string.split('d')[0])
    if value < low_level:
        return f'${{color red}}{string}$color'
    else:
        return string

try:
    xml_data = requests.get(url_api, timeout=2).text
    tree = ET.XML(xml_data)
except Exception:
    tree = None
    print('LTE modem not responding')
    exit()

if tree is not None:
    cell_id = tree.find('cell_id').text[-3:]

    rsrp = tree.find('rsrp').text
    rsrp = rsrp.rjust(7)
    rsrq = tree.find('rsrq').text.replace('.0', '')
    rsrq = rsrq.rjust(5)
    rssi = tree.find('rssi').text
    rssi = rssi.rjust(7)
    sinr = tree.find('sinr').text
    sinr = sinr.rjust(4)
    signal = f'RSRP{rsrp}  RSRQ{rsrq}  RSSI{rssi}  SINR{sinr}'
    spaces = output_len - len(signal) - len(cell_id)

    rsrp = color(rsrp, rsrp_low)
    rsrq = color(rsrq, rsrq_low)
    rssi = color(rssi, rssi_low)
    sinr = color(sinr, sinr_low)
    signal = f'RSRP{rsrp}  RSRQ{rsrq}  RSSI{rssi}  SINR{sinr}'
    output = f'{signal}{' '*spaces} {cell_id}'
else:
    output = f'${{color red}}no cell$color'

print(output)
