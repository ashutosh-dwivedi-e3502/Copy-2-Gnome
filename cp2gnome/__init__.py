import rb, gtk, rhythmdb

ui_str = \
"""<ui>
  <menubar name="MenuBar">
    <menu name="ToolsMenu" action="Tools">
      <placeholder name="ToolsMenuModePlaceholder">
        <menuitem name="ToolsMenuMicroblog" action="Microblog"/>
      </placeholder>
    </menu>
  </menubar>
  <toolbar name="ToolBar">
    <placeholder name="ToolBarPluginPlaceholder">
      <toolitem name="Microblog" action="Microblog"/>
    </placeholder>
  </toolbar>
</ui>"""

class cp2gnome(rb.Plugin):
    def activate(self, shell):
	print('plugin cp2gnome activated :)')
        icon_file_name = "./icon.png"
        iconsource = gtk.IconSource()
        iconsource.set_filename(icon_file_name)
        iconset = gtk.IconSet()
        iconset.add_source(iconsource)
        iconfactory = gtk.IconFactory()
        iconfactory.add("cp2gnome-button", iconset)
        iconfactory.add_default()

        action = gtk.Action("cp2gnome", "cp2gnome",
                            "copy the current selection to gnome clipboard",
                            "cp2gnome-button");
        action.connect("activate", self.copy_to_clipboard, shell)
        
        self.action_group = gtk.ActionGroup('cp2gnomeActionGroup')
        self.action_group.add_action(action)
        manager = shell.get_ui_manager()
        manager.insert_action_group(self.action_group, 0)
        self.UI_ID copy_to_clipboard= manager.add_ui_from_string(ui_str)
        manager.ensure_update()

    def deactivate(self, shell):
        manager = shell.get_ui_manager()
        manager.remove_ui(self.UI_ID)
        manager.remove_action_group(self.action_group)
        manager.ensure_update()

    def copy_to_clipboard(self, event, shell):
	print 'copying files to clipboard'
        

