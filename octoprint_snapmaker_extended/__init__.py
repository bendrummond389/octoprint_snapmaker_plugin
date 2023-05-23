# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
from octoprint.filemanager import FileLocations
from flask import jsonify, request
import os

class SnapmakerExtendedPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.BlueprintPlugin,
):

    ## Octoprint required plugin methods ##
    def get_settings_defaults(self):
        return {}

    def get_assets(self):
        return {
            "js": ["js/snapmaker_extended.js"],
            "css": ["css/snapmaker_extended.css"],
            "less": ["less/snapmaker_extended.less"],
        }

    def get_update_information(self):
        return {
            "snapmaker_extended": {
                "displayName": "Snapmaker_extended Plugin",
                "displayVersion": self._plugin_version,
                "type": "github_release",
                "user": "bendrummond389",
                "repo": "octoprint_snapmaker_plugin",
                "current": self._plugin_version,
                "pip": f"https://github.com/bendrummond389/octoprint_snapmaker_plugin/archive/{self._plugin_version}.zip",
            }
        }

    ## Plugin specific methods ##
    def send_gcode_file(self, file_path):
        if not os.path.isfile(file_path):
            return False, "File not found"
        try:
            with open(file_path) as file:
                gcode = file.readlines()
            self._printer.commands([command.strip() for command in gcode])
            return True, "File sent successfully"
        except Exception as e:
            self._logger.exception("Error while trying to send file to printer: {0}".format(e))
            return False, str(e)

    ## Plugin routes ##
    @octoprint.plugin.BlueprintPlugin.route("/autolevel", methods=["POST"])
    def auto_level(self):
        self._printer.commands("G1029 A")
        return jsonify(success=True)

    @octoprint.plugin.BlueprintPlugin.route("/setZOffset", methods=["POST"])
    def set_z_offset(self):
        self._printer.commands("G92 Z0")
        return jsonify(success=True)

    @octoprint.plugin.BlueprintPlugin.route("/engraveTestLines", methods=["POST"])
    def engrave_test_lines(self):
        file_path = "/home/pi/oprint/lib/python3.9/site-packages/octoprint_snapmaker_extended/gcode/test_lines.gcode"
        success, message = self.send_gcode_file(file_path)
        return jsonify(success=success, message=message)

    @octoprint.plugin.BlueprintPlugin.route("/setFocusedZOffset", methods=["POST"])
    def set_focused_z_offset(self):
        selected_line = request.json.get("selectedLine")
        new_z_offset = 1 + (float(selected_line) * 0.5)
        self._printer.commands([f"G0 Z{new_z_offset}", "G92 Z0"])
        return jsonify(success=True)


__plugin_name__ = "Snapmaker_extended Plugin"
__plugin_pythoncompat__ = ">=3,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = SnapmakerExtendedPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
