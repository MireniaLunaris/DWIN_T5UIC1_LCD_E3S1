#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (19, 26)
button_Pin = 13
LCD_COM_Port = '/dev/serial0'
API_Key = '3aea6d5b054346ebafadc3ed31d20852'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)