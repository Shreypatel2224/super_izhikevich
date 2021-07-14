#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:23:59 2021

@author: shreyp22
"""

import izhikevich_cells as izh

class ibcell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        """ new constants for equation """
        self.C=150
        self.vr=-75
        self.vt=-45
        self.k=1.2
        self.a=0.01
        self.b=5
        self.c=-56
        self.d=130
        self.vpeak=50
        self.stimVal = stimVal
        
def createCell():
    """ running the simulation and plotting the data """
    myCell = ibcell(stimVal=4000)
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=="__main__":
    createCell()
    
