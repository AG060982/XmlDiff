import sys
import time
from collections import Counter
import xml.etree.ElementTree as ET
from xml.dom import minidom

startTime=time.time()
file1="D:\\Python\\sample.xml"
file2="D:\\Python\\output.xml"

def get_xpath(root,xpath,xpath_list):
    tag=root.tag.strip()
    xpath.append(tag)
    attribute=root.attrib
    value=root.attrib.get('name', root.text)
    xpath_str='/'.join(str(e) for e in xpath)
    if value:
        value=value.strip()
    if value:
        line='<' +str(tag)+ '>/' + xpath_str + ':' + value + '</' +str(tag) + '>'
        xpath_list.append(line)
    for elem in root.getchildren():
        get_xpath(elem,xpath,xpath_list)
    xpath.pop()

def parse_xml(file):
    xpath=[]
    xpath_list=[]
    with open(file) as f:
            file = (''.join([line.strip() for line in f]))
    #print(file)
    #tree=ET.parse(file)
    #root=tree.getroot()
    root = ET.fromstring(file)
    get_xpath(root,xpath,xpath_list)
    lines=Counter(xpath_list)
    return lines


file1_path=parse_xml(file1)
#print(file1_path)
file2_path=parse_xml(file2)

diff1=file1_path-file2_path
diff2=file2_path-file1_path

print("below Values in file1 are diffrent/extra to file2")
print(sorted(list(diff1.elements())))

print('='*100)


print("below Values in file2 are diffrent/extra to file1")
print(sorted(list(diff2.elements())))

print('------')

print('The script took {0} seconds for diff !'.format(time.time()-startTime))




