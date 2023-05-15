G1 F1500                   ; Set the feedrate to 1500mm/minute

G92 X0 Y0 Z0

; Start position
G0 X0 Y0 Z3               ; Move up 3mm from the starting position

; Set Z offset reference
G92 Z0                     ; Set the current Z position as the reference

M3 P100
; Print the lines
G1 X0 Y0 Z0                ; Move to the starting point of the first line
G1 X0 Y20 Z0                
G1 X2 Y0 Z0.5              ; Rapid move to the starting position of the next line
G1 X2 Y20 Z0.5             ; Move to the end of the next line
G1 X4 Y0 Z1                ; Rapid move to the starting position of the line after that
G1 X4 Y20 Z1               ; Move to the end of the line after that
G1 X6 Y0 Z1.5              ; Rapid move to the starting position of the line after that
G1 X6 Y20 Z1.5             ; Move to the end of the line after that
G1 X8 Y0 Z2                ; Rapid move to the starting position of the next line
G1 X8 Y20 Z2               ; Move to the end of the next line
G1 X10 Y0 Z2.5             ; Rapid move to the starting position of the line after that
G1 X10 Y20 Z2.5            ; Move to the end of the line after that
G1 X12 Y0 Z3               ; Rapid move to the starting position of the line after that
G1 X12 Y20 Z3              ; Move to the end of the line after that
G1 X14 Y0 Z3.5             ; Rapid move to the starting position of the next line
G1 X14 Y20 Z3.5            ; Move to the end of the next line
G1 X16 Y0 Z4               ; Rapid move to the starting position of the line after that
G1 X16 Y20 Z4              ; Move to the end of the line after that
G1 X18 Y0 Z4.5             ; Rapid move to the starting position of the line after that
G1 X18 Y20 Z4.5            ; Move to the end of the line after that
G1 X20 Y0 Z5                ; Rapid move to the starting position of the next line
G1 X20 Y20 Z5               ; Move to the end of the next line
G1 X22 Y0 Z5.5              ; Rapid move to the starting position of the line after that
G1 X22 Y20 Z5.5             ; Move to the end of the line after that
G1 X24 Y0 Z6                ; Rapid move to the starting position of the line after that
G1 X24 Y20 Z6               ; Move to the end of the line after that
G1 X26 Y0 Z6.5              ; Rapid move to the starting position of the line after that
G1 X26 Y20 Z6.5             ; Move to the end of the line after that
G1 X28 Y0 Z7                ; Rapid move to the starting position of the next line
G1 X28 Y20 Z7               ; Move to the end of the next line
G1 X30 Y0 Z7.5             ; Rapid move to the starting position of the line after that
G1 X30 Y20 Z7.5            ; Move to the end of the line after that
G1 X32 Y0 Z8               ; Rapid move to the starting position of the line after that
G1 X32 Y20 Z8              ; Move to the end of the line after that
G1 X34 Y0 Z8.5             ; Rapid move to the starting position of the next line
G1 X34 Y20 Z8.5            ; Move to the end of the next line
G1 X36 Y0 Z9               ; Rapid move to the starting position of the line after that
G1 X36 Y20 Z9              ; Move to the end of the line after that
G1 X38 Y0 Z9.5             ; Rapid move to the starting position of the line after that
G1 X38 Y20 Z9.5            ; Move to the end of the line after that
G1 X40 Y0 Z10              ; Rapid move to the starting position of the line after that
G1 X40 Y20 Z10             ; Move to the end of the line after that

M5

; Return to the start position
G0 X0 Y0 Z0
