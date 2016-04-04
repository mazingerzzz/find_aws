#!/usr/bin/env python

import boto.ec2
import boto.ec2.elb
import re
import argparse

# Global Vars
aws_profile = ""
result = {}
inst_ko = []
elb_arg = ""

# Args
parser = argparse.ArgumentParser()
parser.add_argument("--profile")
parser.add_argument("search", nargs="?", default="")
args = parser.parse_args()
if args.profile:
    aws_profile = str(args.profile)
if args.search:
    elb_arg = str(args.search)

# Connect
try:
    conn = boto.ec2.connect_to_region("eu-west-1", profile_name=aws_profile)
    elb = boto.ec2.elb.connect_to_region("eu-west-1", profile_name=aws_profile)
    my_instances = conn.get_all_instances()
    # print "--profile " + aws_profile
except:
    print "Use Default Profile"
    conn = boto.ec2.connect_to_region("eu-west-1")
    elb = boto.ec2.elb.connect_to_region("eu-west-1")
    my_instances = conn.get_all_instances()


class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def find_inst_ip(inst_id):
    for res in my_instances:
        for inst in res.instances:
            if inst_id in str(inst):
                if inst_id in str(inst_ko):
                    return bcolors.RED + str(inst.private_ip_address) + bcolors.ENDC
                else:
                    return inst.private_ip_address


def find_elb(my_tag):
    n = ""
    all_elb = elb.get_all_load_balancers()
    for my_elb in all_elb:
        if re.search(my_tag, str(my_elb), re.IGNORECASE):
            result[my_elb] = []
            inst_health = my_elb.get_instance_health()
            for i in inst_health:
                if re.search("InService", str(i)):
                    n = re.search('[a-z]\-([a-z]|[0-9])*', str(i))
                    result[my_elb].append(n.group(0))
                else:
                    n = re.search('[a-z]\-([a-z]|[0-9])*', str(i))
                    inst_ko.append(n.group(0))
                    result[my_elb].append(n.group(0))
    if result == {} and inst_ko == []:
        print bcolors.RED + "Pas d'ELB correspondant" + bcolors.ENDC


def print_result():
    i = 0
    for k, v in result.iteritems():
        print bcolors.BLUE + str(k) + bcolors.ENDC
        for i in v:
            print bcolors.GREEN + str(find_inst_ip(i)) + bcolors.ENDC,
        print "\n"


def main():
    find_elb(elb_arg)
    print_result()


if __name__ == "__main__":
    main()
