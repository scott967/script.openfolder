import os
import xbmc, xbmcvfs, xbmcgui

try:
    moviepath = xbmcvfs.makeLegalFilename(xbmc.getInfoLabel('ListItem.Path'))
    if moviepath.startswith('smb:'):
        moviepath = moviepath[4:].replace('/','\\')
    os.startfile(moviepath)
except:
    xbmcgui.Dialog().notification('ADDON:context.openfolder2', 
                                  'Unable to open folder', xbmcgui.NOTIFICATION_ERROR)
