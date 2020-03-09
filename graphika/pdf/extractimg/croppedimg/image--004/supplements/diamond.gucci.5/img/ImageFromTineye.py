from maltego_trx.entities import Image 
from maltego_trx.maltego import UIM_PARTIAL
from maltego_trx.transform import DiscoverableTransform
from pytineye import TinEyeAPIRequest

class ImageFromTineye(DiscoverableTransform):
	
	
	@classmethod
	def create_entities(cls, request, response):
		image = request.Properties
		# print(image["fullImage"]	)

		try:
			img_urls = cls.get_image(image["fullImage"])
			if img_urls:
				for u in img_urls:
					myExactEntity=response.addEntity(Image,u.backlinks[0].backlink)
					myExactEntity.addProperty('crawl_date', 'crawl_date', 'False', u.backlinks[0].crawl_date)
					myExactEntity.addProperty('url', 'URL', 'False', u.image_url )
					myExactEntity.addProperty('width', 'width', 'False', u.width )
					myExactEntity.addProperty('height', 'height', 'False', u.height )
					myExactEntity.addProperty('size', 'size', 'False', u.size )
					myExactEntity.addProperty('format', 'format', 'False', u.format )
					myExactEntity.addProperty('filesize', 'filesize', 'False', u.filesize )
					myExactEntity.addProperty('overlay', 'overlay', 'False', u.overlay )
					# myExactEntity.addProperty('contributor', 'contributor', 'False', u.contributor )
					
			else:
				response.addUIMessage("The image given did not return a match")
		except IOError:
			response.addUIMessage("An error occurred search_url", messageType=UIM_PARTIAL)

	@staticmethod
	def get_image(search_image):
		matching_names = []
		# api = TinEyeAPIRequest('http://api.tineye.com/rest/', 'LCkn,2K7osVwkX95K4Oy', '6mm60lsCNIB,FwOWjJqA80QZHh9BMwc-ber4u=t^')
		api = TinEyeAPIRequest('http://api.tineye.com/rest/', 'ojb9F1I1tukn5^2T3=kS', '_PHPNnWCjEpGclFF2U^B0G+K6ypBvwDD-WctQ,Yf')
		# resp=api.search_url(url='http://i.stack.imgur.com/uNibN.png')
		# print(search_image)
		resp=api.search_url(url=search_image)
		for	 g in resp.matches:
			# print(g.image_url)
			matching_names.append(g)
		return matching_names


if __name__ == "__main__":
	print(ImageFromTineye.get_image("http://www.tineye.com/images/meloncat.jpg"))
