from picamera import PiCamera

import time

camera = PiCamera()

#camera.start_preview()

print('capture-begin')

try:
    for i, filename in enumerate(camera.capture_continuous('image{timestamp:%Y%m%d}-{counter:06d}.jpg')):
         print('capture-camera:'+filename) 
         time.sleep(2)
         if i == 10:
             break
finally:
#    camera.stop_preview()
     print('capture-end')
