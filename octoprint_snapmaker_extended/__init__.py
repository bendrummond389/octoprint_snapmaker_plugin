# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
from octoprint.events import Events
from flask import jsonify


class SnapmakerExtendedPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.BlueprintPlugin,
):
    def get_settings_defaults(self):
        return {
            # put your plugin's default settings here
        }

    def get_assets(self):
        return {
            "js": ["js/snapmaker_extended.js"],
            "css": ["css/snapmaker_extended.css"],
            "less": ["less/snapmaker_extended.less"],
        }

    # def get_api_commands(self):
    #     return {
    #         "autolevel": []
    #     }

    # def on_api_command(self, command, data):
    #     if command == "autolevel":
    #         self._printer.commands("G1029 A")
    #         return jsonify(success=True)

    def get_update_information(self):
        return {
            "snapmaker_extended": {
                "displayName": "Snapmaker_extended Plugin",
                "displayVersion": self._plugin_version,
                "type": "github_release",
                "user": "bendrummond389",
                "repo": "octoprint_snapmaker_plugin",
                "current": self._plugin_version,
                "pip": "https://github.com/bendrummond389/octoprint_snapmaker_plugin/archive/{target_version}.zip",
            }
        }

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
        laser_power = 255  # Adjust as necessary
        commands = ["G0 X0 Y0"]  # Move to start position

        for line in range(20):
            z = 1 + (line * 0.5)
            y = line * 2
            commands.extend([f"G1 Z{z}", f"G1 X0 Y{y} F1000", f"M3 P{laser_power}", f"G1 X20 Y{y} F1000", "M5"])

        self._printer.commands(commands)
        
    @octoprint.plugin.BlueprintPlugin.route("/setFocusedZOffset", methods=["POST"])
    def set_focused_z_offset(self):
        selected_line = request.json.get('selectedLine')
        new_z_offset = 1 + (selected_line * 0.5)
        self._printer.commands([f"G0 Z{new_z_offset}", "G92 Z0"])




__plugin_name__ = "Snapmaker_extended Plugin"
__plugin_pythoncompat__ = ">=3,<4"


def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = SnapmakerExtendedPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
