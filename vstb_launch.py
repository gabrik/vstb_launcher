#!/usr/bin/env python3
import libvirt

##
##  vstb_launch.py
##  EU INPUT 
##
##  Created by Gabriele Baldoni on 28/10/2017
##  Copyright (c) 2017 Gabriele Baldoni. All rights reserved.
##

class VSTB(object):
    '''
     This class define, start, and then destroy and undefine the vSTB VMs
    '''
    def __init__(self, base_path, domains):
        self.base_path = base_path
        self.conn = libvirt.open("qemu:///system")
        self.domains = domains

    def define_domans(self):
        '''
        This methods load the proper xml file for each domain and then define the domain
        '''
        for d in self.domains:
            path = str("%s/%s/%s.xml" % (self.base_path, d, d))
            vm_xml = self.read_file(path)
            self.conn.defineXML(vm_xml)

    def launch_domains(self):
        '''
        This method start each domain
        '''
        for d in self.domains:
            dom = self.conn.lookupByName(d)
            dom.create()

    def stop_domains(self):
        '''
        This method stop each domain (stop means that the vm is destroyed)
        '''
        for d in self.domains:
            dom = self.conn.lookupByName(d)
            dom.destroy()

    def undefine_domains(self):
        '''
        This method undefine each domain
        '''
        for d in self.domains:
            dom = self.conn.lookupByName(d)
            dom.undefine()

    def read_file(self, file_path):
        '''
        This method read a file from the filesystem
        '''
        data = ""
        with open(file_path, 'r') as data_file:
            data = data_file.read()
        return data


if __name__ == '__main__':
    print("########################################")
    print("######      vSTB VM Launcher      ######")
    print("########################################")
    images_path = "/home/ubuntu/Scrivania/images"
    components = ['es','ea','cp','pa','dms','dmc','vdi']
    vstb = VSTB(images_path, components)

    print(">>>> Defining Domains...            <<<<")
    vstb.define_domans()
    print(">>>> [ DONE ] Defining Domains      <<<<")

    print(">>>> Starting Domains...            <<<<")
    vstb.launch_domains()
    print(">>>> [ DONE ] Starting Domains      <<<<")

    print("########################################")
    print("#####          vSTB Running        #####")
    print("########################################")

    input("<<<< Press enter to stop the vSTB   >>>>")

    print(">>>> Stopping Domains...            <<<<")
    vstb.stop_domains()
    print(">>>> [ DONE ] Stopping Domains      <<<<")

    print(">>>> Undefining Domains...          <<<<")
    vstb.undefine_domains()
    print(">>>> [ DONE ] Undefining Domains    <<<<")

    print("########################################")
    print("#####          vSTB Stopped        #####")
    print("########################################")

    print(">>>> Bye <<<<")







