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
def calculateFee():
    cmd = "cardano-cli shelley  query tip "+Network
    res=sendCmdtoShell(cmd)
    res = str(res)
    regex = r"\{unSlotNo = [0-9]+}"

    matches1 = re.finditer(regex, res, re.MULTILINE)

    return matches1

test=(calculateFee())
print(test)
