from aqt import mw
from aqt import browser
from anki.hooks import addHook
# import the "show info" tool from utils.py
from aqt.utils import showInfo
# import aqt.utils
# import all of the Qt GUI library
from aqt.qt import *
import requests
import csv
import re

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

config = mw.addonManager.getConfig(__name__)
# tag to add
tag_to_add = config['tag_to_add']
# field to change
note_tags = config['note_tags']
# shortcuts
shortcut_tags = config['shortcut_tags']


def show_selected_from_browser(nids):
    for id in nids:
        note = mw.col.getNote(id)
        note.addTag(tag_to_add)
        note.flush()
        mw.reset()


# create a new menu item, "Add Tag"
def setupMenu(browser):
    action = QAction(f'Add "{tag_to_add}" tag', browser)
    action.setShortcut(shortcut_tags)
    # set it to call testFunction when it's clicked
    action.triggered.connect(lambda: onRegenerate(browser))
    # and add it to the tools menu
    browser.form.menuEdit.addAction(action)

def onRegenerate(browser):
    show_selected_from_browser(browser.selectedNotes())

addHook("browser.setupMenus", setupMenu)

