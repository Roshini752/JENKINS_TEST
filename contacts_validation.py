import uiautomator2 as u2
from time import sleep

c = u2.connect('emulator-5554')

def contacts():
    call = c(className='android.widget.TextView', packageName='com.android.launcher3',
             text='Phone').click()

    #a = c(className='android.widget.LinearLayout').click()
    #, packageName='com.android.contacts' resourceid='android:id/text1',  text='Import/Export contacts'
    #return a
    #b = c(className='android.widget.LinearLayout', packageName='com.android.contacts', text = 'Settings').click()
    #resource = 'android:id/text1', text = 'Settings'


sleep(2)
contacts()
