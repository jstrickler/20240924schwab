import lxml.etree as et

xml_doc = et.parse('DATA/solar.xml')  # ElementTree instance

for planet_tag in xml_doc.findall(".//planet"):
    print(planet_tag.get('planetname'))
    for moon in planet_tag.findall("moon"):
        print(f"    {moon.text}")
