# Extract the XML Data with ElementTree
XMLData = '''
<form_Start-Tag>
  <!-- We use "<!-""->" to write the note. -->
  <!-- XML code also own the feature of nest structure, just like the json code. -->
  <Name_Child-Tag>Jeon</Name_Child-Tag>
  <!-- We could create tags in which we could involve the text nore inside the structure of XML code. -->
  <!-- "Jeon" is the text node here.-->
  <!-- We add "/" to show the ending tag.-->
  <Age_Child-Tag type="intl">
    <!-- We could put some "attributes" inside the tag, just like "type" shows here. -->
    35
  </Age_Child-Tag>
  <email hide="yes"/>
</form_Start-Tag>'''
# ''' means notes of multiple lines.
# After I use other package to parse the XML data, I could run the following codes.

import xml.etree.ElementTree as et

treeData = et.fromstring(XMLData)
# We need to transform the type of data from string to tree so that this package could help us extract the particular data more easily.
# Moreover, this code also could ensure the correction and completion of the XML data.
print(treeData.find('Name_Child-Tag').text)
# We could use find() method to extract the text node inside the particular tags, and use ".text" to transform what we get to what we could understand.
print(treeData.find('email').get('hide'))
# We could use get() method to find the value of an attribute.



# Extract more complex XML Data with ElementTree
complexXMLData = '''
<list>
  <department>
    <project region="1">
      <projectNumber>0001</projectNumber>
      <crew>Alan, betty</crew>
    </project>
    <project region="2">
      <projectNumber>0012</projectNumber>
      <crew>Jeon, Cindy</crew>
    </project>
  </department>
</list>'''
import xml.etree.ElementTree as et

treeData = et.fromstring(complexXMLData)
list = treeData.findall('department/project')   # We use "/" to determine the child tag and the mother tag.
print(len(list))

for i in list:
    print("The region this project belong to is:", i.get('region'))
    print("The project number is:", i.find('projectNumber').text)
    print("The people who worked on this project included:", i.find('crew').text)
