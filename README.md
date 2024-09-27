# CTk Simple Weather Map



## Functionality

This software was mainly developed by me for API-use training reasons, however, this was fun to make and i think it turned out great, that's it.

The core functionality is maintained in the `weatherProcessing()` function, where the user inputs a location and the UI will return some weather data from the given location.

The API is from OpenWeatherMap, and the returned values are: weather description, temperature and thermal sensation.

For error handling, i used the `Exception` value for a general idea, since there were more than the usual requests error when handing in non-existent locations.

The UI was made with CustomTkinter, because of the modern and easy-to-implement interface.

For updating the screen with multiple API requests, there will be a `for` loop, making sure the widgets being displayed are the current ones so no buggy UI behavior ends up happening.

Code block:
```
for widget in [getattr(app, 'conditionImage', None),
               getattr(app, 'conditionDisplay', None),
               getattr(app, 'temperatureDisplay', None),
               getattr(app, 'feelsLikeDisplay', None),
               getattr(app, 'errorImageLabel', None),
               getattr(app, 'errorDisplay', None)]:
               
            if widget:
                widget.destroy()
```

And for the API data handling, i used JSON manipulation with Requests.