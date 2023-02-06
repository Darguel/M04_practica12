import xml.etree.ElementTree as ET

def crearxml():
    p = ET.Element ('students')

    a = ET.SubElement(p, 'student')
    b = ET.SubElement(p, 'student')
    c = ET.SubElement(p, 'student')
    d = ET.SubElement(p, 'student')
    e = ET.SubElement(p, 'student')

    tree = ET.ElementTree(p)
    tree.write("students.xml")

    tree = ET.parse('students.xml')
    root = tree.getroot()
    
    ET.dump(p)
    element = root[0]
    element.set('name', 'David')
    element.set('surname', 'arguelles')
    element.set('email', 'David20@gmail.com')
    element.set('dni', '35154215X')

    element = root[1]
    element.set('name', 'Luis')
    element.set('surname', 'Cornejo')
    element.set('email', 'Luidd20@gmail.com')
    element.set('dni', '35154215X')

    element = root[2]
    element.set('name', 'Carlos')
    element.set('surname', 'Torres')
    element.set('email', 'Carlos20@gmail.com')
    element.set('dni', '35151565X')

    element = root[3]
    element.set('name', 'Jose')
    element.set('surname', 'Perez')
    element.set('email', 'Jose20@gmail.com')
    element.set('dni', '84554215X')

    element = root[4]
    element.set('name', 'Alejandro')
    element.set('surname', 'Aguilero')
    element.set('email', 'Alejandro20@gmail.com')
    element.set('dni', '35154215X')

    ET.dump(root)
