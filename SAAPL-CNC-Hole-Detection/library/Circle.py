

from cv2 import (cvtColor,COLOR_BGR2GRAY,threshold,THRESH_BINARY,erode,findContours,RETR_EXTERNAL,
		 CHAIN_APPROX_NONE,waitKey,imshow,namedWindow,WINDOW_GUI_NORMAL)
from numpy import (ones,float32)


class circles:

	namedWindow("Cam Display",WINDOW_GUI_NORMAL)


	def __init__(self,arr) -> None:
		self._kernal = ones((5,5), float32)/25
		self.crop = arr
	
	    
	def Find(self, image):
		imshow("Cam Display",image)	
		waitKey(0)
		image= image[self.crop]
		imshow("Cam Display",image)	
		waitKey(0)
		
		imgGray = cvtColor(image, COLOR_BGR2GRAY)
		imshow("Cam Display",imgGray)	
		waitKey(0)
		
		
		imgthres = threshold(imgGray,80,255,THRESH_BINARY)[1]
		imshow("Cam Display",imgthres)	
		waitKey(0)
		imgthres = erode(imgthres,self._kernel)
		imshow("Cam Display",imgthres)	
		waitKey(0)
		image , hirearcy = findContours(image=imgthres,mode=RETR_EXTERNAL,method=CHAIN_APPROX_NONE)
		print(image,hirearcy)
                
		#circles = circle.get_contours(imgthres)
		
		# if circles is not None:

		# 	circles = np.uint16(np.around(circles))
			
		# 	for count, i in enumerate (circles[0, :]):
		# 		center = (i[0], i[1])
		# 		# circle center
		# 		cv2.circle(frame, center, 1, (0, 100, 100), 3)
		# 		cv2.putText(frame,str(count+1),center, cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,0),1,cv2.LINE_AA)
		# 		# circle outline
		# 		radius = i[2]
		# 		cv2.circle(frame, center, radius, (255, 0, 255), 3)
		# 		print('Circle Detected')
		# 		#io.output(25,io.HIGH)
		# 		cv2.imshow("Display", frame)
		# 		cv2.waitKey(1)
		# else:

		# 	print('Circle Not Detected')



# from cupy import asarray
# from _camera_ import CameraSDK
# from cv2 import cuda

# cuda.setDevice(0)

# class region_of_interest:

# 	def __init__(self):

# 		self.read_img = CameraSDK.snap()

# 	def select_roi(self):

# 		image = ...  #camera read file
# 		#image = cv2.imread('images\washer.jpg')
# 		# Select ROI
# 		r = cuda.selectROI("select the area", image)
		
# 		# Crop image
# 		cropped_image = image[int(r[1]):int(r[1]+r[3]), 
# 							int(r[0]):int(r[0]+r[2])]
		
# 		# Display cropped image
# 		cuda.imshow("Cropped image", cropped_image)
# 		cuda.waitKey(0)
# 		cuda.destroyAllWindows()

# 	def auto_roi(self):
		
# 		#width,height = 1944,2592
# 		#top = 100
# 		#left = 150
	
# 		roi = self.read_img[190:310,310:450] 
# 		print('ROI Done')
# 		cv2.imshow("ROI", roi)
# 		cv2.waitKey(1)
# 		return roi




	


