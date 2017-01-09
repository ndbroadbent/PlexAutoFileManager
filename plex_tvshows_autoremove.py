#!/usr/bin/env python2
import os, sys, datetime
from plexapi.server import PlexServer
from plexapi.myplex import MyPlexAccount

account = MyPlexAccount.signin('****', '*****')
#plex = PlexServer()
plex = account.resource('****').connect()

keep = []
simFiles = ['.srt', '.nfo', '.tbn', '.nzb', '.nfo-orig', '.sfv', '.srr', '.jpg', '.png', '.jpeg', '.txt', '.idx', '.sub']
kept=0
deleted=0
print '-----------------------------------------------'
print 'Running Plex Cleaner on '+datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
print ''

section = plex.library.section('TV Shows')
recentlyViewed = section.search(sort='lastViewedAt:desc', libtype='episode', maxresults=100)

for entry in recentlyViewed:
    tvFile = entry.media[0].parts[0].file
    if entry.grandparentTitle not in keep:
        if entry not in plex.library.onDeck():
        if os.path.isfile(tvFile):
                print 'Deleting '+entry.grandparentTitle+' - '+entry.title+' ::: '+tvFile
                deleted += 1
                os.remove(tvFile)
            for sim in simFiles:
                simFile = os.path.splitext(tvFile)[0]+sim
                if os.path.isfile(simFile):
                    print '::: Deleting similar file too ::: '+simFile
                    os.remove(simFile)
    else:
        kept += 1

print ''
print str(kept) + ' Episodes Kept'
print str(deleted) + ' Episodes Deleted'
