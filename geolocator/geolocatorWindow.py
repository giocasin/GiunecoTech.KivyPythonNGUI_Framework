import requests
import json

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy_garden.mapview import MapView, MapMarker
from kivy.properties import BooleanProperty

class GeoLocatorWindow(BoxLayout):
    markers = []
    show_map = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_coordinates(self):
        location_field = self.ids.location_field

        payload = {'spot': location_field.text}
        response = requests.get('http://giunecotechazurefunctionspython.azurewebsites.net/api/getCoordinates', payload)

        if response.status_code == 200:
            geo_location = json.loads(response.text)
            mapview = self.ids.map
            marker = MapMarker(lat=geo_location[1], lon=geo_location[2], source='assets/markers/red_marker.png')

            mapview.add_marker(marker)
            self.markers.append(marker)

            mapview.lat = marker.lat
            mapview.lon = marker.lon
            mapview.zoom = 13
            self.show_map = True

    def clear_map(self):
        for marker in self.markers:
            marker.detach()
        self.markers.clear()

    def hide_map(self):
        self.show_map = False


class GeoLocatorApp(App):
    def build(self):
        return GeoLocatorWindow()


if __name__ == "__main__":
    ga = GeoLocatorApp()
    ga.run()
