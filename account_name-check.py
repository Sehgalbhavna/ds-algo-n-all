
def checkAccount_name(account_name):
    if (account_name.upper()).find('MAKS') > 0:
        print('MAKS: ' +account_name)
    elif (account_name.upper()).find('REIS') > 0:
       print('REIS :' +account_name)
    elif (account_name.upper()).find('SBX') > 0:
        print('SBX: ' +account_name)
    elif (account_name.upper()).find('ENCAP') > 0:
        print('ENCAP:' +account_name)
    elif (account_name.upper()).find('ENCP') > 0:
        print('ENCP:' +account_name)
    elif (account_name.upper()).find('SANDBOX') > 0:
        print('SANDBOX:' +account_name)
    # elif (account_name.upper()).find('_PRD') > 0:
    #     return ami_list_prd
    # elif (account_name.upper()).find('_NPRD') > 0:
    #     return ami_list_nprd
    else:
        print("*****")
    
checkAccount_name("AWS_MA_CPG_OMNIENCAP_PRD")