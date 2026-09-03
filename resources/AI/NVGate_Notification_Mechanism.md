# NVGate Notification Mechanism Reference Manual - Markdown mirror

> How to be notified when the operator changes a setting, runs a measurement, or acts on the user interface.
>
> Generated 2026-08-24 by `app/manual_to_markdown.py` from
> `NVGate_Notification_Mechanism_Reference_Manual.pdf` (112 pages), NVGate version 17.00.002.
>
> This file is an **automatic conversion** of the official manual, meant to be
> read by an AI tool or searched as text. Where the two disagree, the official
> PDF prevails. The `<!-- page N -->` markers let you locate any passage back
> in the PDF.

| Measure | Value |
|---|---|
| Pages converted | 112 |
| Headings rebuilt | 83 |
| Tables rendered | 207 |
| Original table-of-contents lines discarded | 135 |

## Contents

- [1 - OVERVIEW](#1---overview)
- [2 - BLOCK FORMAT](#2---block-format)
- [3 - USER INTERFACE COMMANDS](#3---user-interface-commands)
    - [CHANGE USER](#change-user)
    - [APPLIED MODE](#applied-mode)
    - [POST ANALYSIS](#post-analysis)
    - [SET UNIT TO MAGNITUDE](#set-unit-to-magnitude)
    - [TOGGLE DOCKABLE WINDOW](#toggle-dockable-window)
    - [TOGGLE MODULE STATE](#toggle-module-state)
    - [WINDOW REFRESH RATE](#window-refresh-rate)
    - [NEW MEASUREMENT PREFERENCE PARAMETER](#new-measurement-preference-parameter)
    - [CONNECT INPUT](#connect-input)
    - [SELECT WATERFALL CHANNELS](#select-waterfall-channels)
    - [UNSELECT WATERFALL CHANNELS](#unselect-waterfall-channels)
  - [3.3 - ACTION](#33---action)
    - [EXEC COMMAND](#exec-command)
    - [CHANGE ACTION SETTING](#change-action-setting)
    - [CHANGE ARMING ACTION SETTING](#change-arming-action-setting)
    - [CHANGE AUTORANGE ACTION SETTING](#change-autorange-action-setting)
    - [CHANGE ICP ACTION SETTING](#change-icp-action-setting)
    - [CHANGE TEDS ACTION SETTING](#change-teds-action-setting)
    - [ACTIVATE SUB-MODULE COLLECTION](#activate-sub-module-collection)
    - [CHANGE SETTING](#change-setting)
    - [CHANGE STRING SETTING](#change-string-setting)
    - [CHANGE BOOLEAN SETTING](#change-boolean-setting)
    - [CHANGE SCALAR SETTING](#change-scalar-setting)
    - [CHANGE ENUMERATED SETTING](#change-enumerated-setting)
    - [CHANGE FORCE/RESPONSE WINDOWS SETTING](#change-forceresponse-windows-setting)
    - [CHANGE FRACTIONAL TACH SETTING](#change-fractional-tach-setting)
    - [CHANGE SIGNAL FILE SETTING](#change-signal-file-setting)
    - [CHANGE MATRIX SETTING](#change-matrix-setting)
    - [CHANGE TABLE SETTING](#change-table-setting)
    - [REMOVE LINE IN A TABLE SETTING](#remove-line-in-a-table-setting)
    - [FULL SCREEN](#full-screen)
    - [SELECT WORKSPACE](#select-workspace)
    - [SELECT WINDOW](#select-window)
    - [CHANGE LAYOUT](#change-layout)
    - [NEW LAYOUT](#new-layout)
    - [ADD WINDOW RESULT](#add-window-result)
    - [ADD WINDOW WATERFALL RESULT](#add-window-waterfall-result)
    - [ADD WINDOW SAVED RESULT](#add-window-saved-result)
    - [ARRANGE WINDOWS](#arrange-windows)
    - [AUTOSCALE XZ](#autoscale-xz)
    - [AUTOSCALE Y](#autoscale-y)
    - [RESET ZOOM](#reset-zoom)
    - [CASCADE VIEW](#cascade-view)
    - [TRACE ANALYSIS](#trace-analysis)
    - [CHANGE WINDOW PREFERENCES](#change-window-preferences)
    - [OPEN PROJECT](#open-project)
    - [LOAD PROJECT](#load-project)
    - [LOAD WORKBOOK](#load-workbook)
    - [EDIT MEASUREMENT](#edit-measurement)
    - [REMOVE PROJECT](#remove-project)
    - [RESET WORKBOOK](#reset-workbook)
    - [REMOVE MEASUREMENT](#remove-measurement)
    - [SAVE PROJECT](#save-project)
    - [SAVE PROJECT AS](#save-project-as)
    - [SAVE WORKBOOK](#save-workbook)
    - [SAVE WORKBOOK AS MODEL](#save-workbook-as-model)
    - [SAVE EDITED MEASUREMENT](#save-edited-measurement)
    - [SAVE MEASUREMENT](#save-measurement)
    - [CHANGE PROJECT DATABASE](#change-project-database)
    - [DOWNLOAD](#download)
    - [UPLOAD](#upload)
    - [PREVIEW SIGNAL](#preview-signal)
    - [SETUP ADD RESULT](#setup-add-result)
    - [SETUP PARAMETERS](#setup-parameters)
    - [SAVE RESULTS](#save-results)
    - [REMOVE ALL RESULT](#remove-all-result)
    - [REMOVE RESULT](#remove-result)
    - [ADD RESULT TO AUTOMEMORIZE](#add-result-to-automemorize)
    - [ENABLE AUTOMEMORIZE](#enable-automemorize)
    - [MEMORIZE TRACE](#memorize-trace)
    - [REMOVE RESULT FROM AUTOMEMORIZE](#remove-result-from-automemorize)
    - [ADD AUTOMATIC OPERATOR](#add-automatic-operator)
    - [ADD AUTOMATIC OPERATOR SAVED RESULT](#add-automatic-operator-saved-result)
    - [CLEAR MEMORY](#clear-memory)
    - [REFRESH REPORT](#refresh-report)
    - [PRINT REPORT](#print-report)
    - [REFRESH AND PRINT REPORT](#refresh-and-print-report)
    - [ADD TO CONTROL PANEL](#add-to-control-panel)
    - [LAUNCH LINK](#launch-link)
    - [COMPLEX](#complex)


<!-- page 1 -->
NVG NOTIFICATION
ATE
MECHANISM
R
EFERENCE MANUAL

| Compatibility | Identification | Updated |
|---|---|---|
| NVGate® V17.00 | F236-C07-29 | January 2024 |


<!-- page 3 -->
TABLE OF CONTENTS

<!-- page 7 -->

## 1 - OVERVIEW

NVGate® supports a system of event notifications, called "messages", based on a socket
communication.
First of all, the client application must activate the socket connection using the
"ConnectToTCPClient" NVDrive® command, along with the PC address parameter (where
the client application is executed) and the port parameter to use.
This call enables the NVGate Connection to this address on this port.
Then, the client application can register to the wanted messages to receive.
There are 4 family message types:
- Messages generated by the analyzer settings
- Messages generated by the analyzer states
- Messages generated by the commands (run, stop, pause ...)
- Messages generated by the interface actions
For more information, see the "TCP Client to Scan State, Setting, User Interface Notification
and Command Events" chapter from the NVDrive® Commands Reference Manual.

<!-- page 8 -->
1.1.SETTING MESSAGES
These messages are sent by the system when a setting value is changed.
This can happen:
- when the setting is modified through the dependency mechanism included in the
analyzer
- when loading a project
- when modifying a setting value directly in the interface
- when modifying a setting value through a NVDrive® command
To register to a setting message, the client application must use the "RegisterSetting"
NVDrive® command.
To unregister a setting message, the client application must use the "UnregisterSetting"
NVDrive® command.

<!-- page 9 -->
1.2.STATE MESSAGES
These messages are sent by the system when a state value is changed.
As the states are not always refreshed when their values changed, it can happen that some
messages are not sent to notify the change.
To register to a setting message, the client application must use the "RegisterState" NVDrive®
command.
To unregister a setting message, the client application must use the "UnregisterState"
NVDrive® command.

<!-- page 10 -->
1.3.COMMAND MESSAGES
These messages are sent by the system when Run/Pause/Stop command is applied.
This can happen:
- when clicking on a command button from the action Toolbar
- when clicking on a command button from the Control Panel
- when sending an action through a NVDrive command
To register to a command message, the client application must use the "RegisterCommand"
NVDrive® command.
To unregister a command message, the client application must use the "UnregisterCommand"
NVDrive® command.

<!-- page 11 -->
1.4.USER INTERFACE MESSAGES
These messages are sent by the system when an interface action is being executed (for
example, opening/closing a window, loading a project, ...).
At the moment, there is about a hundred user action existing, identified by an integer value.
This limited list will be enhanced in future NVGate® versions.
To register to a user interface notification message, the client application must use the
"RegisterUINotification" NVDrive® command.
To unregister a user interface notification message, the client application must use the
"UnregisterUINotification" NVDrive® command.

<!-- page 12 -->
1.5.NEW RESULT MESSAGES
These messages are sent by the system when new results from the specified Module (FFT,
Synchronous Order ....) are available for transfer.
To register to a new result notification message, the client application must use the
"RegisterNewResult" NVDrive® command.
To unregister a new result notification message, the client application must use the
"UnRegisterNewResult" NVDrive® command.
When new results are ready, use the CreateResultEx and GetResultEx NVDrive® command to
retrieve results.
New results are not computed for transfer until the command UnblockNewResult is sent.

<!-- page 13 -->

## 2 - BLOCK FORMAT

The message sent contains:
- a header block, indicating the type of message sent
- a data block, containing complete information about the message

<!-- page 14 -->
2.1.BLOCK - GENERAL HEADER

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | Message Identifier |   |   | Block Message Type |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


| Message Identifier | Block Message Type | Family |
|---|---|---|
| 0 | SCALAR | SETTING |
| 1 | BOOLEAN | SETTING |
| 2 | ENUMERATED | SETTING |
| 3 | STRING | SETTING |
| 4 | ACTION | SETTING |
| 6 | VIRTUAL TACHO | SETTING |
| 7 | ARRAY | SETTING |
| 8 | INTER-SPECTRUM | SETTING |
| 9 | WATERFALL SOURCE | SETTING |
| 10 | STATE | STATE |
| 11 | FORCE RESPONSE | SETTING |
| 12 | PROGRESSION | STATE |
| 13 | COMMAND | COMMAND |
| 14 | USER INTERFACE | USER INTERFACE |
| 15 | USER INTERFACE PROPERTY | USER INTERFACE |
| 16 | CONST | USER INTERFACE |
| 17 | USER INTERFACE ENUM PROPERTY | USER INTERFACE |


<!-- page 15 -->
2.2.BLOCK - GENERAL DATA
Data Type Size:
Boolean: 1 byte
Short: 2 bytes
Long: 4 bytes
String: End with '\0'

|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Data 1 |   | Type 1 |   |   | Comment about data 1 item |   |   |
|   | Data 2 |   | Type 2 |   |   | Comment about data 2 item |   |   |
|   | Data n |   | Type 3 |   |   | Comment about data 3 item |   |   |


<!-- page 16 -->
2.3.BLOCK - SETTING
IDN
The NVGate settings have a specific IDN (IDentifier Number).
This number consists on 3 fields:
<Module num>.<Sub-module num>.<Setting num>
See the "NVDrive® Reference Manual" document to retrieve a setting IDN.
SCALAR
BOOLEAN

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 0 |   |   | Scalar Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | Float |   |   | Setting value is float type |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 1 |   |   | Boolean Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | Boolean |   |   | Setting value is boolean type |   |   |


<!-- page 17 -->
ENUMERATED
STRING
ACTION

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 2 |   |   | Enumerated Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | String |   |   | Setting value is string type |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 3 |   |   | String Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | String |   |   | Setting value is string type |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 4 |   |   | Action Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | Boolean |   |   | Setting value is boolean type |   |   |


<!-- page 18 -->
VIRTUAL TACHO SETTING
All values are float type such as :
T a c h R a t i o =
D
N
e
u
n
m
o m
e r
i
a
n
t
a
o
t
r
o
1
r 1

D
N
e
u
n
m
o m
e r
i
a
n
t
a
o
t
r
o
2
r 2
ARRAY SETTING

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 6 |   |   | Virtual Tacho Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value1 |   | Float |   |   | Numerator1 |   |   |
|   | Value2 |   | Float |   |   | Denominator1 |   |   |
|   | Value3 |   | Float |   |   | Numerator2 |   |   |
|   | Value4 |   | Float |   |   | Denominator2 |   |   |
|   | Value5 |   | Float |   |   | TachRatio |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 7 |   |   | Array Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value1 |   | Long |   |   | Number of lines |   |   |
|   | Value2 |   | Long |   |   | Number of columns |   |   |
|   | For each line |   |   |   |   |   |   |   |
| Enable | Enable |   | BOOLEAN<br>Block |   |   | Order on or off |   |   |
| OrderNum |   |   | SCALAR<br>Block |   |   | Order number |   |   |
| Bandwidth |   |   | SCALAR<br>Block |   |   | Bandwidth |   |   |


<!-- page 19 -->
INTER-SPECTRUM SETTING
WATERFALL SOURCE SETTING

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 8 |   |   | Inter-Spectrum Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Nb couples |   | Long |   |   | Number of couples (can range from 1 to 500) |   |   |
|   | For each couple |   |   |   |   |   |   |   |
|   | NumModule1 |   | Short |   |   | First couple item Module identifier |   |   |
|   | NumSubModule1 |   | Short |   |   | First couple item Sub-Module identifier |   |   |
|   | NumSetting1 |   | Short |   |   | First couple item Setting identifier |   |   |
|   | NumModule2 |   | Short |   |   | Second couple item Module identifier |   |   |
|   | NumSubModule2 |   | Short |   |   | Second couple item Sub-Module identifier |   |   |
|   | NumSetting2 |   | Short |   |   | Second couple item Setting identifier |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 9 |   |   | Waterfall Source Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | String |   |   | Setting value is string type |   |   |


<!-- page 20 -->
FORCE RESPONSE SETTING
A force/response window settings is a table of 8 float values.
VISIBILITY SETTING

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 11 |   |   | Force Response Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Window Type |   | Short |   |   | Window Type (Force or Response) |   |   |
|   | Value 1 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 2 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 3 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 4 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 5 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 6 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 7 |   | Float |   |   | Setting value is float type |   |   |
|   | Value 8 |   | Float |   |   | Setting value is float type |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 19 |   |   | Visibility Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | Boolean |   |   | Visibility value is boolean type |   |   |


<!-- page 21 -->
EQUATION SETTING

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 20 |   |   | Equation Setting |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | Setting identifier |   |   |
|   | Value |   | String |   |   | Equation value is string type |   |   |


<!-- page 22 -->
2.4.BLOCK - STATE
IDN
The NVGate state have a specific IDN (IDentifier Number).
This number consists on 3 fields:
<Module num>.<Sub-module num>.<State num>
See the "NVDrive® Reference Manual" document to retrieve a state IDN.
STATE

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 10 |   |   | Normal State |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | State identifier |   |   |
|   | State Type |   | Short |   |   | State can be of different type: |   |   |
|   | If State Type is Input Led (State Type = 0) |   |   |   |   |   |   |   |
|   | Value |   | String |   |   | State value is string type |   |   |
|   | If State Type is Information string (State Type = 1) |   |   |   |   |   |   |   |
|   | Value |   | String |   |   | State value is string type |   |   |
|   | If State Type is Scalar or Float (State Type = 2) |   |   |   |   |   |   |   |
|   | Value |   | Float |   |   | State value float type |   |   |
|   | If State Type is Integer (State Type = 3) |   |   |   |   |   |   |   |
|   | Value |   | Integer |   |   | State value is integer type |   |   |


<!-- page 23 -->
PROGRESSION STATE

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 12 |   |   | Progression State |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module |   | Short |   |   | Module identifier |   |   |
|   | Sub-Module |   | Short |   |   | Sub-Module identifier |   |   |
|   | Setting |   | Short |   |   | State identifier |   |   |
| Progression Mode | Progression Mode |   | Short |   |   | 0 : Normal<br>1 : Reverse<br>2 : Snack |   |   |
| Progression Color |   |   | Short |   |   | 0 : Blue<br>1 : Green<br>2 : Red<br>3 : Text Red |   |   |
|   | Current Position |   | Short |   |   | The position inside the range depends on the context |   |   |


<!-- page 24 -->
2.5.BLOCK - COMMAND
COMMAND IDENTIFIER
Each NVGate command corresponds to an icon in the control bar of NVGate®, and has a
specific identifier number:
COMMAND

| Command Identifier | NVGate Command |
|---|---|
| 0 | RUN |
| 1 | PAUSE |
| 2 | STOP |
| 3 | ACCEPT |
| 4 | REJECT |
| 5 | MANUAL TRIGGER |
| 6 | PLAYER PAUSE |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 13 |   |   | Command |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Command |   | Long |   |   | Command identifier |   |   |
|   | Activation |   | Boolean |   |   | Active (button pushed) / Inactive |   |   |
|   | Authorization |   | Boolean |   |   | Enable / Disable (grey icon) |   |   |


<!-- page 25 -->
2.6.BLOCK - NEWRESULT
MODULE NUMBER
Every NVGate's plug-in have a specific Module Number (first number of IDN).
See the "NVDrive® Reference Manual" document to retrieve a module IDN.
NEWRESULT

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 18 |   |   | NewResult |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Module number |   | Short |   |   | Module number |   |   |


<!-- page 26 -->
2.7.BLOCK - NEWMEASUREMENT

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 21 |   |   | NewResult |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Measurement name |   | String |   |   | Measurement name created is string type |   |   |


<!-- page 27 -->
2.8.BLOCK - USER INTERFACE
USER INTERFACE EVENT
Each NVGate User Interface has a specificic identifier number:

| User<br>Interface<br>Identifier | User Interface Notification | Described on page |
|---|---|---|
| -1 | Undefined |   |
| 0 | Applied Mode | 35 |
| 1 | Change User | 34 |
| 2 | Connect Input | 42 |
| 3 | Exec Command | 46 |
| 4 | Launch Link | 105 |
| 5 | Post Analysis | 36 |
| 8 | Select Waterfall Channels | 42 |
| 9 | Set Unit To Magnitude | 37 |
| 10 | Affectation | internal |
| 11 | Break | internal |
| 12 | Call Macro | internal |
| 13 | Comment | internal |
| 14 | Enter Macro | internal |
| 15 | Execute Macro | internal |
| 16 | Get Enumerated Value | internal |
| 17 | Get Exec Macro Parameter | internal |
| 18 | Get Scalar Value | internal |
| 19 | Get Time | internal |
| 20 | Group | internal |
| 21 | If Then | internal |
| 22 | Incrementation | internal |
| 23 | Loop For | internal |
| 24 | Make String | internal |
| 25 | Message Box | internal |
| 26 | Run Macro | internal |
| 27 | Send Trace | internal |
| 28 | Set Enumerated Value | internal |
| 29 | Set Exec Macro Parameter | internal |
| 30 | Set Macro Parameter | internal |
| 31 | Set Scalar Value | internal |
| 32 | Timer Loop | internal |
| 33 | Wait | internal |
| 34 | While | internal |
| 35 | Add To Control Panel | 101 |
| 36 | Change Layout | 62 |
| 37 | Download | 80 |
| 38 | Edit Measurement | 74 |
| 39 | Load Project | 72 |
| 40 | Load Workbook | 73 |
| 41 | New Layout | 63 |
| 42 | New Measurement Preference Parameter | 40 |
| 43 | Remove Measurement | 75 |
| 44 | Remove Project | 74 |
| 45 | Reset Workbook | 75 |
| 46 | Save Measurement | 78 |
| 47 | Save Measure | 78 |


<!-- page 28 -->
The macros are not described.

| 48 | Save Project | 76 |
|---|---|---|
| 49 | Save Project as | 76 |
| 50 | Save Results | 86 |
| 51 | Save Workbook | 77 |
| 52 | Upload | 81 |
| 53 | Activate Sub-Module Collection | 51 |
| 54 | Change Setting | 51 |
| 55 | Change Action Setting | 46 |
| 56 | Change Arming Setting | 47 |
| 57 | Change Autorange Setting | 48 |
| 58 | Change ICP Setting | 49 |
| 59 | Change Boolean Setting | 53 |
| 60 | Change String Setting | 52 |
| 61 | Change Enumerated Setting | 54 |
| 62 | Change Force/Response Windows Setting | 55 |
| 63 | Change Matrix Setting | 58 |
| 64 | Change Scalar Setting | 54 |
| 65 | Change Signal File Setting | 58 |
| 66 | Change Table Setting | 59 |
| 67 | Change Virtual Tacho Setting | 56 |
| 68 | Remove Line in a Table Setting | 60 |
| 69 | Arrange Windows | 68 |
| 70 | Window Refresh Rate | 39 |
| 71 | Full Screen | 61 |
| 72 | Select Workspace | 61 |
| 73 | Toggle Dockable Window | 37 |
| 74 | Toggle Module State | 38 |
| 76 | Add Automatic Operator | 96 |
| 77 | Add Automatic Operator Saved Result | 98 |
| 78 | Add Result to Automemorize | 90 |
| 79 | Add Window Result | 64 |
| 80 | Add Window Saved Result | 67 |
| 81 | Add Window Waterfall Result | 66 |
| 82 | Autoscale XZ | 69 |
| 83 | Autoscale Y | 69 |
| 84 | Cascade View | 70 |
| 85 | Enable Automemorize | 92 |
| 86 | Memorize Trace | 93 |
| 87 | Preview Signal | 82 |
| 88 | Remove Result from Automemorize | 94 |
| 89 | Reset Zoom | 70 |
| 90 | Select Window | 62 |
| 91 | Setup Add Result | 83 |
| 92 | Setup Parameters | 85 |
| 93 | Remove All Results | 87 |
| 94 | Remove Result | 88 |
| 95 | Exit Macro | internal |
| 96 | Command Complex | 105 |
| 97 | Change Project Database | 79 |
| 98 | Change TEDS Action Setting | 50 |
| 99 | Clear Memory | 100 |
| 100 | Trace Analysis | 70 |
| 101 | Unselect Waterfall Chanel | 44 |
| 102 | Get Boolean Value | internal |
| 103 | Get String Value | internal |
| 104 | Save Workbook As Model | 77 |
| 111 | Change window preferences | internal |


<!-- page 29 -->
They are internally used inside NVGate and do not send notification.

<!-- page 30 -->
USER INTERFACE
USER INTERFACE PROPERTY

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 14 |   |   | User Interface identifier |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
|   | Command ID |   | Long |   |   | User Interface Identifier |   |   |
| NB Properties | NB Properties |   | Long |   |   | Number of properties (each properties is described in a<br>property block) |   |   |
| Executed |   |   | Boolean |   |   | Indicates if the command has been executed or not.<br>(This depends on the mode parameter assigned when<br>registering the command) |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 15 |   |   | Normal property |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
| Type | Type |   | Long |   |   | Type of the property<br>See the "TABLE 1: Property Type Identifier", page 106 |   |   |
|   | Name ID |   | Long |   |   | Identifier of the property |   |   |
|   | Value |   | String |   |   | Value of the property |   |   |
|   | Unit |   | String |   |   | Empty or unit of the property |   |   |
|   | Hidden |   | Boolean |   |   | Indicates if the property can be edited or not |   |   |
| Const | Const |   | Boolean |   |   | If TRUE, a BLOCK-CONST is added here<br>(see page 31) |   |   |


<!-- page 31 -->
USER INTERFACE ENUM PROPERTY
CONST

|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 17 |   |   | Enumerated Property |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
| Type | Type |   | Long |   |   | Type of the property<br>See the "TABLE 3: Property Identifier", page 108 |   |   |
|   | Name ID |   | Long |   |   | Identifier of the property |   |   |
|   | Value |   | String |   |   | Value of the property |   |   |
|   | Unit |   | String |   |   | Empty or unit of the property |   |   |
|   | Hidden |   | Boolean |   |   | Indicates if the property can be edited or not |   |   |
| Const | Const |   | Boolean |   |   | If TRUE, a BLOCK-CONST is added here<br>(see page 31) |   |   |
| EnumType |   |   | Long |   |   | Type of enumerated property (optional)<br>See the "TABLE 2: Enumerated Property Type<br>Identifier", page 107 |   |   |


|   | HEADER |   |   | Data Type |   |   | Value |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | Version |   | Short |   |   | 0 |   |   | Version number |   |   |
|   | Block ID |   | Short |   |   | 16 |   |   | Block Const |   |   |
|   | Size |   | Long |   |   | Data size |   |   | Size of the following data |   |   |


|   | DATA |   |   | Data Type |   |   | Comment |   |
|---|---|---|---|---|---|---|---|---|
| Property Type | Property Type |   | Long |   |   | Type of the property<br>See the "TABLE 1: Property Type Identifier", page 106 |   |   |
|   | Name |   | String |   |   | Name of the const |   |   |
|   | Value |   | String |   |   | Value of the const |   |   |


<!-- page 33 -->

## 3 - USER INTERFACE COMMANDS

This chapter lists the use of all available User Interface Notifications commands that can be
subscribed to receive notification when they occur, along with the corresponding result format
description.
To subscribe to all commands, set the command number to "-1"
The NVDrive® commands used are:
- "ConnectToTCPClient" to connect the TCP client,
- "RegisterUINotification" to register an User Interface Notification,
- "ExecUINotification" to execute an User Interface Notification,
- "UnregisterUINotification" to unregister an User Interface Notification.
See the "NVDrive Reference Manual" document for more information about these
commands.
GENERAL NOTIFICATION RULES
- A notification can be sent for each NVGate® internal command.
- If an action is called by another one, the corresponding notification is not sent.
- When a command is executed through the "ExecUINotification" NVDrive® command,
no notification is sent.
- Some internal actions required to execute macros prevent them being executed from
NVDrive as all the required parameters cannot be transmitted. These commands are
the following macro algorithmics item: "Call Macro", "Group", "If Then", "Loop
For", "Timer Loop" and "While".
Moreover, as these commands are internally used inside NVGate, they cannot send
notification.
- While editing a macro or executing step by step a macro, no notification is sent.

<!-- page 34 -->
3.1.USER PREFERENCES
This paragraph described the User Interface Notification related to the general User
Preferences commands to configure the interface.

#### CHANGE USER


**Semantics**

Scan when the User is being changed.

**To activate command**

This command can be sent from the "Home/User" ribbon or "Preferences/User" ribbon.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 1 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 100<br>First Name |   |   | "First_Name" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 101<br>Last Name |   |   | "Last_Name" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 102<br>Password |   |   | "Password" |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 35 -->

#### APPLIED MODE


**Semantics**

Scan when the "applied mode" is being changed.

**To activate command**

This command can be sent with the activation or desactivation of the specialized modes:
Rotating or Structural, in "Preferences/General" window.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 0 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 3300<br>Mode |   |   | 1: Rotating<br>2: Structural<br>-1: All |   |   |   |   |   | 0 |   |   | 0 |   |   | 18 |   |   |
| 9<br>User Enum |   |   | 3301<br>Action |   |   | 0: Activate<br>1: Deactivate<br>2: Switch |   |   |   |   |   | 0 |   |   | 0 |   |   | 19 |   |   |


<!-- page 36 -->

#### POST ANALYSIS


**Semantics**

Scan when the analyzer is being switched to/from the post-analysis mode.

**To activate command**

This command can be sent from the "Home/Go to result" ribbon.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 5 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 3200<br>Analysis Mode |   |   | 0: On-line<br>1: Post-analysis |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 37 -->

#### SET UNIT TO MAGNITUDE


**Semantics**

Scan when the physical quantity is being modified.

**To activate command**

Use the "SetUnit" NVDrive command.

**Notification returned**

```
```

#### TOGGLE DOCKABLE WINDOW


**Semantics**

Scan when one of the "View" elements is being displayed or hidden.

**To activate command**

Click on one of the check boxes from the "Preferences/View" ribbon.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 9 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1<br>Integer |   |   | 1701<br>Magnitude ID |   |   | "MagitudeID" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   |   | 1700<br>Current Unit |   |   | "CurrentUnit" |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 73 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 1400<br>Dockable<br>Window |   |   | 33309: Analyzer Status<br>34047: Workspace<br>34048: Log Window<br>34057: Setting Grid |   |   |   |   |   | 0 |   |   | 0 |   |   | 2 |   |   |
| 2<br>Boolean |   |   | 1300<br>Show |   |   | 0: hidden<br>1: displayed |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 38 -->

#### TOGGLE MODULE STATE


**Semantics**

Scan when the plug-in states are being displayed or hidden.

**To activate command**

Right-click on an active analysis plug-in and select/unselect the "View States" item.

**Notification returned**

```
For exemple, when displaying the FFT1 states, the IDN value is "010.000.000".
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 74 |   |   | 2 |   |   |


| Type |   | Name |   | Value | Unit | Hidden | Const | EnumType |
|---|---|---|---|---|---|---|---|---|
|   |   | ID |   |   |   |   |   |   |
| 9<br>User Enum | 1800<br>Module |   |   | IDN of the type of<br>analyzer |   | 0 | 0 | 4 |
| 2<br>Boolean | 1300<br>Show |   |   | 0: hidden<br>1: displayed |   | 0 | 0 |   |


<!-- page 39 -->

#### WINDOW REFRESH RATE


**Semantics**

Scan when the user Refresh Rate preference is being modified.

**To activate command**

Open the dialog box with the "Preference/General" ribbon.
Move the "Windows refresh rate" cursor to modify its value:

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 70 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1<br>Integer |   |   | 1600<br>Window<br>refresh rate |   |   | 'value'<br>(range from 1 to 30) |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 40 -->

#### NEW MEASUREMENT PREFERENCE PARAMETER


**Semantics**

Scan when a measurement preference to save measurement is being changed.

**To activate command**

Click on the "General" button from the "Preferences / Preferences" ribbon to open the
"Preferences" dialog box.
Change one of the save options from the "Save" tab:

**Notification returned**

```
```

<!-- page 41 -->
```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 42 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User<br>Enum |   |   | 2503<br>Save Mode |   |   | 0: Do not save<br>1: In Default<br>Measurement<br>2: With name<br>confirmation<br>3: Without name<br>confirmation |   |   |   |   |   | 0 |   |   | 0 |   |   | 16 |   |   |
| 0<br>String |   |   | 908<br>Keyword |   |   | "keyword value" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 2<br>Boolean |   |   | 2504<br>Set preferences |   |   | 0: read preferences<br>1: set preferences |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 42 -->
3.2.CONNECTION
This paragraph described the User Interface Notification related to the connections.

#### CONNECT INPUT


**Semantics**

Scan when an input or a track is being connected to a module.

**To activate command**

Use "ConnectInput" NVDrive command.
Either, this command can be sent when connecting inputs or tracks (in the post-analysis
mode) to an analysis module. Select "Show Results" from the "Home / Go to result" ribbon.

**Notification returned**

```
```

#### SELECT WATERFALL CHANNELS


**Semantics**

Scan when a channel is being connected to the waterfall module.

**To activate command**

To connect waterfall channels:
Open the dialog box with the "Analysis / Waterfall" ribbon.

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 2 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 2804<br>IDN<br>source |   |   | player.431:1<br>(example for<br>player track 1) |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2805<br>IDN target |   |   | fft1.channel1 |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 43 -->
Or, open this dialog box from the Analyzer Setting Browser by a right-click on "Waterfall→
Channels" and select the item "Add/Remove".
Select items to add from the left frames and click on the green-arrow button.

**Notification returned**

```
* Module ID: See the NVDrive Reference Manual for the Module ID table.
The available module ID are the plugs-in that can be connected to the Waterfall (ex: fft1)
* Process ID: See the NVDrive Reference Manual for the Process ID table.
The available process ID are the results that can be connected to the Waterfall (ex: 2, for an
average spectrum).
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 8 |   |   | 4 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User<br>Enum |   |   | 2601<br>Module ID |   |   | Module ID* |   |   |   |   |   | 0 |   |   | 0 |   |   | 20 |   |   |
| 1<br>Integer |   |   | 4505<br>Response |   |   | Channel number |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 4506<br>Reference |   |   | Reference channel number |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User<br>Enum |   |   | 2602<br>Process<br>Type |   |   | Process ID* |   |   |   |   |   | 0 |   |   | 0 |   |   | 22 |   |   |
| 1<br>Integer |   |   | 4508<br>Connection<br>mode |   |   | 0: WtfConnectAndCreate,<br>1: WtfOnlyConnect,<br>2: WtfOnlyCreate,<br>3: WtfConnectThenCreate |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 44 -->

#### UNSELECT WATERFALL CHANNELS


**Semantics**

Scan when a channel is being disconnected from the waterfall module.

**To activate command**

To disconnect waterfall channels:
Open the dialog box with the "Analysis / Waterfall" ribbon.
Or, open this dialog box from the Analyzer Setting Browser by a right-click on "Waterfall→
Channels" and select the item "Add/Remove".
Select items to be removed from the "Waterfall" or "References & Profiles" frames and click
on the red-cross button.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 101 |   |   | 4 |   |   |


<!-- page 45 -->
* Module ID: See the NVDrive Reference Manual for the Module ID table.
The available module ID are the plugs-in that can be connected to the Waterfall.
* Process ID: See the NVDrive Reference Manual for the Process ID table.
The available process ID are the results that can be connected to the Waterfall.

|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 2601<br>Module ID |   |   | Module ID* |   |   |   |   |   | 0 |   |   | 0 |   |   | 20 |   |   |
| 1<br>Integer |   |   | 4505<br>Response |   |   | Channel number |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 4506<br>Reference |   |   | Reference<br>channel number |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2602<br>Process<br>Type |   |   | Process ID* |   |   |   |   |   | 0 |   |   | 0 |   |   | 22 |   |   |


<!-- page 46 -->

### 3.3 - ACTION

This paragraph described the User Interface Notification related to the Actions.

#### EXEC COMMAND


**Semantics**

Scan when an analysis command is being executed.

**To activate command**

This command can be sent with the [Run / Pause / Stop / Trigger / Pause Player] and [Accept
/ Reject] buttons.

**Notification returned**

```
```

#### CHANGE ACTION SETTING


**Semantics**

Scan when an action is performed (hidden).

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 3 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1<br>Integer |   |   | 5900<br>Command |   |   | 0 Run<br>1 Pause<br>2 Stop<br>3 Accept<br>4 Reject<br>5 Manual Trigger<br>6 Pause Player |   |   |   |   |   | 0 |   |   | 0 |   |   |


| Column 1 | Column 2 | Column 3 |
|---|---|---|
|   | Command ID |   |
| 55 |   |   |


<!-- page 47 -->

#### CHANGE ARMING ACTION SETTING


**Semantics**

Scan when the [Recorder Arming] button state is being changed.

**To activate command**

At least one input must be connected to a recorder track to activate the recorder module.
Click on the Armed/Unarmed button from the "Analysis / Record" ribbon.
Or from the Analyzer Setting Browser, select the "Recorder → Trigger → Recorder" setting
and click on the button to change it to [Arm] or [Unarm].

**Notification returned**

```
"recorder.recTrigger.407" = Arming IDN
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 56 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | recorder.recTrigger.407 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1000<br>Property value |   |   | 0: Unarmed<br>1: Armed |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 48 -->

#### CHANGE AUTORANGE ACTION SETTING


**Semantics**

Scan when the [Autorange] action is being executed.

**To activate command**

Click on the [Autorange] button from the "Acquisition / Inputs" ribbon.
Or from the Analyzer Setting Browser, select the "Front-End → Auto-ranging → Autorange"
setting and click on the [Run] button to start the Autorange.

**Notification returned**

```
"frontEnd.autoRanging.335" = Autorange IDN
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 57 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN setting |   |   | frontEnd.autoRanging.335 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1000<br>Value |   |   | 0: not OK<br>1: OK |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 49 -->

#### CHANGE ICP ACTION SETTING


**Semantics**

Scan when the ICP checking is being executed.

**To activate command**

At least one input must be of the ICP coupling type.
From the Analyzer Setting Browser, select the "Front-End → Input Settings → Check ICP"
setting and click on the [Run] button to start the ICP checking.

**Notification returned**

```
"frontEnd.inputSettings.353" = ICP IDN
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 58 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | frontEnd.inputSettings.353 |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 50 -->

#### CHANGE TEDS ACTION SETTING


**Semantics**

Scan when the ICP checking is being executed.

**To activate command**

At least one input must be of the ICP TEDS coupling type.
From the Analyzer Setting Browser, select the "Front-End → Input Settings → Detect TEDS"
setting and click on the [Run] button to start the TEDS checking.
Or click on the "detect TEDS" button from the "Acquisition / Transducers" ribbon.

**Notification returned**

```
"frontEnd.inputSettings.414" = Detect TEDS IDN
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 98 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | frontEnd.inputSettings.414 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 2008<br>IDN Input |   |   | null (not used) |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1009<br>Silent |   |   | 0: normal<br>1: silent |   |   |   |   |   |   |   |   |   |   |   |


<!-- page 51 -->
3.4.SETTINGS
This paragraph described the User Interface Notification related to the Settings command.

#### ACTIVATE SUB-MODULE COLLECTION


**Semantics**

Scan when an item from a sub-module collection is being activated/desabled.

**To activate command**

From the Analyzer Setting Browser, select a sub-module setting and right-click the
"Add/Remove" item to open a dialog box.
The sub-module collection is recognizable by an icon.
Example: Select the "FFT 1→ Channels" collection and open the Add/Remove dialog box.
Then select channel3.

**Notification returned**

```
"fft1.channel3" = example of String submodule IDN.
Warning, this command does not notify when adding/removing front-end inputs.
```

#### CHANGE SETTING


**Semantics**

Scan when a setting is modified.
Not used (hidden).

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 53 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | fft1.channel3 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1000<br>Property value |   |   | 0: Desable<br>1: Activate |   |   |   |   |   | 0 |   |   | 0 |   |   |


| Column 1 | Column 2 | Column 3 |
|---|---|---|
|   | Command ID |   |
| 54 |   |   |


<!-- page 52 -->

#### CHANGE STRING SETTING


**Semantics**

Scan when the value of a string setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select a string setting and assign a new string value.
The string setting is recognizable by an icon.
Example: Select the "Front-End → Inputs → Input 1 → Label" setting and write another
label.

**Notification returned**

```
"frontEnd.input1.label" = example of String setting IDN, for the Label setting above.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 60 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | frontEnd.input1.label |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 1000<br>Property value |   |   | "new value" |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 53 -->

#### CHANGE BOOLEAN SETTING


**Semantics**

Scan when the value of a boolean setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select a boolean setting and switch it.
The boolean setting is recognizable by an icon.
Example: Select the "Front-End → Inputs → Input 1 → Enable auto-range" setting and
tick/untick the box.

**Notification returned**

```
"frontEnd.input1.enableAutorange" = example of Boolean setting IDN, for the enable auto-
range setting.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 59 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | frontEnd.input1.enableAutorange |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1000<br>property<br>value |   |   | 0: Off<br>1: On |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 54 -->

#### CHANGE SCALAR SETTING


**Semantics**

Scan when the value of a scalar setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select a scalar setting and modify its value.
The scalar setting is recognizable by an icon.
Example: Select the "Front-End → Input Settings → Sensitivity" setting assign a new scalar
value.

**Notification returned**

```
"frontEnd.input1.sensitivity" = example of Scalar setting IDN, for the Sensitivity setting
above.
(V)/(V) is an example of the scalar setting unit.
```

#### CHANGE ENUMERATED SETTING


**Semantics**

Scan when the value of an enumerated setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select an enumerated setting and select an item from the
list.
The enumerated setting is recognizable by an icon.
Example: Select the "Front-End → Input Settings → High Input sampling" setting and select
an item from the list.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 64 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | frontEnd.input1.sensitivity |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 1000<br>property value |   |   | 'new value' |   |   | (V)/(V) |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 61 |   |   | 2 |   |   |


<!-- page 55 -->
"frontEnd.inputSettings.inputSampling" = example of Enumerated setting IDN, for the Label
setting above.
Note that the "new value" is a string value (example: "51200"), not the index from the
enumerated list.

#### CHANGE FORCE/RESPONSE WINDOWS SETTING


**Semantics**

Scan when one of the values of the Force or Response window setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select the "Time Windows → Force → Settings" or the
"Time Windows → Response → Settings" and change one of the window settings.
The force/response window setting is recognizable by an icon.

**Notification returned**

```
See property details below:
Force Window properties:
```

|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN<br>Setting |   |   | frontEnd.inputSettings.inputSampling |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 4<br>Enumerated |   |   | 1000<br>property<br>value |   |   | "new value" |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 62 |   |   | 9 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | window.328:1.226 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3102<br>Start value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3103<br>Stop value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3100<br>First value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3101<br>End value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3106<br>X Right value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3107<br>Y Right value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3104<br>X Left value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |


<!-- page 56 -->
Response Window properties:

#### CHANGE FRACTIONAL TACH SETTING


**Semantics**

Scan when one of the values of the fractional tach ratio setting is being changed.

**To activate command**

It is activated with a NVDrive command: "SetVirtualTachoSettingValue".

**Notification returned**

```
```

| 3<br>Float | 3105<br>Y Left Value | 'value' |   | 1 | 0 |
|---|---|---|---|---|---|


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | window.329:1.226 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3102<br>Start value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3103<br>Stop value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3100<br>First value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3101<br>End value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3106<br>X Right value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3107<br>Y Right value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3104<br>X Left value |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 3105<br>Y Left Value |   |   | 'value' |   |   |   |   |   | 1 |   |   | 0 |   |   |


<!-- page 57 -->
"tach.171:1.304" = "Tachometer - Fractional Tachs - Fractional tach. 1 - Tach ratio" IDN.
The float values are:
t a c h R a t i o =
D
N
e
u
n
m
o m
e r
i
a
n
t
a
o
t
r
o
1
r 1

D
N
e
u
n
m
o m
e r
i
a
n
t
a
o
t
r
o
2
r 2

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 67 |   |   | 5 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | tach.171:1.304 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 1003<br>Numerator1 |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 1004<br>Denominator 1 |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 1005<br>Numerator 2 |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   |   | 1006<br>Denominator 2 |   |   | 'value |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 58 -->

#### CHANGE SIGNAL FILE SETTING


**Semantics**

Scan when the signal file loaded in the Player module is being changed.

**To activate command**

From the Analyzer Setting Browser, select the "Player → Selected Record → Signal File"
setting select a signal file from a project.
The signal file setting is recognizable by an icon.

**Notification returned**

```
"player.90:1.233" = "Player - Signal File" IDN
```

#### CHANGE MATRIX SETTING


**Semantics**

Scan when the value of a matrix setting is being changed.

**To activate command**

From the Analyzer Setting Browser, select a matrix setting and add/remove an item.
The matrix setting is recognizable by an icon.
Example: When 2 inputs are connected to the FFT1 module, select the "FFT1→ FFT analysis
→ Cross Spectrum" setting and add a matrix cross between channel 2 and channel 1.

**Notification returned**

```
The number of properties depends on the number of couples selected in the matrix.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 65 |   |   | 3 |   |   |


|   | Type |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   | 1007<br>IDN Setting |   |   | player.90:1.233 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   | 1001<br>Project name |   |   | "name of the<br>project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   | 1002<br>Measure name |   |   | "name of the<br>measure" |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 63 |   |   | 3 to 501 |   |   |


|   | Type | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   | 1007<br>IDN Setting |   | fft1.363:1.205 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   | 3500<br>Matrix couple 1 |   | fft1.channel2;fft1.channel1 |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 59 -->
"fft1.363:1.205" = example of Matrix setting IDN, for the Cross Spectrum setting above.
For example, when adding a cross between Channel 1 and Channel 2, the two following
properties are added:
3500 = fft1.channel2;fft1.channel1 ➔ Channel 2 / Channel 1 cross spectrum enabled
3501 = fft1.channel1;fft1.channel2 ➔ Channel 1 / Channel 2 cross spectrum enabled

#### CHANGE TABLE SETTING


**Semantics**

Scan when one of the values of a line in a table setting is being changed.

**To activate command**

Use a NVDrive command: AddArrayLine (and NB Properties = 5).
You can either select a Table setting and add a new line from the Analyzer Setting Browser
(then NB Properties = 1).
The table setting is recognizable by an icon.
Example: Select the "FFT 1 → Channels→ Channel 1→ Tracked Order" setting and Click
on the [Add] button.

**Notification returned**

```
"fft1.channel1.251" = example of Table setting IDN, for the Tracked Order setting above.
The table index value is the index of the line added or modified.
The 'first value' and 'second value' correspond to the values assigned to the table line.
```

| 0<br>String | 3501<br>Matrix couple 2 | fft1.channel1;fft1.channel2 |   | 0 | 0 |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |
| 0<br>String | 3998<br>Matrix couple 499 | idny;idnx |   | 0 | 0 |
| 0<br>String | 3999<br>Matrix couple 500 | idnx;idny |   | 0 | 0 |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 66 |   |   | 5 |   |   |


|   | Type |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   | 1007<br>IDN Setting |   |   | fft1.channel1.251 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   | 4500<br>Table index |   |   | 'value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   | 4501<br>Table boolean |   |   | 0: disable<br>1: enable |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   | 4502<br>Table float 1 |   |   | 'first value' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 3<br>Float |   | 4502<br>Table float 2 |   |   | 'second value' |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 60 -->
For example, for a FFT tracked order table, the first value is the Order number, while the
second value is the Bandwidth.
If one of these values is "-1", it means that NVGate assigns the value by itself.

#### REMOVE LINE IN A TABLE SETTING


**Semantics**

Scan when a line is being removed from a table setting.

**To activate command**

From the Analyzer Setting Browser, select a Table setting and remove one of its lines.
Example: Select the "FFT 1 → Channels→ Channel 1→ Tracked Order" setting, select an
exiting item (or click on [Add] to add a line) and click on the [Remove] button.

**Notification returned**

```
"fft1.channel1.215" = example of a Table setting IDN, for the Tracked Order setting above.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 68 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 1007<br>IDN Setting |   |   | fft1.channel1.215 |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   |   | 4500<br>Table index |   |   | 'index of the<br>removed line'<br>[1 .. nbLines] |   |   |   |   |   |   |   |   |   |   |   |


<!-- page 61 -->
3.5.GRAPHS
This paragraph described the User Interface Notification related to the windows
command.

#### FULL SCREEN


**Semantics**

Scan when the Full Screen display mode is being switched.

**To activate command**

Click on the "Full Screen" button in the "Dispplay / Arrangement" ribbon to switch the Full
Screen mode.

**Notification returned**

```
```

#### SELECT WORKSPACE


**Semantics**

Scan when the Workspace tab is being changed.

**To activate command**

Select the "Analyzer Setting Brower / Control Panel / Project Manager" tab from the
Workspace.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 71 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 72 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 1200<br>Workspace |   |   | 0: Analyzer<br>Setting Browser<br>1: Control Panel<br>2: Project<br>Manager |   |   |   |   |   | 0 |   |   | 0 |   |   | 1 |   |   |


<!-- page 62 -->

#### SELECT WINDOW


**Semantics**

Scan when a window is being selected.

**To activate command**

Click inside a window to select it.

**Notification returned**

```
```

#### CHANGE LAYOUT


**Semantics**

Scan when another layout is being selected.

**To activate command**

Select the layout from the "Display / View" ribbon.
Or select the layout from the Project Manager.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 90 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden | Const |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 2600<br>Window name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   | 0 |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 36 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden | Const |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout<br>Name |   |   | "Name of the layout" |   |   |   |   |   | 0 |   | 0 |
| 2<br>Boolean |   |   | 801<br>Send<br>Message |   |   | 0: do not change<br>current layout<br>1: change current<br>layout |   |   |   |   |   | 0 |   | 0 |


<!-- page 63 -->

#### NEW LAYOUT


**Semantics**

Scan when a new layout is being created.

**To activate command**

Open the Add/Remove window dialog box.
Click on the [Create a New Layout] button:

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 41 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout<br>Name |   |   | "Name of<br>the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 2400<br>Layout<br>become<br>current |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 64 -->

#### ADD WINDOW RESULT


**Semantics**

Scan when a trace is being added to a Window.

**To activate command**

When adding inputs, tick the [AutoDisplay] box:

<!-- page 65 -->

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available Module ID are the one that can display results.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 79 |   |   | 11 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID' * |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel'* |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight<br>operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display unit<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time<br>operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |
| 9<br>User Enum |   |   | 1100<br>Arrange Style |   |   | -1 : Nothing<br>0: Tile Horizontally<br>1: Tile Vertically<br>2: Cascade<br>3: Automatic Tile<br>4: Grid |   |   |   |   |   | 0 |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 2608<br>WTF 2D |   |   | 0: No<br>1: Yes |   |   |   |   |   | 1 |   |   | 0 |   |   |   |   |   |


<!-- page 66 -->

#### ADD WINDOW WATERFALL RESULT


**Semantics**

Scan when a waterfall trace is being added to a Window.

**To activate command**

Use the corresponding NVDrive command.

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 81 |   |   | 10 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight<br>operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display unit<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time<br>operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |
| 9<br>User Enum |   |   | 1100<br>Arrange Style |   |   | 0: Tile Horizontally<br>1: Tile Vertically<br>2: Cascade<br>3: Automatic Tile<br>4: Grid |   |   |   |   |   | 0 |   |   | 0 |   |   | 0 |   |   |


<!-- page 67 -->

#### ADD WINDOW SAVED RESULT


**Semantics**

Scan when a result trace saved in a measurement is being displayed.

**To activate command**

Select the "Result" item from a Measurement saved in the Project Manager or select only one
of the traces from the "Result".
Right-click to select the "Display" item.

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can display result.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 80 |   |   | 11 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 901<br>Project name |   |   | "name of the project" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 902<br>Measure<br>name |   |   | "name of the measure" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel'* |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel'* |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight<br>operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display unit<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time<br>operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |


<!-- page 68 -->

#### ARRANGE WINDOWS


**Semantics**

Scan when windows are being arranged.

**To activate command**

From the "Display / Arrangement" ribbon, select one of the arrange window items (Cascade,
Tile Horizontally, Tile Vertically, Automatic Tile, Grid)

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 69 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 1100<br>Arrange Style |   |   | 0: Tile Horizontally<br>1: Tile Vertically<br>2: Cascade<br>3: Automatic Tile<br>4: Grid |   |   |   |   |   | 0 |   |   | 0 |   |   | 0 |   |   |


<!-- page 69 -->

#### AUTOSCALE XZ


**Semantics**

Scan when an Autoscale on X (or Z) is being performed on a Window.

**To activate command**

Select a Window.
Click on the [X/Z Adjust] button from the "Display / Scales" ribbon

**Notification returned**

```
```

#### AUTOSCALE Y


**Semantics**

Scan when an Autoscale on Y is being performed on a Window.

**To activate command**

Select a Window.
Click on the [AutoScale] button from the "Display / Scales" ribbon

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 82 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 5600<br>Apply to ... |   |   | 0: Current Window<br>1: All window |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 83 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 5600<br>Apply to ... |   |   | 0: Current Window<br>1: All window |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 70 -->

#### RESET ZOOM


**Semantics**

Scan when a window zoom is being reset.

**To activate command**

Select a window.
Click on the [Reset Scales] button from the "Display / Scales" ribbon.

**Notification returned**

```
```

#### CASCADE VIEW


**Semantics**

Scan when a window is being switched to/from the "Cascade View" mode.

**To activate command**

Right-click on the left side of a window containing traces and select/unselect the "Cascade
View" item.

**Notification returned**

```
```

#### TRACE ANALYSIS


**Semantics**

Scan when a module setting window is being displayed from a window trace.

**To activate command**

Right-click on the left side of a window containing trace and select the "Analysis ..." item.
Or double-click on the left side of a window containing trace.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 89 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 5600<br>Apply to ... |   |   | 0: Current Window<br>1: All window |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 84 |   |   | 0 |   |   |


<!-- page 71 -->

#### CHANGE WINDOW PREFERENCES


**Semantics**

Change window preferences.

**To activate command**

Internal command

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 100 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 111 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 6100<br>Parameters |   |   | "list of preference<br>values to change"<br>Format: [key=value;] |   |   |   |   |   | 0 |   |   | 0 |   |   |


| Key preferences | Descritption |
|---|---|
| background_color | Modify "Window background" preference. Possible<br>RGB value format:<br>- #RGB (each of R, G, and B is a single hex digit)<br>- #RRGGBB<br>- #RRRGGGBBB<br>- #RRRRGGGGBBBB<br>- A name from the list of SVG color names<br>provided by the World Wide Web Consortium; for<br>example, "steelblue" or "gainsboro". |


<!-- page 72 -->
3.6.PROJECT MANAGER
This paragraph described the User Interface Notification related to the Project Manager
commands.

#### OPEN PROJECT


**Semantics**

Open a project.

**To activate command**

Select a project from the Project Manager and right-click to select the "open and load setup"
item.
Or open the dialog box with the "File → Project →Open" menu and select a project.

**Notification returned**

```
```

#### LOAD PROJECT


**Semantics**

Scan when a project is being loaded.

**To activate command**

Use NVDrive command "LoadProject".

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 107 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 901<br>Project name |   |   | "Name of the Project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   |   | 919<br>Workbook<br>type |   |   | 0: Empty<br>1: Project<br>2: Model<br>3: Measurement<br>4: Current workbook<br>5: New Online<br>6: New Post analysis |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 900<br>Workbook<br>name |   |   | "Name of the<br>Workbook" |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 39 |   |   | 2 |   |   |


<!-- page 73 -->

#### LOAD WORKBOOK


**Semantics**

Scan when a workbook is being loaded.

**To activate command**

Select a project from the Project Manager, select its workbook and right-click to select the
"Load" item or the "Partial Load" item.

**Notification returned**

```
```

|   | Type |   | Name ID |   |   | Value |   |   | Unit | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 903<br>Database<br>Path |   | "Path of the<br>projects database" |   |   |   |   | 0 |   | 0 |   |   |
| 0<br>String |   |   | 901<br>Project<br>Name |   | "Name of the<br>Project" |   |   |   |   | 0 |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 40 |   |   | 11 |   |   |


|   | Type |   | Name ID |   |   | Value |   |   | Unit | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   | 901<br>Project Name |   |   | "Name of the<br>Project" |   |   |   |   | 0 |   | 0 |   |   |
| 0<br>String |   | 902<br>Measurement<br>Name |   |   | "Name of the<br>Measurement" |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 903<br>Load<br>Configuration |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 904<br>Load Control<br>Panel |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 905<br>Load Layouts |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 906<br>Load Save<br>Setup |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 907<br>Load Print<br>Setup |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 918<br>Load Alarm |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 2<br>Boolean |   | 921<br>Load Mask |   |   | 0: No<br>1: Yes |   |   |   |   | 0 |   | 0 |   |   |
| 0<br>String |   | 911<br>Project Path |   |   | "Path of the<br>Project" |   |   |   |   | 0 |   | 0 |   |   |


<!-- page 74 -->

#### EDIT MEASUREMENT


**Semantics**

Scan when a measurement is being loaded.

**To activate command**

Right-Click on a Measurement from the Project Manager.
Select the "Edit" item.

**Notification returned**

```
```

#### REMOVE PROJECT


**Semantics**

Scan when a project is being removed.

**To activate command**

Select the Project from the Project Manager.
Right-Click and Select the "Remove" item.

**Notification returned**

```
```

| 2<br>Boolean | 913<br>Save Previous<br>Workbook | 0: No<br>1: Yes |   | 0 | 0 |
|---|---|---|---|---|---|


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 38 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 901<br>Project<br>Name |   |   | "Name of the Project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 902<br>Measure<br>Name |   |   | "Name of the Measure" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 910<br>Save |   |   | 0: Do not save Current<br>Workbook<br>1: Save Current<br>Workbook |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 44 |   |   | 1 |   |   |


|   | Type |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   | 901<br>Project<br>Name |   |   | "Name of<br>the Project' |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 75 -->

#### RESET WORKBOOK


**Semantics**

Scan when a workbook is being reset.

**To activate command**

Select the "Reset" button from the "Home / Setup" ribbon.

**Notification returned**

```
```

#### REMOVE MEASUREMENT


**Semantics**

Scan when a measurement is being removed.

**To activate command**

Select the Measurement from the Project Manager.
Right-Click and Select the "Remove" item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 45 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 43 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 901<br>Project<br>Name |   |   | "Name of the<br>Project' |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 902<br>Measurement<br>Name |   |   | "Name of the<br>Measurement" |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 76 -->

#### SAVE PROJECT


**Semantics**

Scan when a project is being saved.

**To activate command**

Select "File → Project → Save" menu.
Or select the current project from the Project Manager and right-click to select the "Save"
item.

**Notification returned**

```
```

#### SAVE PROJECT AS


**Semantics**

Scan when a project is being saved with a new name.

**To activate command**

Select "File → Project → Save as" menu.
Or select the current project from the Project Manager and right-click to select the "Save as"
item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 48 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 6000<br>Need to confirm |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 49 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 2900<br>Project Name |   |   | "New Project<br>Name" |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 77 -->

#### SAVE WORKBOOK


**Semantics**

Scan when workbook(s) is (are) being saved.

**To activate command**

This command is no more available from the NVGate menu.
Nevertheless, it can be called through the "SaveWorkbook" NVDrive command.

**Notification returned**

```
```

#### SAVE WORKBOOK AS MODEL


**Semantics**

Scan when workbook is being saved as a model.

**To activate command**

It can be called through the "SaveWorkbookModel" NVDrive command.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 51 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 6000<br>Need to confirm |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   |   | 6001<br>NB Workbook |   |   | "number of<br>workbook" |   |   |   |   |   | 0 |   |   | 0 |   |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 104 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 900<br>Workbook<br>Name |   |   | "Name of the<br>workbook model" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 1009<br>Silent |   |   | 0: normal<br>1: silent |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 917<br>Save signal |   |   | 0: do not save<br>1: save signal |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 920<br>Is autosave |   |   | 0: inactive autosave<br>1: active autosave |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 78 -->

#### SAVE EDITED MEASUREMENT


**Semantics**

Scan when a measurement is being saved, while it is edited.

**To activate command**

Select a Measurement in the Project Manager.
Right-click on the "Edit" item.
Right-click on the "Save" item.

**Notification returned**

```
```

#### SAVE MEASUREMENT


**Semantics**

Scan when a default measurement is being saved with a name in the Result mode.

**To activate command**

Set the "Save Option" to "In Default Measurement".
Select result(s) to save.
Run the analyzer.
When the analyzer stops, the results are saved under « Default Measurement ».
Right-click on this Default Measurement and select the « Save Measurement » item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 47 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 6000<br>Need to<br>confirm |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |


|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 46 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 902<br>Measurement<br>name |   |   | "Name of the<br>Measurement" |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 908<br>Keyword |   |   | "keyword_value" |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 909<br>Measurement<br>comment |   |   | "comment_value" |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 79 -->

#### CHANGE PROJECT DATABASE


**Semantics**

Scan when the project database is being switched between Common and Private, by a user
which is not the default user.

**To activate command**

Right click in the "Project Manager" space, and select "Common Base" or "Private Base".

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 97 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 1000<br>Property value |   |   | 0: switch to<br>Private base<br>1: switch to<br>Common base |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 80 -->
3.7.SIGNAL
This paragraph described the User Interface Notification related to the recorded signal.

#### DOWNLOAD


**Semantics**

Scan when a signal is being downloaded from the OR3X internal disk to the PC.

**To activate command**

Select a project containing a signal file from the Project Manager.
Right-Click on the signal item and select "Download".

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 37 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 901<br>Project<br>Name |   |   | "Name of the Project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 902<br>Measurement<br>Name |   |   | "Name of the<br>Measurement" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 3000<br>Remove<br>from OR3X |   |   | 0: Do not remove file<br>from OR3X<br>1: Remove file from<br>OR3X |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 81 -->

#### UPLOAD


**Semantics**

Scan when a signal is being uploaded from the PC to the OR3X internal disk.

**To activate command**

Select a project containing a signal file from the Project Manager.
Right-Click on the signal item and select "Upload".

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 52 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 901<br>Project Name |   |   | "Name of the<br>Project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 902<br>Measurement<br>Name |   |   | "Name of the<br>Measurement" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 3001<br>Remove from<br>PC |   |   | 0: Do not<br>remove file<br>from PC<br>1: Remove<br>file from PC |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 82 -->

#### PREVIEW SIGNAL


**Semantics**

Scan when the recorded signal is being displayed.

**To activate command**

Select a signal from a project in the Project Manager.
Right-click and select the "Preview" or "Load and Preview" item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 87 |   |   | 6 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the<br>layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 901<br>Project name |   |   | "name of the<br>project" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 902<br>Measurement<br>name |   |   | "name of the<br>measurement" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 914<br>Loaded in<br>Player |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 1<br>Integer |   |   | 915<br>Nb Response |   |   | -1: all tracks<br>are displayed<br>1: number of<br>tracks<br>displayed |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 83 -->
3.8.RESULTS
This paragraph described the User Interface Notification related to the Results
management commands.

#### SETUP ADD RESULT


**Semantics**

Scan when result(s) is (are) added to the Save Setup dialog box.

**To activate command**

Click on "Save option" button, in the "Home / Save" ribbon".
Select the "Save Selection" tab:
Select the result(s) to be saved and add it (them) to the Result selection

<!-- page 84 -->

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can save results.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 91 |   |   | 7 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 2601<br>Analyzer saver |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 6 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display<br>unit operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |


<!-- page 85 -->

#### SETUP PARAMETERS


**Semantics**

Scan when the Base Name and Auto-increment parameters are being changed in the Save
Setup dialog box.

**To activate command**

Click on "Save option" button, in the "Home / Save" ribbon".
Select the "Save Setup" tab:
Modify the "Base Name" and the "Auto-increment" parameter.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 92 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 2700<br>Base<br>measurement<br>name |   |   | "name of the base" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2701<br>Increment |   |   | 0: Number<br>1: Date |   |   |   |   |   | 0 |   |   | 0 |   |   | 11 |   |   |


<!-- page 86 -->

#### SAVE RESULTS


**Semantics**

Scan when results are being saved.

**To activate command**

Results must be selected in the "Result Setup" dialog box.
Click on the "Save Measurement" button to save Results.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 50 |   |   | 1 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2<br>Boolean |   |   | 5500<br>Need to confirm<br>name |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 87 -->

#### REMOVE ALL RESULT


**Semantics**

Scan when all results are being removed from the Save Setup dialog box.

**To activate command**

Select the "File → Setup" menu.
Select the "Save Selection" tab:
Click on the [Reset all selected results] button.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 93 |   |   | 0 |   |   |


<!-- page 88 -->

#### REMOVE RESULT


**Semantics**

Scan when result(s) is (are) being removed from the Save Setup dialog box.

**To activate command**

Select the "File → Setup" menu.
Select the "Save Selection" tab:
Select the result(s) to be removed and click on the [Remove a result] button.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 94 |   |   | 7 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 9<br>User Enum |   |   | 2601<br>Analyzer saver |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 6 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of<br>process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response<br>channel'* |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference<br>channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 89 -->
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).

| 9<br>User Enum | 2605<br>Weight operator | 'Type of weight<br>operator'* |   | 0 | 0 | 8 |
|---|---|---|---|---|---|---|
| 9<br>User Enum | 2607<br>Display unit operator | 'Type of display<br>unit operator'* |   | 0 | 0 | 10 |
| 9<br>User Enum | 2606<br>Time operator | 'Type of time<br>operator'* |   | 0 | 0 | 9 |


<!-- page 90 -->
3.9.AUTOMEMORIZE
This paragraph describes the User Interface Notification related to the Automemorize
commands.

#### ADD RESULT TO AUTOMEMORIZE


**Semantics**

Scan when a trace is being added to the window with the automemorize function.

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Automatic Memorization ..." item:
Select the trace(s) to be memorized.

<!-- page 91 -->

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can display result.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 78 |   |   | 9 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display<br>unit operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |


<!-- page 92 -->

#### ENABLE AUTOMEMORIZE


**Semantics**

Scan when the "Enable/Disabled" parameter for the automemorize traces is being changed.

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Automatic Memorization ..." item:
Select the Enable or Disable Memorization choice.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 85 |   |   | 3 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout<br>name |   |   | "name of the<br>layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 5800<br>Activate |   |   | 0: Disable<br>1: Enable |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 93 -->

#### MEMORIZE TRACE


**Semantics**

Scan when a trace is being memorized.

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Memorize Trace" item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 86 |   |   | 0 |   |   |


<!-- page 94 -->

#### REMOVE RESULT FROM AUTOMEMORIZE


**Semantics**

Scan when trace is being removed from the window with the automemorize function.

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Automatic Memorization ..." item:
Unselect the trace(s) to be removed.

<!-- page 95 -->

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can display result.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 88 |   |   | 10 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight operator |   |   | 'Type of weight<br>operator' |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display<br>unit operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |
| 2<br>Boolean |   |   | 2608<br>WTF 2D |   |   | 0: No<br>1: Yes |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 96 -->

#### ADD AUTOMATIC OPERATOR


**Semantics**

Scan when a trace is being added to the window with the operator function (for memorized
traces).

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Operators-Arithmetic Average..." or "Operators - Quadratric Average..." item:
In the "Automatic" frame, tick the [Add new traces to operand list] box and select either the
"All compatible traces" or the "Memorized traces" item.

<!-- page 97 -->

**Notification returned**

```
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can display result.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 76 |   |   | 14 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout<br>name |   |   | "name of the<br>layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 13 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight<br>operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Display unit<br>operator |   |   | 'Type of display<br>unit operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time<br>operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |
| 9<br>User Enum |   |   | 5700<br>Operand<br>type |   |   | 0 : arithmetic<br>average<br>1 : quadratic<br>average |   |   |   |   |   | 0 |   |   | 0 |   |   | 29 |   |   |
| 9<br>User Enum |   |   | 5701<br>Operand<br>selection<br>type |   |   | 0 : memorized<br>traces<br>1 : all compatible<br>traces |   |   |   |   |   | 0 |   |   | 0 |   |   | 30 |   |   |
| 0<br>String |   |   | 5702<br>Operand<br>name |   |   | 'name of the<br>operand trace' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 2<br>Boolean |   |   | 5703<br>Frequency<br>domain |   |   | 0: Real/Imag.<br>(time)<br>1: Module<br>(frequency) |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 3<br>Float |   |   | 5704<br>X Step |   |   | 'value of the step' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 98 -->

#### ADD AUTOMATIC OPERATOR SAVED RESULT


**Semantics**

Scan when a trace is being added to the window with the operator function (for memorized
traces), for a saved result.

**To activate command**

Display saved result(s) from a measurement.
Right-click on the left side of a window displaying traces.
Select the "Operators-Arithmetic Average..." or "Operators - Quadratric Average..." item:
In the "Automatic" frame, tick the [Add new traces to operand list] box and select either the
"All compatible traces" or the "Memorized traces" item.
.

<!-- page 99 -->
* These enumerated types are described in the NVDrive Reference Manual (Result Format
and Description).
The available module ID are the plugs-in that can display result.

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 77 |   |   | 16 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |   | EnumType |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 800<br>Layout name |   |   | "name of the<br>layout" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 2600<br>Window<br>name |   |   | "name of the<br>window" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 901<br>Project<br>Name |   |   | "name of the<br>project" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 0<br>String |   |   | 902<br>Measurement<br>Name |   |   | "name of the<br>measurement" |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2601<br>Analyzer<br>displayer |   |   | 'module ID'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 6 |   |   |
| 9<br>User Enum |   |   | 2602<br>Process |   |   | 'type of process'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 7 |   |   |
| 1<br>Integer |   |   | 2603<br>Response |   |   | 'response channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 1<br>Integer |   |   | 2604<br>Reference |   |   | 'reference channel' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 9<br>User Enum |   |   | 2605<br>Weight<br>operator |   |   | 'Type of weight<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 8 |   |   |
| 9<br>User Enum |   |   | 2607<br>Unit operator |   |   | 'Type of unit<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 10 |   |   |
| 9<br>User Enum |   |   | 2606<br>Time<br>operator |   |   | 'Type of time<br>operator'* |   |   |   |   |   | 0 |   |   | 0 |   |   | 9 |   |   |
| 9<br>User Enum |   |   | 5700<br>Operand type |   |   | 0: arithmetic<br>average<br>1: quadratic average |   |   |   |   |   | 0 |   |   | 0 |   |   | 29 |   |   |
| 9<br>User Enum |   |   | 5701<br>Operand auto<br>type |   |   | 0: memorized traces<br>1: all compatible<br>traces |   |   |   |   |   | 0 |   |   | 0 |   |   | 30 |   |   |
| 0<br>String |   |   | 5702<br>Operand<br>name |   |   | 'name of operand<br>trace' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 2<br>Boolean |   |   | 5703<br>Frequency<br>domain |   |   | 0: Real/Imag. (time)<br>1: Module<br>(frequency) |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |
| 3<br>Float |   |   | 5704<br>X Step |   |   | 'value of the step' |   |   |   |   |   | 0 |   |   | 0 |   |   |   |   |   |


<!-- page 100 -->

#### CLEAR MEMORY


**Semantics**

Scan when memorized trace(s) is (are) being cleared from a window.

**To activate command**

Right-click on the left side of a window displaying traces.
Select the "Clear Memory" item.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 99 |   |   | 0 |   |   |


<!-- page 101 -->
3.10.REPORTS

#### REFRESH REPORT


**Semantics**

Refresh the report.

**To activate command**

Use the "Refresh" button in the "Report / Active file" ribbon.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 108 |   |   | 0 |   |   |


<!-- page 102 -->

#### PRINT REPORT


**Semantics**

Print the report.

**To activate command**

Use the "Print" button in the "Report / Active file" ribbon.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 109 |   |   | 0 |   |   |


<!-- page 103 -->

#### REFRESH AND PRINT REPORT


**Semantics**

Refresh and print the report.

**To activate command**

Use the "Refresh and Print" button in the "Report" tab.

**Notification returned**

```
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 110 |   |   | 0 |   |   |


<!-- page 104 -->
MISCELLANEOUS

#### ADD TO CONTROL PANEL


**Semantics**

Scan when an item (setting, state or macro) is being added to the Control Panel

**To activate command**

Right-Click on a setting from the Analyzer Setting Browser and select the "Add to Control
Panel" item.

**Notification returned**

```
Note that the "status" and "macros" added to the control panel cannot be scanned with this
command.
```

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 35 |   |   | 5 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 3400<br>Tab Name |   |   | "name of the<br>tab" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 3401<br>Setting<br>Name |   |   | "name of the<br>setting" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 0<br>String |   |   | 3402<br>Setting<br>IDN |   |   | "idnA" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 3404<br>Tab Active |   |   | 0: FALSE<br>1:TRUE |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 3403<br>IsState |   |   | 0: other<br>1: state |   |   |   |   |   | 0 |   |   | 0 |   |   |


<!-- page 105 -->

#### LAUNCH LINK


**Semantics**

Scan when an application is being launched from NVGate.

**To activate command**

This command can be sent with the « execute » button from the "Automation / Links" ribbon
.

**Notification returned**

```
```

#### COMPLEX


**Semantics**

Not used (hidden).

|   | Command ID |   |   | NB Properties |   |
|---|---|---|---|---|---|
| 4 |   |   | 2 |   |   |


|   | Type |   |   | Name ID |   |   | Value |   |   | Unit |   |   | Hidden |   |   | Const |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0<br>String |   |   | 4800<br>Application<br>launched |   |   | "AppName.exe" |   |   |   |   |   | 0 |   |   | 0 |   |   |
| 2<br>Boolean |   |   | 4801<br>Wait End |   |   | 0: do not wait the<br>application to be<br>launched.<br>1: wait the<br>application to be<br>launched. |   |   |   |   |   | 0 |   |   | 0 |   |   |


| Column 1 | Column 2 | Column 3 |
|---|---|---|
|   | Command ID |   |
| 96 |   |   |


<!-- page 106 -->
TABLES
TABLE 1: Property Type Identifier

| Identifier | Value |
|---|---|
| 0 | String |
| 1 | Integer |
| 2 | Boolean |
| 3 | Float |
| 4 | Enumerated setting |
| 5 | Enumerated State |
| 6 | Filename |
| 7 | Constant |
| 8 | Boolean Constant |
| 9 | Enumerated User |
| 10 | Enumerated Unit |
| 11 | Integer Constant |
| 12 | Enumerated Alarm |
| 13 | String Constant |
| 14 | String or Constant |
| 15 | Float Constant |
| 16 | Scalar Constant |
| 17 | Scalar |
| 18 | Enumerated Magnitude |


<!-- page 107 -->
TABLE 2: Enumerated Property Type Identifier

| Identifier | Value |
|---|---|
| 0 | Arrange Window type |
| 1 | Workspace Tab type |
| 2 | Dockable Window type |
| 3 | Toolbar type |
| 4 | Analyzer (player included) |
| 5 | Template |
| 6 | Analyzers that can save results |
| 7 | Result Type |
| 8 | Weigth operator type |
| 9 | Time operator type |
| 10 | Display unit operator |
| 11 | Measurement increment type |
| 12 | Analyzers on which input can be connected to |
| 13 | Analyzers that can display results |
| 14 | Analyzer states |
| 15 | Real Time Trigger |
| 16 | Save Mode |
| 17 | Condition on a simple alarm template |
| 18 | Applied mode |
| 19 | Applied mode action |
| 20 | Analyzers that can be a Waterfall source |
| 21 | Rough source Result<br>(example: global level instead of DC, RMS, Skew ...) |
| 22 | Rough Source Waterfall result |
| 23 | Waterfall process |
| 24 | Time format print type |
| 25 | Scalar information type |
| 26 | Scalar change type |
| 27 | Enumerated information type |
| 28 | Enumerated change type |
| 29 | Operator type |
| 30 | Operator selection type |


<!-- page 108 -->
TABLE 3: Property Identifier

| Identifier | Value |
|---|---|
|   | Used in Change User |
| 100 | First name |
| 101 | Last name |
| 102 | Password |
|   | Used in Execute Macro |
| 200 | Macro name |
|   | Used in Loop For |
| 300 | Iteration count |
|   | Used in Message Box - Set Macro Parameter |
| 400 | Constant |
|   | Used in Message Box |
| 500 | Window caption |
| 501 | Prompt |
| 502 | True button caption |
| 503 | False button caption |
|   | Used in Set Macro Parameter |
| 600 | Comment |
|   | Used in Change Layout / New Layout / Add Window Result /<br>Add Window Saved Result / Change Window Preferences |
| 800 | Layout name |
|   | Used in Change Layout |
| 801 | Send message |
|   | Used in Load Workbook |
| 900 | Workbook name |
|   | Used in Load Workbook / Add Window Saved Result / Remove<br>Measurement / Save Project As / Download |
| 901 | Project name |
| 902 | Measurement name |
| 903 | Project base |
|   | Used in Load Workbook |
| 903 | Load configuration |
| 904 | Load control panel |
| 905 | Load layouts |
| 906 | Load save setup |
| 907 | Load print setup |
| 908 | Keyword |
| 909 | Measurement comment |
| 910 | Saving |
| 911 | Load directory |
| 912 | What to load |
| 913 | Save previous |
|   | Used in Preview Signal |
| 914 | Is in player |


<!-- page 109 -->

| Error code | Meaning |
|---|---|
| 915 | NB Response |
|   | Used in Change Boolean Setting - Change String Setting -<br>Change Enumerated Setting - Change Scalar Setting - Change<br>Signal File Setting |
| 1000 | Value |
| 1001 | Project value |
| 1002 | Measurement value |
| 1003 | Numerator 1 |
| 1004 | Denominator 1 |
| 1005 | Numerator 2 |
| 1006 | Denominator 2 |
| 1007 | IDN setting value |
| 1008 | IDN Slave |
|   | Used in Arrange Windows |
| 1100 | Style |
|   | Used in Select Workspace |
| 1200 | Workspace |
|   | Used in Toggle Dockable Window - Toggle Toolbar - Toggle<br>Module State |
| 1300 | Show |
|   | Used in Toggle Dockable Window |
| 1400 | Dockable Window |
|   | Used in Toggle Toolbar |
| 1500 | Toolbar |
|   | Used in Change Window Refresh Rate |
| 1600 | Window refresh rate |
|   | Used in Set Unit To Magnitude |
| 1700 | Current Unit |
| 1701 | Magnitude ID |
|   | Used in Toggle Module State |
| 1800 | Module |
|   | Used in Select Report Template |
| 1900 | Template name |
|   | Used in Timer Loop |
| 2000 | Time lap |
|   | Used in Affectation |
| 2100 | Right operator affectation |
| 2101 | Left operator affectation |
|   | Used in Incrementation |
| 2200 | Parameter |
| 2201 | Incrementation value |
|   | Used in Wait |
| 2300 | Waiting time |
|   | Used in New Layout |
| 2400 | New layout become current |


<!-- page 110 -->

| Error code | Meaning |
|---|---|
|   | Used in New Measurement Preference Parameter |
| 2501 | Save immediately |
| 2502 | Skip confirmation |
| 2503 | Save mode |
|   | Used in Add Window Result - Add Window Saved Result -<br>Change Window Preferences |
| 2600 | Window name |
|   | Used in Add Window Result - Add Window Saved Result -<br>Setup Add Result |
| 2601 | Analyzer |
| 2602 | Process |
| 2603 | Response |
| 2604 | Reference |
| 2605 | Weight operator |
| 2606 | Time operator |
| 2607 | Diplay Unit operator |
| 2608 | Waterfall 2D |
|   | Used in Setup Parameters |
| 2700 | Measurement base name |
| 2701 | Increment |
|   | Used in Connect Input |
| 2800 | Input |
| 2801 | Channel |
| 2802 | Player track |
| 2803 | Module source |
|   | Used in Save Project As |
| 2900 | Project save as name |
|   | Used in Download |
| 3000 | Remove file from OR3X |
|   | Used in Upload |
| 3001 | Remove file from PC |
|   | Used in Change Force/Response Windows Setting |
| 3100 | First |
| 3101 | End |
| 3102 | Start |
| 3103 | Stop |
| 3104 | X Left |
| 3105 | Y Left |
| 3106 | X right |
| 3107 | Y right |
|   | Used in Post Analysis |
| 3200 | Switch to post analysis |
|   | Used in Applied Mode |
| 3300 | Applied mode |
| 3301 | Applied mode change |
|   | Used in Add To Control Panel |
| 3400 | Control Panel Tab name |
| 3401 | Setting name |
| 3402 | Setting IDN |
| 3403 | Setting state |


<!-- page 111 -->

| 3404 | Setting active tab |
|---|---|
|   | Used in Change Matrix Setting |
| 3500<br>to<br>3999 | Matrix Couple 1<br>to<br>Matrix Couple 500 |
|   | Used in Change Table Setting |
| 4500 | Table Index |
| 4501 | Table boolean |
| 4502 | Table float 1 |
| 4503 | Table float 2 |
| 4504 | Waterfall module source |
| 4505 | Waterfall sub-module response |
| 4506 | Waterfall sub-module reference |
| 4507 | Waterfall process type |
|   | Used in Send Trace |
| 4600 | Play sound |
| 4601 | Message |
|   | Used in Make String |
| 4700 | String to add |
| 4701 | Add String |
|   | Used in Launch Link |
| 4800 | Application name |
| 4801 | Wait end |
|   | Used in Set Exec Macro Param - Get Exec Macro Param |
| 4900 | Macro parameter name |
| 4901 | Macro parameter value |
|   | Used in Get Time |
| 5000 | Time Format |
|   | Used in Get Scalar Value |
| 5100 | Module identifier |
| 5101 | Sub-module identifier |
| 5102 | Setting identifier |
| 5103 | Get scalar info |
|   | Used in Set Scalar Value |
| 5200 | Set scalar action |
|   | Used in Get Enumerated Value |
| 5300 | Get enumerated information |
|   | Used in Set Enumerated Value |
| 5400 | Set enumerated information |
|   | Used in Save Results |
| 5500 | Confirm name |
|   | Used in Autoscale XZ - Autoscale Y - Reset Zoom |
| 5600 | Apply to layout |
|   | Used in Add Automatic Operator |
| 5700 | Operator type |
| 5701 | Operator auto type |
| 5702 | Operator name |


<!-- page 112 -->

| 5703 | Frequency domain |
|---|---|
| 5704 | X step |
|   | Used in Enable AutoMemorize |
| 5800 | Activate |
|   | Used in Exec Command |
| 5900 | N command type |
|   | Used in Save Measurement / Save Workbook / Save Project |
| 6000 | Need to confirm |
|   | Used in Save Workbook |
| 6001 | NB Workbook |
|   | Used in Change Window Preferences |
| 6100 | Preference parameters |

