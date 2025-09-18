from tkinter import *
import tkinter.messagebox as tsmg
import random
import requests

root = Tk()
root.geometry("400x300")
root.title("OTP Sender via SMS")

num = StringVar()
otp = ""

def send_otp():
    global otp
    number = num.get().strip()
    if number == "":
        tsmg.showerror("Error", "Enter your mobile number")
        return
    elif not ((number.isdigit() and len(number) == 11 and number.startswith("01")) or
              (number.startswith("+880") and number[1:].isdigit() and len(number) == 13)):
        tsmg.showerror("Error", "Invalid Bangladeshi mobile number")
        return

    otp = str(random.randint(100000, 999999))
    message = f"Your OTP is {otp}"

    url = "https://api.example.com/send" 
    params = {
        "apiKey": "YOUR_API_KEY", 
        "numbers": number,          
        "sender": "TXTLCL",  
        "message": message
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            tsmg.showinfo("OTP Sent", f"OTP sent successfully to {number}")
        else:
            tsmg.showerror("Error", "Failed to send OTP. Check API Key or Number")
    except Exception as e:
        tsmg.showerror("Error", f"Something went wrong: {e}")



def check_otp():
    user_otp = otp_entry.get().strip()
    if user_otp == "":
        tsmg.showerror("Error", "Enter OTP")
    elif user_otp == otp:
        tsmg.showinfo("Success", "OTP Verified Successfully!")
    else:
        tsmg.showerror("Error", "Invalid OTP")


Label(root, text="Enter your Bangladeshi mobile number:").pack(pady=10)
Entry(root, textvariable=num).pack(pady=5)
Button(root, text="Send OTP", command=send_otp).pack(pady=10)

Label(root, text="Enter OTP:").pack(pady=10)
otp_entry = Entry(root)
otp_entry.pack(pady=5)
Button(root, text="Verify OTP", command=check_otp).pack(pady=10)

root.mainloop()
