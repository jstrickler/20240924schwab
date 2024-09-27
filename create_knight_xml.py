import lxml.etree as et

root = et.Element("knights")


with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_tag = et.SubElement(root, "knight", title=title)
        name_tag = et.SubElement(knight_tag, "name")
        name_tag.text = name
        et.SubElement(knight_tag, "color").text = color
        et.SubElement(knight_tag, "quest").text = quest
        et.SubElement(knight_tag, "comment").text = comment
        

raw_xml = et.tostring(root, pretty_print=True, xml_declaration=True)
xml = raw_xml.decode()
print(xml)

doc = et.ElementTree(root)
doc.write('knights.xml', pretty_print=True, xml_declaration=True)
