from tkinter import *
import requests


def get_quote():
    response = requests.get("https://shloka.onrender.com/api/v1/sanskrit/slogan/random")
    print(response)
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["Sloka"])
    print(data)
    # Write your code here.


window = Tk()
window.title("Krishna Says")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="जय श्री कृष्णा", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)


krishna_image = PhotoImage(file="krishna.png")

krishna = PhotoImage(file="pngwing.com.png")
kanye_button = Button(image=krishna, highlightthickness=0, bd=0, command=get_quote, background="white")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()
