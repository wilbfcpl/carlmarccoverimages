#OverDrive

import re

imageURLPattern=re.compile('^HTTPS://IMG1.OD-CDN\.COM/IMAGETYPE')
imageTypePattern=re.compile('^THUMBNAIL COVER IMAGE')

for field in record.getFields('856'):
	if  field['u']!=None and record['029']!=None:
		ImageURL=field['u'].strip()
		ImageType=field['z'].strip()
		if imageTypePattern.match(ImageType.upper()) and imageURLPattern.match(ImageURL.upper()):
                        record.remove_field(field)



#Kanopy
import re

imageURLPattern=re.compile('^HTTPS://WWW.KANOPY(STREAMING)*\.COM/NODE')
imageTypePattern=re.compile('^COVER IMAGE')

for field in record.getFields('856'):
	if  field['u']!=None and record['029']!=None:
		ImageURL=field['u'].strip()
		ImageType=field['z'].strip()
		if imageTypePattern.match(ImageType.upper()) and imageURLPattern.match(ImageURL.upper()):
			record.addField('029','$a' + ImageURL)
                        record.remove_field(field)

