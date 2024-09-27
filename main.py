from customtkinter import *
import requests
from PIL import Image

app = CTk()
app.geometry("500x500")
app.title("talindev's Weather UI")

set_appearance_mode("dark")
set_default_color_theme("green")
set_widget_scaling(1.2)

def weatherProcessing():
    global info, firstClickCheck
    info = cityEntry.get()

    API_KEY = open('API_KEY.txt', 'r').read()
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={info}&APPID={API_KEY}"

    try:
        weatherGet = requests.get(URL)
        response = weatherGet.json()

        temperatureKelvin = response['main']['temp']
        feelsLikeKelvin = response['main']['feels_like']
        condition = response['weather'][0]['description']
        feelsLikeCelsius = round(feelsLikeKelvin - 273.15, 1)
        temperatureCelsius = round(temperatureKelvin - 273.15, 1)
        feelsLikeLabel = f"{feelsLikeCelsius}°C"
        celsiusLabel = f"{temperatureCelsius}°C"

        icon = response['weather'][0]['icon']

        for widget in [getattr(app, 'conditionImage', None),
                        getattr(app, 'conditionDisplay', None),
                        getattr(app, 'temperatureDisplay', None),
                        getattr(app, 'feelsLikeDisplay', None),
                        getattr(app, 'errorImageLabel', None),
                        getattr(app, 'errorDisplay', None)]:
            if widget:
                widget.destroy()

        image = CTkImage(dark_image=Image.open(f"./assets/{icon}.png"), light_image=Image.open(f"./assets/{icon}.png"), size=(100,100))
        app.conditionDisplay = CTkLabel(master=app, text=condition.title(), font=("Arial", 20, "bold"))
        app.conditionImage = CTkLabel(master=app, image=image, text="")
        app.temperatureDisplay = CTkLabel(master=app, text=f"Temperature: {celsiusLabel}", font=("Arial", 15))
        app.feelsLikeDisplay = CTkLabel(master=app, text=f"Thermal Sensation: {feelsLikeLabel}", font=("Arial", 10))

        app.conditionImage.place(relx=0.5, rely=0.5, anchor="center")
        app.conditionDisplay.place(relx=0.5, rely=0.65, anchor="center")
        app.temperatureDisplay.place(relx=0.5, rely=0.725, anchor="center")
        app.feelsLikeDisplay.place(relx=0.5, rely=0.80, anchor="center")
    
    except Exception:
        for widget in [getattr(app, 'conditionImage', None),
                        getattr(app, 'conditionDisplay', None),
                        getattr(app, 'temperatureDisplay', None),
                        getattr(app, 'feelsLikeDisplay', None),
                        getattr(app, 'errorImageLabel', None),
                        getattr(app, 'errorDisplay', None)]:
            if widget:
                widget.destroy()
        errorImage = CTkImage(dark_image=Image.open("./assets/errorX.png"), light_image=(Image.open("./assets/errorX.png")), size=(100,100))
        app.errorImageLabel = CTkLabel(master=app, image=errorImage, text="")
        app.errorDisplay = CTkLabel(master=app, text="Error! Insert valid location!", font=("Arial", 20, "bold"), text_color="red")

        app.errorImageLabel.place(relx=0.5, rely=0.575, anchor="center")
        app.errorDisplay.place(relx=0.5, rely=0.75, anchor="center")


cityLabel = CTkLabel(master=app, text="Insert location")
cityEntry = CTkEntry(master=app)
sendButton = CTkButton(master=app, text="Send information to API", command=weatherProcessing)
cityLabel.place(relx=0.5, rely=0.1, anchor="center")
cityEntry.place(relx=0.5, rely=0.2, anchor="center")
sendButton.place(relx=0.5, rely=0.3, anchor="center")
app.mainloop()