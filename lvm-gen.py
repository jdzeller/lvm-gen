#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Spit out custom LVM commands.')
parser.add_argument('-pv', metavar='Physical Volume', dest='pv', help='name of physical volume to create')
parser.add_argument('-vg', metavar='Volume Group', dest='vg', help='name of volume group')
parser.add_argument('-lv', metavar='Logical Volume', dest='lv', help='name of volume group')
parser.add_argument('-gb', metavar='Size in GB', dest='gb', help='size in GB')
args = parser.parse_args()

def create_pv(pv):
    print('pvcreate /dev/' + pv)

def create_vg(vg, pv):
    print('vgcreate ' + vg + 'vg /dev/' + pv)

def create_lv(lv, gb, vg):
    lvs = lv.split (",")
    gbs = gb.split (",")
    for i in range(0, len(lvs)):
        if i <= (len(lvs) - 2):
            print('lvcreate -L ' + str(gbs[i]) + 'G -n ' + lvs[i] + 'lv ' + vg + 'vg')
        else:
            print('lvcreate -l +100%FREE -n ' + lvs[i] + 'lv ' + vg + 'vg')
            
create_pv(args.pv)
create_vg(args.vg, args.pv)
create_lv(args.lv, args.gb, args.vg)