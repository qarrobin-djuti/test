import ephem
from datetime import datetime, timedelta
from kivymd.app import MDApp
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem
from kivymd.uix.screen import MDScreen
from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.dialog import MDDialog
from geopy.geocoders import Nominatim
import pytz
from timezonefinder import TimezoneFinder

class TharihSanahApp(MDApp):
    def build(self):
        self.screen = MDScreen()

        # Top Toolbar
        self.toolbar = MDTopAppBar(
        title = "Tharih Sanah",
        pos_hint = {"top": 1})
        self.screen.add_widget(self.toolbar)

        self.input_year = MDTextField(
            hint_text = "Masukkan Tahun dari 1970 hingga 2999",
            size_hint = (0.8, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.8},
            input_filter = "int"
        )
        self.screen.add_widget(self.input_year)

        self.input_location = MDTextField(
            hint_text = "Masukkan Nama Wilayah",
            size_hint = (0.8, 1),
            pos_hint = {"center_x": 0.5, "center_y": 0.7}
        )
        self.screen.add_widget(self.input_location)

        self.button = MDRaisedButton(
            text = "Cari New Moon",
            pos_hint = {"center_x": 0.5, "center_y": 0.6},
            on_release = self.show_new_moon_dates
        )
        self.screen.add_widget(self.button)

        self.scroll_view = ScrollView(
            pos_hint = {"center_x": 0.5, "center_y": 0.3},
            size_hint = (0.9, 0.4)
        )
        self.list_view = MDList()
        self.scroll_view.add_widget(self.list_view)
        self.screen.add_widget(self.scroll_view)
        return self.screen

    def show_new_moon_dates(self, *args):
        try:
            year = int(self.input_year.text)
            location_name = self.input_location.text

            start_date = datetime(year, 3, 1)
            end_date = datetime(year+1, 3, 31)

            # Menampilkan hasil
            self.list_view.clear_widgets()
            bulan_index = 0

            # Menampilkan daftar lengkap bulan dalam satu tahun dengan tanggal bulan baru yang sesuai
            list_item = TwoLineListItem(
            text=f"\nDaftar new moon di kalender Sanah tahun {start_date.year} hingga {end_date.year}:",
            secondary_text=f"\nLintang : {location_name}, Bujur : {location_name}"
            )
            self.list_view.add_widget(list_item)
            list_item = OneLineListItem(text=f"\nTahun {year} :")
                        
        except (ValueError, AttributeError) as e:
            dialog = MDDialog(
                title = "Input Error",
                text = "Masukkan data yang valid!",
                size_hint = (0.8, 0.2)
            )
            dialog.open()
        

if __name__ == "__main__":
    TharihSanahApp().run()