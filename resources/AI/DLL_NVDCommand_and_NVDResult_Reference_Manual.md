# DLL NVDCommand and NVDResult Reference Manual - Markdown mirror

> The C++ / Visual Basic entry points of the NVDrive DLLs, for driving NVGate without the Python library.
>
> Generated 2026-08-24 by `app/manual_to_markdown.py` from
> `DLL_NVDCommand_and_DLL_NVDResult_Reference_Manual.pdf` (159 pages), NVGate version 17.00.002.
>
> This file is an **automatic conversion** of the official manual, meant to be
> read by an AI tool or searched as text. Where the two disagree, the official
> PDF prevails. The `<!-- page N -->` markers let you locate any passage back
> in the PDF.

| Measure | Value |
|---|---|
| Pages converted | 159 |
| Headings rebuilt | 301 |
| Tables rendered | 4 |
| Original table-of-contents lines discarded | 115 |

## Contents

- [I - Introduction](#i---introduction)
- [II - DLL NVD_Result and DLL NVD_Command](#ii---dll-nvdresult-and-dll-nvdcommand)
  - [1 - Writing convention](#1---writing-convention)
  - [2 - NVGate connection](#2---nvgate-connection)
  - [3 - Error management](#3---error-management)
- [III - Functions of the DLL NVD_Result](#iii---functions-of-the-dll-nvdresult)
  - [1 - GetResult functions (commandFunctions)](#1---getresult-functions-commandfunctions)
  - [2 - Info Functions: HEAD](#2---info-functions-head)
  - [3 - Info Functions: XREG](#3---info-functions-xreg)
  - [4 - Info Functions: XREF](#4---info-functions-xref)
  - [5 - Info Functions: CVEC](#5---info-functions-cvec)
  - [6 - Info Functions: RVEC](#6---info-functions-rvec)
  - [7 - Info Functions: SCAL](#7---info-functions-scal)
  - [8 - Info Functions: DWTF](#8---info-functions-dwtf)
  - [9 - Info Functions: RWTF](#9---info-functions-rwtf)
  - [10 - Info Functions: CWTF](#10---info-functions-cwtf)
  - [11 - Info Functions: RNFO](#11---info-functions-rnfo)
- [IV - Functions for external result creation](#iv---functions-for-external-result-creation)
  - [1 - NVD_CreateTCPResultChannel](#1---nvdcreatetcpresultchannel)
    - [a - Command function](#a---command-function)
  - [2 - NVD_NewDataForTCPResultChannel](#2---nvdnewdatafortcpresultchannel)
    - [a - Command function](#a---command-function)
  - [3 - NVD_SetTCPResultChannel](#3---nvdsettcpresultchannel)
    - [a - Command function](#a---command-function)
  - [4 - NVD_AddDatatoTCPResultChannel](#4---nvdadddatatotcpresultchannel)
    - [a - Command function](#a---command-function)
- [V - Functions of the DLL NVD_Command](#v---functions-of-the-dll-nvdcommand)
  - [1 - NVD_Action](#1---nvdaction)
    - [a - Command function](#a---command-function)
  - [2 - NVD_CmdGetSettingValue](#2---nvdcmdgetsettingvalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [3 - NVD_CmdGetSettingValueString](#3---nvdcmdgetsettingvaluestring)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [4 - NVD_CmdGetSettingInfo](#4---nvdcmdgetsettinginfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [5 - NVD_CmdGetSettingValues](#5---nvdcmdgetsettingvalues)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [6 - NVD_CmdGetSettingValuesString](#6---nvdcmdgetsettingvaluesstring)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [7 - NVD_CmdEditSetting](#7---nvdcmdeditsetting)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [8 - NVD_CmdGetSignalFileSettingValues](#8---nvdcmdgetsignalfilesettingvalues)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [9 - NVD_CmdGetStateValue](#9---nvdcmdgetstatevalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [10 - NVD_CmdGetInputInfo](#10---nvdcmdgetinputinfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [11 - NVD_GetSubmoduleList](#11---nvdgetsubmodulelist)
    - [a - Command function](#a---command-function)
  - [12 - NVD_CmdGetTransducerInfo](#12---nvdcmdgettransducerinfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [13 - NVD_CmdGetTEDSContent](#13---nvdcmdgettedscontent)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [14 - NVD_CmdGetTEDSContentOnInput](#14---nvdcmdgettedscontentoninput)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [15 - NVD_CmdEditCalibration](#15---nvdcmdeditcalibration)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [16 - NVD_CmdGetMarkerList](#16---nvdcmdgetmarkerlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [17 - NVD_CmdGetFreeMarkerParameters](#17---nvdcmdgetfreemarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [18 - NVD_CmdGetPeakMarkerParameters](#18---nvdcmdgetpeakmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [19 - NVD_CmdGetPeakMarkerParametersEx](#19---nvdcmdgetpeakmarkerparametersex)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [20 - NVD_CmdGetMaxMarkerParameters](#20---nvdcmdgetmaxmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [21 - NVD_CmdGetMaxMarkerParametersEx](#21---nvdcmdgetmaxmarkerparametersex)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [22 - NVD_CmdGetPowerBandMarkerParameters](#22---nvdcmdgetpowerbandmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [23 - NVD_CmdGetSideBandMarkerParameters](#23---nvdcmdgetsidebandmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [24 - NVD_CmdGetHarmonicMarkerParameters](#24---nvdcmdgetharmonicmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [25 - NVD_CmdGetPeriodMarkerParameters](#25---nvdcmdgetperiodmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [26 - NVD_CmdGetRecordMarkerParameters](#26---nvdcmdgetrecordmarkerparameters)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [27 - NVD_CmdGetNumberOfRecordMarker](#27---nvdcmdgetnumberofrecordmarker)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [28 - NVD_CmdGetFreeMarkerValue](#28---nvdcmdgetfreemarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [29 - NVD_CmdGetPeakMarkerValue](#29---nvdcmdgetpeakmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [30 - NVD_CmdGetPeakMarkerValueEx](#30---nvdcmdgetpeakmarkervalueex)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [31 - NVD_CmdGetMaxMarkerValue](#31---nvdcmdgetmaxmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [32 - NVD_CmdGetMaxMarkerValueEx](#32---nvdcmdgetmaxmarkervalueex)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [33 - NVD_CmdGetPowerBandMarkerValue](#33---nvdcmdgetpowerbandmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [34 - NVD_CmdGetSideBandMarkerValue](#34---nvdcmdgetsidebandmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [35 - NVD_CmdGetHarmonicMarkerValue](#35---nvdcmdgetharmonicmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [36 - NVD_CmdGetPeriodMarkerValue](#36---nvdcmdgetperiodmarkervalue)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [37 - NVD_CmdGetAnalyzerModes](#37---nvdcmdgetanalyzermodes)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [38 - NVD_CmdGetUnitInfo](#38---nvdcmdgetunitinfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [39 - NVD_CmdGetMagnitudeList](#39---nvdcmdgetmagnitudelist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [40 - NVD_CmdGetMagnitudeInfo](#40---nvdcmdgetmagnitudeinfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [41 - NVD_CmdGetUnitList](#41---nvdcmdgetunitlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [42 - NVD_CmdGetCurrentUnit](#42---nvdcmdgetcurrentunit)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [43 - NVD_CmdGetTransducerList](#43---nvdcmdgettransducerlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [44 - NVD_CmdGetProjectList](#44---nvdcmdgetprojectlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [45 - NVD_CmdGetMeasureList](#45---nvdcmdgetmeasurelist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [46 - NVD_CmdGetWindowList](#46---nvdcmdgetwindowlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [47 - NVD_CmdGetWindowNameList](#47---nvdcmdgetwindownamelist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [48 - NVD_CmdGetLayoutList](#48---nvdcmdgetlayoutlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [49 - NVD_CmdGetCurrentLayout](#49---nvdcmdgetcurrentlayout)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [50 - NVD_CmdGetDisplayMode](#50---nvdcmdgetdisplaymode)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [51 - NVD_CmdGetDisplayModeList](#51---nvdcmdgetdisplaymodelist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [52 - NVD_CmdGetReferenceList](#52---nvdcmdgetreferencelist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [53 - NVD_CmdGetCurrentReference](#53---nvdcmdgetcurrentreference)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [54 - NVD_CmdGetPreferedWtfReference](#54---nvdcmdgetpreferedwtfreference)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [55 - NVD_CmdGetScaleInfo](#55---nvdcmdgetscaleinfo)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [56 - NVD_CmdGetAvailableScale](#56---nvdcmdgetavailablescale)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [57 - NVD_IsResultWaterfallisable](#57---nvdisresultwaterfallisable)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [58 - NVD_CmdGetWindowDisplayZone](#58---nvdcmdgetwindowdisplayzone)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [59 - NVD_CmdGetWindowTraces](#59---nvdcmdgetwindowtraces)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [60 - NVD_CmdGetActiveWindow](#60---nvdcmdgetactivewindow)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [61 - NVD_CmdGetWindowPosition](#61---nvdcmdgetwindowposition)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [62 - NVD_CmdGetRotationPreferences](#62---nvdcmdgetrotationpreferences)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [63 - NVD_CmdGetPinStatus](#63---nvdcmdgetpinstatus)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [64 - NVD_CmdGetResultCaption](#64---nvdcmdgetresultcaption)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [65 - NVD_CmdGetResultList](#65---nvdcmdgetresultlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [66 - NVD_CmdGetWtfResultList](#66---nvdcmdgetwtfresultlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [67 - NVD_CmdGetSavedResultCaption](#67---nvdcmdgetsavedresultcaption)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [68 - NVD_CmdGetSavedResultList](#68---nvdcmdgetsavedresultlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [69 - NVD_CmdGetTCPResultChannelList](#69---nvdcmdgettcpresultchannellist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [70 - NVD_CmdGetAnalyzer_TriggerState](#70---nvdcmdgetanalyzertriggerstate)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [71 - NVD_CmdGetAnalyzer_Count](#71---nvdcmdgetanalyzercount)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [72 - NVD_CmdGetAnalyzer_ RealTime](#72---nvdcmdgetanalyzer-realtime)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [73 - NVD_CmdGetAnalyzer_BlockOverload](#73---nvdcmdgetanalyzerblockoverload)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [74 - NVD_CmdGetAnalyzer_AnalysisOverload](#74---nvdcmdgetanalyzeranalysisoverload)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [75 - NVD_CmdGetAnalyzer_RecordCounter](#75---nvdcmdgetanalyzerrecordcounter)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [76 - NVD_CmdGetAnalyzer_TimeToStabilization](#76---nvdcmdgetanalyzertimetostabilization)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [77 - NVD_CmdGetAnalyzer_PerCentBlockLost](#77---nvdcmdgetanalyzerpercentblocklost)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [78 - NVD_CmdGetAnalyzer_PerCentBlockTransfered](#78---nvdcmdgetanalyzerpercentblocktransfered)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [79 - NVD_CmdGetEvent](#79---nvdcmdgetevent)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [80 - NVD_CmdGetStatus](#80---nvdcmdgetstatus)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [81 - NVD_CmdGetSignalProperties](#81---nvdcmdgetsignalproperties)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [82 - NVD_CmdGetRecordDate](#82---nvdcmdgetrecorddate)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [83 - NVD_CmdGetProjectProperties](#83---nvdcmdgetprojectproperties)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [84 - NVD_CmdGetProjectUserPropertiesList](#84---nvdcmdgetprojectuserpropertieslist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [85 - NVD_CmdGetMeasurementUserPropertiesList](#85---nvdcmdgetmeasurementuserpropertieslist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [86 - NVD_CmdGetCurrentNVGatePath](#86---nvdcmdgetcurrentnvgatepath)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [87 - NVD_CmdGetDatabasePath](#87---nvdcmdgetdatabasepath)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [88 - NVD_CmdGetCurrentProjectName](#88---nvdcmdgetcurrentprojectname)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [89 - NVD_CmdGetCurrentUserName](#89---nvdcmdgetcurrentusername)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [90 - NVD_CmdGetUserList](#90---nvdcmdgetuserlist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [91 - NVD_CmdGetMacroList](#91---nvdcmdgetmacrolist)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)
  - [92 - NVD_CmdGetPermission](#92---nvdcmdgetpermission)
    - [a - Command function](#a---command-function)
    - [b - Info Functions](#b---info-functions)


<!-- page 1 -->
DLL NVD_C
OMMAND
AND
DLL NVD_R
ESULT
R
EFERENCE MANUAL
DLL FOR A SIMPLIFIED ACCESS
TO THE NVDRIVE COMMANDS

| Compatibility | Identification | Updated |
|---|---|---|
| NVGate® V17.00 | F227-C05-22 | January 2024 |


<!-- page 6 -->

## I - Introduction

One of the main difficulties to use NVDrive is to decode the data block following the
header. The most meaningful example is the "GetResult" command. In order to simplify
the use of all the commands that return data, 2 DLL have been created:
DllNVDCommand and DllNVDResult.
There are 2 types of functions available in those DLLs:
- Command functions: functions which send a command to NVGate (name begins
with NVD_Cmd)
- Info functions: functions which enable to get information from a previous
command. Each of those functions is associated to a function NVD_Cmd.
An NVD_Command function must first be called, and then any associated function can
be called.
The purpose of this manual is to give prototypes (in C++ and Visual Basic) of functions
that replace an NVDrive command. The description of a command and its parameters is
already written in the NVDrive manual, so it is not reminded in this document.
NB: The commands that only return an error code are not present in the DLLs. One can
use NVD_Action to use them.

<!-- page 7 -->

## II - DLL NVD_Result and DLL NVD_Command


### 1 - Writing convention

In this document, the prototypes of functions are given for Visual C++ and Visual Basic.
For Visual C++, the header files:
NVD_Result_EntryPoint.h (for the NVD_Result DLL) and
NVD_Command_EntryPoint.h (for the NVD_Command DLL
must be added to the application using those DLL. They contain the prototype of all the
functions available in the DLL. The prototype is as follow:
EXPORT_API_DLLNVDRESULT int _stdcall NVD_CmdGetResult(...
The italic part will not be repeated in the rest of the document to lighten the writing. The
"EXPORT_API_DLLNVDRESULT" replace "__declspec(dllimport)", as defined in the
header file.
For Visual Basic, the .bas files:
NVD_Result_DllFunctions.bas (for the NVD_Result DLL) and
NVD_Command_DllFunctions.bas (for the NVD_Command DLL)
must be added to the application using those DLL. They contain the prototype of all the
functions available in the DLL. The prototype is as follow:
Declare Function NVD_CmdGetResult Lib "DllNVDResult" ( _
The italic part will not be repeated in the rest of the document to lighten the writing.

### 2 - NVGate connection

The return value of the following functions is "-1" if the action failed, or "0" if the
function succeeded.
a) Connection
The first thing to do in an application which wants to use those DLLs to communicate
with NVGate is to connect to NVGate. One function exists to do this. It has been added
to the 2 DLLs (because each DLL can be used independently), with different names:
- NVD_ResultConnect (in the NVD_Result DLL)
- NVD_CommandConnect (in the NVD_Command DLL)

<!-- page 8 -->
The connection must be done once (with NVD_ResultConnect or NVD_
CommandConnect). This connection creates a unique socket.
The prototype is as follow:
- Visual C++ declaration:
int NVD_CommandConnect(int nPort,
char* szAdress,
int nSocket);
- Visual Basic declaration:
NVD_CommandConnect(ByVal nPort As Long,
ByVal szAdress As String,
ByVal nsocket As Long) As Long
Using the 2 DLLs needs to connect NVDCommand and then to affect the created socket
to the NVDResult DLL:
- Visual C++ declaration:
int NVD_ResultAffectSocket(int nSocket);
- Visual Basic declaration:
NVD_ResultAffectSocket(ByVal nSocket As Long) As Long
Debug option
A similar prototype of the connection command is available for debugging:
- Visual C++ declaration:
int NVD_CommandConnectEx(int nPort,
char* szAdress,
int nSocket,
char* szTraceFile);
- Visual Basic declaration:
NVD_CommandConnectEx(ByVal nPort As Long,
ByVal szAdress As String,
ByVal nsocket As Long,
ByVal szTraceFile As String) As Long

<!-- page 9 -->
The parameter szTraceFile is optional and should be used only for debuging. When this
parameter is filled, a file with the given name is created. It will contain a trace of every
data sent and received on the socket.
b) Initialisation
The DLLs store data into several arrays, which need to be initialized - before being
used - in function of the number of sockets used (nNbSockets parameter).
For the NVDCommand DLL:
- Visual C++ declaration:
InitBufferContents(int nNbSockets)
- Visual Basic declaration:
InitBufferContents(ByVal nNbSockets As Long)
For the NVDResult DLL:
- Visual C++ declaration:
InitpResults(int nNbSockets)
- Visual Basic declaration:
InitpResults(ByVal nNbSockets As Long)
c) Deletion
This step is necessary to free memory used by the data arrays.
For the NVDCommand DLL:
- Visual C++ declaration:
void DeleteBufferContents()
- Visual Basic declaration:
DeleteBufferContents()

<!-- page 10 -->
For the NVDResult DLL:
- Visual C++ declaration:
void DeletepResult()
- Visual Basic declaration:
InitpResults()
d) Disconnection
The last thing to do before ending the application is to disconnect the application from
NVGate.
- Visual C++ declaration:
int NVD_DisConnect(int nSocket, BOOL bDoClose = TRUE) ;
- Visual Basic declaration:
NVD_DisConnect(ByVal nSocket As Long, _
ByVal bDoClose As Boolean) As Long
The nSocket parameter identifies the socket.
The bDoClose parameter must be equal to TRUE (in order to close properly the socket
before deleting it).

### 3 - Error management

When an NVDrive command fails, the returned header consists of an error code
(composed of 10 characters). For each DLL, a function exists in order to get the last
error.
- Visual C++ declaration:
int GetResultLastError(int nSocket, char* szError) ; // for the NVD_Result DLL
int GetCommandLastError(int nSocket, char* szError) ;// for the NVD_Command
DLL
- Visual Basic declaration:

<!-- page 11 -->
GetResultLastError (ByVal nSocket As Long, _
ByVal szError As String) As Long
GetCommandLastError (ByVal nSocket As Long, _
ByVal szError As String) As Long
If a command function fails (return "-1"), the "Get...LastError" function can be called to
a precisions about the error.
If an info function fails (return "-1"), the reason is that the command function previously
called is not associated to this info function.
The following commands enable to translate the last error code into a description of this
error:
- Visual C++ declaration:
int NVD_CmdGetErrorMessage(int nSocket, char* szError);
int GEM_GetErrorMessage(int nSocket, char* szMessage, int nBufferSize);
- Visual Basic declaration:
NVD_CmdGetErrorMessage(ByVal nSocket As Long, _
ByVal szError As String) As Long
GEM_GetErrorMessage (ByVal nSocket As Long, _
ByVal szMessage As String, _
ByVal nBufferSize As Long) As Long

<!-- page 12 -->

## III - Functions of the DLL NVD_Result

There are 3 command functions in this DLL. They enable to get Result characteristics
and values. As those functions ask for the same kind of information, they have the same
associated Info Functions.
The Results in NVGate are structured in blocks (HEAD, XREG, XREF, CVEC, RVEC,
SCAL, DWTF, RWTF, CWTF, INFO and RNFO). For more information about Results,
see the NVDrive user manual.
The return value of any function is "-1" if the action failed, or "0" if the function
succeeded.

### 1 - GetResult functions (commandFunctions)

NVD_CmdGetResult
This function runs the "GetResult" NVDrive command. The version parameter of the
NVDrive command corresponds to the "nVersionToSend" following parameter.
- Visual C++ declaration:
int NVD_CmdGetResult(
int nSocket,
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel,
unsigned short bGlobalLevel,
unsigned short bPondGlobalLevel,
unsigned short nVersionToSend);
- Visual Basic declaration:
NVD_CmdGetResult(ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nProcess As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer, _
ByVal bGlobalLevel As Integer, _
ByVal bPondGlobalLevel As Integer, _
ByVal nVersionToSend As Integer) As Long
NVD_CmdGetWtfResult
This function runs the "GetWtfResult" NVDrive command. The version parameter of the
NVDrive command corresponds to the "nVersionToSend" following parameter.

<!-- page 13 -->
- Visual C++ declaration:
int NVD_CmdGetWtfResult(
int nSocket,
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel,
unsigned short bGlobalLevel,
unsigned short bPondGlobalLevel,
unsigned short nVersionToSend,
int nStartIndex,
int nWillSize);
- Visual Basic declaration:
NVD_CmdGetWtfResult (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nProcess As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer, _
ByVal bGlobalLevel As Integer, _
ByVal bPondGlobalLevel As Integer, _
ByVal nVersionToSend As Integer, _
ByVal nStartIndex As Integer, _
ByVal nWillSize As Integer) As Long
NVD_CmdGetResultEx
This function runs the "GetResultEx" NVDrive command. The version parameter of the
NVDrive command is the result block last version.
- Visual C++ declaration:
int NVD_CmdGetResultEx(
int nSocket,
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel,
unsigned short bWaterfall);
- Visual Basic declaration:
NVD_CmdGetResultEx(ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nProcess As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer, _
ByVal bWaterfall As Integer) As Long

<!-- page 14 -->
NVD_CmdGetSavedResult
This function runs the "GetSavedResult" NVDrive command. The version parameter of
the NVDrive command is the result block last version.
- Visual C++ declaration:
int NVD_CmdGetSavedResult(
int nSocket,
char* szProjectName,
char* szMeasurementName,
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel,
unsigned short bGlobalLevel,
unsigned short bPondGlobalLevel,
unsigned short nVersionToSend);
- Visual Basic declaration:
NVD_CmdGetSavedResult Lib "DllNVDResult" ( _
ByVal nSocket As Long, _
ByVal szProjectName As String, _
ByVal szMeasurementName As String, _
ByVal nModule As Integer, _
ByVal nProcess As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer, _
ByVal bGlobalLevel As Integer, _
ByVal bPondGlobalLevel As Integer, _
ByVal nVersionToSend As Integer) As Long
Note: If there is no reference channel, nRefChannel must be equal to 0.
NVD_CmdGetSavedResultEx
This function runs the "GetSavedResultEx" NVDrive command. The version parameter
of the NVDrive command is the result block last version.
- Visual C++ declaration:
int NVD_CmdGetSavedResultEx(
int nSocket,
char* szProjectName,
char* szMeasurementName,

<!-- page 15 -->
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel,
unsigned short bWaterfall);
- Visual Basic declaration:
NVD_CmdGetSavedResultEx Lib "DllNVDResult" ( _
ByVal nSocket As Long, _
ByVal szProjectName As String, _
ByVal szMeasurementName As String, _
ByVal nModule As Integer, _
ByVal nProcess As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer, _
ByVal bWaterfalll As Integer) As Long
Note: If there is no reference channel, nRefChannel must be equal to 0.
NVD_CmdGetResultRecordSignalBlock
This function runs the "CmdGetResultRecordSignalBlock" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetResultRecordSignalBlock(
int nSocket,
size_t track,
uint64_t firstSample,
size_t size,
bool details,
size_t recordId = 1);
NVD_CmdGetResultRecordSignalZoom
This function runs the "CmdGetResultRecordSignalZoom" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetResultRecordSignalZoom(
int nSocket,
size_t track,
float start,
float end,
size_t size,
bool details,
size_t recordId = 1);

<!-- page 16 -->
The info functions associated to those command functions begins with "GR_" to remind
GetResult.

<!-- page 17 -->

### 2 - Info Functions: HEAD

The following functions enable to get information from the HEAD block of the result.
The functions are ordered as information is stored in the Head block (see NVDrive
reference manual).
- Visual C++ declarations:
int GR_GetHead_Version(int nSocket,short& nVersion);
int GR_GetHead_BlockSize(int nSocket,long& lSize);
int GR_GetHead_ResultType(int nSocket,short& nType);
int GR_GetHead_Size(int nSocket,long& lSize);
int GR_GetHead_Dimension(int nSocket,short& nDim);
int GR_GetHead_Complex(int nSocket,short& nComplex);
int GR_GetHead_MeasureStatus(int nSocket,short& nStatus);
int GR_GetHead_PhysicalQty(int nSocket, char* szQty, int nBufferSize);
int GR_GetHead_UnitName(int nSocket, char* szName, int nBufferSize);
int GR_GetHead_UnitLabel(int nSocket, char* szLabel, int nBufferSize);
int GR_GetHead_ResultName(int nSocket, char* szName, int nBufferSize);
The following functions return -1 if the version of the Head block is lower than 1.
int GR_GetHead_GlobalLevelStatus(int nSocket, short& nStatus);
int GR_GetHead_WeightGLStatus(int nSocket, short& nStatus);
The following functions return -1 if the version of the Head block is lower than 4.
int GR_GetHead_WeightingWindow(int nSocket,unsigned short& ww);
The following functions return -1 if the version of the Head block is lower than 5.
int GR_GetHead_MagnitudeKey(int nSocket,char* key, int nBufferSize);
- Visual Basic declarations:
GR_GetHead_Version (ByVal nSocket As Long,_
ByRef nVersion As Integer) As Long
GR_GetHead_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetHead_ResultType (ByVal nSocket As Long, _
ByRef nType As Integer) As Long
GR_GetHead_Size (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetHead_Dimension (ByVal nSocket As Long, _
ByRef nDim As Integer) As Long
GR_GetHead_Complex (ByVal nSocket As Long, _
ByRef nComplex As Integer) As Long
GR_GetHead_MeasureStatus (ByVal nSocket As Long, _
ByRef nStatus As Integer) As Long

<!-- page 18 -->
GR_GetHead_PhysicalQty (ByVal nSocket As Long, _
ByVal szQty As String, ByVal nBufferSize As Long) As Long
GR_GetHead_UnitName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GR_GetHead_UnitLabel (ByVal nSocket As Long, _
ByVal szLabel As String, ByVal nBufferSize As Long) As Long
GR_GetHead_ResultName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
The following functions return -1 if the version of the Head block is lower than 1.
GR_GetHead_GlobalLevelStatus (ByVal nSocket As Long, _
ByRef nStatus As Integer) As Long
GR_GetHead_WeightGLStatus (ByVal nSocket As Long, _
ByRef nStatus As Integer) As Long
The following functions return -1 if the version of the Head block is lower than 4.
GR_GetHead_WeightingWindow(ByVal nSocket As Long, _
ByRef ww As Integer) As Long
The following functions return -1 if the version of the Head block is lower than 5.
GR_GetHead_MagnitudeKey(ByVal nSocket As Long, _
ByVal key As String, ByVal nBufferSize As Long) As Long

### 3 - Info Functions: XREG

The following functions enable to get information from the XREG block of the result. If
the asked result does not contain an XReg block, then the following functions always
return -1. The functions are ordered as information is stored in the XReg block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetXReg_Version(int nSocket, short& nVersion);
int GR_GetXReg_BlockSize(int nSocket, long& lSize);
int GR_GetXReg_Start(int nSocket, float& fStart);
int GR_GetXReg_Stop(int nSocket, float& fStop);
int GR_GetXReg_NOctave(int nSocket, short& nStep);
int GR_GetXReg_PhysicalQty(int nSocket, char* szQty, int nBufferSize);
int GR_GetXReg_UnitName(int nSocket, char* szName, int nBufferSize);
int GR_GetXReg_UnitLabel(int nSocket, char* szLabel, int nBufferSize);
int GR_GetXReg_MagnitudeKey(int nSocket, char* key, int nBufferSize);
The following functions return -1 if the version of the XReg block is lower than 1.
int GR_GetXReg_RelPrecision(int nSocket, float& fRelPrecision);
int GR_GetXReg_AbsPrecision(int nSocket, float& fAbsPrecision);

<!-- page 19 -->
- Visual Basic declarations:
GR_GetXReg_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetXReg_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetXReg_Start (ByVal nSocket As Long, _
ByRef fStart As Single) As Long
GR_GetXReg_Stop (ByVal nSocket As Long, _
ByRef fStop As Single) As Long
GR_GetXReg_NOctave (ByVal nSocket As Long, _
ByRef nStep As Integer) As Long
GR_GetXReg_PhysicalQty (ByVal nSocket As Long, _
ByVal szQty As String, ByVal nBufferSize As Long) As Long
GR_GetXReg_UnitName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GR_GetXReg_UnitLabel (ByVal nSocket As Long, _
ByVal szLabel As String, ByVal nBufferSize As Long) As Long
The following functions return -1 if the version of the XReg block is lower than 1.
GR_GetXReg_RelPrecision (ByVal nSocket As Long, _
ByRef fRelPrecision As Single) As Long
GR_GetXReg_AbsPrecision (ByVal nSocket As Long, _
ByRef fAbsPrecision As Single) As Long
The following functions return -1 if the version of the XReg block is lower than 3.
GR_GetXReg_MagnitudeKey(ByVal nSocket As Long, _
ByVal key As String, ByVal nBufferSize As Long) As Long

<!-- page 20 -->

### 4 - Info Functions: XREF

The following functions enable to get information from the XREF block of the result. If
the asked result does not contain an XRef block, then the following functions always
return -1. The functions are ordered as information is stored in the XRef block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetXRef_Version(int nSocket, short& nVersion);
int GR_GetXRef_BlockSize(int nSocket, long& lSize);
int GR_GetXRef_NbRef(int nSocket, short& nReferenceNumber);
The following functions refer to a reference "nRef". The possible values for "nRef" go
from 0 to nReferenceNumber-1.
int GR_GetXRef_ReferenceName(int nSocket, char* szRefName,
int nBufferSize, short nRef);
int GR_GetXRef_PhysicalQty(int nSocket, char* szQty, int nBufferSize,
short nRef);
int GR_GetXRef_UnitName(int nSocket, char* szName, int nBufferSize,
short nRef);
int GR_GetXRef_UnitLabel(int nSocket, char* szLabel, int nBufferSize,
short nRef);
int GR_GetXRef_Data(int nSocket, float& fValue, short nRef, long nPos);
int GR_GetXRef_DataArray(int nSocket, float* pFloatArray);
The following functions return -1 if the version of the XRef block is lower than 1.
int GR_GetXRef_RelPrecision(int nSocket, float& fRelPrecision, short nRef);
int GR_GetXRef_AbsPrecision(int nSocket, float& fAbsPrecision, short nRef);
The following functions return -1 if the version of the XRef block is lower than 2.
int GR_GetXRef_Min(int nSocket, float& fMin, short nRef);
int GR_GetXRef_Max(int nSocket, float& fMax, short nRef);
The following function return -1 if the version of the XRef block is lower than 3.
int GR_GetXRef_MagnitudeKey(int nSocket, char* key, int nBufferSize,
short nRef);
- Visual Basic declarations:
GR_GetXRef_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetXRef_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetXRef_NbRef (ByVal nSocket As Long, _
ByRef nReferenceNumber As Integer) As Long

<!-- page 21 -->
The following functions refer to a reference "nRef". The possible values for "nRef" go
from 0 to nReferenceNumber-1.
GR_GetXRef_ReferenceName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long, _
ByVal nRef As Integer) As Long
GR_GetXRef_PhysicalQty (ByVal nSocket As Long, _
ByVal szQty As String, ByVal nBufferSize As Long, _
ByVal nRef As Integer) As Long
GR_GetXRef_UnitName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long, _
ByVal nRef As Integer) As Long
GR_GetXRef_UnitLabel (ByVal nSocket As Long, _
ByVal szLabel As String, ByVal nBufferSize As Long, _
ByVal nRef As Integer) As Long
GR_GetXRef_Data (ByVal nSocket As Long, ByRef fValue As Single, _
ByVal nRef As Integer, ByVal nPos As Long) As Long
The following functions return -1 if the version of the XRef block is lower than 1.
GR_GetXRef_RelPrecision (ByVal nSocket As Long, _
ByRef fRelPrecision As Single, _
ByVal nRef As Integer) As Long
GR_GetXRef_AbsPrecision (ByVal nSocket As Long, _
ByRef fAbsPrecision As Single, _
ByVal nRef As Integer) As Long
The following functions return -1 if the version of the XRef block is lower than 2.
GR_GetXRef_Min (ByVal nSocket As Long, _
ByRef fMin As Single, ByVal nRef As Integer) As Long
GR_GetXRef_Max (ByVal nSocket As Long, _
ByRef fMax As Single, ByVal nRef As Integer) As Long
The following functions return -1 if the version of the XRef block is lower than 3.
GR_GetXRef_MagnitudeKey (ByVal nSocket As Long, _ ByVal key As String, _
ByVal nBufferSize As Long, _
ByVal nRef As Integer) As Long

<!-- page 22 -->

### 5 - Info Functions: CVEC

The following functions enable to get information from the CVEC block of the result. If
the asked result does not contain a CVec block, then the following functions always
return -1. The functions are ordered as information is stored in the CVec block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetCVec_Version(int nSocket, short& nVersion);
int GR_GetCVec_BlockSize(int nSocket, long& lSize);
int GR_GetCVec_RealMin(int nSocket, float& fMin);
int GR_GetCVec_RealMax(int nSocket, float& fMax);
int GR_GetCVec_ImMin(int nSocket, float& fMin);
int GR_GetCVec_ImMax(int nSocket, float& fMax);
int GR_GetCVec_Data(int nSocket, float& fValue, long nPos);
The following functions return -1 if the GlobalLevelStatus of the Head block is 0
(= FALSE).
int GR_GetCVec_RealGlobalLevel(int nSocket, float& fLevel);
int GR_GetCVec_ImGlobalLevel(int nSocket, float& fLevel);
The following functions return -1 if the WeightGLStatus of the Head block is 0
(= FALSE).
int GR_GetCVec_RealWeightGL(int nSocket, float& fLevel);
int GR_GetCVec_ImWeightGL(int nSocket, float& fLevel);
The following functions return -1 if the version of the CVec block is lower than 1.
int GR_GetCVec_RealRelPrecision(int nSocket, float& fMin);
int GR_GetCVec_RealAbsPrecision(int nSocket, float& fMax);
int GR_GetCVec_ImRelPrecision(int nSocket, float& fMin);
int GR_GetCVec_ImAbsPrecision(int nSocket, float& fMax);
- Visual Basic declarations:
GR_GetCVec_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetCVec_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetCVec_RealMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetCVec_RealMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetCVec_ImMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long

<!-- page 23 -->
GR_GetCVec_ImMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetCVec_Data (ByVal nSocket As Long, _
ByRef fValue As Single, ByVal nPos As Long) As Long
The following functions return -1 if the GlobalLevelStatus of the Head block is 0
(= FALSE).
GR_GetCVec_RealGlobalLevel (ByVal nSocket As Long, _
ByRef fLevel As Single) As Long
GR_GetCVec_ImGlobalLevel (ByVal nSocket As Long, _
ByRef fLevel As Single) As Long
The following functions return -1 if the WeightGLStatus of the Head block is 0
(= FALSE).
GR_GetCVec_RealWeightGL (ByVal nSocket As Long, _
ByRef fLevel As Single) As Long
GR_GetCVec_ImWeightGL (ByVal nSocket As Long, _
ByRef fLevel As Single) As Long
The following functions return -1 if the version of the CVec block is lower than 1.
GR_GetCVec_RealRelPrecision (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetCVec_RealAbsPrecision (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetCVec_ImRelPrecision (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetCVec_ImAbsPrecision (ByVal nSocket As Long, _
ByRef fMax As Single) As Long

<!-- page 24 -->

### 6 - Info Functions: RVEC

The following functions enable to get information from the RVEC block of the result. If
the asked result does not contain an RVec block, then the following functions always
return -1. The functions are ordered as information is stored in the RVec block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetRVec_Version(int nSocket, short& nVersion);
int GR_GetRVec_BlockSize(int nSocket, long& lSize);
int GR_GetRVec_RealMin(int nSocket, float& fMin);
int GR_GetRVec_RealMax(int nSocket, float& fMax);
int GR_GetRVec_Data(int nSocket, float& fValue, long nPos);
int GR_GetRVec_DataArray(int nSocket, float* pFloatArray) ;
The following function returns -1 if the GlobalLevelStatus of the Head block is 0
(= FALSE).
int GR_GetRVec_GlobalLevel(int nSocket, float& fLevel);
The following function returns -1 if the WeightGLStatus of the Head block is 0
(= FALSE).
int GR_GetRVec_WeightGL(int nSocket, float& fLevel);
The following functions return -1 if the version of the RVec block is lower than 1.
int GR_GetRVec_RealRelPrecision(int nSocket, float& fMin);
int GR_GetRVec_RealAbsPrecision(int nSocket, float& fMax);
- Visual Basic declarations:
GR_GetRVec_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetRVec_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetRVec_RealMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetRVec_RealMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetRVec_Data (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nPos As Long) As Long
The following function returns -1 if the GlobalLevelStatus of the Head block is 0
(= FALSE).
GR_GetRVec_GlobalLevel (ByVal nSocket As Long, _

<!-- page 25 -->
ByRef fLevel As Single) As Long
The following function returns -1 if the WeightGLStatus of the Head block is 0
(= FALSE).
GR_GetRVec_WeightGL (ByVal nSocket As Long, _
ByRef fLevel As Single) As Long
The following functions return -1 if the version of the RVec block is lower than 1.
GR_GetRVec_RealRelPrecision (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetRVec_RealAbsPrecision (ByVal nSocket As Long, _
ByRef fMax As Single) As Long

<!-- page 26 -->

### 7 - Info Functions: SCAL

The following functions enable to get information from the SCAL block of the result. If
the asked result does not contain a Scal block, then the following functions always return
-1. The functions are ordered as information is stored in the Scal block (see NVDrive
reference manual).
- Visual C++ declarations:
int GR_GetScal_Version(int nSocket, short& nVersion);
int GR_GetScal_BlockSize(int nSocket, long& lSize);
int GR_GetScal_Min(int nSocket, float& fMin);
int GR_GetScal_Max(int nSocket, float& fMax);
int GR_GetScal_Value(int nSocket, float& fValue);
The following functions return -1 if the version of the Scal block is lower than 1.
int GR_GetScal_RelPrecision(int nSocket, float& fRelPrecision);
int GR_GetScal_AbsPrecision(int nSocket, float& fAbsPrecision);
The following functions return -1 if the version of the Scal block is lower than 1.
int GR_GetScal_Imag(int nSocket, float& fValue);
- Visual Basic declarations:
GR_GetScal_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetScal_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetScal_Min (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetScal_Max (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetScal_Value (ByVal nSocket As Long, _
ByRef fValue As Single) As Long
The following functions return -1 if the version of the Scal block is lower than 1.
GR_GetScal_RelPrecision (ByVal nSocket As Long, _
ByRef fRelPrecision As Single) As Long
GR_GetScal_AbsPrecision (ByVal nSocket As Long, _
ByRef fAbsPrecision As Single) As Long
The following functions return -1 if the version of the Scal block is lower than 2.
GR_GetScal_Imag (ByVal nSocket As Long, _
ByRef fValue As Single) As Long

<!-- page 27 -->

### 8 - Info Functions: DWTF

The following functions enable to get information from the DWTF block of the result. If
the asked result does not contain a DWtf block, then the following functions always
return -1. The functions are ordered as information is stored in the DWtf block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetDWtf_Version(int nSocket, short& nVersion);
int GR_GetDWtf_BlockSize(int nSocket, long& lSize);
int GR_GetDWtf_ProcessNumber(int nSocket, short& nProcessNumber);
int GR_GetDWtf_FirstIndex(int nSocket, long& lIndex);
int GR_GetDWtf_LastIndex(int nSocket, long& lIndex);
int GR_GetDWtf_RequestStatus(int nSocket, short& nStatus);
- Visual Basic declarations:
GR_GetDWtf_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetDWtf_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetDWtf_ProcessNumber (ByVal nSocket As Long, _
ByRef nProcessNumber As Integer) As Long
GR_GetDWtf_FirstIndex (ByVal nSocket As Long, _
ByRef lIndex As Long) As Long
GR_GetDWtf_LastIndex (ByVal nSocket As Long, _
ByRef lIndex As Long) As Long
GR_GetDWtf_RequestStatus (ByVal nSocket As Long, _
ByRef nStatus As Integer) As Long

<!-- page 28 -->

### 9 - Info Functions: RWTF

The following functions enable to get information from the RWTF block of the result. If
the asked result does not contain an RWtf block, then the following functions always
return -1. The functions are ordered as information is stored in the RWtf block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetRWtf_Version(int nSocket, short& nVersion);
int GR_GetRWtf_BlockSize(int nSocket, long& lSize);
int GR_GetRWtf_RealMin(int nSocket, float& fMin);
int GR_GetRWtf_RealMax(int nSocket, float& fMax);
int GR_GetRWtf_VectorSize(int nSocket, long& lSize);
int GR_GetRWtf_Depth(int nSocket, long& lDepth);
int GR_GetRWtf_Data(int nSocket, float& fValue, long nPos);
The following functions return -1 if the version of the RWtf block is lower than 1.
int GR_GetRWtf_RelPrecision(int nSocket, float& fRelPrecision);
int GR_GetRWtf_AbsPrecision(int nSocket, float& fAbsPrecision);
- Visual Basic declarations:
GR_GetRWtf_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetRWtf_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetRWtf_RealMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetRWtf_RealMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetRWtf_VectorSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetRWtf_Depth (ByVal nSocket As Long, _
ByRef lDepth As Long) As Long
GR_GetRWtf_Data (ByVal nSocket As Long, _
ByRef fValue As Single, ByVal nPos As Long) As Long
The following functions return -1 if the version of the RWtf block is lower than 1.
GR_GetRWtf_RelPrecision (ByVal nSocket As Long, _
ByRef fRelPrecision As Single) As Long
GR_GetRWtf_AbsPrecision (ByVal nSocket As Long, _
ByRef fAbsPrecision As Single) As Long

<!-- page 29 -->

### 10 - Info Functions: CWTF

The following functions enable to get information from the CWTF block of the result. If
the asked result does not contain a CWtf block, then the following functions always
return -1. The functions are ordered as information is stored in the CWtf block (see
NVDrive reference manual).
- Visual C++ declarations:
int GR_GetCWtf_Version(int nSocket, short& nVersion);
int GR_GetCWtf_BlockSize(int nSocket, long& lSize);
int GR_GetCWtf_RealMin(int nSocket, float& fMin);
int GR_GetCWtf_RealMax(int nSocket, float& fMax);
int GR_GetCWtf_ImMin(int nSocket, float& fMin);
int GR_GetCWtf_ImMax(int nSocket, float& fMax);
int GR_GetCWtf_VectorSize(int nSocket, long& lSize);
int GR_GetCWtf_Depth(int nSocket, long& lDepth);
int GR_GetCWtf_Data(int nSocket, float& fValue, long nPos);
The following functions return -1 if the version of the CWtf block is lower than 1.
int GR_GetCWtf_RealRelPrecision(int nSocket, float& fPrecision);
int GR_GetCWtf_RealAbsPrecision(int nSocket, float& fPrecision);
int GR_GetCWtf_ImRelPrecision(int nSocket, float& fPrecision);
int GR_GetCWtf_ImAbsPrecision(int nSocket, float& fPrecision);
- Visual Basic declarations:
GR_GetCWtf_Version (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GR_GetCWtf_BlockSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetCWtf_RealMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetCWtf_RealMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetCWtf_ImMin (ByVal nSocket As Long, _
ByRef fMin As Single) As Long
GR_GetCWtf_ImMax (ByVal nSocket As Long, _
ByRef fMax As Single) As Long
GR_GetCWtf_VectorSize (ByVal nSocket As Long, _
ByRef lSize As Long) As Long
GR_GetCWtf_Depth (ByVal nSocket As Long, _
ByRef lDepth As Long) As Long
GR_GetCWtf_Data (ByVal nSocket As Long, _
ByRef fValue As Single, ByVal nPos As Long) As Long

<!-- page 30 -->
The following functions return -1 if the version of the CWtf block is lower than 1.
GR_GetCWtf_RealRelPrecision (ByVal nSocket As Long, _
ByRef fPrecision As Single) As Long
GR_GetCWtf_RealAbsPrecision (ByVal nSocket As Long, _
ByRef fPrecision As Single) As Long
GR_GetCWtf_ImRelPrecision (ByVal nSocket As Long, _
ByRef fPrecision As Single) As Long
GR_GetCWtf_ImAbsPrecision (ByVal nSocket As Long, _
ByRef fPrecision As Single) As Long

### 11 - Info Functions: RNFO

The following functions enable reading information from the RNFO block of the result. If
the asked result does not contain a RNFO block, then it returns -1.
- Visual C++ declarations:
int GR_GetSignalInfo(
int nSocket,
uint64_t & readPos,
uint16_t & sampleNb,
uint16_t & recNb,
uint16_t & state);

<!-- page 31 -->

## IV - Functions for external result creation

Those commands are specific to create and modify external result channels.

### 1 - NVD_CreateTCPResultChannel


#### a - Command function

NVD_CreateTCPResultChannel
This function runs the "CreateTCPResultChannel" NVDrive command, and returns the
value of the identifier of the created channel (the first one will have the identifier "0"). If
the command fails, the returned value is -1.
- Visual C++ declaration:
int NVD_CreateTCPResultChannel(int nSocket,
void* pBuffer, long nBufferSize);
- Visual Basic declaration:
NVD_CreateTCPResultChannel(ByVal nSocket As Long, _
ByRef pBuffer As Byte, ByVal nBufferSize As Long) As Long
There is no info functions associated to this command.
The buffer contains data of the result description followed by data of the blocks of the
result (HEAD + ...). The BufferSize is the size of this buffer (in bytes).
NB: In the result description, the channel number and reference number have no utility,
so their value can be set to 0. The consequence is that the fiels "name of the input
connected to the reference channel" does not exist.

<!-- page 32 -->

### 2 - NVD_NewDataForTCPResultChannel


#### a - Command function

NVD_NewDataForTCPResultChannel
This function runs the "NewDataTCPResultChannel" NVDrive command.
- Visual C++ declaration:
int NVD_NewDataForTCPResultChannel(int nSocket,
void* pBuffer, long nBufferSize, long nTCP_ID);
- Visual Basic declaration:
NVD_NewDataForTCPResultChannel(ByVal nSocket As Long, _
ByRef pBuffer As Byte, ByVal nBufferSize As Long, _
ByVal nTCP_ID As Long) As Long
There is no info functions associated to this command.
The buffer contains data of the blocks of the result (HEAD + ...). The BufferSize is the
size of this buffer (in bytes).
The nTCP_ID parameter is the identifier of the channel that was created with the
"CreateTCPResultChannel" command.

<!-- page 33 -->

### 3 - NVD_SetTCPResultChannel


#### a - Command function

NVD_SetTCPResultChannel
This function runs the "SetTCPResultChannel" NVDrive command.
- Visual C++ declaration:
int NVD_SetTCPResultChannel(int nSocket,
void* pBuffer, long nBufferSize, long nTCP_ID);
- Visual Basic declaration:
NVD_SetTCPResultChannel(ByVal nSocket As Long, _
ByRef pBuffer As Byte, ByVal nBufferSize As Long, _
ByVal nTCP_ID As Long) As Long
There is no info functions associated to this command.
The buffer contains data of the blocks of the result (HEAD + ...). The BufferSize is the
size of this buffer (in bytes).
The nTCP_ID parameter is the identifier of the channel that was created with the
"CreateTCPResultChannel" command.

<!-- page 34 -->

### 4 - NVD_AddDatatoTCPResultChannel


#### a - Command function

NVD_AddDataToTCPResultChannel
This function runs the "AddDataToTCPResultChannel" NVDrive command.
- Visual C++ declaration:
int NVD_AddDataToTCPResultChannel(int nSocket,
void* pBuffer, long nBufferSize, long nTCP_ID);
- Visual Basic declaration:
NVD_AddDataToTCPResultChannel(ByVal nSocket As Long, _
ByRef pBuffer As Byte, ByVal nBufferSize As Long, _
ByVal nTCP_ID As Long) As Long
There is no info functions associated to this command.
The buffer contains data of the blocks of the result (HEAD + ...). The BufferSize is the
size of this buffer (in bytes).
The nTCP_ID parameter is the identifier of the channel that was created with the
"CreateTCPResultChannel" command.

<!-- page 35 -->

## V - Functions of the DLL NVD_Command


### 1 - NVD_Action


#### a - Command function

NVD_Action
This function runs any NVDrive command that returns no value (ex: "Run", "Stop", etc.)
- Visual C++ declaration:
int NVD_Action (int nSocket,
const char* pCommand);
- Visual Basic declaration:
NVD_Action (ByVal nSocket As Long, _
ByVal command As String) As Long

<!-- page 36 -->

### 2 - NVD_CmdGetSettingValue


#### a - Command function

NVD_CmdGetSettingValue
This function runs the "GetSettingValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSettingValue(int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nSetting,
int nOption = 0);
- Visual Basic declaration:
NVD_CmdGetSettingValue (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nSetting As Integer, _
ByVal nOption As Long) As Long
The info functions associated to this command function begin with "GSV_" to remind
GetSettingValue.

#### b - Info Functions

The following functions enable to get information from the GetSettingValue command.
- Visual C++ declarations:
int GSV_GetSettingType(int nSocket, short& nType);
int GSV_GetSettingStringValue(int nSocket, char* szName, int nBufferSize);
int GSV_GetSettingFloatValue(int nSocket, float& fValue);
int GSV_GetSettingBooleanValue(int nSocket, short& nShort);
- Visual Basic declaration:
GSV_GetSettingType (ByVal nSocket As Long, _
ByRef nType As Integer) As Long
GSV_GetSettingStringValue (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GSV_GetSettingFloatValue (ByVal nSocket As Long, _
ByRef fValue As Single) As Long

<!-- page 37 -->
GSV_GetSettingBooleanValue (ByVal nSocket As Long, _
ByRef nInteger As Integer) As Long
Note: "GSV_GetSettingType" return a number to identify the type of setting
Boolean (Boolean) 0
String (string) 1
Scalar (float) 2
Enumerated (string) 3
SignalFile (string) 4

<!-- page 38 -->

### 3 - NVD_CmdGetSettingValueString


#### a - Command function

NVD_CmdGetSettingValueString
This function runs the "GetSettingValue" NVDrive command. This command is useful in
NVGateTeamWork but it can also be used in NVGate.
- Visual C++ declaration:
int NVD_CmdGetSettingValueString(
int nSocket,
const char* setting ,
int nOption = 0);
- Visual Basic declaration:
NVD_ CmdGetSettingValueString( ByVal nSocket As Long, _
ByVal setting As String, _
ByVal Nopt As Long) As Long
The info functions associated to this command function begin with "GSV_" to remind
GetSettingValue.

#### b - Info Functions

The same functions as NVD_CmdGetSettingValue info functions.

<!-- page 39 -->

### 4 - NVD_CmdGetSettingInfo


#### a - Command function

NVD_CmdGetSettingInfo
This function runs the "GetSettingInfo" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSettingInfo(int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nSetting);
- Visual Basic declaration:
NVD_CmdGetSettingInfo (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nSetting As Integer) As Long
The info functions associated to this command function begin with "GSI_" to remind
GetSettingInfo.

#### b - Info Functions

The following functions enable to get information from the GetSettingInfo command.
- Visual C++ declarations:
int GSI_GetSettingName(int nSocket, char* szName, int nBufferSize);
int GSI_GetSettingValue(int nSocket, char* szValue, int nBufferSize);
int GSI_GetSettingStyle(int nSocket, char* szStyle, int nBufferSize);
int GSI_GetSettingEffect(int nSocket, char* szEffect, int nBufferSize);
int GSI_GetSettingVisible(int nSocket, char* szVisible, int nBufferSize);
- Visual Basic declaration:
GSI_GetSettingName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GSI_GetSettingValue (ByVal nSocket As Long, _
ByVal szValue As String, ByVal nBufferSize As Long) As Long
GSI_GetSettingStyle (ByVal nSocket As Long, _
ByVal szStyle As String, ByVal nBufferSize As Long) As Long
GSI_GetSettingEffect (ByVal nSocket As Long, _

<!-- page 40 -->
ByVal szEffect As String, ByVal nBufferSize As Long) As Long
GSI_GetSettingVisible (ByVal nSocket As Long, _
ByVal szVisible As String, ByVal nBufferSize As Long) As Long

<!-- page 41 -->

### 5 - NVD_CmdGetSettingValues


#### a - Command function

NVD_CmdGetSettingValues
This function runs the "GetSettingValues" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSettingValues(int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nSetting);
- Visual Basic declaration:
NVD_CmdGetSettingValues (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nSetting As Integer) As Long
The info functions associated to this command function begin with "GSVS_" to remind
GetSettingValues.

#### b - Info Functions

The following functions enable to get information from the GetSettingValues command.
- Visual C++ declarations:
int GSVS_GetSettingType (int nSocket, short& nType);
int GSVS_GetSize (int nSocket, int& nNbElt);
int GSVS_GetKeyInList (int nSocket, char* szKey, int nBufferSize, int nIndex);
int GSVS_GetValueInList (int nSocket, char* szValue, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GSVS_GetSettingType (ByVal nSocket As Long, _
ByRef nType As Integer) As Long
GSVS_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Long) As Long
GSVS_GetKeyInList (ByVal nSocket As Long, ByVal szKey As String, _
ByVal nBufferSize As Long, ByVal nIndex As Long) As Long
GSVS_GetValueInList (ByVal nSocket As Long, ByVal szValue As String, _

<!-- page 42 -->
ByVal nBufferSize As Long, ByVal nIndex As Long) As Long
Note: "GSVS_GetSettingType" return a number to identify the type of setting
Boolean (Boolean) 0
String (string) 1
Scalar (float) 2
Enumerated (string) 3
SignalFile (string) 4

<!-- page 43 -->

### 6 - NVD_CmdGetSettingValuesString


#### a - Command function

NVD_CmdGetSettingValueString
This function runs the "GetSettingValues" NVDrive command. This command is useful
in NVGateTeamWork but it can also be used in NVGate.
- Visual C++ declaration:
int NVD_CmdGetSettingValuesString(int nSocket, const char* setting);
- Visual Basic declaration:
NVD_ CmdGetSettingValuesString (ByVal nSocket As Long, _
ByVal setting As String) As Long
The info functions associated to this command function begin with "GSVS_" to remind
GetSettingValues.

#### b - Info Functions

The same functions as NVD_CmdGetSettingValues info functions.

<!-- page 44 -->

### 7 - NVD_CmdEditSetting


#### a - Command function

NVD_CmdEditSetting
This function runs the "EditSetting" NVDrive command.
- Visual C++ declaration:
int NVD_CmdEditSetting (int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nSetting,
unsigned short nCollection);
- Visual Basic declaration:
NVD_CmdEditSetting (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nSetting As Integer, _
ByVal nCollection As Integer) As Long
The info functions associated to this command function begin with "EST_" to remind
EditSetting.

#### b - Info Functions

The following functions enable to get information from the EditSetting command.
- Visual C++ declarations:
int EST_GetCloseDialogMode(int nSocket, short& nMode);
- Visual Basic declaration:
EST_GetCloseDialogMode (ByVal nSocket As Long, _
ByRef nMode As Integer) As Long

<!-- page 45 -->

### 8 - NVD_CmdGetSignalFileSettingValues


#### a - Command function

NVD_CmdGetSignalFileSettingValues
This function runs the "GetSignalFileSettingValues" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSignalFileSettingValues (int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nSetting);
- Visual Basic declaration:
NVD_CmdGetSignalFileSettingValues (ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nSetting As Integer) As Long
The info functions associated to this command function begin with "GSFSVS_" to
remind GetSignalFileSettingValues

#### b - Info Functions

The following functions enable to get information from the GetSignalFileSettingValues
command.
- Visual C++ declarations:
int GSFSVS_GetMeasureCount(int nSocket, long& lValue);
int GSFSVS_GetMeasureInfo (int nSocket, int nIndex,
char* szProjectName, int nBufferSizeProject,
char* szMeasureName, int nBufferSizeMeasure);

<!-- page 46 -->
- Visual Basic declaration:
GSFSVS_GetMeasureCount (ByVal nSocket As Long, _
ByRef lValue As Long) As Long
GSFSVS_GetMeasureInfo (ByVal nSocket As Long, _
ByVal nIndex As Long, _
ByVal szProjectName As String, _
ByVal nBufferSize1 As Long, _
ByVal szMeasureName As String, _
ByVal nBufferSize2 As Long) As Long

<!-- page 47 -->

### 9 - NVD_CmdGetStateValue


#### a - Command function

NVD_CmdGetStateValue
This function runs the "GetStateValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetStateValue(int nSocket,
unsigned short nModule,
unsigned short nSubModule,
unsigned short nState);
- Visual Basic declaration:
NVD_CmdGetStateValue(ByVal nSocket As Long, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nState As Integer) As Long
The info functions associated to this command function begin with "GSV_" to remind
GetStateValue

#### b - Info Functions

The following functions enable to get information from the GetStateValuecommand.
- Visual C++ declarations:
int GSV_GetState(int nSocket, char* szState, int nBufferSize);
- Visual Basic declaration:
GSV_GetState (ByVal nSocket As Long,
ByVal szStateAs String, _
ByVal nBufferSize) As Long

<!-- page 48 -->

### 10 - NVD_CmdGetInputInfo


#### a - Command function

NVD_CmdGetInputInfo
This function runs the "GetInputInfo" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetInputInfo(int nSocket,
unsigned short nSubModule);
- Visual Basic declaration:
NVD_CmdGetInputInfo(ByVal nSocket As Long, _
ByVal nSubModule As Integer) As Long
The info functions associated to this command function begin with "GII_" to remind
GetInputInfo

#### b - Info Functions

The following functions enable to get information from the GetInputInfo command.
- Visual C++ declarations:
int GII_GetNbInput(int nSocket, short& nNbInput);
int GII_GetFirstInput(int nSocket, short& nNumFirstSubModule);
- Visual Basic declaration:
GII_GetNbInput(ByVal nSocket As Long, _
ByRef nNbInput as Integer) As Long
GII_GetFirstInput(ByVal nSocket As Long, _
ByRef nNumFirstSubModule As Integer) As Long

<!-- page 49 -->

### 11 - NVD_GetSubmoduleList


#### a - Command function

NVD_GetSubmoduleList
This function runs the "GetSubModuleList" NVDrive command.
- Visual C++ declaration:
int NVD_GetSubmoduleList(int nSocket, const char* submodule,
char* bufferSubmodulelist, int bufferSize);
- Visual Basic declaration:
NVD_ GetSubmoduleList ( ByVal nSocket As Long, _
ByVal submodule As String, _
ByVal bufferSubmodulelist As String, _
ByVal bufferSize As Interger) As Long
This function returns :
- 0 if no error,
- -1 if an error occurred calling command
- Size required if bufferSize parameter is too small.

<!-- page 50 -->

### 12 - NVD_CmdGetTransducerInfo


#### a - Command function

NVD_CmdGetTransducerInfo
This function runs the "GetTransducerInfo" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetTransducerInfo(int nSocket, char* szTransducId);
- Visual Basic declaration:
NVD_CmdGetTransducerInfo (ByVal nSocket As Long, _
ByVal szTransducId As String) As Long
The info functions associated to this command function begin with "GTI_" to remind
GetTransducerInfo.

#### b - Info Functions

The following functions enable to get information from the GetTransducerInfo command.
The functions are ordered as information is stored in the block (see NVDrive reference
manual).
- Visual C++ declarations:
int GTI_GetTransducerName(int nSocket, char* szName, int nBufferSize);
int GTI_GetManufacturerName(int nSocket, char* szName, int nBufferSize);
int GTI_GetModelName(int nSocket, char* szName, int nBufferSize);
int GTI_GetSerialNumber(int nSocket, char* szSerialNum, int nBufferSize);
int GTI_GetCouplingType(int nSocket, char* szCoupling, int nBufferSize);
int GTI_GetFactorySensitivity(int nSocket, float& fSensitivity);
int GTI_GetSensitivityUnit(int nSocket, char* szSensitivity, int nBufferSize);
int GTI_GetOffset(int nSocket, float& fOffset);
int GTI_GetOffsetUnit(int nSocket, char* szUnit, int nBufferSize);
int GTI_GetYearLastCalib(int nSocket, long& lYear);
int GTI_GetMonthLastCalib(int nSocket, long& lMonth);
int GTI_GetDayLastCalib(int nSocket, long& lDay);
int GTI_GetComment(int nSocket, char* szComment);
int GTI_GetSensitivityLastCalib(int nSocket, float& fSensitivityLastCalib);
int GTI_GetOffsetLastCalib(int nSocket, float& fOffsetLastCalib);
int GTI_GetUserLastCalib(int nSocket, char* szUserLastCalib, int nBufferSize);
int GTI_GetAnalyzerLastCalib(int nSocket, char* szAnalyzerLastCalib, int
nBufferSize);
int GTI_GetInputLastCalib(int nSocket, char* szInputLastCalib, int nBufferSize);

<!-- page 51 -->
int GTI_GetCalibratorLastCalib(int nSocket, char* szCalibratorLastCalib, int
nBufferSize);
int GTI_GetAlwaysUseFactory(int nSocket, bool& bAlwaysUseFactory);
- Visual Basic declaration:
GTI_GetTransducerName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GTI_GetManufacturerName (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GTI_GetModelName (ByVal nSocket As Long,
ByVal szName As String, ByVal nBufferSize As Long) As Long
GTI_GetSerialNumber (ByVal nSocket As Long, _
ByVal szSerialNum As String, ByVal nBufferSize As Long) As Long
GTI_GetCouplingType (ByVal nSocket As Long, _
ByVal szCoupling As String, ByVal nBufferSize As Long) As Long
GTI_GetFactorySensitivity (ByVal nSocket As Long, _
ByRef fSensitivity As Single) As Long
GTI_GetSensitivityUnit (ByVal nSocket As Long, _
ByVal szSensitivity As String, ByVal nBufferSize As Long) As Long
GTI_GetOffset (ByVal nSocket As Long, _
ByRef fOffset As Single) As Long
GTI_GetOffsetUnit (ByVal nSocket As Long, _
ByVal szUnit As String, ByVal nBufferSize As Long) As Long
GTI_GetYearLastCalib (ByVal nSocket As Long, _
ByRef lYear As Long) As Long
GTI_GetMonthLastCalib (ByVal nSocket As Long, _
ByRef lMonth As Long) As Long
GTI_GetDayLastCalib (ByVal nSocket As Long, _
ByRef lDay As Long) As Long
GTI_GetComment (ByVal nSocket As Long, _
ByVal szComment As String, ByVal nBufferSize As Long) As Long
GTI_GetSensitivityLastCalib(ByVal nSocket As Long, _
ByRef fSensitivityLastCalib AsSingle) As Long
GTI_GetOffsetLastCalib(ByVal nSocket As Long, _
ByRef fOffsetLastCalib As Single) As Long
GTI_GetUserLastCalib(ByVal nSocket As Long, _
ByVal szUserLastCalib As String, ByVal nBufferSize As Long) As Long
GTI_GetAnalyzerLastCalib(ByVal nSocket As Long, _
ByVal szAnalyzerLastCalib As String, ByVal nBufferSize As Long) _
As Long
GTI_GetInputLastCalib(ByVal nSocket As Long, _
ByVal szInputLastCalib As String ByVal nBufferSize As Long) As Long
GTI_GetCalibratorLastCalib(ByVal nSocket As Long, _
ByVal szCalibratorLastCalib As String, ByVal nBufferSize As Long) _
As Long

<!-- page 52 -->
GTI_GetAlwaysUseFactory(ByVal nSocket As Long, _
ByVal bAlwaysUseFactory as Boolean) as Long

<!-- page 53 -->

### 13 - NVD_CmdGetTEDSContent


#### a - Command function

NVD_CmdGetTEDSContent
This function runs the "GetTEDSContent" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetTEDSContent(int nSocket, char* szTransducId);
- Visual Basic declaration:
NVD_CmdGetTEDSContent (ByVal nSocket As Long, _
ByVal szTransducId As String) As Long
The info functions associated to this command function begin with "GTC_" to remind
GetTEDSContent.

#### b - Info Functions

The following functions enable to get information from the GetTEDSContent command.
- Visual C++ declarations:
int GTC_GetTEDSBufferContent(int nSocket, char*& szBuffer, long&
lBufferSize);
- Visual Basic declaration:
GTC_GetTEDSBufferContent (ByVal nSocket As Long, _
ByRef szBuffer As String, ByRef lBufferSize As Long) As Long

<!-- page 54 -->

### 14 - NVD_CmdGetTEDSContentOnInput


#### a - Command function

NVD_CmdGetTEDSContentOnInput
This function runs the "GetTEDSContentOnInput" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetTEDSContentOnInput(int nSocket, int nInput);
- Visual Basic declaration:
NVD_CmdGetTEDSContentOnInput (ByVal nSocket As Long, _
ByVal nInput as Long) As Long
The info functions associated to this command function begin with "GTCI_" to remind
GetTEDSContentOnInput.

#### b - Info Functions

The following functions enable to get information from the GetTEDSContentOnInput
command.
- Visual C++ declarations:
int GTCI_GetTEDSBufferContentOnInput(int nSocket, char*& szBuffer, long&
lBufferSize);
- Visual Basic declaration:
GTCI_GetTEDSBufferContentOnInput (ByVal nSocket As Long, _
ByRef szBuffer As String, ByRef lBufferSize As Long) As Long

<!-- page 55 -->

### 15 - NVD_CmdEditCalibration


#### a - Command function

NVD_CmdEditCalibration
This function runs the "EditCalibration" NVDrive command.
- Visual C++ declaration:
int NVD_CmdEditCalibration (int nSocket);
- Visual Basic declaration:
NVD_CmdEditCalibration (ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "ECB_" to remind
EditCalibration.

#### b - Info Functions

The following functions enable to get information from the EditCalibration command.
- Visual C++ declarations:
int ECB_GetCloseDialogMode(int nSocket, short& nMode);
- Visual Basic declaration:
ECB_GetCloseDialogMode (ByVal nSocket As Long, _
ByRef nMode As Integer) As Long

<!-- page 56 -->

### 16 - NVD_CmdGetMarkerList


#### a - Command function

NVD_CmdGetMarkerList
This function runs the "GetMarkerList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetMarkerList(int nSocket, char* szWindow,
unsigned short nDisplayZoneType);
- Visual Basic declaration:
NVD_CmdGetMarkerList (ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nDisplayZoneType As Integer) As Long
The info functions associated to this command function begin with "GMAL_" to remind
GetMarkerList.

#### b - Info Functions

The following functions enable to get information from the CmdGetMarkerList
command. The first function enables to get the number of elements in the list. For the
other functions, nIndex identify the position of the marker in the list (from 0 to nNbElt -
1).
- Visual C++ declarations:
int GMAL_GetSize(int nSocket, int& nNbElt);
int GMAL_GetMarkerType(I nt nSocket, short& nType, int nIndex);
int GMAL_GetMarkerNumber(int nSocket, int& nNumber, int nIndex);
int GMAL_GetTraceApplication(int nSocket, short& nApplied, int nIndex);
int GMAL_GetTraceModuleID(int nSocket, short& nID, int nIndex);
int GMAL_GetTraceProcessID(int nSocket, int& nID, int nIndex);
int GMAL_GetTraceChannelNumber(int nSocket, int& nNum, int nIndex);
int GMAL_GetTraceRefChannelNumber(int nSocket, int& nNum, int nIndex);
int GMAL_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
int GMAL_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:

<!-- page 57 -->
GMAL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GMAL_GetMarkerType (ByVal nSocket As Long, _
ByRef nType As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GMAL_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 58 -->

### 17 - NVD_CmdGetFreeMarkerParameters


#### a - Command function

NVD_CmdGetFreeMarkerParameters
This function runs the "GetFreeMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetFreeMarkerParameters (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetFreeMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GFMP_" to remind
GetFreeMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the GetFreeMarkerParameters
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
- Visual C++ declarations:
int GFMP_GetMarkerPosition(int nSocket, float& fPos);
int GFMP_GetMarkerLabel(int nSocket, char* szName, int nBufferSize);
int GFMP_GetInterpolationType(int nSocket, int& nType);
- Visual Basic declaration:
GFMP_GetMarkerPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GFMP_GetMarkerLabel (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long) As Long
GFMP_GetInterpolationType (ByVal nSocket As Long, _
ByRef nType As Long) As Long

<!-- page 59 -->

### 18 - NVD_CmdGetPeakMarkerParameters


#### a - Command function

NVD_CmdGetPeakMarkerParameters
This function runs the "GetPeakMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetPeakMarkerParameters (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetPeakMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GPMP_" to remind
GetPeakMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the
CmdGetPeakMarkerParameters command. The functions are ordered as information is
stored in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GPMP_GetMarkerThreshold(int nSocket, float& fPos);
int GPMP_GetMarkerAbsThreshold(int nSocket, float& fPos);
int GPMP_GetMaxNumOfPeaks(int nSocket, int& nNum);
int GPMP_GetInterpolationType(int nSocket, int& nType);
int GPMP_GetIsSortedByFreq (int nSocket, bool& bIsSortedByFreq);
- Visual Basic declaration:
GPMP_GetMarkerThreshold (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GPMP_GetMarkerAbsThreshold (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GPMP_GetMaxNumOfPeaks (ByVal nSocket As Long, _
ByRef nNum As Long) As Long
GPMP_GetInterpolationType (ByVal nSocket As Long, _

<!-- page 60 -->
ByRef nType As Long) As Long
GPMP_GetIsSortedByFreq(ByVal nSocket As Long, _
ByRef bIsSortedByFreq As Boolean) As Long

<!-- page 61 -->

### 19 - NVD_CmdGetPeakMarkerParametersEx


#### a - Command function

NVD_CmdGetPeakMarkerParametersEx
This function runs the "GetPeakMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetPeakMarkerParametersEx (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
long version);
- Visual Basic declaration:
NVD_CmdGetPeakMarkerParametersEx (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,
ByVal version As Long) As Long
The info functions associated to this command function begin with "GPMP_" to remind
GetPeakMarkerParameters. It's ths same as NVD_CmdGetPeakMarkerParameters
command. But, in addition, you can specify a version number associated to this command
to get more information like damping ratio.

#### b - Info Functions

Functions are described in chapter § 14.b NVD_CmdGetPeakMarkerParameters
Function.
If version command is >= 1, following functions enable to get more information from
GetPeakMarkerParameters command. The functions are ordered as information is stored
in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GPMP_GetIsDampingRatio(int nSocket, bool& bIsDampingRatio);
- Visual Basic declaration:
GPMP_GetIsDampingRatio (ByVal nSocket As Long, _
ByRef bIsDampingRatio As Boolean) As Long

<!-- page 62 -->

### 20 - NVD_CmdGetMaxMarkerParameters


#### a - Command function

NVD_CmdGetMaxMarkerParameters
This function runs the "GetMaxMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetMaxMarkerParameters (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetMaxMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GMMP_" to remind
GetMaxMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the
CmdGetMaxMarkerParameters command. The functions are ordered as information is
stored in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GMMP_GetMarkerThreshold(int nSocket, float& fPos);
int GMMP_GetMarkerAbsThreshold(int nSocket, float& fPos);
int GMMP_GetMaxNumOfMaxMarkers(int nSocket, int& nNum);
int GMMP_GetInterpolationType(int nSocket, int& nType);
- Visual Basic declaration:
GMMP_GetMarkerThreshold (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GMMP_GetMarkerAbsThreshold (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GMMP_GetMaxNumOfMaxMarkers (ByVal nSocket As Long, _
ByRef nNum As Long) As Long
GMMP_GetInterpolationType (ByVal nSocket As Long, _

<!-- page 63 -->
ByRef nType As Long) As Long

<!-- page 64 -->

### 21 - NVD_CmdGetMaxMarkerParametersEx


#### a - Command function

NVD_CmdGetPeakMarkerParametersEx
This function runs the "GetMaxMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetMaxMarkerParametersEx (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
long version);
- Visual Basic declaration:
NVD_CmdGetMaxMarkerParametersEx (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,
ByVal version As Long) As Long
The info functions associated to this command function begin with "GMMP_" to remind
GetMaxMarkerParameters. It's the same as NVD_CmdGetMaxMarkerParameters
command. But, in addition, you can specify a version number associated to this command
to get more information like damping ratio.

#### b - Info Functions

Functions are described in chapter § 16.b NVD_CmdGetMaxMarkerParameters
Function.
If version command is >= 1, following functions enable to get more information from
GetPeakMarkerParameters command. The functions are ordered as information is stored
in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GMMP_GetIsDampingRatio(int nSocket, bool& bIsDampingRatio);
- Visual Basic declaration:
GMMP_GetIsDampingRatio (ByVal nSocket As Long, _
ByRef bIsDampingRatio As Boolean) As Long

<!-- page 65 -->

### 22 - NVD_CmdGetPowerBandMarkerParameters


#### a - Command function

NVD_CmdGetPowerBandMarkerParameters
This function runs the "GetPowerBandMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPowerBandMarkerParameters (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetPowerBandMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GPBMP_" to
remind GetPowerBandMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the
CmdGetPowerBandMarkerParameters command. The functions are ordered as
information is stored in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GPBMP_GetMarkerStartPosition(int nSocket, float& fPos);
int GPBMP_GetMarkerDelta(int nSocket, float& fPos);
- Visual Basic declaration:
GPBMP_GetMarkerStartPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GPBMP_GetMarkerDelta (ByVal nSocket As Long, _
ByRef fPos As Single) As Long

<!-- page 66 -->

### 23 - NVD_CmdGetSideBandMarkerParameters


#### a - Command function

NVD_CmdGetSideBandMarkerParameters
This function runs the "GetSideBandMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSideBandMarkerParameters (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetSideBandMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GSBMP_" to
remind GetSideBandMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the
CmdGetSideBandMarkerParameters command. The functions are ordered as information
is stored in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GSBMP_GetMarkerStartPosition(int nSocket, float& fPos);
int GSBMP_GetMarkerDelta(int nSocket, float& fPos);
int GSBMP_GetMaxNumOfBands(int nSocket, int& nNum);
int GSBMP_GetInterpolationType(int nSocket, int& nType);
- Visual Basic declaration:
GSBMP_GetMarkerStartPosition(ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GSBMP_GetMarkerDelta(ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GSBMP_GetMaxNumOfBands(ByVal nSocket As Long, _

<!-- page 67 -->
ByRef nNum As Long) As Long
GSBMP_GetInterpolationType(ByVal nSocket As Long, _
ByRef nType As Long) As Long

<!-- page 68 -->

### 24 - NVD_CmdGetHarmonicMarkerParameters


#### a - Command function

NVD_CmdGetHarmonicMarkerParameters
This function runs the "GetHarmonicMarkerParameters" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetHarmonicMarkerParameters (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber);
- Visual Basic declaration:
NVD_CmdGetHarmonicMarkerParameters (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer) As Long
The info functions associated to this command function begin with "GHMP_" to remind
GetHarmonicMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the
CmdGetHarmonicMarkerParameters command. The functions are ordered as information
is stored in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GHMP_GetMarkerStartPosition(int nSocket, float& fPos);
int GHMP_GetMaxNumOfHarmonics(int nSocket, int& nNum);
int GHMP_GetInterpolationType(int nSocket, int& nType);
- Visual Basic declaration:
GSBMP_GetMarkerStartPosition(ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GSBMP_GetMaxNumOfBands(ByVal nSocket As Long, _
ByRef nNum As Long) As Long
GSBMP_GetInterpolationType(ByVal nSocket As Long, _
ByRef nType As Long) As Long

<!-- page 69 -->

### 25 - NVD_CmdGetPeriodMarkerParameters


#### a - Command function

NVD_CmdGetPeriodMarkerParameters
This function runs the "CmdGetPeriodMarkerParameters" NVDrive command.
- Visual C++ declaration:
int CmdGetPeriodMarkerParameters(int nSocket, const char* szWindow,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber) ;
- Visual Basic declaration:
CmdGetPeriodMarkerParameters(ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nDisplayZoneType As Integer,_
ByVal nMarkerNumber As Integer) As Long
The info function associated to this command function begins with "GPRDMP_" to
remind GetPeRioDicMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the GetPeriodMarkerParameters
command.
- Visual C++ declarations:
int GPRDMP_GetMarkerStartPosition(int nSocket, float& fPos);
int GPRDMP_GetMaxNumOfPeriods(int nSocket, int& nNum);
int GPRDMP_GetPeriod(int nSocket, float& fPeriod);
- Visual Basic declaration:
GPRDMP_GetMarkerStartPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GPRDMP_GetMaxNumOfPeriods (ByVal nSocket As Long, _
ByRef nNum As Integer) As Long
GPRDMP_GetPeriod (ByVal nSocket As Long, _
ByRef fPeriod As Single) As Long

<!-- page 70 -->

### 26 - NVD_CmdGetRecordMarkerParameters


#### a - Command function

NVD_CmdGetRecordMarkerParameters
This function runs the "CmdGetRecordMarkerParameters" NVDrive command.
- Visual C++ declaration:
int CmdGetRecordMarkerParameters(int nSocket, const char* szWindow,
unsigned short nMarkerNumber) ;
- Visual Basic declaration:
CmdGetRecordMarkerParameters(ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nMarkerNumber As Integer) As Long
The info function associated to this command function begins with "GRMP_" to remind
GetRecordMarkerParameters.

#### b - Info Functions

The following functions enable to get information from the GetRecordMarkerParameters
command.
- Visual C++ declarations:
int GRMP_GetMarkerPosition(int nSocket, float& fPos);
int GRMP_GetMarkerLabel(int nSocket, char* szLabel, int nBufferSize);
- Visual Basic declaration:
GRMP_GetMarkerPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GRMP_GetMarkerLabel (ByVal nSocket As Long, _
ByVal szLabel As String , ByVal nBufferSize As Long) As Long

<!-- page 71 -->

### 27 - NVD_CmdGetNumberOfRecordMarker


#### a - Command function

NVD_CmdGetNumberOfRecordMarker
This function runs the "CmdGetNumberOfRecordMarker" NVDrive command.
- Visual C++ declaration:
int CmdGetNumberOfRecordMarker(int nSocket); ;
- Visual Basic declaration:
CmdGetNumberOfRecordMarker(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GNRM_" to remind
GetNumberOfRecordMarker.

#### b - Info Functions

The following functions enable to get information from the
CmdGetNumberOfRecordMarker command.
- Visual C++ declarations:
int GNRM_GetNumber(int nSocket, short& nMarkerNumber);
- Visual Basic declaration:
GNRM_GetNumber (ByVal nSocket As Long, _
ByRef nMarkerNumber As Integer) As Long

<!-- page 72 -->

### 28 - NVD_CmdGetFreeMarkerValue


#### a - Command function

NVD_CmdGetFreeMarkerValue
This function runs the "GetFreeMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetFreeMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetFreeMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GFMV_" to remind
GetFreeMarkerValue.

#### b - Info Functions

The following functions enable to get information from the CmdGetFreeMarkerValue
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
The "nTrace" parameter is 0 for the first trace.
- Visual C++ declarations:
int GFMV_GetMarkerNumber(int nSocket, int& nNumber);
int GFMV_GetTraceApplication(int nSocket, short& nApplied);
int GFMV_GetMarkerLabel(int nSocket, char* szLabel, int nBufferSize);
int GFMV_GetMarkerXPosition(int nSocket, float& fPos);
int GFMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GFMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GFMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GFMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GFMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);
int GFMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);

<!-- page 73 -->
int GFMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GFMV_GetMarkerValue(int nSocket, float& fValue, long nTrace);
- Visual Basic declaration:
GFMV_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GFMV_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GFMV_GetMarkerLabel (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long) As Long
GFMV_GetMarkerXPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GFMV_GetNumberOfTraces (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GFMV_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GFMV_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GFMV_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GFMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GFMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GFMV_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GFMV_GetMarkerValue (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long

<!-- page 74 -->

### 29 - NVD_CmdGetPeakMarkerValue


#### a - Command function

NVD_CmdGetPeakMarkerValue
This function runs the "GetPeakMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPeakMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetPeakMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GPMV_" to remind
GetPeakMarkerValue.

#### b - Info Functions

The following functions enable to get information from the CmdGetPeakMarkerValue
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
The "nTrace" parameter is 0 for the first trace.
The "nPeak" parameter is 0 for the first peak.
- Visual C++ declarations:
int GPMV_GetMarkerNumber(int nSocket, int& nNumber);
int GPMV_GetTraceApplication(int nSocket, short& nApplied);
int GPMV_GetMarkerThreshold(int nSocket, float& fThreshold);
int GPMV_GetMarkerAbsThreshold(int nSocket, float& fThreshold);
int GPMV_GetMaxNbPeaks(int nSocket, int& nNumber);
int GPMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GPMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GPMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GPMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GPMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);

<!-- page 75 -->
int GPMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GPMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GPMV_GetNumberOfPeaks(int nSocket, int& nNumber, long nTrace);
int GPMV_GetMarkerPeakXPos(int nSocket, float& fValue, long nTrace, long
nPeak);
int GPMV_GetMarkerPeakYPos(int nSocket, float& fValue, long nTrace, long
nPeak);
- Visual Basic declaration:
GPMV_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPMV_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GPMV_GetMarkerThreshold (ByVal nSocket As Long, _
ByRef fThreshold As Single) As Long
GPMV_GetMarkerAbsThreshold (ByVal nSocket As Long, _
ByRef fThreshold As Single) As Long
GPMV_GetMaxNbPeaks (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPMV_GetNumberOfTraces (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPMV_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, ByVal nTrace As Long) As Long
GPMV_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Long, ByVal nTrace As Long) As Long
GPMV_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, ByVal nTrace As Long) As Long
GPMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, ByVal nTrace As Long) As Long
GPMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GPMV_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GPMV_GetNumberOfPeaks (ByVal nSocket As Long, _
ByRef nNumber As Long, ByVal nTrace As Long) As Long
GPMV_GetMarkerPeakXPos (ByVal nSocket As Long, _
ByRef fThreshold As Single, ByVal nTrace As Long, _
ByVal nPeak As Long) As Long
GPMV_GetMarkerPeakYPos (ByVal nSocket As Long, _
ByRef fThreshold As Single, ByVal nTrace As Long, _
ByVal nPeak As Long) As Long

<!-- page 76 -->

### 30 - NVD_CmdGetPeakMarkerValueEx


#### a - Command function

NVD_CmdGetPeakMarkerParametersEx
This function runs the "GetPeakMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetPeakMarkerValueEx (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails,
long version);
- Visual Basic declaration:
NVD_ CmdGetPeakMarkerValueEx (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer,_
ByVal verions As Long) As Long
The info functions associated to this command function begin with "GPMV_" to remind
GetPeakMarkerValue. It's ths same as NVD_CmdGetPeakMarkerValue command.
But, in addition, you can specify a version number associated to this command to get
more information like damping ratio.

#### b - Info Functions

Functions are described in chapter § 25.b NVD_CmdGetPeakMarkerValue Function.
If version command is >= 1, following functions enable to get more information from
GetPeakMarkerParameters command. The functions are ordered as information is stored
in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GPMV_GetIsDampingRatio(int nSocket, bool& bIsDampingRatio);
int GPMV_GetNumberOfDampings(int nSocket, int& nNumber, long nTrace);
int GPMP_ GetMarkerPeakDampingRatio(int nSocket, float& fValue,
long nTrace, long index);

<!-- page 77 -->
- Visual Basic declaration:
GPMV_GetIsDampingRatio (ByVal nSocket As Long, _
ByRef bIsDampingRatio As Boolean) As Long
GPMV_ GetNumberOfDampings (ByVal nSocket As Long, _
ByRef nNumber As Long, ByVal nTrace As Long) As Long
GPMV_ GetMarkerPeakDampingRatio (ByVal nSocket As Long, _
ByRef fValue As Single, ByVal nTrace As Long, _
ByVal index As Long) As Long

<!-- page 78 -->

### 31 - NVD_CmdGetMaxMarkerValue


#### a - Command function

NVD_CmdGetMaxMarkerValue
This function runs the "GetMaxMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetMaxMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetMaxMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GMMV_" to remind
GetMaxMarkerValue.

#### b - Info Functions

The following functions enable to get information from the CmdGetMaxMarkerValue
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
The "nTrace" parameter is 0 for the first trace.
The "nPeak" parameter is 0 for the first peak.
- Visual C++ declarations:
int GMMV_GetMarkerNumber(int nSocket, int& nNumber);
int GMMV_GetTraceApplication(int nSocket, short& nApplied);
int GMMV_GetMarkerThreshold(int nSocket, float& fThreshold);
int GMMV_GetMarkerAbsThreshold(int nSocket, float& fThreshold);
int GMMV_GetMaxNbMax(int nSocket, int& nNumber);
int GMMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GMMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GMMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GMMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GMMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);

<!-- page 79 -->
int GMMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GMMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GMMV_GetNumberOfMax(int nSocket, int& nNumber, long nTrace);
int GMMV_GetMarkerMaxXPos(int nSocket, float& fValue, long nTrace, long
nPeak);
int GMMV_GetMarkerMaxYPos(int nSocket, float& fValue, long nTrace, long
nPeak);
- Visual Basic declaration:
GMMV_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GMMV_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GMMV_GetMarkerThreshold (ByVal nSocket As Long, _
ByRef fThreshold As Single) As Long
GMMV_GetMarkerAbsThreshold (ByVal nSocket As Long, _
ByRef fThreshold As Single) As Long
GMMV_GetMaxNbMax (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GMMV_GetNumberOfTraces (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GMMV_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GMMV_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Long, _
ByVal nTrace As Long) As Long
GMMV_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GMMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GMMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String,
ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GMMV_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String,
ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GMMV_GetNumberOfMax (ByVal nSocket As Long, _
ByRef nNumber As Long, _

<!-- page 80 -->
ByVal nTrace As Long) As Long
GMMV_GetMarkerMaxXPos (ByVal nSocket As Long, _
ByRef fThreshold As Single, _
ByVal nTrace As Long, _
ByVal nPeak As Long) As Long
GMMV_GetMarkerMaxYPos (ByVal nSocket As Long, _
ByRef fThreshold As Single, _
ByVal nTrace As Long, _
ByVal nPeak As Long) As Long

<!-- page 81 -->

### 32 - NVD_CmdGetMaxMarkerValueEx


#### a - Command function

NVD_CmdGetPeakMarkerParametersEx
This function runs the "GetMaxMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_ CmdGetMaxMarkerValueEx (int nSocket,
char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails,
long version);
- Visual Basic declaration:
NVD_ CmdGetMaxMarkerValueEx (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer,_
ByVal verions As Long) As Long
The info functions associated to this command function begin with "GMMV_" to remind
GetMaxMarkerValue. It's ths same as NVD_CmdGetMaxMarkerValue command.
But, in addition, you can specify a version number associated to this command to get
more information like damping ratio.

#### b - Info Functions

Functions are described in chapter § 27.b NVD_CmdGetMaxMarkerValue Function.
If version command is >= 1, following functions enable to get more information from
GetPeakMarkerParameters command. The functions are ordered as information is stored
in the block (see NVDrive reference manual).
- Visual C++ declarations:
int GMMV_GetIsDampingRatio(int nSocket, bool& bIsDampingRatio);
int GMMV_GetNumberOfDampings(int nSocket, int& nNumber, long nTrace);
int GMMV_GetMarkerMaxDampingRatio(int nSocket, float& fValue,
long nTrace, long index);

<!-- page 82 -->
- Visual Basic declaration:
GMMV_GetIsDampingRatio (ByVal nSocket As Long, _
ByRef bIsDampingRatio As Boolean) As Long
GMMV_ GetNumberOfDampings (ByVal nSocket As Long, _
ByRef nNumber As Long, ByVal nTrace As Long) As Long
GMMV_ GetMarkerMaxDampingRatio (ByVal nSocket As Long, _
ByRef fValue As Single, ByVal nTrace As Long, _
ByVal index As Long) As Long

<!-- page 83 -->

### 33 - NVD_CmdGetPowerBandMarkerValue


#### a - Command function

NVD_CmdGetPowerBandMarkerValue
This function runs the "GetPowerBandMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPowerBandMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetPowerBandMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GPBMV_" to
remind GetPowerBandMarkerValue.

#### b - Info Functions

The following functions enable to get information from the
CmdGetPowerBandMarkerValue command. The functions are ordered as information is
stored in the block (see NVDrive reference manual).
The "nTrace" parameter is 0 for the first trace.
- Visual C++ declarations:
int GPBMV_GetMarkerNumber(int nSocket, int& nNumber);
int GPBMV_GetTraceApplication(int nSocket, short& nApplied);
int GPBMV_GetMarkerStartPosition(int nSocket, float& fPos);
int GPBMV_GetMarkerDelta(int nSocket, float& fDelta);
int GPBMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GPBMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GPBMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GPBMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GPBMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);
int GPBMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);

<!-- page 84 -->
int GPBMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GPBMV_GetMarkerPower(int nSocket, float& fValue, long nTrace);
- Visual Basic declaration:
GPBMV_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPBMV_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GPBMV_GetMarkerStartPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GPBMV_GetMarkerDelta (ByVal nSocket As Long, _
ByRef fDelta As Single) As Long
GPBMV_GetNumberOfTraces (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPBMV_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GPBMV_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Long, _
ByVal nTrace As Long) As Long
GPBMV_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GPBMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GPBMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String,
ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GPBMV_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String,
ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GPBMV_GetMarkerPower (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long

<!-- page 85 -->

### 34 - NVD_CmdGetSideBandMarkerValue


#### a - Command function

NVD_CmdGetSideBandMarkerValue
This function runs the "GetSideBandMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSideBandMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetSideBandMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GSBMV_" to
remind GetSideBandMarkerValue.

#### b - Info Functions

The following functions enable to get information from the
CmdGetSideBandMarkerValue command. The functions are ordered as information is
stored in the block (see NVDrive reference manual).
The "nTrace" parameter is 0 for the first trace.
- Visual C++ declarations:
int GSBMV_GetMarkerNumber(int nSocket, int& nNumber);
int GSBMV_GetTraceApplication(int nSocket, short& nApplied);
int GSBMV_GetMarkerStartPosition(int nSocket, float& fPos);
int GSBMV_GetMarkerDelta(int nSocket, float& fDelta);
int GSBMV_GetMaxNbBand (int nSocket, int& nNumber);
int GSBMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GSBMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GSBMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GSBMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GSBMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);
int GSBMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,

<!-- page 86 -->
long nTrace);
int GSBMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GSBMV_GetMarkerBandXPos(int nSocket, float& fValue, long nTrace);
int GSBMV_GetMarkerBandYPos(int nSocket, float& fValue, long nTrace);
int GSBMV_GetNumberOfLeftBand(int nSocket, int& nNum, long nTrace);
int GSBMV_GetNumberOfRightBand(int nSocket, int& nNum, long nTrace);
int GSBMV_GetMarkerLeftBandXPos(int nSocket, float& fValue, long nTrace);
int GSBMV_GetMarkerLeftBandYPos(int nSocket, float& fValue, long nTrace);
int GSBMV_GetMarkerRightBandXPos(int nSocket, float& fValue, long
nTrace);
int GSBMV_GetMarkerRightBandYPos(int nSocket, float& fValue, long
nTrace);
- Visual Basic declaration:
GSBMV_GetMarkerNumber (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GSBMV_GetTraceApplication (ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GSBMV_GetMarkerStartPosition (ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GSBMV_GetMarkerDelta (ByVal nSocket As Long, _
ByRef fDelta As Single) As Long
GSBMV_GetMaxNbBand (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GSBMV_GetNumberOfTraces (ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GSBMV_GetTraceModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GSBMV_GetTraceProcessID (ByVal nSocket As Long, _
ByRef nID As Long, _
ByVal nTrace As Long) As Long
GSBMV_GetTraceChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GSBMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GSBMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GSBMV_GetTraceRefInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long

<!-- page 87 -->
GSBMV_GetMarkerBandXPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GSBMV_GetMarkerBandYPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GSBMV_GetNumberOfLeftBand (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nTrace As Long) As Long
GSBMV_GetNumberOfRightBand (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nTrace As Long) As Long
GSBMV_GetMarkerLeftBandXPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GSBMV_GetMarkerLeftBandYPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GSBMV_GetMarkerRightBandXPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GSBMV_GetMarkerRightBandYPos (ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long

<!-- page 88 -->

### 35 - NVD_CmdGetHarmonicMarkerValue


#### a - Command function

NVD_CmdGetHarmonicMarkerValue
This function runs the "GetHarmonicMarkerValue" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetHarmonicMarkerValue (int nSocket, char* szWindowName,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails);
- Visual Basic declaration:
NVD_ CmdGetHarmonicMarkerValue (ByVal nSocket As Long, _
ByVal szWindowName As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer,_
ByVal nDetails As Integer) As Long
The info functions associated to this command function begin with "GHMV_" to remind
GetHarmonicMarkerValue.

#### b - Info Functions

The following functions enable to get information from the
CmdGetHarmonicMarkerValue command. The functions are ordered as information is
stored in the block (see NVDrive reference manual).
The "nTrace" parameter is 0 for the first trace.
- Visual C++ declarations:
int GHMV_GetMarkerNumber(int nSocket, int& nNumber);
int GHMV_GetTraceApplication(int nSocket, short& nApplied);
int GHMV_GetMarkerStartPosition(int nSocket, float& fPos);
int GHMV_GetMaxNbHarmonic(int nSocket, int& nNumber);
int GHMV_GetNbHarmonicVisible(int nSocket, int& nNumber);
int GHMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GHMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GHMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GHMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GHMV_GetTraceRefChannelNumber(int nSocket, int& nNum, long nTrace);
int GHMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,

<!-- page 89 -->
long nTrace);
int GHMV_GetTraceRefInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GHMV_GetMarkerXPos(int nSocket, float& fValue, long nTrace);
int GHMV_GetMarkerYPos(int nSocket, float& fValue, long nTrace);
int GHMV_GetNumberOfHarmonic(int nSocket, int& nNum, long nTrace);
int GHMV_GetMarkerHarmonicXPos(int nSocket, float& fValue, long nTrace,
long nHarmonic);
int GHMV_GetMarkerHarmonicYPos (int nSocket, float& fValue, long nTrace,
long nHarmonic);
- Visual Basic declaration:
GHMV_GetMarkerNumber(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GHMV_GetTraceApplication(ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GHMV_GetMarkerStartPosition(ByVal nSocket As Long, _
ByRef fPos As Single) As Long
GHMV_GetMaxNbHarmonic(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GHMV_GetNbHarmonicVisible(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GHMV_GetNumberOfTraces(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GHMV_GetTraceModuleID(ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nTrace As Long) As Long
GHMV_GetTraceProcessID(ByVal nSocket As Long, _
ByRef nID As Long, _
ByVal nTrace As Long) As Long
GHMV_GetTraceChannelNumber(ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GHMV_GetTraceRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Long, _
ByVal nTrace As Long) As Long
GHMV_GetTraceInputName (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GHMV_GetTraceRefInputName(ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nTrace As Long) As Long
GHMV_GetMarkerXPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long

<!-- page 90 -->
GHMV_GetMarkerYPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long) As Long
GHMV_GetNumberOfLeftBand (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nTrace As Long) As Long
GHMV_GetMarkerHarmonicXPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long, _
ByVal nHarmonic As Long) As Long
GHMV_GetMarkerHarmonicYPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByVal nTrace As Long, _
ByVal nHarmonic As Long) As Long

<!-- page 91 -->

### 36 - NVD_CmdGetPeriodMarkerValue


#### a - Command function

NVD_CmdGetPeriodMarkerValue
This function runs the "CmdGetPeriodMarkerValue" NVDrive command.
- Visual C++ declaration:
int CmdGetPeriodMarkerValue(int nSocket, const char* szWindow,
unsigned short nDisplayZoneType,
unsigned short nMarkerNumber,
unsigned short nDetails) ;
- Visual Basic declaration:
CmdGetPeriodMarkerValue(ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nDisplayZoneType As Integer, _
ByVal nMarkerNumber As Integer, _
ByVal nDetails As Integer) As Long
The info function associated to this command function begins with "GPRDMV_" to
remind GetPeRioDicMarkerValue.

#### b - Info Functions

The following functions enable to get information from the GetPeriodMarkerValue
command.
- Visual C++ declarations:
int GPRDMV_GetMarkerNumber(int nSocket, int& nNumber);
int GPRDMV_GetTraceApplication(int nSocket, short& nApplied);
int GPRDMV_GetStartPosition(int nSocket, float& fStartPosition);
int GPRDMV_GetMaxNbPeriod(int nSocket, int& nNumber);
int GPRDMV_GetNumberOfTraces(int nSocket, int& nNumber);
int GPRDMV_GetTraceModuleID(int nSocket, short& nID, long nTrace);
int GPRDMV_GetTraceProcessID(int nSocket, int& nID, long nTrace);
int GPRDMV_GetTraceChannelNumber(int nSocket, int& nNum, long nTrace);
int GPRDMV_GetTraceRefChannelNumber(int nSocket, int& nNum,
long nTrace);
int GPRDMV_GetTraceInputName(int nSocket, char* szName, int nBufferSize,
long nTrace);
int GPRDMV_GetTraceRefInputName(int nSocket, char* szName,
int nBufferSize, long nTrace);

<!-- page 92 -->
int GPRDMV_GetMarkerXPos(int nSocket, float& fValue, long nTrace);
int GPRDMV_GetMarkerYPos(int nSocket, float& fValue, long nTrace);
int GPRDMV_GetNumberOfPeriod(int nSocket, int& nNumber, long nTrace);
int GPRDMV_GetMarkerPeriodXPos(int nSocket, float& fValue, long nTrace,
long nPeriod);
int GPRDMV_GetMarkerPeriodYPos(int nSocket, float& fValue, long nTrace,
long nPeriod);
- Visual Basic declaration:
GPRDMV_GetMarkerNumber(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPRDMV_GetTraceApplication(ByVal nSocket As Long, _
ByRef nApplied As Integer) As Long
GPRDMV_GetStartPosition(ByVal nSocket As Long, _
ByRef fStartPosition As Single) As Long
GPRDMV_GetMaxNbPeriod(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPRDMV_GetNumberOfTraces(ByVal nSocket As Long, _
ByRef nNumber As Long) As Long
GPRDMV_GetTraceModuleID(ByVal nSocket As Long, _
ByRef nID as Integer, _
ByVal nTrace As Long) As Long
GPRDMV_GetTraceProcessID(ByVal nSocket As Long, _
ByRef nID As Long, _
ByVal nTrace As Long) As Long
GPRDMV_GetTraceChannelNumber(ByVal nSocket As Long, _
ByRef nNum As Long, _
ByRef nTrace As Long) As Long
GPRDMV_GetTraceRefChannelNumber(ByVal nSocket As Long, _
ByRef nNum As Long, _
ByRef nTrace As Long) As Long
GPRDMV_GetTraceInputName(ByVal nSocket As Long, _
ByVal szMessage As String, _
ByVal nBufferSize As Long, _
ByRef nTrace As Long) As Long
GPRDMV_GetTraceRefInputName(ByVal nSocket As Long, _
ByVal szMessage As String, _
ByVal nBufferSize As Long, _
ByRef nTrace As Long) As Long
GPRDMV_GetMarkerXPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByRef nTrace As Long) As Long
GPRDMV_GetMarkerYPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByRef nTrace As Long) As Long

<!-- page 93 -->
GPRDMV_GetNumberOfPeriod(ByVal nSocket As Long, _
ByRef nNumber As Long, _
ByRef nTrace As Long) As Long
GPRDMV_GetMarkerPeriodXPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByRef nTrace As Long, _
ByRef nPeriod As Long) As Long
GPRDMV_GetMarkerPeriodYPos(ByVal nSocket As Long, _
ByRef fValue As Single, _
ByRef nTrace As Long, _
ByRef nPeriod As Long) As Long

<!-- page 94 -->

### 37 - NVD_CmdGetAnalyzerModes


#### a - Command function

NVD_CmdGetAnalyzerModes
This function runs the "GetAnalyzerModes" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetAnalyzerModes(int nSocket);
- Visual Basic declaration:
NVD_CmdGetAnalyzerModes (ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GAM_" to remind
GetAnalyzerModes.

#### b - Info Functions

The following functions enable to get information from the CmdGetAnalyzerModes
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
- Visual C++ declarations:
int GAM_GetAnalysisMode(int nSocket, short& nMode);
int GAM_GetConnectionMode(int nSocket, short& nMode);
- Visual Basic declaration:
GAM_GetAnalysisMode (ByVal nSocket As Long, _
ByRef nMode As Integer) As Long
GAM_GetConnectionMode (ByVal nSocket As Long, _
ByRef nMode As Integer) As Long

<!-- page 95 -->

### 38 - NVD_CmdGetUnitInfo


#### a - Command function

NVD_CmdGetUnitInfo
This function runs the "GetUnitInfo" NVDrive command.
- Visual C++ declaration:
int NVD_GetUnitInfo (int nSocket, char* szMagnitude, char* szUnit);
- Visual Basic declaration:
NVD_CmdGetUnitInfo (ByVal nSocket As Long, _
ByVal szMagnitude As String, _
ByVal szUnit As String) As Long
The info functions associated to this command function begin with "GUI_" to remind
GetUnitInfo.

#### b - Info Functions

The following functions enable to get information from the CmdGetUnitInfo command.
The functions are ordered as information is stored in the block (see NVDrive reference
manual).
- Visual C++ declarations:
int GUI_GetVersion(int nSocket, int& nVersion);
int GUI_GetMagnitudeSI_Unit(int nSocket, char* szSIUnit, int nBufferSize);
int GUI_GetRadiansExponent(int nSocket, short& nExp);
int GUI_GetSteradiansExponent(int nSocket, short& nExp);
int GUI_GetMetersExponent(int nSocket, short& nExp);
int GUI_GetKilogramsExponent(int nSocket, short& nExp);
int GUI_GetSecondsExponent(int nSocket, short& nExp);
int GUI_GetAmperesExponent(int nSocket, short& nExp);
int GUI_GetKelvinsExponent(int nSocket, short& nExp);
int GUI_GetMolesExponent(int nSocket, short& nExp);
int GUI_GetCandelasExponent(int nSocket, short& nExp);
int GUI_GetLabel(int nSocket, char* szLabel, int nBufferSize);
int GUI_GetACoefForSIConvert(int nSocket, float& fCoef);
int GUI_GetBCoefForSIConvert(int nSocket, float& fCoef);
int GUI_Get0dBRef(int nSocket, float& fRef);
int GUI_GetFactorFordBConvert(int nSocket, float& fFactor);

<!-- page 96 -->
- Visual Basic declaration:
GUI_GetVersion (ByVal nSocket As Long, _
ByRef nVersion As Integer) As Long
GUI_GetMagnitudeSI_Unit (ByVal nSocket As Long, _
ByVal szSIUnit As String, _
ByVal nBufferSize As Long) As Long
GUI_GetRadiansExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetSteradiansExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetMetersExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetKilogramsExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetSecondsExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetAmperesExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetKelvinsExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetMolesExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetCandelasExponent (ByVal nSocket As Long, _
ByRef nExp As Integer) As Long
GUI_GetLabel(ByVal nSocket As Long, _
ByVal szSIUnit As String, _
ByVal nBufferSize As Long) As Long
GUI_GetACoefForSIConvert(ByVal nSocket As Long, _
ByRef fCoef As Single) As Long
GUI_GetBCoefForSIConvert(ByVal nSocket As Long, _
ByRef fCoef As Single) As Long
GUI_Get0dBRef(ByVal nSocket As Long, _
ByRef fRef As Single) As Long
GUI_GetFactorFordBConvert(ByVal nSocket As Long, _
ByRef fFactor As Single) As Long

<!-- page 97 -->

### 39 - NVD_CmdGetMagnitudeList


#### a - Command function

NVD_CmdGetMagnitudeList
This function runs the "GetMagnitudeList" NVDrive command.
- Visual C++ declaration:
int NVD_GetMagnitudeList (int nSocket);
- Visual Basic declaration:
NVD_GetMagnitudeList (ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GML_" to remind
GetMagnitudeList.

#### b - Info Functions

The following functions enable to get information from the CmdGetMagnitudeList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GML_GetSize(int nSocket, int& nNbElt);
int GML_GetMagnitudeInList(int nSocket, char* szMagnitude, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GML_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Long) As Long
GML_GetMagnitudeInList (ByVal nSocket As Long, _
ByVal szMagnitude As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Long) As Long

<!-- page 98 -->

### 40 - NVD_CmdGetMagnitudeInfo


#### a - Command function

NVD_CmdGetMagnitudeInfo
This function runs the "GetMagnitudeInfo" NVDrive command.
- Visual C++ declaration:
int NVD_GetMagnitudeInfo (int nSocket, char* szMagnitudeKey);
- Visual Basic declaration:
NVD_CmdGetMagnitudeInfo (ByVal nSocket As Long, _
ByVal szMagnitudeKey As String) As Long
The info functions associated to this command function begin with "GMI_" to remind
GetMagnitudeInfo.

#### b - Info Functions

The following functions enable to get information from the CmdGetMagnitudeInfo
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
- Visual C++ declarations:
int GMI_GetMagnitudeName(int nSocket, char* szMagnitudeName,
int nBufferSize);
int GMI_GetUnitName(int nSocket, char* szUnitName, int nBufferSize);
int GMI_GetUnitLabel(int nSocket, char* szUnitLabel, int nBufferSize);
- Visual Basic declaration:
GMI_GetMagnitudeName(ByVal nSocket As Long, _
ByVal szMagnitudeName As String, _
ByVal nBufferSize As Long) As Long
GMI_GetUnitName(ByVal nSocket As Long, _
ByVal szUnitName As String, _
ByVal nBufferSize As Long) As Long
GMI_GetUnitLabel(ByVal nSocket As Long, _
ByVal szUnitLabel As String , _
ByVal nBufferSize As Long) As Long

<!-- page 99 -->

### 41 - NVD_CmdGetUnitList


#### a - Command function

NVD_CmdGetUnitList
This function runs the "GetUnitList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetUnitList(int nSocket, char* szMagnitude);
- Visual Basic declaration:
NVD_CmdGetUnitList (ByVal nSocket As Long, _
ByVal szMagnitude As String) As Long
The info functions associated to this command function begin with "GUL_" to remind
GetUnitList.

#### b - Info Functions

The following functions enable to get information from the CmdGetUnitList command.
The first function enables to get the number of elements in the list. The second function
enables to get 1 element in the list.
- Visual C++ declarations:
int GUL_GetSize(int nSocket, int& nNbElt);
int GUL_GetUnitInList(int nSocket, char* szUnit, int nBufferSize, int nIndex);
- Visual Basic declaration:
GUL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GUL_GetUnitInList (ByVal nSocket As Long, _
ByVal szUnit As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 100 -->

### 42 - NVD_CmdGetCurrentUnit


#### a - Command function

NVD_CmdGetCurrentUnit
This function runs the "GetCurrentUnit" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentUnit(int nSocket, char* szMagnitude);
- Visual Basic declaration:
NVD_CmdGetCurrentUnit(ByVal nSocket As Long, _
ByVal szMagnitude As String) As Long
The info functions associated to this command function begin with "GCU_" to remind
GetCurrentUnit.

#### b - Info Functions

The following function enables to get information from the CmdGetCurrentUnit
command.
- Visual C++ declarations:
int GCU_GetUnitName(int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GCU_GetUnitName(ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 101 -->

### 43 - NVD_CmdGetTransducerList


#### a - Command function

NVD_CmdGetTransducerList
This function runs the "GetTransducerList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetTransducerList (int nSocket, char* szWindow);
- Visual Basic declaration:
NVD_CmdGetTransducerList (ByVal nSocket As Long, _
ByVal szWindow As String) As Long
The info functions associated to this command function begin with "GTL_" to remind
GetTransducerList.

#### b - Info Functions

The following functions enable to get information from the CmdGetTransducerList
command. The first function enables to get the number of elements in the list. For the
other functions, nIndex identify the position of the marker in the list (from 0 to nNbElt -
1).
- Visual C++ declarations:
int GTL_GetSize(int nSocket, int& nNbElt);
int GTL_GetTransducerIdInList (int nSocket, char* szId, int nBufferSize,
int nIndex);
int GTL_GetTransducerNameInList(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GTL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GTL_GetTransducerIdInList (ByVal nSocket As Long, _
ByVal szId As String , ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GTL_GetTransducerNameInList (ByVal nSocket As Long, _
ByVal szName As String , ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 102 -->

### 44 - NVD_CmdGetProjectList


#### a - Command function

NVD_CmdGetProjectList
This function runs the "GetProjectList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetProjectList(int nSocket);
- Visual Basic declaration:
NVD_CmdGetProjectList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GPL_" to remind
GetProjectList.

#### b - Info Functions

The following functions enable to get information from the CmdGetProjectList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GPL_GetSize(int nSocket, int& nNbElt);
int GPL_GetProjectInList(int nSocket, char* szProject, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GPL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GPL_GetProjectInList (ByVal nSocket As Long, _
ByVal szProject As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 103 -->

### 45 - NVD_CmdGetMeasureList


#### a - Command function

NVD_CmdGetMeasureList
This function runs the "GetMeasureList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetMeasureList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetMeasureList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GMEL_" to remind
GetMeasureList.

#### b - Info Functions

The following functions enable to get information from the CmdGetMeasureList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GMEL_GetSize(int nSocket, int& nNbElt);
int GMEL_GetMeasureInList(int nSocket, char* szMeasure, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GMEL_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GMEL_GetMeasureInList(ByVal nSocket As Long, _
ByVal szMeasure As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 104 -->

### 46 - NVD_CmdGetWindowList


#### a - Command function

NVD_CmdGetWindowList
This function runs the "GetWindowList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWindowList(
int nSocket,
int nModule,
int nProcess,
int nChannel,
int nRefChannel);
- Visual Basic declaration:
NVD_CmdGetWindowList( _
The info functions associated to this command function begin with "GWL_" to remind
GetWindowList.

#### b - Info Functions

The following functions enable to get information from the CmdGetWindowList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GWL_GetSize(int nSocket, int & nNbElt);
int GWL_GetWindowInList(
int nSocket,
char* szWindow,
int nBufferSize,
int nIndex);

**ByVal nSocket As Long, _**

| Column 1 |
|---|
| ByVal nModule As Long, _ |
| ByVal nProcess As Long, _ |
| ByVal nChannel As Long, _ |
| ByVal nRefChannel As Long) As Long |


<!-- page 105 -->
- Visual Basic declaration:

**GWL_GetSize(ByVal nSocket As Long, ByRef nNbElt As Long) As Long**

| Column 1 |
|---|
| GWL_GetWindowInList( _ |


**ByVal nSocket As Long, _**

| Column 1 |
|---|
| ByVal szWindow As String, _ |
| ByVal nBufferSize As Long, _ |
| ByVal nIndex As Long) As Long |


<!-- page 106 -->

### 47 - NVD_CmdGetWindowNameList


#### a - Command function

NVD_CmdGetWindowNameList
This function runs the "GetWindowNameList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWindowNameList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetWindowNameList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GWNL_" to remind
GetWindowNameList.

#### b - Info Functions

The following functions enable to get information from the CmdGetWindowNameList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GWNL_GetSize(int nSocket, int& nNbElt);
int GWNL_GetWindowInList(int nSocket, char* szWindow,
int nBufferSize, int nIndex);
- Visual Basic declaration:
GWNL_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GWNL_GetWindowInList(ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 107 -->

### 48 - NVD_CmdGetLayoutList


#### a - Command function

NVD_CmdGetLayoutList
This function runs the "GetLayoutList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetLayoutList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetLayoutList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GLL_" to remind
GetLayoutList.

#### b - Info Functions

The following functions enable to get information from the CmdGetLayoutList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GLL_GetSize(int nSocket, int& nNbElt);
int GLL_GetWindowInList(int nSocket, char* szLayout,
int nBufferSize, int nIndex);
- Visual Basic declaration:
GWNL_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GWNL_GetWindowInList(ByVal nSocket As Long, _
ByVal szWindow As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 108 -->

### 49 - NVD_CmdGetCurrentLayout


#### a - Command function

NVD_CmdGetCurrentLayout
This function runs the "GetCurrentLayout" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentLayout(int nSocket);
- Visual Basic declaration:
NVD_CmdGetCurrentLayout(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GCL_" to remind
GetCurrentLayout.

#### b - Info Functions

The following functions enable to get information from the GetCurrentLayout command.
- Visual C++ declarations:
int GCL_GetLayoutName (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GCL_GetLayoutName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 109 -->

### 50 - NVD_CmdGetDisplayMode


#### a - Command function

NVD_CmdGetDisplayMode
This function runs the "GetDisplayMode" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetDisplayMode (int nSocket,
char* szLayout, char* szWindow);
- Visual Basic declaration:
NVD_CmdGetDisplayMode(ByVal nSocket As Long, _
ByVal szLayout As String, ByVal szWindow As String) As Long
The info functions associated to this command function begin with "GDM_" to remind
GetDisplayMode.

#### b - Info Functions

The following functions enable to get information from the CmdGetDisplayMode
command. The function enables to get the current window display mode.
- Visual C++ declarations:
int GDM_GetCurrentDisplayMode(int nSocket, int& nDisplayMode);
- Visual Basic declaration:
GDM_GetCurrentDisplayMode(ByVal nSocket As Long, _
ByRef nDisplayMode As Integer) As Long

<!-- page 110 -->

### 51 - NVD_CmdGetDisplayModeList


#### a - Command function

NVD_CmdGetDisplayModeList
This function runs the "GetDisplayModeList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetDisplayModeList (int nSocket,
char* szLayout, char* szWindow);
- Visual Basic declaration:
NVD_CmdGetDisplayModeList(ByVal nSocket As Long, _
ByVal szLayout As String, ByVal szWindow As String) As Long
The info functions associated to this command function begin with "GDML_" to remind
GetDisplayModeList.

#### b - Info Functions

The following functions enable to get information from the CmdGetDisplayModeList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GDML_GetSize(int nSocket, int& nNbElt);
int GDML_GetDisplayModeInList(int nSocket, int& nDisplayMode, int nIndex);
- Visual Basic declaration:
GDML_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GDML_GetDisplayModeInList(ByVal nSocket As Long, _
ByRef nDisplayMode As Integer, _
ByVal nIndex As Integer) As Long

<!-- page 111 -->

### 52 - NVD_CmdGetReferenceList


#### a - Command function

NVD_CmdGetReferenceList
This function runs the "GetReferenceList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetReferenceList (int nSocket,
char* szLayout, char* szWindow,
unsigned short nAreaType);
- Visual Basic declaration:
NVD_CmdGetReferenceList(ByVal nSocket As Long, _
ByVal szLayout As String, ByVal szWindow As String, _
ByVal nAreaType As Integer) As Long
The info functions associated to this command function begin with "GRL_" to remind
GetReferenceList.

#### b - Info Functions

The following functions enable to get information from the CmdGetReferenceList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GRL_GetReferenceNumber (int nSocket, int& nNumberOfReference);
int GRL_GetReferenceName (int nSocket, int nReferenceNumber,
char* szRefName, int nBufferSize);
- Visual Basic declaration:
GRL_GetReferenceNumber (ByVal nSocket As Long, _
ByRef nNumberOfReference As Integer) As Long
GRL_GetReferenceName (ByVal nSocket As Long, _
ByVal nReferenceNumber As Integer, _
ByVal szRefName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 112 -->

### 53 - NVD_CmdGetCurrentReference


#### a - Command function

NVD_CmdGetCurrentReference
This function runs the "GetCurrentReference" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentReference(int nSocket,
char* szLayout, char* szWindow,
unsigned short nDisplayZoneType);
- Visual Basic declaration:
NVD_CmdGetCurrentReference(ByVal nSocket As Long, _
ByVal szLayout As String, ByVal szWindow As String, _
ByVal nDisplayZoneType As Integer) As Long
The info functions associated to this command function begin with "GCR_" to remind
GetCurrentReference.

#### b - Info Functions

The following functions enable to get information from the CmdGetCurrentReference
command.
- Visual C++ declarations:
int GCR_GetReferenceName (int nSocket, char* szRefName, int nBufferSize);
- Visual Basic declaration:
GCR_GetReferenceName(ByVal nSocket As Long, _
ByVal szRefName As String,
ByVal nBufferSize As Long) As Long

<!-- page 113 -->

### 54 - NVD_CmdGetPreferedWtfReference


#### a - Command function

NVD_CmdGetPreferedWtfReference
This function runs the "GetPreferedWtfReference" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPreferedWtfReference (int nSocket);
- Visual Basic declaration:
NVD_CmdGetPreferedWtfReference(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GPWR_" to remind
GetPreferedWtfReference.

#### b - Info Functions

The following functions enable to get information from the CmdGetCurrentReference
command.
- Visual C++ declarations:
int GPWR_GetIdMagnitude (int nSocket, short& nIdMagnitude);
- Visual Basic declaration:
GPWR_GetIdMagnitude(ByVal nSocket As Long, _
ByRef nIdMagnitude As Integer) As Long

<!-- page 114 -->

### 55 - NVD_CmdGetScaleInfo


#### a - Command function

NVD_CmdGetScaleInfo
This function runs the "GetScaleInfo" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetScaleInfo(int nSocket, char* szWindowName,
unsigned short nDisplayZoneType, int nAxis, BOOL bGraduationInfo);
int NVD_CmdGetScaleInfoEx(int nSocket, char* szWindowName,
unsigned short nDisplayZoneType, int nAxis, BOOL bGraduationInfo,
int nTrace);
- Visual Basic declaration:
NVD_CmdGetScaleInfo (ByVal nSocket As Long, _
ByVal szWndName As String, _
ByVal nDisplayZoneType As Integer , _
ByVal nAxis As Integer, _
ByVal bGraduationInfo As Boolean) As Long
NVD_CmdGetScaleInfoEx (ByVal nSocket As Long, _
ByVal szWndName As String, _
ByVal nDisplayZoneType As Integer , _
ByVal nAxis As Integer, _
ByVal bGraduationInfo As Boolean, _
ByVal nTrace as Integer) As Long
The info function associated to this command function begins with "GSI_" to remind
GetScaleInfo.

#### b - Info Functions

The following functions enable to get information from the GetScaleInfo command.
- Visual C++ declarations:
int GSI_GetScaleMin (int nSocket, float& fValue);
int GSI_GetScaleMax (int nSocket, float& fValue);
int GSI_GetType (int nSocket, int& nType);
int GSI_GetGraduations(int nSocket, char* szGraduationList, int nBufferSize);
- Visual Basic declaration:
GSI_GetScaleMin (ByVal nSocket As Long, _

<!-- page 115 -->
ByRef fValue As Single) As Long
GSI_GetScaleMax (ByVal nSocket As Long, _
ByRef fValue As Single) As Long
GSI_GetType (ByVal nSocket As Long, _
ByRef nType As Integer) As Long
GSI_GetGraduations(ByVal nSocket As Long, _
ByVal szGraduationLists As String, _
ByVal nBufferSize As Long) As Long

<!-- page 116 -->

### 56 - NVD_CmdGetAvailableScale


#### a - Command function

NVD_CmdGetAvailableScale
This function runs the "GetAvailableScale" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetAvailableScale(int nSocket, char* szWndName,
unsigned short nAreaType, unsigned short nScaleType) ;
- Visual Basic declaration:
NVD_CmdGetAvailableScale (ByVal nSocket As Long, _
ByVal szWndName As String, ByVal nAreaType As Integer,
ByVal nScaleType As Integer) As Long
The info function associated to this command function begins with "GAS_" to remind
GetAvailableScale.

#### b - Info Functions

The following functions enable to get information from the GetAvailableScale command.
- Visual C++ declarations:
int GAS_GetLinearAvailability (int nSocket, bool& ScaleAvailability);
int GAS_GetLogAvailability (int nSocket, bool& ScaleAvailability);
int GAS_GetdBAvailability (int nSocket, bool& ScaleAvailability);
int GAS_GetOctaveAvailability (int nSocket, bool& ScaleAvailability);
- Visual Basic declaration:
GAS_GetLinearAvailability(ByVal nSocket As Long, _
ByRef ScaleAvailability As Boolean) As Long
GAS_GetLogAvailability(ByVal nSocket As Long, _
ByRef ScaleAvailability As Boolean) As Long
GAS_GetdBAvailability(ByVal nSocket As Long, _
ByRef ScaleAvailability As Boolean) As Long
GAS_GetOctaveAvailability(ByVal nSocket As Long, _
ByRef ScaleAvailability As Boolean) As Long

<!-- page 117 -->

### 57 - NVD_IsResultWaterfallisable


#### a - Command function

NVD_CmdIsResultWaterfallisable
This function runs the "IsResultWaterfallisable" NVDrive command.
- Visual C++ declaration:
int NVD_CmdIsResultWaterfallisable(int nSocket,
int nNumModule, int nNumProcess);
- Visual Basic declaration:
NVD_CmdIsResultWaterfallisable(ByVal nSocket As Long, _
ByVal nNumModule As Long, _
ByVal nNumProcess As Long) As Long
The info functions associated to this command function begin with "IRW_" to remind
IsResultWaterfallisable.

#### b - Info Functions

The following functions enable to get information from the IsResultWaterfallisable
command.
- Visual C++ declarations:
int IRW_IsWaterfallisable(int nSocket, bool& bIsWTFable);
- Visual Basic declaration:
IRW_IsWaterfallisable (ByVal nSocket As Long, _
ByVal bIsWTFable As Boolean) As Long

<!-- page 118 -->

### 58 - NVD_CmdGetWindowDisplayZone


#### a - Command function

NVD_CmdGetWindowDisplayZone
This function runs the "GetWindowDisplayZone" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWindowDisplayZone (int nSocket, char* szWindow);
- Visual Basic declaration:
NVD_CmdGetWindowDisplayZone (ByVal nSocket As Long, _
ByVal szWindow As String) As Long
The info functions associated to this command function begin with "GWDZ_" to remind
GetWindowDisplayZone.

#### b - Info Functions

The following functions enable to get information from the CmdGetWindowDisplayZone
command. The first function enables to get the number of elements in the list. For the
other functions, nIndex identify the position of the marker in the list (from 0 to nNbElt -
1).
- Visual C++ declarations:
int GWDZ_GetSize(int nSocket, int& nNbElt);
int GWDZ_GetDisplayZoneInList(int nSocket, short& nZone, int nIndex);
- Visual Basic declaration:
GWDZ_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GWDZ_GetDisplayZoneInList (ByVal nSocket As Long, _
ByRef nZone As Integer, _
ByVal nIndex As Integer) As Long

<!-- page 119 -->

### 59 - NVD_CmdGetWindowTraces


#### a - Command function

NVD_CmdGetWindowTraces
This function runs the "GetWindowTraces" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWindowTraces(int nSocket);
- Visual Basic declaration:
NVD_CmdGetWindowTraces(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GWT_" to remind
GetWindowTraces.

#### b - Info Functions

The following functions enable to get information from the CmdGetWindowNameList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GWT_GetSize(int nSocket, int& nNbElt);
int GWT_GetModuleID(int nSocket, short& nID, int nIndex);
int GWT_GetProcessID(int nSocket, int& nID, int nIndex);
int GWT_GetChannelNumber(int nSocket, int& nNum, int nIndex);
int GWT_GetRefChannelNumber(int nSocket, int& nNum, int nIndex);
int GWT_GetInputName(int nSocket, char* szName, int nBufferSize, int nIndex);
int GWT_GetRefInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GWT_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GWT_GetModuleID(ByVal nSocket As Long, _
ByRef nID As Integer, ByVal nIndex As Integer) As Long
GWT_GetProcessID(ByVal nSocket As Long, ByRef nID As Integer, ByVal
nIndex As Integer) As Long
GWT_GetChannelNumber(ByVal nSocket As Long, _
ByRef nNum As Integer, ByVal nIndex As Integer) As Long

<!-- page 120 -->
GWT_GetRefChannelNumber(ByVal nSocket As Long, _
ByRef nNum As Integer, ByVal nIndex As Integer) As Long
GWT_GetInputName(ByVal nSocket As Long, ByVal szName As String, _
ByVal nBufferSize As Long, ByVal nIndex As Integer) As Long
GWT_GetRefInputName(ByVal nSocket As Long, ByVal szName As String, _
ByVal nBufferSize As Long, ByVal nIndex As Integer) As Long

<!-- page 121 -->

### 60 - NVD_CmdGetActiveWindow


#### a - Command function

NVD_CmdGetActiveWindow
This function runs the "GetActiveWindow" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetActiveWindow(int nSocket);
- Visual Basic declaration:
NVD_CmdGetActiveWindow(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GAW_" to remind
GetActiveWindow.

#### b - Info Functions

The following functions enable to get information from the CmdGetActiveWindow
command and retrieve the window name.
- Visual C++ declarations:
int GAW_GetWindowName (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GAW_GetWindowName (ByVal nSocket As Long, _
ByVal szName As String) As Long

<!-- page 122 -->

### 61 - NVD_CmdGetWindowPosition


#### a - Command function

NVD_CmdGetWindowPosition
This function runs the "GetWindowPosition" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWindowPosition(int nSocket, char* szLayout,
char* szWindowName);
- Visual Basic declaration:
NVD_CmdGetWindowPosition(ByVal nSocket As Long _
ByVal szLayout As String _
ByVal szWindowName As String) As Long
The info functions associated to this command function begin with "GWP_" to remind
GetWindowPosition.

#### b - Info Functions

The following functions enable to get information from the CmdGetWindowPosition
command.
- Visual C++ declarations:
int GWP_GetLeftPosition(int nSocket, int& nLeft);
int GWP_GetRightPosition(int nSocket, int& nRight);
int GWP_GetTopPosition(int nSocket, int& nTop);
int GWP_GetBottomPosition(int nSocket, int& nBottom);
- Visual Basic declaration:
GWP_GetLeftPosition (ByVal nSocket As Long, _
ByRef nLeft as Long) As Long
GWP_GetRightPosition (ByVal nSocket As Long, _
ByRef nRight as Long) As Long
GWP_GetTopPosition (ByVal nSocket As Long, _
ByRef nTop as Long) As Long
GWP_GetBottomPosition (ByVal nSocket As Long, _
ByRef nBottom as Long) As Long

<!-- page 123 -->

### 62 - NVD_CmdGetRotationPreferences


#### a - Command function

NVD_CmdGetRotationPreferences
This function runs the "CmdGetRotationPreferences" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetRotationPreferences(int nSocket, const char* szLayout, const
char* szWindow) ;
- Visual Basic declaration:
NVD_ CmdGetRotationPreferences (ByVal nSocket As Long, _
ByVal szLayout As String, _
ByVal szWindow As String) As Long
The info function associated to this command function begins with "GRP_" to remind
GetRotationPreferences.

#### b - Info Functions

The following functions enable to get information from the GetRotationPreferences
command.
- Visual C++ declarations:
int GRP_GetDirection(int nSocket,int & nDirection);
int GRP_GetX(int nSocket,int & nX);
int GRP_GetY(int nSocket,int & nY);
- Visual Basic declaration:
GRP_GetDirection (ByVal nSocket As Long, _
ByRef nDirection As Integer) As Long
GRP_GetX (ByVal nSocket As Long, _
ByRef nX As Integer) As Long
GRP_GetY (ByVal nSocket As Long, _
ByRef nY As Integer) As Long

<!-- page 124 -->

### 63 - NVD_CmdGetPinStatus


#### a - Command function

NVD_CmdGetPinStatus
This function runs the "CmdGetPinStatus" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPinStatus(int nSocket, const char* szLayout, const char*
szWindow) ;
- Visual Basic declaration:
NVD_ CmdGetPinStatus(ByVal nSocket As Long, _
ByVal szLayout As String, _
ByVal szWindow As String) As Long
The info function associated to this command function begins with "GPS_" to remind
GetPinStatus.

#### b - Info Functions

The following function enables to get information from the GetPinStatus command.
- Visual C++ declarations:
int GPS_GetStatus(int nSocket, bool& bPinned);
- Visual Basic declaration:
GPS_GetStatus (ByVal nSocket As Long, _
ByRef bPinned As Boolean) As Long

<!-- page 125 -->

### 64 - NVD_CmdGetResultCaption


#### a - Command function

NVD_CmdGetResultCaption
This function runs the "GetResultCaption" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetResultCaption (int nSocket, unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel = 0);
- Visual Basic declaration:
NVD_CmdGetResultCaption(ByVal nSocket As Long , _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer) As Long
The info functions associated to this command function begin with "GRC_" to remind
GetResultCaption.

#### b - Info Functions

The following functions enable to get information from the CmdGetResultCaption
command.
- Visual C++ declarations:
int GRC_GetCaption (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GRC_GetCaption (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 126 -->

### 65 - NVD_CmdGetResultList


#### a - Command function

NVD_CmdGetResultList
This function runs the "GetResultList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetResultList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetResultList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GRL_" to remind
GetResultList.

#### b - Info Functions

The following functions enable to get information from the CmdGetResultList command.
The first function enables to get the number of elements in the list. The second function
enables to get 1 element in the list.
- Visual C++ declarations:
int GRL_GetSize(int nSocket, int& nNbElt);
int GRL_GetModuleID(int nSocket, short& nID, int nIndex);
int GRL_GetProcessID(int nSocket, int& nID, int nIndex);
int GRL_GetChannelNumber(int nSocket, int& nNum, int nIndex);
int GRL_GetRefChannelNumber(int nSocket, int& nNum, int nIndex);
int GRL_GetInputName(int nSocket, char* szName, int nBufferSize, int nIndex);
int GRL_GetRefInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GRL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GRL_GetModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GRL_GetProcessID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long

<!-- page 127 -->
GRL_GetChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GRL_GetRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GRL_GetInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GRL_GetRefInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 128 -->

### 66 - NVD_CmdGetWtfResultList


#### a - Command function

NVD_CmdGetWtfResultList
This function runs the "GetWtfResultList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetWtfResultList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetWtfResultList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GWRL_" to remind
GetWtfResultList.

#### b - Info Functions

The following functions enable to get information from the CmdGetWtfResultList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GWRL_GetSize(int nSocket, int& nNbElt);
int GWRL_GetModuleID(int nSocket, short& nID, int nIndex);
int GWRL_GetProcessID(int nSocket, int& nID, int nIndex);
int GWRL_GetChannelNumber(int nSocket, int& nNum, int nIndex);
int GWRL_GetRefChannelNumber(int nSocket, int& nNum, int nIndex);
int GWRL_GetInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
int GWRL_GetRefInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GWRL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GWRL_GetModuleID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GWRL_GetProcessID (ByVal nSocket As Long, _
ByRef nID As Integer, _

<!-- page 129 -->
ByVal nIndex As Integer) As Long
GWRL_GetChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GWRL_GetRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GWRL_GetInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GWRL_GetRefInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 130 -->

### 67 - NVD_CmdGetSavedResultCaption


#### a - Command function

NVD_CmdGetSavedResultCaption
This function runs the "GetSavedResultCaption" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSavedResultCaption (int nSocket,
char* szProjectName,
char* szMeasurementName,
unsigned short nModule,
unsigned short nProcess,
unsigned short nChannel,
unsigned short nRefChannel = 0);
- Visual Basic declaration:
NVD_CmdGetSavedResultCaption(ByVal nSocket As Long , _
ByVal szProjectName As String, _
ByVal szMeasurementName As String, _
ByVal nModule As Integer, _
ByVal nSubModule As Integer, _
ByVal nChannel As Integer, _
ByVal nRefChannel As Integer) As Long
The info functions associated to this command function begin with "GSRC_" to remind
GetSavedResultCaption.

#### b - Info Functions

The following functions enable to get information from the CmdGetSavedResultCaption
command
- Visual C++ declarations:
int GSRC_GetCaption (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GSRC_GetCaption (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 131 -->

### 68 - NVD_CmdGetSavedResultList


#### a - Command function

NVD_CmdGetSavedResultList
This function runs the "GetSavedResultList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSavedResultList (int nSocket,
char* szMeasurementName,
char* szProjectName);
- Visual Basic declaration:
NVD_CmdGetSavedResultList(ByVal nSocket As Long,
ByVal szMeasure As String,
ByVal szProject As String) As Long
The info functions associated to this command function begin with "GSRL_" to remind
GetSavedResultList.

#### b - Info Functions

The following functions enable to get information from the CmdGetSavedResultList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GSRL_GetSize (int nSocket, int& nNbElt);
int GSRL_GetModuleID(int nSocket, short& nID, int nIndex);
int GSRL_GetProcessID(int nSocket, int& nID, int nIndex);
int GSRL_GetChannelNumber(int nSocket, int& nNum, int nIndex);
int GSRL_GetRefChannelNumber(int nSocket, int& nNum, int nIndex);
int GSRL_GetInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
int GSRL_GetRefInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GSRL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GSRL_GetModuleID (ByVal nSocket As Long, _

<!-- page 132 -->
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GSRL_GetProcessID (ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GSRL_GetChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GSRL_GetRefChannelNumber (ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GSRL_GetInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GSRL_GetRefInputName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 133 -->

### 69 - NVD_CmdGetTCPResultChannelList


#### a - Command function

NVD_ CmdGetTCPResultChannelList
This function runs the "GetTCPResultChannelList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetTCPResultChannelList (int nSocket);
- Visual Basic declaration:
NVD_CmdGetTCPResultChannelList(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GTRCL_" to
remind GetTCPResultChannelList.

#### b - Info Functions

The following functions enable to get information from the GetTCPResultChannelList
command. The first function enables to get the number of elements in the list. The second
function enables to get 1 element in the list.
- Visual C++ declarations:
int GTRCL_GetSize(int nSocket, int& nNbElt);
int GTRCL_GetProcessID(int nSocket, int& nID, int nIndex);
int GTRCL_GetTcpId(int nSocket, int& nNum, int nIndex);
int GTRCL_GetInputName(int nSocket, char* szName, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GTRCL_GetSize(ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GTRCL_GetProcessID(ByVal nSocket As Long, _
ByRef nID As Integer, _
ByVal nIndex As Integer) As Long
GTRCL_GetTcpId(ByVal nSocket As Long, _
ByRef nNum As Integer, _
ByVal nIndex As Integer) As Long
GTRCL_GetInputName(ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 134 -->

### 70 - NVD_CmdGetAnalyzer_TriggerState


#### a - Command function

NVD_CmdGetAnalyzer_TriggerState
This function runs the "GetAnalyzerState" NVDrive command, with the "Trigger state"
parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_TriggerState(int nSocket,
unsigned short nAnalyzerNum);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_TriggerState(ByVal nSocket As Long, _
ByVal nAnalyzerNum As Integer) As Long
The info functions associated to this command function begin with "GATS_" to remind
GetAnalyzer_TriggerState.

#### b - Info Functions

The following function enables to get the trigger state of the selected analyzer.
- Visual C++ declarations:
int GATS_GetTriggerState(int nSocket, char* szTriggerState, int nBufferSize);
- Visual Basic declaration:
GATS_GetTriggerState(ByVal nSocket As Long, _
ByVal szTriggerState As String, _
ByVal nBufferSize As Long) As Long

<!-- page 135 -->

### 71 - NVD_CmdGetAnalyzer_Count


#### a - Command function

NVD_CmdGetAnalyzer_Count
This function runs the "GetAnalyzerState" NVDrive command, with the "Count"
parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_Count(int nSocket,
unsigned short nAnalyzerNum);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_Count(ByVal nSocket As Long, _
ByVal nAnalyzerNum As Integer) As Long
The info functions associated to this command function begin with "GAC_" to remind
GetAnalyzerCount.

#### b - Info Functions

The following function enables to get the count of the selected analyzer.
- Visual C++ declarations:
int GAC_GetCount(int nSocket, float& fCount);
- Visual Basic declaration:
GAC_GetCount (ByVal nSocket As Long, _
ByRef fCount As Single) As Long

<!-- page 136 -->

### 72 - NVD_CmdGetAnalyzer_ RealTime


#### a - Command function

NVD_CmdGetAnalyzer_ RealTime
This function runs the "GetAnalyzerState" NVDrive command, with the "Real-time"
parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_RealTime(int nSocket,
unsigned short nAnalyzerNum);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_RealTime(ByVal nSocket As Long, _
ByVal nAnalyzerNum As Integer) As Long
The info functions associated to this command function begin with "GART_" to remind
GetAnalyzerRealTime.

#### b - Info Functions

The following function enables to get the real-time state of the selected analyzer.
- Visual C++ declarations:
int GART_GetRealTime(int nSocket, char* szRealTime, int nBufferSize);
- Visual Basic declaration:
GART_GetRealTime(ByVal nSocket As Long, _
ByVal szRealTime As String, _
ByVal nBufferSize As Long) As Long

<!-- page 137 -->

### 73 - NVD_CmdGetAnalyzer_BlockOverload


#### a - Command function

NVD_CmdGetAnalyzer_BlockOverload
This function runs the "GetAnalyzerState" NVDrive command, with the "Block
overload" parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_BlockOverload(int nSocket,
unsigned short nAnalyzerNum);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_BlockOverload(ByVal nSocket As Long, _
ByVal nAnalyzerNum As Integer) As Long
The info functions associated to this command function begin with "GABO_" to remind
GetAnalyzerBlockOverload.

#### b - Info Functions

The following function enables to get the Block overload state of the selected analyzer.
- Visual C++ declarations:
int GABO_GetBlockOverload(int nSocket, char* szBlockOverload,
int nBufferSize);
- Visual Basic declaration:
GABO_GetBlockOverload(ByVal nSocket As Long, _
ByVal szBlockOverload As String, _
ByVal nBufferSize As Long) As Long

<!-- page 138 -->

### 74 - NVD_CmdGetAnalyzer_AnalysisOverload


#### a - Command function

NVD_CmdGetAnalyzer_AnalysisOverload
This function runs the "GetAnalyzerState" NVDrive command, with the "Analysis
overload" parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_AnalysisOverload(int nSocket,
unsigned short nAnalyzerNum);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_AnalysisOverload(ByVal nSocket As Long, _
ByVal nAnalyzerNum As Integer) As Long
The info functions associated to this command function begin with "GAAO_" to remind
GetAnalyzerAnalysisOverload.

#### b - Info Functions

The following function enables to get the Analysis overload state of the selected analyzer.
- Visual C++ declarations:
int GAAO_GetAnalysisOverload(int nSocket, char* szAnalysisOverload,
int nBufferSize);
- Visual Basic declaration:
GAAO_GetAnalysisOverload(ByVal nSocket As Long, _
ByVal szAnalysisOverloadAs String, _
ByVal nBufferSize As Long) As Long

<!-- page 139 -->

### 75 - NVD_CmdGetAnalyzer_RecordCounter


#### a - Command function

NVD_CmdGetAnalyzer_RecordCounter
This function runs the "GetAnalyzerState" NVDrive command, with the "Record
counter" parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_RecordCounter(int nSocket);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_RecordCounter(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GARC_" to remind
GetAnalyzerRecordCounter.

#### b - Info Functions

The following function enables to get the record counter (of the Recorder analyzer).
- Visual C++ declarations:
int GARC_RecordCounter(int nSocket, int& nCount);
- Visual Basic declaration:
GARC_RecordCounter(ByVal nSocket As Long, _
ByRef nCount As Integer) As Long

<!-- page 140 -->

### 76 - NVD_CmdGetAnalyzer_TimeToStabilization


#### a - Command function

NVD_CmdGetAnalyzer_TimeToStabilization
This function runs the "GetAnalyzerState" NVDrive command, with the "Time to
stabilization" parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_TimeToStabilization(int nSocket);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_TimeToStabilization(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GATTS_" to remind
GetAnalyzerTimeToStabilization.

#### b - Info Functions

The following function enables to get the Time to stabilization (of the Octave analyzer).
- Visual C++ declarations:
int GATTS_GetTimeToStabilization(int nSocket, float& fCount);
- Visual Basic declaration:
GATTS_GetTimeToStabilization(ByVal nSocket As Long, _
ByRef fCount As Single) As Long

<!-- page 141 -->

### 77 - NVD_CmdGetAnalyzer_PerCentBlockLost


#### a - Command function

NVD_CmdGetAnalyzer_PerCentBlockLost
This function runs the "GetAnalyzerState" NVDrive command, with the "% Block lost"
parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_PerCentBlockLost(int nSocket);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_PerCentBlockLost(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GAPBL_" to remind
GetAnalyzerPerCentBlockLost.

#### b - Info Functions

The following function enables to get the percent block lost (of the Waterfall analyzer).
- Visual C++ declarations:
int GAPBL_GetPerCentLost(int nSocket, float& fCount);
- Visual Basic declaration:
GAPBL_GetPerCentLost(ByVal nSocket As Long, _
ByRef fCount As Single) As Long

<!-- page 142 -->

### 78 - NVD_CmdGetAnalyzer_PerCentBlockTransfered


#### a - Command function

NVD_CmdGetAnalyzer_PerCentBlockTransfered
This function runs the "GetAnalyzerState" NVDrive command, with the "% Block
transfered" parameter.
- Visual C++ declaration:
int NVD_CmdGetAnalyzer_PerCentBlockTransfered (int nSocket);
- Visual Basic declaration:
NVD_CmdGetAnalyzer_PerCentBlockTransfered(ByVal nSocket As Long) As
Long
The info functions associated to this command function begin with "GAPBT_" to remind
GetAnalyzerPerCentBlockTransfered.

#### b - Info Functions

The following function enables to get the percent block transfered (of the Waterfall
analyzer).
- Visual C++ declarations:
int GAPBT_GetPerCentTransfered(int nSocket, float& fCount);
- Visual Basic declaration:
GAPBT_GetPerCentTransfered(ByVal nSocket As Long, _
ByRef fCount As Single) As Long

<!-- page 143 -->

### 79 - NVD_CmdGetEvent


#### a - Command function

NVD_CmdGetEvent
This function runs the "GetEvent" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetEvent(int nSocket, char* szEventName);
- Visual Basic declaration:
NVD_CmdGetEvent(ByVal nSocket As Long, _
ByVal szEventName As String) As Long
The info functions associated to this command function begin with "GE_" to remind
GetEvent.

#### b - Info Functions

The following functions enable to get information from the GetEvent command.
- Visual C++ declarations:
int GE_GetEventState(int nSocket, short& nState);
- Visual Basic declaration:
GE_GetEventState(ByVal nSocket As Long, _
ByRef nState As Integer) As Long

<!-- page 144 -->

### 80 - NVD_CmdGetStatus


#### a - Command function

NVD_CmdGetStatus
This function runs the "GetStatus" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetStatus(int nSocket);
- Visual Basic declaration:
NVD_CmdGetStatus(ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GS_" to remind
GetStatus.

#### b - Info Functions

The following functions enable to get information from the GetStatus command.
- Visual C++ declarations:
int GS_GetMeasurementStatus(int nSocket, short& nState);
int GS_GetAnalyzerStatus(int nSocket, short& nState);
- Visual Basic declaration:
GS_GetMeasurementStatus(ByVal nSocket As Long, _
ByRef nState As Integer) As Long
GS_GetAnalyzerStatus(ByVal nSocket As Long, _
ByRef nState As Integer) As Long

<!-- page 145 -->

### 81 - NVD_CmdGetSignalProperties


#### a - Command function

NVD_CmdGetSignalProperties
This function runs the "GetSignalProperties" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetSignalProperties (int nSocket,
char* szProject, char* szMeasure);
- Visual Basic declaration:
NVD_ CmdGetSignalProperties (ByVal nSocket As Long, _
ByVal szProject As String, ByVal szMeasure As String) As Long
The info functions associated to this command function begin with "GSP_" to remind
GetSignalProperties.

#### b - Info Functions

The following functions enable to get information from the GetSignalProperties
command.
- Visual C++ declarations:
int GSP_GetCreationTime (int nSocket, char* szCreationTime, int nBufferSize);
int GSP_GetEditType (int nSocket, char* szEditType, int nBufferSize);
int GSP_GetFrequency1 (int nSocket, char* szFrequency1, int nBufferSize);
int GSP_GetFrequency2 (int nSocket, char* szFrequency2, int nBufferSize);
int GSP_GetFrequency3 (int nSocket, char* szFrequency3, int nBufferSize);
int GSP_GetszOnAnalyzer (int nSocket, char* szOnAnalyzer, int nBufferSize);
int GSP_GetszOnComputer (int nSocket, char* szOnComputer, int nBufferSize);
int GSP_GetSizeInBytes (int nSocket, char* szSizeInBytes, int nBufferSize);
int GSP_GetSizeInSecond (int nSocket, char* szSizeInSecond, int nBufferSize);
int GSP_GetSizeInTime (int nSocket, char* szSizeInTime, int nBufferSize);
int GSP_GetNbTrack (int nSocket, char* szNbTrack, int nBufferSize);
int GSP_GetFormat (int nSocket, char* szFormat, int nBufferSize);
int GSP_GetFreq1ValueInSampPerSec (int nSocket, float& fFrequency);
int GSP_GetFreq2ValueInSampPerSec (int nSocket, float& fFrequency);
int GSP_GetFreq3ValueInSampPerSec (int nSocket, float& fFrequency);
int GSP_GetSizeValueInBytes (int nSocket, float& fSize);
- Visual Basic declaration:

<!-- page 146 -->
GSP_GetCreationTime (ByVal nSocket As Long, _
ByVal szCreationTime As String, ByVal nBufferSize As Long) As Long
GSP_GetEditType (ByVal nSocket As Long, _
ByVal szEditType As String, ByVal nBufferSize As Long) As Long
GSP_GetFrequency1 (ByVal nSocket As Long, _
ByVal szFrequency1 As String, ByVal nBufferSize As Long) As Long
GSP_GetFrequency2 (ByVal nSocket As Long, _
ByVal szFrequency2 As String, ByVal nBufferSize As Long) As Long
GSP_GetFrequency3 (ByVal nSocket As Long, _
ByVal szFrequency3 As String, ByVal nBufferSize As Long) As Long
GSP_GetszOnAnalyzer (ByVal nSocket As Long, _
ByVal szOnAnalyzer As String, ByVal nBufferSize As Long) As Long
GSP_GetszOnComputer (ByVal nSocket As Long, _
ByVal szOnComputer As String, ByVal nBufferSize As Long) As Long
GSP_GetSizeInBytes (ByVal nSocket As Long, _
ByVal szSizeInBytes As String, ByVal nBufferSize As Long) As Long
GSP_GetSizeInSecond (ByVal nSocket As Long, _
ByVal szSizeInSecond As String, ByVal nBufferSize As Long) As Long
GSP_GetSizeInTime (ByVal nSocket As Long, _
ByVal GSP_GetSizeInTime As String, _
ByVal nBufferSize As Long) As Long
GSP_GetNbTrack (ByVal nSocket As Long, _
ByVal szNbTrack As String, ByVal nBufferSize As Long) As Long
GSP_GetFormat (ByVal nSocket As Long, _
ByVal szFormat As String, ByVal nBufferSize As Long) As Long
GSP_GetFreq1ValueInSampPerSec (ByVal nSocket As Long, _
ByRef fFrequency As Single) As Long
GSP_GetFreq2ValueInSampPerSec (ByVal nSocket As Long, _
ByRef fFrequency As Single) As Long
GSP_GetFreq3ValueInSampPerSec (ByVal nSocket As Long, _
ByRef fFrequency As Single) As Long
GSP_GetSizeValueInBytes (ByVal nSocket As Long, _
ByRef fSize As Single) As Long

<!-- page 147 -->

### 82 - NVD_CmdGetRecordDate


#### a - Command function

NVD_CmdGetRecordDate
This function runs the "GetRecordDate" NVDrive command.
- Visual C++ declaration:
int NVD_GetRecordDate (int nSocket, unsigned short nRecNumber);
- Visual Basic declaration:
NVD_GetRecordDate (ByVal nSocket As Long, _
ByVal nRecNum As Integer) As Long
The info functions associated to this command function begin with "GRD_" to remind
GetRecordDate.

#### b - Info Functions

The following functions enable to get information from the CmdGetRecordDate
command. The functions are ordered as information is stored in the block (see NVDrive
reference manual).
- Visual C++ declarations:
int GRD_GetRecordYear(int nSocket, int& nYear);
int GRD_GetRecordMonth(int nSocket, int& nMonth);
int GRD_GetRecordDay(int nSocket, int& nDay);
int GRD_GetRecordHour(int nSocket, int& nHour);
int GRD_GetRecordMinute(int nSocket, int& nMinute);
int GRD_GetRecordSecond(int nSocket, int& nSecond);
int GRD_GetRecordMillisecond(int nSocket, int& nMillis);
- Visual Basic declaration:
GRD_GetRecordMonth (ByVal nSocket As Long, _
ByRef nYear As Long) As Long
GRD_GetRecordYear (ByVal nSocket As Long, _
ByRef nMonth As Long) As Long
GRD_GetRecordDay (ByVal nSocket As Long, _
ByRef nDay As Long) As Long
GRD_GetRecordHour (ByVal nSocket As Long, _
ByRef nHour As Long) As Long

<!-- page 148 -->
GRD_GetRecordMinute (ByVal nSocket As Long, _
ByRef nMinute As Long) As Long
GRD_GetRecordSecond (ByVal nSocket As Long, _
ByRef nSecond As Long) As Long
GRD_GetRecordMillisecond (ByVal nSocket As Long, _
ByRef nMillis As Long) As Long

<!-- page 149 -->

### 83 - NVD_CmdGetProjectProperties


#### a - Command function

NVD_CmdGetProjectProperties
This function runs the "GetProjectProperties" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetProjectProperties (int nSocket,
char* szProject);
- Visual Basic declaration:
NVD_ CmdGetProjectProperties (ByVal nSocket As Long, _
ByVal szProject As String) As Long
The info functions associated to this command function begin with "GPP_" to remind
GetProjectProperties.

#### b - Info Functions

The following functions enable to get information from the GetProjectProperties
command.
- Visual C++ declarations:
int GPP_GetCreatorName(int nSocket, char* szName ,int nBufferSize);
int GPP_GetCreatorFirstName(int nSocket, char* szName, int nBufferSize);
int GPP_GetKeyWord(int nSocket, char* szKey, int nBufferSize);
int GPP_GetComment (int nSocket, char* szComment, int nBufferSize);
int GPP_GetExtUserReadOnly(int nSocket, short& nState);
int GPP_GetReadOnly(int nSocket, short& nState);
int GPP_GetCreationYear (int nSocket, int& nYear);
int GPP_GetCreationMonth (int nSocket, int& nMonth);
int GPP_GetCreationDay (int nSocket, int& nDay);
int GPP_GetLastModifYear (int nSocket, int& nYear);
int GPP_GetLastModifMonth (int nSocket, int& nMonth);
int GPP_GetLastModifDay (int nSocket, int& nDay);
- Visual Basic declaration:
GPP_GetCreatorName(ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GPP_GetCreatorFirstName (ByVal nSocket As Long, _

<!-- page 150 -->
ByVal szName As String, ByVal nBufferSize As Long) As Long
GPP_GetKeyWord (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GPP_GetComment (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long) As Long
GPP_GetExtUserReadOnly(ByVal nSocket As Long, _
ByRef nState As Integer) As Long
GPP_GetReadOnly(ByVal nSocket As Long, _
ByRef nState As Integer) As Long
GPP_GetCreationYear(ByVal nSocket As Long, _
ByRef nYear As Integer) As Long
GPP_GetCreationMonth(ByVal nSocket As Long, _
ByRef nMonth As Integer) As Long
GPP_GetCreationDay(ByVal nSocket As Long, _
ByRef nDay As Integer) As Long
GPP_GetLastModifYear(ByVal nSocket As Long, _
ByRef nYear As Integer) As Long
GPP_GetLastModifMonth(ByVal nSocket As Long, _
ByRef nMonth As Integer) As Long
GPP_GetLastModifDay(ByVal nSocket As Long, _
ByRef nDay As Integer) As Long

<!-- page 151 -->

### 84 - NVD_CmdGetProjectUserPropertiesList


#### a - Command function

NVD_CmdGetProjectUserPropertiesList
This function runs the "GetProjectUserPropertiesList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetProjectUserPropertiesList (int nSocket,
char* szProject);
- Visual Basic declaration:
NVD_ CmdGetProjectUserPropertiesList (ByVal nSocket As Long, _
ByVal szProject As String) As Long
The info functions associated to this command function begin with "GPUPL_" to remind
GetProjectUserPropertiesList.

#### b - Info Functions

The following functions enable to get information from the GetProjectUserPropertiesList
command.
- Visual C++ declarations:
int GPUPL_GetPropertiesCount (int nSocket, short& nCount);
int GPUPL_GetPropertyId (int nSocket, char* szId, int nBufferSize);
int GPUPL_GetPropertyTitle (int nSocket, char* szTitle, int nBufferSize);
int GPUPL_GetPropertyType (int nSocket, char* szType, int nBufferSize);
int GPUPL_GetPropertyValue (int nSocket, char* szValue, int nBufferSize);
- Visual Basic declaration:
GPUPL_GetPropertiesCount (ByVal nSocket As Long, _
ByRef nCount As Integer) As Long
GPP_ GPUPL_GetPropertyId (ByVal nSocket As Long, _
ByVal szId As String, ByVal nBufferSize As Long) As Long
GPP_ GPUPL_GetPropertyTitle (ByVal nSocket As Long, _
ByVal szTitle As String, ByVal nBufferSize As Long) As Long
GPP_ GPUPL_GetPropertyType (ByVal nSocket As Long, _
ByVal szType As String, ByVal nBufferSize As Long) As Long
GPP_ GPUPL_ GetPropertyValue (ByVal nSocket As Long, _
ByVal szValue As String, ByVal nBufferSize As Long) As Long

<!-- page 152 -->

### 85 - NVD_CmdGetMeasurementUserPropertiesList


#### a - Command function

NVD_CmdGetMeasurementUserPropertiesList
This function runs the "GetMeasurementUserPropertiesList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetMeasurementUserPropertiesList (int nSocket,
char* szProject);
- Visual Basic declaration:
NVD_ CmdGetMeasurementUserPropertiesList (ByVal nSocket As Long, _
ByVal szProject As String) As Long
The info functions associated to this command function begin with "GMUPL_" to
remind GetMeasurementUserPropertiesList.

#### b - Info Functions

The following functions enable to get information from the GetProjectUserPropertiesList
command.
- Visual C++ declarations:
int GMUPL_GetPropertiesCount (int nSocket, short& nCount);
int GMUPL_GetPropertyId (int nSocket, char* szId, int nBufferSize);
int GMUPL_GetPropertyTitle (int nSocket, char* szTitle, int nBufferSize);
int GMUPL_GetPropertyType (int nSocket, char* szType, int nBufferSize);
int GMUPL_GetPropertyValue (int nSocket, char* szValue, int nBufferSize);
- Visual Basic declaration:
GMUPL_GetPropertiesCount (ByVal nSocket As Long, _
ByRef nCount As Integer) As Long
GMUPL_GetPropertyId (ByVal nSocket As Long, _
ByVal szId As String, ByVal nBufferSize As Long) As Long
GMUPL_GetPropertyTitle (ByVal nSocket As Long, _
ByVal szTitle As String, ByVal nBufferSize As Long) As Long
GMUPL_GetPropertyType (ByVal nSocket As Long, _
ByVal szType As String, ByVal nBufferSize As Long) As Long
GMUPL_GetPropertyValue (ByVal nSocket As Long, _
ByVal szValue As String, ByVal nBufferSize As Long) As Long

<!-- page 153 -->

### 86 - NVD_CmdGetCurrentNVGatePath


#### a - Command function

NVD_CmdGetCurrentNVGatePath
This function runs the "GetCurrentNVGatePath" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentNVGatePath(int nSocket);
- Visual Basic declaration:
NVD_CmdGetCurrentNVGatePath(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GCNVP_" to
remind GetCurrentNVGatePath.

#### b - Info Functions

The following functions enable to get information from the GetCurrentNVGatePath
command.
- Visual C++ declarations:
int GCNVP_GetPath(int nSocket, char* szPath, int nBufferSize);
- Visual Basic declaration:
GCNVP_GetPath(ByVal nSocket As Long, _
ByVal szPath As String, _
ByVal nBufferSize As Long) As Long

<!-- page 154 -->

### 87 - NVD_CmdGetDatabasePath


#### a - Command function

NVD_CmdGetDatabasePath
This function runs the "GetDatabasePath" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetDatabasePath(int nSocket);
- Visual Basic declaration:
NVD_CmdGetDatabasePath(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GDP_" to remind
GetDatabasePath.

#### b - Info Functions

The following functions enable to get information from the GetDatabasePath command.
- Visual C++ declarations:
int GDP_GetPath(int nSocket, char* szPath, int nBufferSize);
- Visual Basic declaration:
GDP_GetPath(ByVal nSocket As Long, _
ByVal szPath As String, _
ByVal nBufferSize As Long) As Long

<!-- page 155 -->

### 88 - NVD_CmdGetCurrentProjectName


#### a - Command function

NVD_CmdGetCurrentProjectName
This function runs the "GetCurrentProjectName" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentProjectName(int nSocket);
- Visual Basic declaration:
NVD_CmdGetCurrentProjectName(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GCPN_" to remind
GetCurrentProjectName.

#### b - Info Functions

The following functions enable to get information from the GetCurrentProjectName
command.
- Visual C++ declarations:
int GCPN_GetProjectName (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GCPN_GetProjectName (ByVal nSocket As Long, _
ByVal szName As String, _
ByVal nBufferSize As Long) As Long

<!-- page 156 -->

### 89 - NVD_CmdGetCurrentUserName


#### a - Command function

NVD_CmdGetCurrentUserName
This function runs the "GetCurrentUserName" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetCurrentUserName(int nSocket);
- Visual Basic declaration:
NVD_CmdGetCurrentUserName(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GCUN_" to remind
GetCurrentUserName.

#### b - Info Functions

The following functions enable to get information from the GetCurrentUserName
command.
- Visual C++ declarations:
int GCUN_GetUserName (int nSocket, char* szName, int nBufferSize);
- Visual Basic declaration:
GCUN_GetUserName (ByVal nSocket As Long, _
ByVal szName As String) As Long

<!-- page 157 -->

### 90 - NVD_CmdGetUserList


#### a - Command function

NVD_CmdGetUserList
This function runs the "GetUserList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetUserList(int nSocket);
- Visual Basic declaration:
NVD_CmdGetUserList (ByVal nSocket As Long) As Long
The info functions associated to this command function begin with "GUSL_" to remind
GetUserList.

#### b - Info Functions

The following functions enable to get information from the CmdGetUserList command.
The first function enables to get the number of elements in the list. The second function
enables to get 1 element in the list.
- Visual C++ declarations:
int GUSL_GetSize(int nSocket, int& nNbElt);
int GUSL_GetLastNameInList(int nSocket, char* szUnit, int nBufferSize,
int nIndex);
int GUSL_GetFirstNameInList(int nSocket, char* szUnit, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GUSL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GUSL_GetLastNameInList (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long
GUSL_GetFirstNameInList (ByVal nSocket As Long, _
ByVal szName As String, ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 158 -->

### 91 - NVD_CmdGetMacroList


#### a - Command function

NVD_CmdGetMacroList
This function runs the "GetMacroList" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetMacroList(int nSocket);
- Visual Basic declaration:
NVD_CmdGetMacroList(ByVal nSocket As Long) As Long
The info function associated to this command function begins with "GMCL_" to remind
GetMacroList.

#### b - Info Functions

The following functions enable to get information from the GetMacroList command. The
first function enables to get the number of elements in the list. The second function
enables to get 1 element in the list.
- Visual C++ declarations:
int GMCL_GetSize (int nSocket, int& nNbElt);
int GMCL_GetMacroInList (int nSocket, char* szMacro, int nBufferSize,
int nIndex);
- Visual Basic declaration:
GMCL_GetSize (ByVal nSocket As Long, _
ByRef nNbElt As Integer) As Long
GMCL_GetMacroInList (ByVal nSocket As Long, _
ByVal szMacro As String, ByVal nBufferSize As Long, _
ByVal nIndex As Integer) As Long

<!-- page 159 -->

### 92 - NVD_CmdGetPermission


#### a - Command function

NVD_CmdGetPermission
This function runs the "GetPermission" NVDrive command.
- Visual C++ declaration:
int NVD_CmdGetPermission(int nSocket, char* szApplicationName) ;
- Visual Basic declaration:
NVD_CmdGetPermission(ByVal nSocket As Long, _
ByVal szApplicationName As String) As Long
The info function associated to this command function begins with "GP_" to remind
GetPermission.

#### b - Info Functions

The following function enables to get information from the GetPermission command.
- Visual C++ declarations:
int GP_IsAllowed(int nSocket, short& nAllowed);
- Visual Basic declaration:
GP_IsAllowed(ByVal nSocket As Long, _
ByRef nAllowed As Integer) As Long
