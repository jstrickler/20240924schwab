import lxml.etree as et

xml_doc = et.parse('DATA/solar.xml')

print(f"{xml_doc = }")

root = xml_doc.getroot()
print(f"{root = }")

for child_tag in root:
    for tag in child_tag:
        if tag.tag == 'planet':
            print(tag.get('planetname'))
            for moon in tag:
                print(f"    {moon.text}")
