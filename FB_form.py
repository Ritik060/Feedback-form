from tkinter import *
import tkinter.messagebox as tmsg
 
root = Tk()
root.geometry("999x555")
root.title("fb_form")
root.configure(bg="#FFFDD0")

Label(root, text="Food Feedback Form", font=("Ubuntu", 18, "bold"), bg="#FFFDD0", fg="#6A5ACD", padx=10, pady= 10).grid(row=0, column=1)

def on_entry(e):
    e.widget['background'] = '#32CD32'
def on_leave(e):
    e.widget['background'] = 'green'

def send_fb():
    with open("fb_form.text","+a") as f:
        f.write("-"*40 + "\n")
        f.write(f"Name : {namevalue.get()}\n")
        f.write(f"Phone : {phonevalue.get()}\n")
        f.write(f"Email : {emailvalue.get()}\n")
        f.write(f"Courtesy of staff : {radiovalue1.get()}\n")
        f.write(f"Ease of scheduling : {radiovalue2.get()}\n")
        f.write(f"Accuracy of service : {radiovalue3.get()}\n")
        f.write(f"Timeliness of food delivery : {radiovalue4.get()}\n")
        f.write(f"Quality of food : {radiovalue5.get()}\n")
        f.write(f"Quantity of food : {radiovalue6.get()}\n")
        f.write(f"Efficiency of setup : {radiovalue7.get()}\n")
        f.write(f"Overall quality of catering services for this event : {radiovalue8.get()}\n")
        f.write(f"Additional comments/suggestions : {acsvalue.get()}\n")
        f.write(f"Overall Rating of service : {trvalue.get()}/5\n")
        f.write("-"*40 + "\n")
    
    tmsg.showinfo( "Feedback", "Thank you for rating us!")
    root.quit()

namevalue = StringVar()
phonevalue = StringVar()
emailvalue = StringVar()
radiovalue1 = StringVar()
radiovalue2 = StringVar()
radiovalue3 = StringVar()
radiovalue4 = StringVar()
radiovalue5 = StringVar()
radiovalue6 = StringVar()
radiovalue7 = StringVar()
radiovalue8 = StringVar()
acsvalue = StringVar()
trvalue = IntVar()

Label(root, text="Name", font=("Arial", 14), bg="#FFFDD0", padx=10, pady= 5).grid(row=1, column=0, sticky="w")
Entry(root, textvariable=namevalue, bd=3, relief=SUNKEN, font=("Arial", 12, "italic")).grid(row=1, column=1)
Label(root, text="Phone", font=("Arial", 14), bg="#FFFDD0", padx=10, pady= 5).grid(row=2, column=0, sticky="w")
Entry(root, textvariable=phonevalue, bd=3, relief=SUNKEN, font=("Arial", 12, "italic")).grid(row=2, column=1)
Label(root, text="Email", font=("Arial", 14), bg="#FFFDD0", padx=10, pady= 5).grid(row=3, column=0, sticky="w")
Entry(root, textvariable=emailvalue, bd=3, relief=SUNKEN, font=("Arial", 12, "italic")).grid(row=3, column=1)

Label(root, text="Poor", bg="#FFFDD0", font=("Arial", 14)).grid(row=4, column=2)
Label(root, text="Fair", bg="#FFFDD0", font=("Arial", 14)).grid(row=4, column=3)
Label(root, text="Good", bg="#FFFDD0", font=("Arial", 14)).grid(row=4, column=4)
Label(root, text="Excellent", bg="#FFFDD0", font=("Arial", 14)).grid(row=4, column=5)

Label(root, text="Courtesy of staff", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=5, column=0, sticky="w")
Radiobutton(root, variable=radiovalue1, value="Poor", bg="#FFFDD0").grid(row=5, column=2)
Radiobutton(root, variable=radiovalue1, value="Fair", bg="#FFFDD0").grid(row=5, column=3)
Radiobutton(root, variable=radiovalue1, value="Good", bg="#FFFDD0").grid(row=5, column=4)
Radiobutton(root, variable=radiovalue1, value="Excellent", bg="#FFFDD0").grid(row=5, column=5)

Label(root, text="Ease of scheduling", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=6, column=0, sticky="w")
Radiobutton(root, variable=radiovalue2, value="Poor", bg="#FFFDD0").grid(row=6, column=2)
Radiobutton(root, variable=radiovalue2, value="Fair", bg="#FFFDD0").grid(row=6, column=3)
Radiobutton(root, variable=radiovalue2, value="Good", bg="#FFFDD0").grid(row=6, column=4)
Radiobutton(root, variable=radiovalue2, value="Excellent", bg="#FFFDD0").grid(row=6, column=5)

Label(root, text="Accuracy of service", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=7, column=0, sticky="w")
Radiobutton(root, variable=radiovalue3, value="Poor", bg="#FFFDD0").grid(row=7, column=2)
Radiobutton(root, variable=radiovalue3, value="Fair", bg="#FFFDD0").grid(row=7, column=3)
Radiobutton(root, variable=radiovalue3, value="Good", bg="#FFFDD0").grid(row=7, column=4)
Radiobutton(root, variable=radiovalue3, value="Excellent", bg="#FFFDD0").grid(row=7, column=5)

Label(root, text="Timeliness of food delivery", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=8, column=0, sticky="w")
Radiobutton(root, variable=radiovalue4, value="Poor", bg="#FFFDD0").grid(row=8, column=2)
Radiobutton(root, variable=radiovalue4, value="Fair", bg="#FFFDD0").grid(row=8, column=3)
Radiobutton(root, variable=radiovalue4, value="Good", bg="#FFFDD0").grid(row=8, column=4)
Radiobutton(root, variable=radiovalue4, value="Excellent", bg="#FFFDD0").grid(row=8, column=5)

Label(root, text="Quality of food", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=9, column=0, sticky="w")
Radiobutton(root, variable=radiovalue5, value="Poor", bg="#FFFDD0").grid(row=9, column=2)
Radiobutton(root, variable=radiovalue5, value="Fair", bg="#FFFDD0").grid(row=9, column=3)
Radiobutton(root, variable=radiovalue5, value="Good", bg="#FFFDD0").grid(row=9, column=4)
Radiobutton(root, variable=radiovalue5, value="Excellent", bg="#FFFDD0").grid(row=9, column=5)

Label(root, text="Quantity of food", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=10, column=0, sticky="w")
Radiobutton(root, variable=radiovalue6, value="Poor", bg="#FFFDD0").grid(row=10, column=2)
Radiobutton(root, variable=radiovalue6, value="Fair", bg="#FFFDD0").grid(row=10, column=3)
Radiobutton(root, variable=radiovalue6, value="Good", bg="#FFFDD0").grid(row=10, column=4)
Radiobutton(root, variable=radiovalue6, value="Excellent", bg="#FFFDD0").grid(row=10, column=5)

Label(root, text="Efficiency of setup", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=11, column=0, sticky="w")
Radiobutton(root, variable=radiovalue7, value="Poor", bg="#FFFDD0").grid(row=11, column=2)
Radiobutton(root, variable=radiovalue7, value="Fair", bg="#FFFDD0").grid(row=11, column=3)
Radiobutton(root, variable=radiovalue7, value="Good", bg="#FFFDD0").grid(row=11, column=4)
Radiobutton(root, variable=radiovalue7, value="Excellent", bg="#FFFDD0").grid(row=11, column=5)

Label(root, text="Overall quality of catering\n services for this event", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=12, column=0, sticky="w")
Radiobutton(root, variable=radiovalue8, value="Poor", bg="#FFFDD0").grid(row=12, column=2)
Radiobutton(root, variable=radiovalue8, value="Fair", bg="#FFFDD0").grid(row=12, column=3)
Radiobutton(root, variable=radiovalue8, value="Good", bg="#FFFDD0").grid(row=12, column=4)
Radiobutton(root, variable=radiovalue8, value="Excellent", bg="#FFFDD0").grid(row=12, column=5)

Label(root, text="Additional comments/suggestions :", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=13, column=0, sticky="w")
Entry(root, textvariable=acsvalue, bd=3, relief=SUNKEN, font=("Arial", 12, "italic"),width=50).grid(row=13, column=1, columnspan=6)

Label(root, text="Overall Rating of service :", bg="#FFFDD0", font=("Arial", 14), padx=10).grid(row=14, column=0, sticky="w")
Scale(root, variable=trvalue, from_=1, to=5, orient=HORIZONTAL, bg="#FFFDD0", troughcolor="#ADD8E6", sliderrelief=RAISED, length=300, sliderlength=50, fg="#2F4F4F", font="bold" ).grid(row=14, column=1, columnspan=6, pady=5)

b1 = Button(root, text="SEND FEEDBACK", command=send_fb, font=("Arial", 14),bg="green", fg="white")
b1.bind("<Enter>", on_entry)
b1.bind("<Leave>", on_leave)
b1.grid(row=15, column=1)

root.mainloop()