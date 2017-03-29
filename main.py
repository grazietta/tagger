import sys
from PyQt5 import QtWidgets

from db.dbHelper import *
from gui.mainWindow import MainWindow, TAB_INDICES
from observer import *
from watcher import Watcher


class Controller(Observer):
    def __init__(self):
        super(Controller, self).__init__()
        self.flights = get_all_flights()
        self.currentFlight = None
        self.imageWatcher = Watcher()
        self.tags = []
        self.images = []

        self.window = MainWindow()
        self.window.show()
        self.window.setupTab.addObserver(self)
        self.window.taggingTab.addObserver(self)
        self.imageWatcher.event_handler.addObserver(self)

        # populate lists
        for flight in self.flights.values():
            self.window.setupTab.addFlightToUi(flight)

    def notify(self, event, id, data):
        if event is "FLIGHT_LOAD":
            self.window.resetGui()
            self.loadFlight(id)
        elif event is "FLIGHT_CREATED":
            self.flights[id] = data
            self.window.setupTab.addFlightToUi(data)
            self.loadFlight(id)
        elif event is "TAG_CREATED":
            self.tags.append(data)
        elif event is "TAG_DELETED":
            self.tags.remove(data)
            data.delete()
            delete_tag(data) # This also deletes all the markers associated with this tag (Cascaded delete)
        elif event is "IMAGE_ADDED":
            self.images.append(data)
        elif event is "IMAGE_RECEIVED":
            new_image = data
            self.images.append(new_image)
            self.window.taggingTab.addImageToUi(new_image)

    def loadFlight(self, id):
        self.previousFlight = self.currentFlight
        self.currentFlight = self.flights[id]

        self.imageWatcher.startWatching(self.currentFlight, self.window.setupTab.line_watchDirectory.text()) \
            if not self.imageWatcher.isRunning \
            else self.imageWatcher.event_handler.changeTargetFlight(self.currentFlight)

        self.loadTags()
        self.loadMap(self.currentFlight)
        self.window.taggingTab.currentFlight = self.currentFlight
        self.window.mapTab.currentFlight = self.currentFlight
        self.loadImages()
        self.window.ui.tabWidget.setCurrentIndex(TAB_INDICES['TAB_TAGGING'])

    def isFlightChanged(self, prev_flight, curr_flight):
        if prev_flight is not None:
            return prev_flight.pk == curr_flight.pk
        return False

    def loadTags(self):
        self.tags = get_all_tags()
        for tag in self.tags:
            self.window.taggingTab.addTagToUi(tag)

    def loadMap(self, flight):
        self.window.taggingTab.minimap.setMinimap(flight)

    def loadImages(self):
        self.images = get_all_images_for_flight(self.currentFlight)
        self.window.taggingTab.clearImagesFromUi()
        for i in self.images:
            self.window.taggingTab.addImageToUi(i)
            self.window.mapTab.addImageToUi(i)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)

    controller = Controller()

    sys.exit(app.exec_())