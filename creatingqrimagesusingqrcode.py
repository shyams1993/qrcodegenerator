import qrcode											                    #Import QRCode Module
img=qrcode.make("https://www.sutherlandglobal.com")		#make the qrcode for a text or an URL and save it inside variable "img" with qrcode.make() func
img.save("Test.png")									                #save the resultant image 
