#!/usr/bin/env python

import os, datetime
from plexapi.server import PlexServer
plex = PlexServer()
""" Todo: Change to directive """
trialRun = 1 # Testing purposes. Use 1 for normal use. Set to 0 for debugging/testing runs that don't delete anything.
""" Todo: move to its own separate setting.cfg file """
doTV=1 # default action. Use 1 for deleting; use 0 for keeping TV Shows, all but those in skipTV[]
skipTV = []
doSim=1 # Use 1 for deleting similar files with the extensions on simFiles[]; use 0 to avoid deleting them.
simFiles = ['.srt', '.nfo', '.tbn', '.nzb', '.nfo-orig', '.sfv', '.srr', '.jpg', '.png', '.jpeg', '.txt', '.idx', '.sub']
kept=0
deleted=0
delSim=0
print '-----------------------------------------------'
print 'Running Plex Cleaner on '+datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
print ''
for entry in plex.library.section('TV Shows').recentlyViewed():
    tvFile = entry.media[0].parts[0].file
    """ (bool(doTV) is not bool(entry.grandparentTitle in skipTV) is a logic XOR, in Python
        as far as I know there is no logic operand to do XOR (only bitwise xor ^)
        It can be written using the bitwise xor operand (bool(doTV) ^ bool(entry.grandparentTitle in skipTV) """ 
    if (bool(doTV) is not bool(entry.grandparentTitle in skipTV)) and entry not in plex.library.onDeck():
        print 'Deleting '+entry.title+' ::: '+tvFile
        deleted += 1
        if trialRun: os.remove(tvFile)
        if doSim:
            for sim in simFiles:
                simFile = os.path.splitext(tvFile)[0]+sim
                if os.path.isfile(simFile):
                    print '::: Deleting it\'s similar file too ::: '+simFile
                    delSim += 1
                    if trialRun: os.remove(simFile)
    else:
        kept += 1
print ''
print str(kept) + ' Episodes Kept'
print str(deleted) + ' Episodes Deleted'
print str(delSim) + ' Related Files Deleted'
