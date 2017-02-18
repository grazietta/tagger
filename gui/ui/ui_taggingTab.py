# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/ui_taggingTab.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TaggingTab(object):
    def setupUi(self, TaggingTab):
        TaggingTab.setObjectName("TaggingTab")
        TaggingTab.resize(795, 592)
        self.horizontalLayout = QtWidgets.QHBoxLayout(TaggingTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.layout_taggingControls = QtWidgets.QVBoxLayout()
        self.layout_taggingControls.setObjectName("layout_taggingControls")
        self.groupBox_2 = QtWidgets.QGroupBox(TaggingTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.list_tags = QtWidgets.QTableWidget(self.groupBox_2)
        self.list_tags.setMaximumSize(QtCore.QSize(16777215, 150))
        self.list_tags.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.list_tags.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.list_tags.setObjectName("list_tags")
        self.list_tags.setColumnCount(4)
        self.list_tags.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.list_tags.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.list_tags)
        self.layout_tagsButtons = QtWidgets.QHBoxLayout()
        self.layout_tagsButtons.setObjectName("layout_tagsButtons")
        self.button_addTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_addTag.setObjectName("button_addTag")
        self.layout_tagsButtons.addWidget(self.button_addTag)
        self.button_editTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_editTag.setObjectName("button_editTag")
        self.layout_tagsButtons.addWidget(self.button_editTag)
        self.button_removeTag = QtWidgets.QPushButton(self.groupBox_2)
        self.button_removeTag.setObjectName("button_removeTag")
        self.layout_tagsButtons.addWidget(self.button_removeTag)
        self.verticalLayout_2.addLayout(self.layout_tagsButtons)
        self.layout_taggingControls.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(TaggingTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.list_images = QtWidgets.QListWidget(self.groupBox_3)
        self.list_images.setObjectName("list_images")
        item = QtWidgets.QListWidgetItem()
        self.list_images.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_images.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.list_images.addItem(item)
        self.verticalLayout_3.addWidget(self.list_images)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.button_toggleReviewed = QtWidgets.QPushButton(self.groupBox_3)
        self.button_toggleReviewed.setObjectName("button_toggleReviewed")
        self.gridLayout_2.addWidget(self.button_toggleReviewed, 0, 0, 1, 3)
        self.button_next = QtWidgets.QPushButton(self.groupBox_3)
        self.button_next.setObjectName("button_next")
        self.gridLayout_2.addWidget(self.button_next, 1, 2, 1, 1)
        self.button_fitScreen = QtWidgets.QPushButton(self.groupBox_3)
        self.button_fitScreen.setObjectName("button_fitScreen")
        self.gridLayout_2.addWidget(self.button_fitScreen, 2, 2, 1, 1)
        self.button_previous = QtWidgets.QPushButton(self.groupBox_3)
        self.button_previous.setObjectName("button_previous")
        self.gridLayout_2.addWidget(self.button_previous, 1, 0, 1, 1)
        self.button_toggleView = QtWidgets.QPushButton(self.groupBox_3)
        self.button_toggleView.setObjectName("button_toggleView")
        self.gridLayout_2.addWidget(self.button_toggleView, 2, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMinimumSize(QtCore.QSize(0, 150))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.layout_taggingControls.addWidget(self.groupBox_3)
        self.horizontalLayout.addLayout(self.layout_taggingControls)
        self.layout_taggingImage = QtWidgets.QVBoxLayout()
        self.layout_taggingImage.setObjectName("layout_taggingImage")
        self.viewer_single = PhotoViewer(TaggingTab)
        self.viewer_single.setObjectName("viewer_single")
        self.layout_taggingImage.addWidget(self.viewer_single)
        self.horizontalLayout.addLayout(self.layout_taggingImage)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(TaggingTab)
        QtCore.QMetaObject.connectSlotsByName(TaggingTab)

    def retranslateUi(self, TaggingTab):
        _translate = QtCore.QCoreApplication.translate
        TaggingTab.setWindowTitle(_translate("TaggingTab", "Form"))
        self.groupBox_2.setTitle(_translate("TaggingTab", "Tags"))
        item = self.list_tags.horizontalHeaderItem(0)
        item.setText(_translate("TaggingTab", "Type"))
        item = self.list_tags.horizontalHeaderItem(1)
        item.setText(_translate("TaggingTab", "Subtype"))
        item = self.list_tags.horizontalHeaderItem(2)
        item.setText(_translate("TaggingTab", "Current (Total)"))
        item = self.list_tags.horizontalHeaderItem(3)
        item.setText(_translate("TaggingTab", "Icon"))
        self.button_addTag.setText(_translate("TaggingTab", "Add"))
        self.button_editTag.setText(_translate("TaggingTab", "Edit"))
        self.button_removeTag.setText(_translate("TaggingTab", "Remove"))
        self.groupBox_3.setTitle(_translate("TaggingTab", "Images"))
        __sortingEnabled = self.list_images.isSortingEnabled()
        self.list_images.setSortingEnabled(False)
        item = self.list_images.item(0)
        item.setText(_translate("TaggingTab", "20160430_111051_217148.jpg"))
        item = self.list_images.item(1)
        item.setText(_translate("TaggingTab", "20160430_111051_217148.jpg"))
        item = self.list_images.item(2)
        item.setText(_translate("TaggingTab", "20160430_111051_217148.jpg"))
        self.list_images.setSortingEnabled(__sortingEnabled)
        self.button_toggleReviewed.setText(_translate("TaggingTab", "Mark as Reviewed"))
        self.button_next.setText(_translate("TaggingTab", "Next"))
        self.button_fitScreen.setText(_translate("TaggingTab", "Fit to Screen"))
        self.button_previous.setText(_translate("TaggingTab", "Previous"))
        self.button_toggleView.setText(_translate("TaggingTab", "Toggle View"))
        self.label_5.setText(_translate("TaggingTab", "MINIMAP"))

from gui.photoViewer import PhotoViewer
