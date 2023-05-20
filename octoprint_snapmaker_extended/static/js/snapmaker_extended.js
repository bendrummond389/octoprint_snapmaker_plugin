/*
 * View model for SnapMaker Extended
 *
 * Author: Ben Drummond
 * License: MIT
 */
$(function () {
    function SnapmakerExtendedViewModel(parameters) {
        var self = this;

        // This is your currently selected line, initialized to 0
        self.selectedLine = ko.observable(0);

        // Obtain the controlViewModel from the parameters
        var controlViewModel = parameters[0];

        // Import functions from the ControlViewModel
        self.isOperational = controlViewModel.isOperational;
        self.isPrinting = controlViewModel.isPrinting;
        self.stripDistanceDecimal = controlViewModel.stripDistanceDecimal;

        // These are the observables for your distances
        self.distances = ko.observableArray([0.1, 1, 10, 100]);
        self.distance = ko.observable(10);

        // Debugging: Log initial values
        console.log('Initial values:', self.distance(), self.distances());

        // This function performs auto-leveling by sending a POST request to the server
        self.performAutoLevel = function () {
            $.ajax({
                url: window.location.origin + "/plugin/snapmaker_extended/autolevel",
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

        // This function sets the Z offset by sending a POST request to the server
        self.setZOffset = function () {
            $.ajax({
                url: window.location.origin + "/plugin/snapmaker_extended/setZOffset",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({}),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
                },
            });
        };

        // This function sends a jog command to the OctoPrint server
        self.sendJogCommand = function (axis, multiplier, distance) {
            if (typeof distance === "undefined") distance = self.distance();
            if (
                self.settings.printerProfiles.currentProfileData() &&
                self.settings.printerProfiles.currentProfileData()["axes"] &&
                self.settings.printerProfiles.currentProfileData()["axes"][axis] &&
                self.settings.printerProfiles
                    .currentProfileData()
                    ["axes"][axis]["inverted"]()
            ) {
                multiplier *= -1;
            }

            var data = {};
            data[axis] = distance * multiplier;
            OctoPrint.printer.jog(data);
        };

        // This function engraves test lines by sending a POST request to the server
        self.engraveTestLines = function () {
            $.ajax({
                url: window.location.origin + "/plugin/snapmaker_extended/engraveTestLines",
                type: "POST",
                dataType: "json",
                data: JSON.stringify({}),
                contentType: "application/json; charset=UTF-8",
                success: function (response) {
                    console.log(response);
                },
            });
        };

        // This function sets the focused Z offset by sending a POST request to the server
        self.setFocusedZOffset = function (selectedLine) {
            $.ajax({
                url: window.location.origin + "/plugin/snapmaker_extended/setFocusedZOffset",
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

    // Register this view model with OctoPrint
    OCTOPRINT_VIEWMODELS.push({
        construct: SnapmakerExtendedViewModel,
        dependencies: ["controlViewModel"],
        elements: ["#tab_plugin_snapmaker_extended"],
    });
});
