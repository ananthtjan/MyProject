from cv2 import VideoCapture
from numpy import ndarray
from threading import Thread
from queue import Queue

class CameraSDK:

    def __init__(self) -> None:

        self._queue = Queue(5)
        self.looper = True

    @staticmethod
    def snap(cam_id = 0) -> ndarray:
        """
        This program returns a numpy ndarray 
            @param:
            cam_id = give linux camera index by default its 0
        """
        ret,frame = (VideoCapture(cam_id)).read()

        if ret:
            return frame
        else:
            return None
        
    def VideoStart(self,cam_id = 0):
        """
        This program returns a generator of image
        @param:
        cam_id = give index of linux camera, by default it is 0
        """ 
        vid_handle = Thread(target = self._video_handler,args=(cam_id,))
        vid_handle.setDaemon(True)
        vid_handle.start()
        
    def _video_handler(self,cam_id):
          
        while(self.looper):
            self.looper,frame = (VideoCapture(cam_id)).read()
            if self.looper == True:
                self._queue.put(frame)
    
    def getFrames(self) -> ndarray:
        """Returns a numpy array """
        return self._queue.get()
    
    def closeCamera(self):

        self.looper = False
             
if __name__ == "__main__":

    import cv2
    cv2.namedWindow("display",cv2.WINDOW_GUI_NORMAL)

    # img = CameraSDK.snap()
    # cv2.imshow("display", img)
    # cv2.waitKey(0)

    vid = CameraSDK()
    vid.VideoStart()
   
    while True :
        cv2.imshow("display",vid.getFrames())
        
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

    vid.closeCamera()
    cv2.destroyAllWindows()


