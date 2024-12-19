"""
The Adapter Pattern is used to make two incompatible interfaces work together.
It acts as a bridge between two systems, enabling them to communicate without modifying their existing code.


Imagine you have a laptop with a USB-C port, but your headphones use a 3.5mm jack.
You use a USB-C to 3.5mm adapter to connect them. The laptop and headphones don’t need to change—only the adapter handles the compatibility.

"""


# Real World example:


# Media Players

# with out adapter pattern


import json
import xml.etree.ElementTree as ET  # extraterrestial LOL!


class MediaPlayer:

    def play(self, audio_type, file_name):

        if audio_type == 'mp3':
            print(f"Playing MP3 file: {file_name}")
        else:
            print(f"Cannot play {audio_type} files. Unsupported format.")


player = MediaPlayer()
player.play('mp3', 'song.mp3')

player.play('mp4', 'movie.mp4')


# Adding new formats (e.g., MP4, VLC) requires modifying the MediaPlayer class.

# with adapter pattern


class MediaPlayer:
    def play(self, audio_type, file_name):
        pass


#  Adaptee 1: mp4 plyer

class AdvancedMediaPlayer:
    def play_mp4(self, file_name):
        print(f"Playing MP4 file: {file_name}")


class VLCMediaPlayer:
    def play_vlc(self, file_name):
        print(f"Playing VLC file: {file_name}")


#  Adapter

class MediaAdapter(MediaPlayer):

    def __init__(self, audio_type):
        if audio_type == 'mp4':
            self.advanced_player = AdvancedMediaPlayer()
        elif audio_type == 'vlc':
            self.advanced_player = VLCMediaPlayer()
            # pass

    def play(self, audio_type, file_name):
        if audio_type == 'mp4':
            self.advanced_player.play_mp4(file_name)
        elif audio_type == 'vlc':
            self.advanced_player.play_vlc((file_name))


# client

class UniversalMediaPlayer(MediaPlayer):

    def play(self, audio_type, file_name):
        if audio_type == 'mp3':
            print(f"Playing MP3 file: {file_name}")
        elif audio_type in ['vlc', 'mp4']:
            adapter = MediaAdapter(audio_type)
            adapter.play(audio_type, file_name)
        else:
            print(f"Cannot play {audio_type} files. Unsupported format.")


player = UniversalMediaPlayer()


player.play("mp3", "song.mp3")
player.play("vlc", "video.vlc")
player.play("mp4", "movie.mp4")


#  lets take a look at another example okay

#  electic recharge plugs


# adaptee
class USPlug:
    def plug_into_us_socket(self):
        print("Plugged into US socket with 110V.")


# interfadce
class EuropeanSocket:
    def plug_into_european_socket(self):
        pass

# Adapter


class SockerAdapter(EuropeanSocket):

    def __init__(self, us_plug):
        self.us_plug = us_plug

    def plug_into_european_socket(self):
        print("Adapting.........................")
        self.us_plug.plug_into_us_socket()


# client

us_plug = USPlug()
adapter = SockerAdapter(us_plug)
adapter.plug_into_european_socket()


"""
Adaptee: The class with the incompatible interface (e.g., AdvancedMediaPlayer or USPlug).
Target Interface: The expected interface (e.g., MediaPlayer or EuropeanSocket).
Adapter: The class that bridges the gap.
"""


"""
Adaptee:
    A class that already exists and provides some functionality.
    However, it does not conform to the interface expected by the client.
    The client cannot directly use the Adaptee because their interfaces don’t match.


Adapter:
    A bridge between the client and the Adaptee.
    It inherits or implements the target interface (e.g., MediaPlayer) expected by the client.
    It translates the client’s requests (via the target interface method) into a format that the Adaptee understands.
    This allows the Adaptee to be used seamlessly without the client needing to know about its mismatched interface.



i.e The Adapter makes the Adaptee "fit" into the client's expectations, like a power plug adapter allows a foreign device to work with your local sockets.


Client: Wants to use a class (MediaPlayer) with a specific method signature (play).
Adaptee: Provides useful functionality but has a different method signature (e.g., play_mp4, play_vlc).
Adapter: Implements the MediaPlayer interface. Inside its play method, it calls the Adaptee’s specific methods (play_mp4, etc.), effectively "adapting" the Adaptee to work with the client.


"""

""""
# lets have a look at another better example

Problem:

Your stock market monitoring app uses XML data as its format.
The 3rd-party analytics library only works with JSON data.
You cannot change either the XML format from your app or the JSON dependency of the library.

The Adapter will act as a bridge between your app (which produces XML data) and the analytics library (which consumes JSON data). It will convert the XML data into JSON format, allowing seamless integration.


"""


class AnalyticsLibrary:
    def process_json(self, json_data):
        print(f"Analyzing data: {json_data}")


# adaptee

class StockDataProvider:

    def get_xml_data(self):
        return "<stocks><stock><name>ABC</name><price>100</price></stock></stocks>"

# adapter


class AnalyticsAdapter:

    def __init__(self, stock_data_provider):
        self.stock_data_provider = stock_data_provider  # adaptee

    def get_data_in_json(self):

        xml_data = self.stock_data_provider.get_xml_data()

        root = ET.fromstring(xml_data)

        stocks = []
        for stock in root.findall('stock'):
            stock_info = {
                "name": stock.find('name').text,
                "price": stock.find('price').text
            }
            stocks.append(stock_info)

        return json.dumps(stocks)


stock_data_prov = StockDataProvider()
analytics_library = AnalyticsLibrary()

adapter = AnalyticsAdapter(stock_data_prov)
json_data = adapter.get_data_in_json()
analytics_library.process_json(json_data=json_data)
