/*
 * View model for SnapMaker Extended
 *
 * Author: Ben Drummond
 * License: MIT
 */
$(function () {
    function SnapmakerExtendedViewModel(parameters) {
        var self = this;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
        self.performAutoLevel = function () {
            $.ajax({
                url: API_BASEURL + "plugin/snapmaker_extended/autolevel",
                type: "POST",
                dataType: "json",
                success: function () {
                    new PNotify({
                        title: "Success",
                        text: "Auto bed leveling initiated.",
                        type: "success",
                        hide: true,
                    });
                },
                error: function () {
                    new PNotify({
                        title: "Error",
                        text: "Failed to initiate auto bed leveling.",
                        type: "error",
                        hide: true,
                    });
                },
            });
        };
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: SnapmakerExtendedViewModel,
        dependencies: ["loginStateViewModel", "settingsViewModel"],
        elements: ["#tab_plugin_snapmaker_extended"]
    });
});
