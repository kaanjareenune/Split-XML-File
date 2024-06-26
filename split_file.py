import xml.etree.ElementTree as ET
def writeTagsToFile(new_root, elementList, fileName):
    for element in elementList:
        new_root.append(element)
    new_tree = ET.ElementTree(new_root)
    new_tree.write(fileName)

def main():

    #inputs
    fileNamePrefix = "tags"
    noOfTagsPerFile = 10

    #parse the xml file
    tree = ET.parse(fileNamePrefix+".xml")
    root = tree.getroot()
    for child in root:
        child_tag = child.tag

    elementList = []
    fileNameSuffix = 1
    tags_current_file = 0

    for element in tree.iter():
        if(element.tag == child_tag):
            elementList.append(element)
            tags_current_file += 1
            if(tags_current_file >= noOfTagsPerFile):
                writeTagsToFile(ET.Element(root.tag),elementList,fileNamePrefix+"_"+str(fileNameSuffix)+".xml")
                tags_current_file = 0
                elementList = []
                fileNameSuffix += 1
    if(tags_current_file > 0 and tags_current_file < noOfTagsPerFile):
        writeTagsToFile(ET.Element(root.tag),elementList,fileNamePrefix+"_"+str(fileNameSuffix)+".xml")

if __name__ == "__main__":
    main()