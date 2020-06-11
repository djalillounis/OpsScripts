#!/usr/bin/env python

import os
import re
import subprocess
import time
import datetime

#---------------Global Variables-----------------


Network = "--testnet-magic 42"

#------------------------------------------------

#----------------Functions----------------------


def sendCmdtoShell(cmd):
    result = subprocess.run([cmd], stdout=subprocess.PIPE,shell=True)
    res = result.stdout
    res = str(res)
    return res


def protocolParms(Network):

    datetime.datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
    fileName = datetime.datetime.now().strftime('%y-%m-%d %a %H:%M:%S')
    fileName = str(fileName)
    fileName = fileName+".json"

    outFile = "--out-file " + fileName
    cmd="cardano-cli shelley query protocol-parameters"+Network+outFile
    sendCmdtoShell(cmd)
    Print ("Parm  File Created : " + )


def currentSlot():
    cmd = "cardano-cli shelley  query tip "+Network
    res=sendCmdtoShell(cmd)
    res = str(res)
    print(res)
    regex = r"\{unSlotNo = [0-9]+}"
    reg= re.compile(regex)

    CurrentSlot = reg.findall(res)
    print(CurrentSlot)
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
#---------------Calculate Fee---------------------------------
def calcultaFee(type,CurrentSlot,Network,signingKeyFile):

    txOutCount =0
    if type="Self":
        txOutCount =1
    else:
        txOutCount =2
    txInCount = 1
    tx-in-count = "--tx-in-count "+txInCount
    tx-out-count = "--tx-out-count "+txOutCount
    ttl = "--ttl "+CurrentSlot
    igning-key-file ="--signing-key-file "+signingKeyFile




    cmd = "cardano-cli shelley transaction calculate-min-fee"





protocolParms(Network)
