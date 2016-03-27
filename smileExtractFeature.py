# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:05:35 2016

@author: Nagaraja
"""

#TODO features extraction using OPENSMILE

#TODO COnvert mp3 to wav files
#TODO Read/Create inpput directory
#TODO Execute the SMILEEXtract command on the input files
#TODO Make&Copy the files into target folder


from pydub import AudioSegment;

from glob import glob
from pydub import AudioSegment
import os

os.chdir('input\\angry\\');

for mp3_file in list(glob("*.mp3")):

    song = open(mp3_file,"rb")
    print(song);
    AudioSegment.from_file(song,format="wav").export(song.name, format='wav')
   