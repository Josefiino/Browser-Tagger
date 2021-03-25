from aqt import mw
from anki.hooks import addHook
from aqt.qt import *

config = mw.addonManager.getConfig(__name__)
# tag to add
tag_to_add = config['tag_to_add']
tag_to_add_2 = config['tag_to_add_2']
# shortcuts
shortcut_tags = config['shortcut_tags']
shortcut_tags_2 = config['shortcut_tags_2']

def show_selected_from_browser(nids, tag):
    for id in nids:
        note = mw.col.getNote(id)
        note.addTag(tag)
        note.flush()
        mw.reset()

# create a new menu items, "Add Tag"
def setupMenu(browser):
    action = QAction(f'Add "{tag_to_add}" tag', browser)
    action.setShortcut(shortcut_tags)
    # set it to call testFunction when it's clicked
    action.triggered.connect(lambda: onRegenerate(browser, tag_to_add))
    # and add it to the tools menu
    browser.form.menuEdit.addAction(action)

    action2 = QAction(f'Add "{tag_to_add_2}" tag', browser)
    action2.setShortcut(shortcut_tags_2)
    # set it to call testFunction when it's clicked
    action2.triggered.connect(lambda: onRegenerate(browser, tag_to_add_2))
    # and add it to the tools menu
    browser.form.menuEdit.addAction(action2)


def onRegenerate(browser, tags):
    show_selected_from_browser(browser.selectedNotes(), tags)

addHook("browser.setupMenus", setupMenu)

