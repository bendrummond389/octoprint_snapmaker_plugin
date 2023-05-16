/*
 * View model for SnapMaker Extended
 *
 * Author: Ben Drummond
 * License: MIT
 */
$(function () {
    function SnapmakerExtendedViewModel(parameters) {
        var self = this;

        self.selectedLine = ko.observable(0);

        var controlViewModel = parameters[0];

        self.isOperational = controlViewModel.isOperational;

        // assign the injected parameters, e.g.:
        // self.loginStateViewModel = parameters[0];
        // self.settingsViewModel = parameters[1];

        // TODO: Implement your plugin's view model here.
        self.performAutoLevel = function () {
            $.ajax({
                url:
                    window.location.origin +
                    "/plugin/snapmaker_extended/autolevel",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    command: "autolevel",
                }),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
                },
            });
        };

        self.setZOffset = function () {
            $.ajax({
                url:
                    window.location.origin +
                    "/plugin/snapmaker_extended/setZOffset",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({}),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
                },
            });
        };

        self.engraveTestLines = function () {
            $.ajax({
                url:
                    window.location.origin +
                    "/plugin/snapmaker_extended/engraveTestLines",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({}),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
                },
            });
        };

        self.setFocusedZOffset = function (selectedLine) {
            $.ajax({
                url:
                    window.location.origin +
                    "/plugin/snapmaker_extended/setFocusedZOffset",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({
                    selectedLine: selectedLine,
                }),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
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
        dependencies: ["controlViewModel"],
        elements: ["#tab_plugin_snapmaker_extended"],
    });
});
