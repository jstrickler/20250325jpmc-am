# import xml.etree.ElementTree as ET
import lxml.etree as ET

doc = ET.parse('../DATA/solar.xml')  # parse XML file

inner_nodes = doc.findall('innerplanets/planet')  # find all elements (relative to root element) with tag "planet" under "innerplanets" element

outer_nodes = doc.findall('outerplanets/planet')  # find all elements with tag "planet" under "outerplanets" element

print('Inner:')
for planet in inner_nodes:  # loop through search results
    print('\t', planet.get("planetname"))  # print "name" attribute of planet element

print('Outer:')
for planet in outer_nodes:  # loop through search results
    print('\t', planet.get("planetname"))  # print "name" attribute of planet element
