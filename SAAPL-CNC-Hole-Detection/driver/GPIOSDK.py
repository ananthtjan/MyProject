from Jetson import GPIO

class GPIO_SDK():

    def __init__(self):
        pass
    
    def enable_warnings(self):
        GPIO.setwarnings(True)

    def disable_warnings(self):
        GPIO.setwarnings(False)

    def get_version(self):
        return GPIO.VERSION

    def get_board_info(self):
        return GPIO.JETSON_INFO

    def get_pin_mode(self):
        mode = GPIO.getmode()
        if mode == 11:
            pin_mode = "BCM"
        elif mode == 10:
            pin_mode = "BOARD"
        elif mode == 1001:
            pin_mode = "CVM"
        return pin_mode
    
    def set_pin_mode(self, pin_mode):
        if pin_mode == "BCM":
            mode = GPIO.BCM
        elif pin_mode == "BOARD":
            mode = GPIO.BOARD
        elif pin_mode == "CVM":
            mode = GPIO.CVM
        else:
            return "Invalid Pin Mode! Supported Modes are \"BCM\", \"BOARD\", \"CVM\"."
        GPIO.setmode(mode)
    
    def set_pin_direction(self,pin_numbers,pin_direction):
        if pin_direction == "OUTPUT":
            direction = GPIO.OUT
            GPIO.setup(pin_numbers, direction, initial=GPIO.LOW)
        elif pin_direction == "INPUT":
            direction = GPIO.IN
            GPIO.setup(pin_numbers, direction)


    def set_intrupt(self,interrupt_pin,GPIO_action,callbackfuntion):
        GPIO.add_event_detect(interrupt_pin, GPIO_action, callback=callbackfuntion)

        
        

    def turn_on(self,channels):
        GPIO.output(channels, GPIO.HIGH)
    
    def turn_off(self,channels):
        GPIO.output(channels, GPIO.LOW)

    def clean_up(self):
        GPIO.cleanup()

    def read_pin(self, channel):
        return GPIO.input(channel)        
    
if __name__ == "__main__":
    
    
    
    myBoard = GPIO_SDK()
    
    print(myBoard.get_version())
    print(myBoard.get_board_info())
    
    myBoard.set_pin_mode("BCM")
    
    print(myBoard.get_pin_mode())
    
    pin_numbers = [25]

    myBoard.set_pin_direction(25,"INPUT")


    while(1):

    
        print(myBoard.read_pin(25))

    myBoard.clean_up()