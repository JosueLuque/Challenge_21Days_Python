from node_song import Node
'''
    -- Implementación de un Stack -- 
    En este ejercicio, se solicita implementar una playlist utilizando un stack en Python.

    Se debe crear la clase Playlist con las siguientes propiedades: top, bottom y length, para representar el tope,
    la base y la longitud de la pila, respectivamente.

    La clase Playlist debe tener los siguientes métodos:

    :) addSong(song): Este método permite agregar una canción a la pila. La canción se agrega en el tope de la pila.

    :) playSong(): Este método permite reproducir la canción que se encuentra en el tope de la pila y luego eliminarla.
    Si la pila está vacía, se debe lanzar un error con el mensaje "No hay canciones en la lista".

    :) getPlaylist(): Este método transforma la pila en una lista (array) que contiene todas las canciones en orden de
    reproducción, desde la última agregada hasta la primera.
'''


class Playlist:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def addSong(self, song):
        new_song = Node(song)
        if self.length == 0:
            self.top = new_song
            self.bottom = new_song
        else:
            new_song.next = self.top
            self.top = new_song
        self.length += 1

    def playSong(self):
        if not self.top:
            return Exception("No hay canciones en la lista")
        if self.top == self.bottom:
            self.bottom = None
        song = self.top
        self.top = self.top.next
        self.length -= 1
        return song.value

    def getPlaylist(self):
        playlist = []
        if not self.top:
            return playlist
        current_song = self.top
        while current_song:
            playlist.append(current_song.value)
            current_song = current_song.next
        return playlist


# Checking
playlist = Playlist()

playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.getPlaylist())

r = playlist.playSong()
print(r)

print(playlist.getPlaylist())

playlist.playSong()
playlist.playSong()
re = playlist.playSong()
print(re)
