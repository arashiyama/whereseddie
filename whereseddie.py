#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Released as a service to the information security community and police worldwide.

import os.path
import sqlite3
import time
import datetime

# Where you have stored your location consolidated.db
database = sqlite3.connect('/home/jhc/loc.db')
# Set this to whatever makes sense for you
file = '/home/jhc/dec-10.kml'


# Because Mac and iOS computers use a different epoch start date, this offset changes between MAC and UNIX (python) formats
offset = 978307200.0
# Unix Epoch date for 1st November 2010
firstnov = 1288569600
firstdec = 1291161600

start = firstdec - offset


# Do something here to select on date.
pois = database.execute("SELECT * FROM CellLocation WHERE Timestamp> %i" % start).fetchall()
wifis = database.execute("SELECT * FROM WifiLocation WHERE Timestamp > %i" % start).fetchall()
compasses = database.execute("SELECT * FROM CompassSettings").fetchall()
database.close()

# Set this to whatever makes sense for you
file = '/home/jhc/dec-10.kml'
FILE = open(file,'w')
FILE.truncate(0)

FILE.write('<?xml version="1.0" encoding="iso-8859-1"?>\n')
FILE.write('<kml xmlns="http://www.opengis.net/kml/2.2">\n')
# Add some styles

FILE.write('\t<Document>\n')
FILE.write('\t<name>iPhone location map</name>\n')
FILE.write('\t<description>Created by Jonathan Care http://www.lacunae.org</description>\n')
FILE.write('   <Style id="downArrowIcon">\n')
FILE.write('      <IconStyle>\n')
FILE.write('        <Icon>\n')
FILE.write('          <href>http://maps.google.com/mapfiles/kml/pal4/icon28.png</href>\n')
FILE.write('        </Icon>\n')
FILE.write('      </IconStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="globeIcon">\n')
FILE.write('      <IconStyle>\n')
FILE.write('        <Icon>\n')
FILE.write('          <href>http://maps.google.com/mapfiles/kml/pal3/icon19.png</href>\n')
FILE.write('        </Icon>\n')
FILE.write('      </IconStyle>\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <width>2</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="transPurpleLineGreenPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <color>7fff00ff</color>\n')
FILE.write('        <width>4</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7f00ff00</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="yellowLineGreenPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <color>7f00ffff</color>\n')
FILE.write('        <width>4</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7f00ff00</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="thickBlackLine">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <color>87000000</color>\n')
FILE.write('        <width>10</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="redLineBluePoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <color>ff0000ff</color>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>ffff0000</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="blueLineRedPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <color>ffff0000</color>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>ff0000ff</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="transRedPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <width>1.5</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7d0000ff</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="transBluePoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <width>1.5</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7dff0000</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="transGreenPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <width>1.5</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7d00ff00</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="transYellowPoly">\n')
FILE.write('      <LineStyle>\n')
FILE.write('        <width>1.5</width>\n')
FILE.write('      </LineStyle>\n')
FILE.write('      <PolyStyle>\n')
FILE.write('        <color>7d00ffff</color>\n')
FILE.write('      </PolyStyle>\n')
FILE.write('    </Style>\n')
FILE.write('    <Style id="noDrivingDirections">\n')
FILE.write('      <BalloonStyle>\n')
FILE.write('        <text><![CDATA[\n')
FILE.write('          <b>$[name]</b>\n')
FILE.write('          <br /><br />\n')
FILE.write('          $[description]\n')
FILE.write('        ]]></text>\n')
FILE.write('      </BalloonStyle>\n')
FILE.write('    </Style>\n')
# End of styles

#
FILE.write('\t\t<Folder>\n')
FILE.write('\t\t\t<name>GSM Locations</name>\n')
FILE.write('\t\t\t<description>Datadump of GPS derived from GSM location</description>\n')

i = 1
for poi in pois:
#   print '%s : %f, %f' % (poi, poi[2],poi[1],)
#    print datetime.datetime.utcfromtimestamp(poi[4]+offset).ctime()
#    print '%f, %f' % (poi[5],poi[6],)
    FILE.write('\t\t\t<Placemark>\n')
    #FILE.write('\t\t\t\t<name>Lat: %f Lon: %f</name>\n' % (poi[5],poi[6],))
    tmpdate = datetime.datetime.utcfromtimestamp(poi[4]+offset).ctime()
    FILE.write('\t\t\t\t<name>GSM DATE: %s</name>\n' % tmpdate,)
    FILE.write('\t\t\t\t<description><![CDATA[Lat: %f Lon: %f<br>]]></description>\n' % (poi[5],poi[6],))
    FILE.write('\t\t\t\t<Point>\n')
    FILE.write('\t\t\t\t\t<coordinates>%f,%f,0</coordinates>\n' % (poi[6],poi[5],))
    FILE.write('\t\t\t\t</Point>\n')
    FILE.write('\t\t\t</Placemark>\n')
    i = i + 1

FILE.write('\t\t</Folder>\n')
i = 1
FILE.write('\t\t<Folder>\n')
FILE.write('\t\t<name>WiFi Hotspot location</name>\n')
FILE.write('\t\t<description>Locations of WiFI hotspots connected to (with MAC address)</description>\n')
for wifi in wifis:
    FILE.write('\t\t\t<Placemark>\n')
    #FILE.write('\t\t\t<name>Lat: %f Lon: %f</name>\n' % (wifi[2], wifi[3],))
    tmpdate = datetime.datetime.utcfromtimestamp(wifi[1]+offset).ctime()    
    FILE.write('\t\t\t<name>WIFI Date: %s</name>\n' % (tmpdate,))
    FILE.write('\t\t\t\t<description><![CDATA[MAC: %s<br>Lat: %f Lon: %f<br>]]></description>\n' % (wifi[0],wifi[2], wifi[3],))
    FILE.write('\t\t\t\t<Point>\n')
    FILE.write('\t\t\t\t\t<coordinates>%f,%f,0</coordinates>\n' % (wifi[3],wifi[2],))
    FILE.write('\t\t\t\t</Point>\n')
    FILE.write('\t\t\t</Placemark>\n')
    i = i + 1
FILE.write('\t\t</Folder>\n')

#i = 1
#FILE.write('\t\t<Folder>\n')
#FILE.write('\t\t<name>Compass Settings</name>')
#FILE.write('\t\t<description>Locations of Compass Settings logged')
#for compass in compasses:
#    FILE.write('\t\t\t<Placemark>\n')
#    FILE.write('\t\t\t<name>Compass Setting %i</name>\n' % i)
#    tmpdate = datetime.datetime.utcfromtimestamp(compass[0]+offset).ctime()
#    FILE.write('\t\t\t\t<description><![CDATA[Lat: %f <br> Lon: %f Height: %f<br>%s<br>]]></description>\n' % (compass[1],compass[2],compass[3],tmpdate,))
#    FILE.write('\t\t\t\t<Point>\n')
#    FILE.write('\t\t\t\t\t<coordinates>%f,%f,%f</coordinates>\n' % (compass[2],compass[1],compass[3],))
#    FILE.write('\t\t\t\t</Point>\n')
#    FILE.write('\t\t\t</Placemark>\n')
#    i = i + 1
#
#FILE.write('\t\t</Folder>\n')
FILE.write('\t</Document>\n')
FILE.write('</kml>\n')
FILE.close()
