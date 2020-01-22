#!/usr/bin/env python3

pv = input('Physical Volume: ')
vg = input('Volume Group: ')
lv = input('Logical Volume(s): ')
gb = input('Size in GBs: ')

# Determine of single entry or comma separated list
if pv.find(',') != -1:
    # If comma separated list split string into list
    pv = pv.split(',')
    for i in range(len(pv)):
        print('pvcreate /dev/' + pv[i])
        if i == 0:
            print('vgcreate ' + vg + ' /dev/' + pv[i])
        else:
            print('vgextend ' + vg + ' /dev/' + pv[i])
else:
    print('pvcreate /dev/' + pv)
    print('vgcreate ' + vg + ' /dev/' + pv)

if lv.find(',') != -1:
    lv = lv.split (',')
    gb = gb.split (',')

    for i in range(len(lv)):
        if i < (len(lv) - 1):
            print('lvcreate -L ' + str(gb[i]) + 'G -n ' + lv[i] + ' ' + vg)
        else:
            print('lvcreate -l +100%FREE -n ' + lv[i] + ' ' + vg)
else:
    print('lvcreate -l +100%FREE -n ' + lv + ' ' + vg)

print('for i in /dev/' + vg + '/*; do mkfs.ext4 -m 0 $i; done')
