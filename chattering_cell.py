#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:27:15 2021

@author: shreyp22
"""

import izhikevich_cells as izh

class chatcell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        """ new constants for equation """
        self.C=50
        self.vr=-60
        self.vt=-40
        self.k=1.5
        self.a=0.03
        self.b=1
        self.c=-40
        self.d=150
        self.vpeak=25
        self.stimVal = stimVal
        
def createCell():
    """ running the simulation and plotting the data """
    myCell = chatcell(stimVal=4000)
    myCell.simulate()
    izh.plotMyData(myCell)
    
if __name__=="__main__":
    createCell()