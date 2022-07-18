
import uiautomator2 as u2
b = u2.connect('emulator-5554')
print(b.info)
'''print(b.wlan_ip)
print(b.app_info("com.examples.demo"))
b.screen_on()
b.screen_off()

b.press("home")
b.press("menu")
b.press("back")
b.press("phone")


b.screenshot("home1.png")
b.press("back")'''

b(text="Phone").click()
b(text="Contacts").click()

'''
b(text="CREATE NEW CONTACT").click()
b(text="First name").set_text("Vidya")
#b(text="Last name").set_text("Latha")
b(text="Phone").set_text("9578943207")
b(text="SAVE").click()
'''
b.press("back")
#b(text="Settings").click()
#b(text="Network & internet").click()
b(scrollable=True).scroll(steps=10)
#b.press("menu")
b(text="Clock").click()
#b(text="Clock", classname='android.widget.TextView').click()

#b(text="Settings").click()

