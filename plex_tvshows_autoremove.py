import os, datetime
from plexapi.server import PlexServer
plex = PlexServer()
keep = []
simFiles = ['.srt', '.nfo', '.tbn', '.nzb', '.nfo-orig', '.sfv', '.srr', '.jpg', '.png', '.jpeg', '.txt', '.idx', '.sub']
kept=0
deleted=0
print '-----------------------------------------------'
print 'Running Plex Cleaner on '+datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')
print ''
for entry in plex.library.section('TV Shows').recentlyViewed():
    tvFile = entry.media[0].parts[0].file
    if entry.grandparentTitle not in keep:
        if entry not in plex.library.onDeck():
            print 'Deleting '+entry.title+' ::: '+tvFile
            deleted += 1
            os.remove(tvFile)
            for sim in simFiles:
                simFile = os.path.splitext(tvFile)[0]+sim
                if os.path.isfile(simFile):
                    print '::: Deleting it\'s similar file too ::: '+simFile
                    os.remove(simFile)
    else:
        kept += 1
print ''
print str(kept) + ' Episodes Kept'
print str(deleted) + ' Episodes Deleted'