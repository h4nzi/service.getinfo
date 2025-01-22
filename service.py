# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui

addon = xbmcaddon.Addon()
addonName = addon.getAddonInfo('name')

# Name of the properties
PLAYED = 'played_stream'
DOWNLOADED= 'downloaded_server'

def logInfo(text, addon = addonName):
    xbmc.log('[{}] {}'.format(addon,text), xbmc.LOGINFO)

def setProperty(variable, value, window = 10000):
    xbmcgui.Window(window).setProperty(variable, value)

def clearProperty(variable, window = 10000):
    xbmcgui.Window(window).clearProperty(variable)

def clearProperties(variables, window = 10000):
    for variable in variables:
        clearProperty(variable, window)

if __name__ == '__main__':
    logInfo('Start service')
    clearProperties({PLAYED, DOWNLOADED})
    monitor = xbmc.Monitor()    

    while not monitor.abortRequested():
        if monitor.waitForAbort(5):
            break
        if xbmc.getCondVisibility('Player.HasVideo'): #pokud má player video
            stream = xbmc.Player().getPlayingFile() #získej informace o streamu
            if stream != lastStream:
                setProperty(PLAYED, stream)
                logInfo('Played stream: {}'.format(stream))
                parsedAddress = stream.split('/')
                setProperty(DOWNLOADED, parsedAddress[2])
                logInfo('Downloaded server: {}'.format(parsedAddress[2]))
                lastStream = stream
        else:
            lastStream = ''
            clearProperties({PLAYED, DOWNLOADED})

    clearProperties({PLAYED, DOWNLOADED})
    logInfo('Stop service')

        