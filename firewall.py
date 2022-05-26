import subprocess


def block_ip(malADDR): # malADDR wil be the address which is found to send a malicious address
    cmd = 'iptables'
    try:
        blacklist = subprocess.Popen([cmd, '-A', 'INPUT', '-s', malADDR, '-j' 'DROP'], stdout = subprocess.PIPE)
        # everything between the [] is the command used to block the ip

        print(r'Successfully blocked the address: {}.'.format(malADDR))

    except:
        print('Were not able to block the address')
        # if any error occurs, this message will be displayed



