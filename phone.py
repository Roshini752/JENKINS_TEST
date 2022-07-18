import uiautomator2 as u2
from time import sleep

b= u2.connect('emulator-5554')
def MO_call():
    print("MO_Call automation")
    call = b(className='android.widget.TextView', packageName='com.android.launcher3',
                     text ='QTI Phone').click()
sleep(2)

#def MO_dialpad():
    #call = b(className='android.widget.ImageButton', packageName='com.google.android.dialer').click()
sleep(2)

MO_call()