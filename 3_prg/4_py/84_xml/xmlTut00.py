#!/usr/bin/env python3

# gotten from
# https://stackoverflow.com/questions/26434998/parsing-compressed-xml-feed-into-elementtree
#

import xml.etree.ElementTree as etree
from gzip import GzipFile
from urllib.request import urlopen, Request

with urlopen(Request("http://smarkets.s3.amazonaws.com/oddsfeed.xml",
                     headers={"Accept-Encoding": "gzip"})) as response, \
     GzipFile(fileobj=response) as xml_file:
    for elem in getelements(xml_file, 'interesting_tag'):
        process(elem)
        
def getelements(filename_or_file, tag):
    """Yield *tag* elements from *filename_or_file* xml incrementally."""
    context = iter(etree.iterparse(filename_or_file, events=('start', 'end')))
    _, root = next(context) # get root element
    for event, elem in context:
        if event == 'end' and elem.tag == tag:
            yield elem
            root.clear() # free memory