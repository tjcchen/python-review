#
# parsing and processing XML
#

import xml.dom.minidom

def main():
    # use the parse() function to load and parse an XML file
    doc = xml.dom.minidom.parse("samplexml.xml")
    
    # print out the document node and the name of the first child tag
    print(doc.nodeName)           # #document
    print(doc.firstChild.tagName) # person
    
    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print(skills.length, "skills are listed")   # 4 skills are listed

    for skill in skills:
        print(skill.getAttribute("name"))       # JavaScript, Python, C#, HTML
        
    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "Go")
    doc.firstChild.appendChild(newSkill)
    
    skills = doc.getElementsByTagName("skill")
    print(skills.length, "skills are listed")   # 5 skills are listed
    for skill in skills:
        print(skill.getAttribute("name"))       # JavaScript, Python, C#, HTML, Go

if __name__ == "__main__":
    main()
