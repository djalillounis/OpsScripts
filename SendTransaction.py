#!/usr/bin/env python

import os
import re


#---------------Global Variables-----------------


Network = "--testnet-magic 42"

#------------------------------------------------

#----------------Functions----------------------


def sendCmdtoShell(cmd):
    res = os.system(cmd)
    return res

#local currentTip=$(${cardanocli} shelley query tip ${magicparam} | awk 'match($0,/unSlotNo = [0-9]+/) {print substr($0, RSTART+11,RLENGTH-11)}')
def currentSlot():
    cmd = "cardano-cli shelley  query tip "+Network
    res=sendCmdtoShell(cmd)
    #res= "Tip (SlotNo {unSlotNo = 579641}) (ShelleyHash {unShelleyHash = HashHeader {unHashHeader = 4c18abf6f6916872f1128575c2be88b5daac6c946b5fce26b883646164f0716a}}) (BlockNo {unBlockNo = 26720})"
    res = str(res)
    regex = r"\{unSlotNo = [0-9]+}"
    reg= re.compile(regex)

    CurrentSlot = reg.findall(res)
    if CurrentSlot:
       CurrentSlot = CurrentSlot[0]
       CurrentSlot =CurrentSlot.replace('}','')
       CurrentSlot =CurrentSlot.replace('{','')
       CurrentSlot =CurrentSlot.split("=")
       if CurrentSlot:
         CurrentSlot=CurrentSlot[1]
         CurrentSlot =CurrentSlot.replace(' ','')
         CurrentSlot =CurrentSlot.replace(' ','')




    else:
       CurrentSlot=0000





    return CurrentSlot

test=(currentSlot())

print (test)
