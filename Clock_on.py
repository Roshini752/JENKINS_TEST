import uiautomator2 as u2
b=u2.connect('emulator-5554')
b(scrollable=True).scroll(steps=10)

b(text="Clock").click()