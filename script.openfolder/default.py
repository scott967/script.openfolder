import os
import xbmc, xbmcvfs

moviepath = xbmcvfs.makeLegalFilename(xbmc.getInfoLabel('ListItem.Path '))
os.startfile(moviepath)
