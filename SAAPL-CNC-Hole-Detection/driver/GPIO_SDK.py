import Jetson.GPIO as GPIO
import time


class GPIO:

    def __init__(self,sensor_pin, relay_pin):

        self.sensor_pin = sensor_pin
        self.relay_pin = relay_pin
    
        # self.sensor_pin = 25
        # self.relay_pin = [21, 20, 26]

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
    def gpio(self):

        GPIO.setup(self.sensor_pin, GPIO.IN)

        sensor_value = GPIO.input(self.sensor_pin)
        print(sensor_value)
        
        GPIO.cleanup()
         
        return sensor_value
        
    def relay(self):
        
        GPIO.setup(self.relay_pin, GPIO.OUT, initial=GPIO.LOW)
        
        try:
            
            while True:
                
                print("turn off")
                GPIO.output(RelayA, GPIO.LOW)
                time.sleep(3)
                print("turn on")
                GPIO.output(RelayA, GPIO.HIGH)		
                time.sleep(3)

        except:

            GPIO.cleanup()
            
if __name__ == "__main__":
  
  while True:
   
    comm = GPIO()
    comm.gpio()
    comm.relay()

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(interrupt_pin, GPIO.IN)

# # Define the interrupt service routine
# def interrupt_handler(channel):
#     # Perform the desired actions when the interrupt is triggered
#     print("Interrupt occurred!")

# # Set up the interrupt event detection
# GPIO.add_event_detect(interrupt_pin, GPIO.RISING, callback=interrupt_handler)

# try:
#     # Your main program or tasks can continue here
#     while True:
#         # Perform your main program logic

#         # For example, continuously check for a condition
#         if GPIO.input(interrupt_pin):
#             print("Interrupt condition met!")

#         # Continue with other tasks

# except KeyboardInterrupt:
#     # Clean up GPIO on keyboard interrupt
#     GPIO.cleanup()
