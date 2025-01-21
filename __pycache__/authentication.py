import time
import pyotp

key = "SammiKei2017KamwenjiSASAmiMISAMI"
totp=pyotp.TOTP(key)
print(totp.now())
time.sleep(30)
print(totp.now())
