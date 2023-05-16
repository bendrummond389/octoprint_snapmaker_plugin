# coding=utf-8
from __future__ import absolute_import
import octoprint.plugin
from flask import jsonify, request


class SnapmakerExtendedPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.BlueprintPlugin,
):
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
        laser_power = 255
        commands = ["G92 X0 Y0"]

        for line in range(20):
            z = 3 + (line * 0.5)
            y = line * 2
            commands.extend(
                [
                    f"G1 Z{z}",
                    f"G1 X0 Y{y} F1000",
                    f"M3 P{laser_power}",
                    f"G1 X20 Y{y} F1000",
                    "M5",
                ]
            )

        self._printer.commands(commands)
        return jsonify(success=True)

    @octoprint.plugin.BlueprintPlugin.route("/engraveTestBoxes", methods=["POST"])
    def engrave_test_boxes(self):
        num_boxes = 20
        box_size = 1
        max_power = 255
        min_power = max_power * 0.1
        max_feed_rate = 5000
        min_feed_rate = 1000
        commands = ["G92 X0 Y0"]

        for i in range(num_boxes):
            for j in range(num_boxes):
                x = i * box_size
                y = j * box_size
                power = min_power + ((max_power - min_power) / (num_boxes - 1) * i)
                feed_rate = min_feed_rate + (
                    (max_feed_rate - min_feed_rate) / (num_boxes - 1) * j
                )

                commands.extend(
                    [
                        f"G1 Z0",
                        f"G1 X{x} Y{y} F{feed_rate:.0f}",
                        f"M3 P{power:.0f}",
                        f"G1 X{x+box_size} Y{y} F{feed_rate:.0f}",
                        f"G1 X{x+box_size} Y{y+box_size} F{feed_rate:.0f}",
                        f"G1 X{x} Y{y+box_size} F{feed_rate:.0f}",
                        f"G1 X{x} Y{y} F{feed_rate:.0f}",
                        "M5",
                    ]
                )

        self._printer.commands(commands)
        return jsonify(success=True)

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
