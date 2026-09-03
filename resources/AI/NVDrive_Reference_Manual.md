# NVDrive Reference Manual - Markdown mirror

> The TCP/IP command language for NVGate and OROS 3-series analyzers.
>
> Generated 2026-08-24 by `app/manual_to_markdown.py` from
> `NVDrive_Reference_Manual.pdf` (386 pages), NVGate version 17.00.002.
>
> This file is an **automatic conversion** of the official manual, meant to be
> read by an AI tool or searched as text. Where the two disagree, the official
> PDF prevails. The `<!-- page N -->` markers let you locate any passage back
> in the PDF.

| Measure | Value |
|---|---|
| Pages converted | 386 |
| Headings rebuilt | 384 |
| Tables rendered | 401 |
| Original table-of-contents lines discarded | 381 |

## Contents

  - [3.9 - TCP Client to Scan State, Setting, User Interface Notification, Command And Result](#39---tcp-client-to-scan-state-setting-user-interface-notification-command-and-result)
- [1 - OVERVIEW](#1---overview)
  - [1.1 - APPLICATIONS TYPE](#11---applications-type)
    - [1.1.1 - External tool](#111---external-tool)
    - [1.1.2 - Applicative sequence](#112---applicative-sequence)
    - [1.1.3 - Data collector](#113---data-collector)
  - [1.2 - REAL-TIME AND OFFICE POST-ANALYSIS](#12---real-time-and-office-post-analysis)
  - [1.3 - NETWORK CONTROL](#13---network-control)
  - [1.4 - VERSION COMPATIBILITY](#14---version-compatibility)
  - [1.5 - CUSTOMIZATION](#15---customization)
    - [1.5.1 - User profiles](#151---user-profiles)
    - [1.5.2 - Project based application](#152---project-based-application)
- [2 - DESCRIPTION OF SERVICES AND FUNCTIONS](#2---description-of-services-and-functions)
  - [2.1 - PRECAUTIONS](#21---precautions)
  - [2.2 - CONNECTION](#22---connection)
  - [2.3 - EXCHANGE FORMAT](#23---exchange-format)
    - [2.3.1 - Client → Server](#231---client--server)
    - [2.3.2 - Server → Client](#232---server--client)
  - [2.4 - PART LIST OF INTERPRETATION / SYNTAX ERRORS](#24---part-list-of-interpretation--syntax-errors)
    - [2.4.1 - "GetErrorMessage" command](#241---geterrormessage-command)
- [3 - COMMANDS](#3---commands)
  - [3.1 - ACTIONS](#31---actions)
    - [3.1.1 - "ExecMacro" command](#311---execmacro-command)
    - [3.1.2 - "Run" command](#312---run-command)
    - [3.1.3 - "Stop" command](#313---stop-command)
    - [3.1.4 - "Pause" command](#314---pause-command)
    - [3.1.5 - "PlayByStep " command](#315---playbystep--command)
    - [3.1.6 - "Accept" command](#316---accept-command)
    - [3.1.7 - "Reject" command](#317---reject-command)
    - [3.1.8 - "ManualTrigger" command](#318---manualtrigger-command)
    - [3.1.9 - "ShutDown" command](#319---shutdown-command)
    - [3.1.10 - "StandAlone" command](#3110---standalone-command)
    - [3.1.11 - "AbortStandAlone" command](#3111---abortstandalone-command)
    - [3.1.12 - "Autorange" command](#3112---autorange-command)
    - [3.1.13 - "CheckICP" command](#3113---checkicp-command)
    - [3.1.14 - "CheckTEDS" command](#3114---checkteds-command)
    - [3.1.15 - "Emergency stop" command](#3115---emergency-stop-command)
    - [3.1.16 - "EditCalibration" command](#3116---editcalibration-command)
    - [3.1.17 - "RefreshState" command](#3117---refreshstate-command)
    - [3.1.18 - "FormatDisk" command](#3118---formatdisk-command)
  - [3.2 - MARKER](#32---marker)
    - [3.2.1 - "GetWindowTraces" command](#321---getwindowtraces-command)
    - [3.2.2 - "GetWindowDisplayZone" command](#322---getwindowdisplayzone-command)
    - [3.2.3 - "GetMarkerList" command](#323---getmarkerlist-command)
    - [3.2.4 - "AddFreeMarker" command](#324---addfreemarker-command)
    - [3.2.5 - "AddPeakMarker" command](#325---addpeakmarker-command)
    - [3.2.6 - "AddMaxMarker" command](#326---addmaxmarker-command)
    - [3.2.7 - "AddPowerBandMarker" command](#327---addpowerbandmarker-command)
    - [3.2.8 - "AddSideBandMarker" command](#328---addsidebandmarker-command)
    - [3.2.9 - "AddHarmonicMarker" command](#329---addharmonicmarker-command)
    - [3.2.10 - "AddRecordMarker" command](#3210---addrecordmarker-command)
    - [3.2.11 - "AddPeriodMarker" command](#3211---addperiodmarker-command)
    - [3.2.12 - "AddKinematicMarker" command](#3212---addkinematicmarker-command)
    - [3.2.13 - "AddNOctaveMarker" command](#3213---addnoctavemarker-command)
    - [3.2.14 - "GetNumberOfRecordMarker" command](#3214---getnumberofrecordmarker-command)
    - [3.2.15 - "SetRecordMarkerLabel" command](#3215---setrecordmarkerlabel-command)
    - [3.2.16 - "RemoveMarker" command](#3216---removemarker-command)
    - [3.2.17 - "DisplayMarkerProperties" command](#3217---displaymarkerproperties-command)
    - [3.2.18 - "DuplicateMarkerInMultigraphWindow" command](#3218---duplicatemarkerinmultigraphwindow-command)
    - [3.2.19 - "SetFreeMarkerParameters" command](#3219---setfreemarkerparameters-command)
    - [3.2.20 - "GetFreeMarkerParameters" command](#3220---getfreemarkerparameters-command)
    - [3.2.21 - "SetPeakMarkerParameters" command](#3221---setpeakmarkerparameters-command)
    - [3.2.22 - "GetPeakMarkerParameters" command](#3222---getpeakmarkerparameters-command)
    - [3.2.23 - "SetMaxMarkerParameters" command](#3223---setmaxmarkerparameters-command)
    - [3.2.24 - "GetMaxMarkerParameters" command](#3224---getmaxmarkerparameters-command)
    - [3.2.25 - "GetRecordMarkerParameters" command](#3225---getrecordmarkerparameters-command)
    - [3.2.26 - "SetPowerBandMarkerParameters" command](#3226---setpowerbandmarkerparameters-command)
    - [3.2.27 - "GetPowerBandMarkerParameters" command](#3227---getpowerbandmarkerparameters-command)
    - [3.2.28 - "SetSideBandMarkerParameters" command](#3228---setsidebandmarkerparameters-command)
    - [3.2.29 - "GetSideBandMarkerParameters" command](#3229---getsidebandmarkerparameters-command)
    - [3.2.30 - "SetHarmonicMarkerParameters" command](#3230---setharmonicmarkerparameters-command)
    - [3.2.31 - "SetHarmonicMarkerVisibility" command](#3231---setharmonicmarkervisibility-command)
    - [3.2.32 - "GetHarmonicMarkerParameters" command](#3232---getharmonicmarkerparameters-command)
    - [3.2.33 - "SetPeriodMarkerParameters" command](#3233---setperiodmarkerparameters-command)
    - [3.2.34 - "SetPeriodMarkerVisibility" command](#3234---setperiodmarkervisibility-command)
    - [3.2.35 - "SetKinematicMarkerParameters" command](#3235---setkinematicmarkerparameters-command)
    - [3.2.36 - "GetPeriodMarkerParameters" command](#3236---getperiodmarkerparameters-command)
    - [3.2.37 - "GetFreeMarkerValue" command](#3237---getfreemarkervalue-command)
    - [3.2.38 - "GetPeakMarkerValue" command](#3238---getpeakmarkervalue-command)
    - [3.2.39 - "GetMaxMarkerValue" command](#3239---getmaxmarkervalue-command)
    - [3.2.40 - "GetPowerBandMarkerValue" command](#3240---getpowerbandmarkervalue-command)
    - [3.2.41 - "GetSideBandMarkerValue" command](#3241---getsidebandmarkervalue-command)
    - [3.2.42 - "GetHarmonicMarkerValue" command](#3242---getharmonicmarkervalue-command)
    - [3.2.43 - "GetPeriodMarkerValue" command](#3243---getperiodmarkervalue-command)
  - [3.3 - GRAPHICS](#33---graphics)
    - [3.3.1 - "AddWindowResult" command](#331---addwindowresult-command)
    - [3.3.2 - "AddWindowPlayerResult" command](#332---addwindowplayerresult-command)
    - [3.3.3 - "AddWindowSavedResult" command](#333---addwindowsavedresult-command)
    - [3.3.4 - "AddWindowWtfResult" command](#334---addwindowwtfresult-command)
    - [3.3.5 - "AddWindowZoomedSignal" command](#335---addwindowzoomedsignal-command)
    - [3.3.6 - "RenameWindow" command](#336---renamewindow-command)
    - [3.3.7 - "SetLayout" command](#337---setlayout-command)
    - [3.3.8 - "NewLayout" command](#338---newlayout-command)
    - [3.3.9 - "RemoveLayout" command](#339---removelayout-command)
    - [3.3.10 - "RenameLayout" command](#3310---renamelayout-command)
    - [3.3.11 - "GetLayoutList" command](#3311---getlayoutlist-command)
    - [3.3.12 - "GetCurrentLayout" command](#3312---getcurrentlayout-command)
    - [3.3.13 - "MaskAllToolbar" command](#3313---maskalltoolbar-command)
    - [3.3.14 - "SetActiveWindow" command](#3314---setactivewindow-command)
    - [3.3.15 - "GetActiveWindow" command](#3315---getactivewindow-command)
    - [3.3.16 - "GetWindowList" command](#3316---getwindowlist-command)
    - [3.3.17 - "GetWindowNameList" command](#3317---getwindownamelist-command)
    - [3.3.18 - "GetWindowTraces" command](#3318---getwindowtraces-command)
    - [3.3.19 - "GetMeasurementWindowTrace" command](#3319---getmeasurementwindowtrace-command)
    - [3.3.20 - "CloseWindow" command](#3320---closewindow-command)
    - [3.3.21 - "CloseAllWindows" command](#3321---closeallwindows-command)
    - [3.3.22 - "Autoscale" command](#3322---autoscale-command)
    - [3.3.23 - "AutoscaleAllWnd" command](#3323---autoscaleallwnd-command)
    - [3.3.24 - "ChangeSpectralWeighting" command](#3324---changespectralweighting-command)
    - [3.3.25 - "ChangeDisplayMode" command](#3325---changedisplaymode-command)
    - [3.3.26 - "GetDisplayMode" command](#3326---getdisplaymode-command)
    - [3.3.24 - ChangeDisplayMode).](#3324---changedisplaymode)
    - [3.3.27 - "GetDisplayModeList" command](#3327---getdisplaymodelist-command)
    - [3.3.28 - "ArrangeWindows" command](#3328---arrangewindows-command)
    - [3.3.29 - "GroupByMagnitude" command](#3329---groupbymagnitude-command)
    - [3.3.30 - "OpenCloseInfoTrace" command](#3330---opencloseinfotrace-command)
    - [3.3.31 - "MemorizeTrace" command](#3331---memorizetrace-command)
    - [3.3.32 - "RemoveTrace" command](#3332---removetrace-command)
    - [3.3.33 - "ClearMemory" command](#3333---clearmemory-command)
    - [3.3.34 - "CascadeView" command](#3334---cascadeview-command)
    - [3.3.35 - "AddResultAutoMemorize" command](#3335---addresultautomemorize-command)
    - [3.3.36 - "RemoveResultAutoMemorize" command](#3336---removeresultautomemorize-command)
    - [3.3.37 - "EnableAutoMemorize" command](#3337---enableautomemorize-command)
    - [3.3.38 - "AddAutoOperator" command](#3338---addautooperator-command)
    - [3.3.39 - "GetReferenceList" command](#3339---getreferencelist-command)
    - [3.3.40 - "SetReference" command](#3340---setreference-command)
    - [3.3.41 - "GetCurrentReference" command](#3341---getcurrentreference-command)
    - [3.3.42 - "SetCursorPosition" command](#3342---setcursorposition-command)
    - [3.3.43 - "GetCursorInfo" command](#3343---getcursorinfo-command)
    - [3.3.44 - "CopyData" command](#3344---copydata-command)
    - [3.3.45 - "CopyDataAllTraces" command](#3345---copydataalltraces-command)
    - [3.3.46 - "CopyBitmap" command](#3346---copybitmap-command)
    - [3.3.47 - "CopyGraph" command](#3347---copygraph-command)
    - [3.3.48 - "SelectWaterfallWindowView" command](#3348---selectwaterfallwindowview-command)
    - [3.3.49 - "GetScaleInfo" command](#3349---getscaleinfo-command)
    - [3.3.50 - "SetScaleType" command](#3350---setscaletype-command)
    - [3.3.51 - "SetScaleValues" command](#3351---setscalevalues-command)
    - [3.3.52 - "SendScaleCommand" command](#3352---sendscalecommand-command)
    - [3.3.53 - "GetAvailableScale" command](#3353---getavailablescale-command)
    - [3.3.54 - "SetScaleTimeType" command](#3354---setscaletimetype-command)
    - [3.3.55 - "IsScaleTimeInRelative" command](#3355---isscaletimeinrelative-command)
    - [3.3.56 - "GetWindowPosition" command](#3356---getwindowposition-command)
    - [3.3.57 - "SetWindowPosition" command](#3357---setwindowposition-command)
    - [3.3.58 - "GetRotationPreferences" command](#3358---getrotationpreferences-command)
    - [3.3.59 - "SetRotationPreferences" command](#3359---setrotationpreferences-command)
    - [3.3.60 - "SetViewmeterLevels" command](#3360---setviewmeterlevels-command)
    - [3.3.61 - "PinWindow " command](#3361---pinwindow--command)
    - [3.3.62 - "GetPinStatus" command](#3362---getpinstatus-command)
    - [3.3.63 - "SetTachometerPosition" command](#3363---settachometerposition-command)
    - [3.3.64 - "GetTachometerPosition" command](#3364---gettachometerposition-command)
    - [3.3.65 - "AddResultTemplateToWindow" command](#3365---addresulttemplatetowindow-command)
    - [3.3.66 - "SetPhasePreference" command](#3366---setphasepreference-command)
    - [3.3.67 - "SetGraduationDirection" command](#3367---setgraduationdirection-command)
    - [3.3.68 - "GetGraduationDirection" command](#3368---getgraduationdirection-command)
    - [3.3.69 - "GetActiveTrace" command](#3369---getactivetrace-command)
    - [3.3.70 - "SetActiveTrace" command](#3370---setactivetrace-command)
    - [3.3.71 - "ChangeWindowPreferences" command](#3371---changewindowpreferences-command)
  - [3.4 - PROJECT MANAGER](#34---project-manager)
    - [3.4.1 - "LoadProject" command](#341---loadproject-command)
    - [3.4.2 - "NewProject" command](#342---newproject-command)
    - [3.4.3 - "OpenProject" command](#343---openproject-command)
    - [3.4.4 - "SaveProject" command](#344---saveproject-command)
    - [3.4.5 - "SaveProjectAs" command](#345---saveprojectas-command)
    - [3.4.6 - "RemoveProject" command](#346---removeproject-command)
    - [3.4.7 - "ImportProject" command](#347---importproject-command)
    - [3.4.8 - "GetProjectList" command](#348---getprojectlist-command)
    - [3.4.9 - "GetCurrentProjectName" command](#349---getcurrentprojectname-command)
    - [3.4.10 - "GetProjectProperties" command](#3410---getprojectproperties-command)
    - [3.4.11 - "GetProjectUserPropertiesList" command](#3411---getprojectuserpropertieslist-command)
    - [3.4.12 - "GetMeasurementUserPropertiesList" command](#3412---getmeasurementuserpropertieslist-command)
    - [3.4.13 - "AddProjectUserProperty" command](#3413---addprojectuserproperty-command)
    - [3.4.14 - "AddMeasurementUserProperty" command](#3414---addmeasurementuserproperty-command)
    - [3.4.15 - "ModifyProjectUserProperty" command](#3415---modifyprojectuserproperty-command)
    - [3.4.16 - "ModifyMeasurementUserProperty" command](#3416---modifymeasurementuserproperty-command)
    - [3.4.17 - "DeleteProjectUserProperty" command](#3417---deleteprojectuserproperty-command)
    - [3.4.18 - "DeleteMeasurementUserProperty" command](#3418---deletemeasurementuserproperty-command)
    - [3.4.19 - "LoadWorkbook" command](#3419---loadworkbook-command)
    - [3.4.20 - "LoadWorkbookModel" command](#3420---loadworkbookmodel-command)
    - [3.4.21 - "SaveWorkbook" command](#3421---saveworkbook-command)
    - [3.4.22 - "SaveWorkbookModel" command](#3422---saveworkbookmodel-command)
    - [3.4.23 - "DeleteModel" command](#3423---deletemodel-command)
    - [3.4.24 - "ReloadCurrentWorkbook" command](#3424---reloadcurrentworkbook-command)
    - [3.4.25 - "ResetWorkbook" command](#3425---resetworkbook-command)
    - [3.4.26 - "LoadMeasurement" command](#3426---loadmeasurement-command)
    - [3.4.27 - "UnloadCurrentMeasurement" command](#3427---unloadcurrentmeasurement-command)
    - [3.4.28 - "RemoveMeasurement" command](#3428---removemeasurement-command)
    - [3.4.29 - "GetMeasureList" command](#3429---getmeasurelist-command)
    - [3.4.30 - "GetItemPMTree" command](#3430---getitempmtree-command)
    - [3.4.31 - "RefreshPM" command](#3431---refreshpm-command)
    - [3.4.32 - "GetDatabasePath" command](#3432---getdatabasepath-command)
    - [3.4.33 - "SwitchBasePath" command](#3433---switchbasepath-command)
    - [3.4.34 - "RemoveSignalFromAnalyzer" command](#3434---removesignalfromanalyzer-command)
  - [3.5 - GENERAL CONFIGURATION](#35---general-configuration)
    - [3.5.1 - "AppliedMode" command](#351---appliedmode-command)
    - [3.5.2 - "AddToControlPanel" command](#352---addtocontrolpanel-command)
    - [3.5.3 - "ResetControlPanel" command](#353---resetcontrolpanel-command)
    - [3.5.4 - "WorkspaceTab" command](#354---workspacetab-command)
    - [3.5.5 - "SetUser" command](#355---setuser-command)
    - [3.5.6 - "SetSilent" command](#356---setsilent-command)
    - [3.5.7 - "AdministratorMode" command](#357---administratormode-command)
    - [3.5.8 - "SetSaveOption" command](#358---setsaveoption-command)
    - [3.5.9 - "SetNewMeasurementParameters" command](#359---setnewmeasurementparameters-command)
    - [3.5.10 - "GetMagnitudeList" command](#3510---getmagnitudelist-command)
    - [3.5.11 - "GetUnitList" command](#3511---getunitlist-command)
    - [3.5.12 - "SetUnit" command](#3512---setunit-command)
    - [3.5.13 - "GetCurrentUnit" command](#3513---getcurrentunit-command)
    - [3.5.14 - "GetUnitInfo" command](#3514---getunitinfo-command)
    - [3.5.15 - "GetMagnitudeInfo" command](#3515---getmagnitudeinfo-command)
    - [3.5.16 - "SetPreferedWtfReference" command](#3516---setpreferedwtfreference-command)
    - [3.10.3 - Unit ID table).](#3103---unit-id-table)
    - [3.5.17 - "GetPreferedWtfReference" command](#3517---getpreferedwtfreference-command)
    - [3.5.18 - "GetPermission" command](#3518---getpermission-command)
    - [3.5.19 - "ChangeMode" command](#3519---changemode-command)
    - [3.5.20 - "GetAnalyzerModes" command](#3520---getanalyzermodes-command)
    - [3.5.21 - "GetUserList" command](#3521---getuserlist-command)
    - [3.5.22 - "GetCurrentUserName" command](#3522---getcurrentusername-command)
    - [3.5.23 - "GetPreferenceGeneral" command](#3523---getpreferencegeneral-command)
    - [3.5.24 - "SetPreferenceGeneral" command](#3524---setpreferencegeneral-command)
    - [3.5.25 - "GetFanInfo" command](#3525---getfaninfo-command)
    - [3.5.26 - "SetFanStatus" command](#3526---setfanstatus-command)
    - [3.5.27 - "SetFanSpeed" command](#3527---setfanspeed-command)
    - [3.5.28 - "GetMacroList" command](#3528---getmacrolist-command)
    - [3.5.29 - "GetCurrentNVGatePath" command](#3529---getcurrentnvgatepath-command)
    - [3.5.30 - "SetBandState" command](#3530---setbandstate-command)
    - [3.5.31 - "LogWarning" command](#3531---logwarning-command)
  - [3.6 - SETTINGS AND STATES CONFIGURATION](#36---settings-and-states-configuration)
    - [3.6.1 - Identification number setting (setting IDN)](#361---identification-number-setting-setting-idn)
    - [3.6.2 - Identification number state (state IDN)](#362---identification-number-state-state-idn)
    - [3.6.3 - Specifying IDNs in NVDrive commands](#363---specifying-idns-in-nvdrive-commands)
    - [3.6.4 - Teamwork IDN](#364---teamwork-idn)
    - [3.6.5 - "GetSettingValues" command](#365---getsettingvalues-command)
    - [3.6.6 - "GetSettingValue" command](#366---getsettingvalue-command)
    - [3.6.7 - "SetSignalFileSettingValue" command](#367---setsignalfilesettingvalue-command)
    - [3.6.8 - "SetSettingValue" command](#368---setsettingvalue-command)
    - [3.6.9 - "GetSettingInfo" command](#369---getsettinginfo-command)
    - [3.6.10 - "GetSubModuleList" command](#3610---getsubmodulelist-command)
    - [3.6.11 - "GetSignalFileSettingValues" command](#3611---getsignalfilesettingvalues-command)
    - [3.6.12 - "SetVirtualTachoSettingValue" command](#3612---setvirtualtachosettingvalue-command)
    - [3.6.13 - "SetForceSettings" command](#3613---setforcesettings-command)
    - [3.6.14 - "SetResponseSettings" command](#3614---setresponsesettings-command)
    - [3.6.15 - "SetDualExponentialSettings" command](#3615---setdualexponentialsettings-command)
    - [3.6.16 - "AddArrayLine" command](#3616---addarrayline-command)
    - [3.6.17 - "ModifyArrayLine" command](#3617---modifyarrayline-command)
    - [3.6.18 - "RemoveArrayLine" command](#3618---removearrayline-command)
    - [3.6.19 - "EditSetting" command](#3619---editsetting-command)
    - [3.6.20 - "SetToDefault" command](#3620---settodefault-command)
    - [3.6.21 - "SetToDefaultCollection" command](#3621---settodefaultcollection-command)
    - [3.6.22 - "GetInputInfo" command](#3622---getinputinfo-command)
    - [3.6.23 - "ConnectInput" command](#3623---connectinput-command)
    - [3.6.24 - "DisconnectInput" command](#3624---disconnectinput-command)
    - [3.6.25 - "SelectWtfChannels" command](#3625---selectwtfchannels-command)
    - [3.6.26 - "UnSelectWtfChannels" command](#3626---unselectwtfchannels-command)
    - [3.6.27 - "GetTEDSContentOnInput" command](#3627---gettedscontentoninput-command)
    - [3.6.28 - "GetTEDSContent" command](#3628---gettedscontent-command)
    - [3.6.29 - "GetTransducerList" command](#3629---gettransducerlist-command)
    - [3.6.30 - "GetTransducerInfo" command](#3630---gettransducerinfo-command)
    - [3.6.31 - "AddCalibration" command](#3631---addcalibration-command)
    - [3.6.32 - "SetTransducerAppliedSensitivity" command](#3632---settransducerappliedsensitivity-command)
    - [3.6.33 - "GetEvent" command](#3633---getevent-command)
    - [3.6.34 - "ResetEvents" command](#3634---resetevents-command)
    - [3.6.35 - "GetStatus" command](#3635---getstatus-command)
    - [3.6.36 - "GetGeneralAnalyzerState" command](#3636---getgeneralanalyzerstate-command)
    - [3.6.37 - "GetAnalyzerState" command](#3637---getanalyzerstate-command)
    - [3.6.38 - "ExportTransducerDB" command](#3638---exporttransducerdb-command)
    - [3.6.39 - "MergeTransducerDB " command](#3639---mergetransducerdb--command)
    - [3.6.40 - "GetStateValue" command](#3640---getstatevalue-command)
    - [3.6.41 - "WizardBegin" command](#3641---wizardbegin-command)
    - [3.6.42 - "WizardEnd" command](#3642---wizardend-command)
    - [3.6.43 - "TransactionBegin" command](#3643---transactionbegin-command)
    - [3.6.44 - "TransactionEnd" command](#3644---transactionend-command)
    - [3.6.45 - "WaitGUI" command](#3645---waitgui-command)
  - [3.7 - SIGNAL AND RESULT MANAGEMENT](#37---signal-and-result-management)
    - [3.7.1 - Results specificity](#371---results-specificity)
    - [3.7.2 - "IsResultWaterfallisable" command](#372---isresultwaterfallisable-command)
    - [3.7.3 - "GetSignalProperties" command](#373---getsignalproperties-command)
    - [3.7.4 - "GetRecordDate" command](#374---getrecorddate-command)
    - [3.7.5 - "ChangeSignalDate" command](#375---changesignaldate-command)
    - [3.7.6 - "Download" command](#376---download-command)
    - [3.7.7 - "Upload" command](#377---upload-command)
    - [3.7.8 - "ImportFile" command](#378---importfile-command)
    - [3.7.9 - "Export" command](#379---export-command)
    - [3.7.10 - "AddResultToSetup" command](#3710---addresulttosetup-command)
    - [3.7.11 - "RemoveSetupResult" command](#3711---removesetupresult-command)
    - [3.7.12 - "ClearSetupList" command](#3712---clearsetuplist-command)
    - [3.7.13 - "SetSetupParameters" command](#3713---setsetupparameters-command)
    - [3.7.14 - "SetAutomaticExportSetup" command](#3714---setautomaticexportsetup-command)
    - [3.7.15 - "SetNoAutomaticExport" command](#3715---setnoautomaticexport-command)
    - [3.7.16 - "AddToResultSelection" command](#3716---addtoresultselection-command)
    - [3.7.17 - "RemoveToResultSelection" command](#3717---removetoresultselection-command)
    - [3.7.18 - "SaveResults" command](#3718---saveresults-command)
    - [3.7.19 - "GetResultList" command](#3719---getresultlist-command)
    - [3.7.20 - "GetWTFResultList" command](#3720---getwtfresultlist-command)
    - [3.7.21 - "GetResultCaption" command](#3721---getresultcaption-command)
    - [3.7.22 - "GetSavedResultList" command](#3722---getsavedresultlist-command)
    - [3.7.23 - "GetSavedResultCaption" command](#3723---getsavedresultcaption-command)
    - [3.7.24 - "CreateResultEx" command](#3724---createresultex-command)
    - [3.7.25 - "GetResultEx" command](#3725---getresultex-command)
    - [3.7.26 - "GetSavedResultEx" command](#3726---getsavedresultex-command)
    - [3.7.27 - "DeleteResultEx" command](#3727---deleteresultex-command)
    - [3.7.28 - "DeleteAllResultEx" command](#3728---deleteallresultex-command)
    - [3.7.29 - "GetResult" command](#3729---getresult-command)
    - [3.7.30 - "GetWTFResult" command](#3730---getwtfresult-command)
    - [3.7.31 - "GetSavedResult" command](#3731---getsavedresult-command)
    - [3.7.32 - "CreateTCPResultChannel" command](#3732---createtcpresultchannel-command)
    - [3.7.33 - "RemoveTCPResultChannel" command](#3733---removetcpresultchannel-command)
    - [3.7.34 - "NewDataForTCPResultChannel" command](#3734---newdatafortcpresultchannel-command)
    - [3.7.35 - "AddDataToTCPResultChannel" command](#3735---adddatatotcpresultchannel-command)
    - [3.7.36 - "SetTCPResultChannel" command](#3736---settcpresultchannel-command)
    - [3.7.37 - "GetTCPResultChannelList" command](#3737---gettcpresultchannellist-command)
    - [3.7.38 - "GetTCPResult" command](#3738---gettcpresult-command)
    - [3.7.39 - "ChangeTCPResultName" command](#3739---changetcpresultname-command)
    - [3.7.40 - "CreateResultRecordSignal" command](#3740---createresultrecordsignal-command)
    - [3.7.41 - "DeleteResultRecordSignal" command](#3741---deleteresultrecordsignal-command)
    - [3.7.42 - "DeleteAllResultRecordSignal" command](#3742---deleteallresultrecordsignal-command)
    - [3.7.43 - "GetResultRecordSignalBlock" command](#3743---getresultrecordsignalblock-command)
    - [3.7.44 - "GetResultRecordSignalZoom" command](#3744---getresultrecordsignalzoom-command)
  - [3.8 - REPORTS](#38---reports)
    - [3.8.1 - "PrintReport" command](#381---printreport-command)
    - [3.8.1 - "ReportRefreshPrint" command](#381---reportrefreshprint-command)
    - [3.8.2 - "ReportGetInteractiveDocumentList" command](#382---reportgetinteractivedocumentlist-command)
    - [3.8.3 - "ReportSelectInteractiveDocument" command](#383---reportselectinteractivedocument-command)
  - [3.9 - TCP CLIENT TO SCAN STATE, SETTING, USER INTERFACE](#39---tcp-client-to-scan-state-setting-user-interface)
    - [3.9.1 - "ConnectToTCPClient" command](#391---connecttotcpclient-command)
    - [3.9.2 - "DisconnectFromTCPClient" command](#392---disconnectfromtcpclient-command)
    - [3.9.3 - "RegisterState" command](#393---registerstate-command)
    - [3.9.4 - "UnregisterState" command](#394---unregisterstate-command)
    - [3.9.5 - "RegisterSetting" command](#395---registersetting-command)
    - [3.9.6 - "UnregisterSetting" command](#396---unregistersetting-command)
    - [3.9.7 - "RegisterUINotification" command](#397---registeruinotification-command)
    - [3.9.8 - "ExecUINotification" command](#398---execuinotification-command)
    - [3.9.9 - "UnregisterUINotification" command](#399---unregisteruinotification-command)
    - [3.9.10 - "RegisterCommand" command](#3910---registercommand-command)
    - [3.9.11 - "UnregisterCommand" command](#3911---unregistercommand-command)
    - [3.9.12 - "RegisterNewResult" command](#3912---registernewresult-command)
    - [3.9.13 - "UnblockNewResult" command](#3913---unblocknewresult-command)
    - [3.9.14 - "UnregisterNewResult" command](#3914---unregisternewresult-command)
    - [3.9.15 - "RegisterNewMeasurement" command](#3915---registernewmeasurement-command)
    - [3.9.16 - "UnregisterNewMeasurement" command](#3916---unregisternewmeasurement-command)
  - [3.10 - RESULT FORMAT AND DESCRIPTION](#310---result-format-and-description)
    - [3.10.1 - Module ID table](#3101---module-id-table)
    - [3.10.2 - Time operator ID table](#3102---time-operator-id-table)
    - [3.10.3 - Unit ID table](#3103---unit-id-table)
    - [3.10.4 - Weighting operator ID table](#3104---weighting-operator-id-table)
    - [3.10.5 - Process ID table](#3105---process-id-table)
    - [3.10.6 - Corresponding table Process Id <=> NVD process Id](#3106---corresponding-table-process-id--nvd-process-id)
    - [3.10.7 - Result format](#3107---result-format)
    - [3.10.8 - Generic Header](#3108---generic-header)
    - [3.10.9 - HEAD block](#3109---head-block)
    - [3.10.10 - XREG block](#31010---xreg-block)
    - [3.10.11 - XREF block](#31011---xref-block)
    - [3.10.12 - CVEC block](#31012---cvec-block)
    - [3.10.13 - RVEC block](#31013---rvec-block)
    - [3.10.14 - SCAL block](#31014---scal-block)
    - [3.10.15 - DWTF block](#31015---dwtf-block)
    - [3.10.16 - RWTF block](#31016---rwtf-block)
    - [3.10.17 - CWTF block](#31017---cwtf-block)
    - [3.10.18 - INFO block](#31018---info-block)
    - [3.10.19 - RNFO block](#31019---rnfo-block)
  - [3.11 - RECORDER SETUP (OPTION)](#311---recorder-setup-option)
    - [3.11.1 - "AddCurrentSetup" command](#3111---addcurrentsetup-command)
    - [3.11.2 - "RemoveRecorderSetup" command](#3112---removerecordersetup-command)
    - [3.11.3 - "GetRecorderSetupList" command](#3113---getrecordersetuplist-command)
    - [3.11.4 - "GetDefaultRecorderSetup" command](#3114---getdefaultrecordersetup-command)
    - [3.11.5 - "SetDefaultRecorderSetup" command](#3115---setdefaultrecordersetup-command)
    - [3.11.6 - "ExportRecorderConfigAsText" command](#3116---exportrecorderconfigastext-command)
    - [3.11.7 - "ImportRecorderConfigInASB" command](#3117---importrecorderconfiginasb-command)
  - [3.12 - EV/HV (OPTION)](#312---evhv-option)
    - [3.12.1 - "GetEvhvCurrentSpatiogramMeasurement"](#3121---getevhvcurrentspatiogrammeasurement)
- [4 - APPENDIXES](#4---appendixes)
  - [4.1 - LAUNCHING NVGATE® FROM COMMAND LINE](#41---launching-nvgate-from-command-line)
    - [4.1.1 - Connected / office mode](#411---connected--office-mode)
    - [4.1.2 - User profiles set](#412---user-profiles-set)
    - [4.1.3 - User selection](#413---user-selection)
    - [4.1.4 - Client application name](#414---client-application-name)
    - [4.1.5 - Splash screen](#415---splash-screen)
    - [4.1.6 - MessageBox](#416---messagebox)
    - [4.1.7 - Start and Go Dialog](#417---start-and-go-dialog)
    - [4.1.8 - Project base](#418---project-base)
    - [4.1.9 - Analyzer IP address](#419---analyzer-ip-address)
    - [4.1.10 - NVDrive® Disabled](#4110---nvdrive-disabled)
    - [4.1.11 - NVDrive® Port](#4111---nvdrive-port)
    - [4.1.12 - Default project](#4112---default-project)
    - [4.1.13 - Band](#4113---band)
- [5 - COMMANDS INDEX](#5---commands-index)


<!-- page 1 -->
NVDRIVE®
R
EFERENCE MANUAL
TCP/IP BASED COMMAND LANGUAGE FOR
NVGATE®/OROS 3-SERIES ANALYZERS
SOFTWARE PLATFORM

| Compatibility | Identification | Updated |
|---|---|---|
| NVGate® V17.00 | F174-302-29 | February 2024 |


<!-- page 3 -->
CONTENTS

<!-- page 8 -->

### 3.9 - TCP Client to Scan State, Setting, User Interface Notification, Command And Result

Events 335

<!-- page 10 -->

## 1 - OVERVIEW

NVDrive® is a tool to communicate with the OROS 3 Series analyzers. It consists in a set of
commands that offers a simple and direct way to control the analyzer interface via a TCP/IP
link.
This toolkit offers multiple operating modes and benefits. It provides a fast and reliable way
to develop dedicated applications that save development time and gain measurements
productivity.

### 1.1 - APPLICATIONS TYPE

NVDrive® allows building different type of complementary applications, from the
complete application, which use the analyzer as a data provider, to the small calculation
tool.
Depending on the application type there is different way to use NVDrive® developing it,
the following paragraph describe the most adapted use of NVDrive® for each type of
application.

#### 1.1.1 - External tool

This kind of application is to enhance NVGate® with additional functions which are
not present in our analyzer. Usually, these external tools provide only one function
such as a special calculation, or export current data in a special arrangement.
You can develop many of these small tools to be called directly and sequentially from
NVGate®. Note that NVGate® support only one application at a time connected to
listening port.
In order to call these tools from NVGate®, just put your application (or the
corresponding Windows shortcut) in the directory called Links located in the NVGate
installation directory (the one containing NVGate.exe). Then you will be able to call
your application directly from the link toolbar (see fig. 1).
Select your Launch your
External tool External tool
Fig. 1 - NVGate® link tool bar
Examples of external tools experienced by OROS users are:
- Damping calculation based on peak marker
- Absolute date/time cursor in raw signal files
- Append export of multiple resonances FRF in one spreadsheet

<!-- page 11 -->

#### 1.1.2 - Applicative sequence

This type of applications uses the analyzer as a data provider. The collected data are:
- Real-time acquisition (on the flight, or even at end of acquisition)
- Time-signal (triggered, or on the flow)
- Computed results (spectra, order, overall, filtered, etc.)
For this ppurpose, the main job of the NVDrive® application is to sequence the user
operation (a kind of guideline) directly by driving the OROS analyzer settings, then to
collect the results of each acquisition, and at least to process the dedicated treatment
on it.
Note that for all NVDrive® operation NVGate® software must run.
In order to gain development time, you can use the analyzer software for your real-
time displays as you can control windows, markers, auto-scale, etc.
Examples of this type of application are:
- Real-time Sound power measurement based on multi-channel overall
acquisitions.
- Real-time Sound intensity measurement based on 2 parallel FFT analysis.
- Impact hammer acquisition wizard + modal analysis.

#### 1.1.3 - Data collector

For this type of application, the goal is to collect data acquired by one or multiple
OROS analyzer connected to a network (Ethernet, wireless, internet). This type of
application can operate long distance machinery survey, or collect saved data in a
central database.
The data that can be collected are:
- Real-time acquisition (on the flight, or at end of acquisition)
- Exported results (any type of results exported in a preferred format)
- Saved results (any type of results reloaded in NVGate®.
For this purpose, NVDrive® provides a complete set of commands that returns results
in a convenient binary format. It is also possible to reload saved data and download
them from a distant analyzer.

<!-- page 12 -->

### 1.2 - REAL-TIME AND OFFICE POST-ANALYSIS

NVDrive® language allows controlling OROS analyzers during real time acquisition as
well as post-analysis sequence without using the hardware.
The analyzer is controlled by NVGate®, the OROS sound and vibration software platform
that runs on a dedicated PC.
NVDrive® language can access NVGate®
- When it operates connected to the OR3x analyzer (see fig. 2)
- When it operates in the office mode without hardware (see fig. 3)
OR3x
(Analyzer NVGate®
H ardware) (Analyzer
Software)
Real time
Signal
Fig 2 - Real time measurement operations
PC
Hard disk
Recorded
Signal
NVGate®
(Analyzer
Software)
Fig 3 -Office post-analysis operations
This architecture allows your application to use OROS Analyzers for real-time
application as well as post analysis purpose (with or without hardware) through
NVDrive® language.
NVGate® Analysis processes use the same commands and data formats for real-time
and post-analysis; the only difference is the signal source.
That is to say OROS Analyzers manage for your application the Real-time or Post-
analysis capabilities.

<!-- page 13 -->

### 1.3 - NETWORK CONTROL

As NVDrive® controls NVGate® through a standard TCP/IP socket this can be achieve
form any location, i.e., the NVDrive® application can be located in the same computer as
NVGate® (see fig. 4), or even in another machine connected to the NVGate/OR3x
computer by a TCP/IP link
TCP/IP link
NVGate®
Internal socket
Your NVDrive
Application
Fig. 4 - NVDrive® application located on NVGate computer
Note: When using NVGate® and NVDrive® application on the same computer, it is
helpful to use the special IP address: 127.0.0.1 that means "this machine". This will allow
operation on any computer without need of IP address update.
NV Gate® Your NVDrive
Application
TCP/IP link
LAN/Internet
Fig. 5 - NVDrive® application located on another computer
To access NVGate® through a network (see fig. 5) you just need the NVGate® computer
IP address. As NVDrive® language support TCP/IP connection and it is not related to
libraries or other kind of program links, this allows the NVDrive® application to be
written independently.
You can control NVGate® from a Linux computer, with C application for example. This
TCP/IP link support also wireless connection or even Internet connection (if firewall and
address are well controlled).

<!-- page 14 -->

### 1.4 - VERSION COMPATIBILITY

NVDrive® applications are version-independent. Thanks to the TCP/IP control, you can
write an application that will be compatible with all the future versions of NVGate®.
OROS guarantee that all the commands and settings identification numbers will stay
unchanged, or only enhanced, on each new NVGate® release.
This capability lets you share or sale your NVDrive® application to the current and future
set of OR3x customers. All NVGate® versions are NVDrive® compatibles without
additional licenses, key or dongle.

### 1.5 - CUSTOMIZATION

Prior to use NVDrive® to control NVGate® behavior, you can easily create the most
appropriated customization of the analyzer to be used by your application.

#### 1.5.1 - User profiles

NVGate® is a multi-purpose platform that provides variety of display types, scales, units,
colors, etc. You can predefine your application preferences in a specific profile. For this,
do the following:
1. Make a copy of the NVGate.usr file (located in the NVGate® execution directory)
and rename it as MyApp.usr where MyApp is your choice.
2. Launch NVGate® with the following parameter: "NVGate.exe -usr=MyApp"
3. Create a new user with a name for your application (for example: first name =
Sound, last name = intensity)
4. Select all the requested preferences from the User/preferences menu. Select the
visible tools bars, exit NVGate®.
5. Then launch NVGate® from your application using the following parameter:
"NVGate.exe -usr=MyApp" and select your special user with the 3.5.5 - SetUser
command).
Using this technique your application will be totally independent of the modification
made by the regular NVGate® users that use the NVGate.usr profile file.
Note: details on NVGate® command line is given in the appendixes.

<!-- page 15 -->

#### 1.5.2 - Project based application

Another way you can adapt NVGate® to your application is to use predefined projects.
This technique provides a faster and more complete setup of the analyzer. Projects are
compatible between each analyzer's configuration (including channels number
available analysis modes). With a predefined project you may gain development time,
using the NVGate® capabilities serving your application for example:
1. Select the specific setting to be directly used with a control panel.
2. Define Layouts with a specific graph arrangement, windows names, etc.
3. Use macros to interact with the operator, or to automate processing.
For this purpose, you just have to create and save your projects using NVGate®, and
then copy these projects in the analyzer project directory during your application
installation procedure. NVGate® project directory path is available in the NVGate.ini
file located in the NVGate® execution directory.

<!-- page 16 -->

## 2 - DESCRIPTION OF SERVICES AND FUNCTIONS

The external language offers a set of commands designed to control the analyzer interface
via a TCP/IP link.

### 2.1 - PRECAUTIONS

Hyperthreading.

### 2.2 - CONNECTION

NVGate® software must be launched prior to any commands.
One of the threads of the NVGate® software places the port 3000 of the system to wait
for a socket connection. NVGate® is thus the server and waits for queries from one
client external application.
NVDrive® commands are available whatever the Analyzer operating mode is
connected or office. In both case NVDrive® is available for real-time acquisition and
analysis or post analysis.
NVGate® must operate in connected mode in order to control the analyzer thought
NVDrive®.

### 2.3 - EXCHANGE FORMAT


#### 2.3.1 - Client → Server

- The command lines are transmitted in ASCII format.
- A carriage return (ASCII 13, \r in C language) and/or a line return (ASCII 10,
\n in C language) indicate the end of the command, in order to simplify client
application programming. This is because some programming languages do not
allow the user to choose the end of line characters.
- Command names are only made up of letters.
- Commands and parameters are separated by spaces. If a parameter must
contain spaces, it must be noted between quotes.
- The anti-slash character (\) indicates that the next character must be considered
as a normal character and not as a language word (despecialization). Examples
of how to use the anti-slash are given at the end of this section.
There are three parameter types:
- Compulsory parameters: they must be given in the order defined in the
command documentation.
- Optional parameters: Each command accepts a maximum number of optional
parameters. If an optional parameter is omitted, its default value is used.
Parameters must be given in order unless the rank of the parameter given is

<!-- page 17 -->
specified. Parameter rank is specified by the prefix "pi=" where i gives the
rank of the optional parameter (1 for the first optional parameter). If an
optional parameter is given with its rank, the following parameters must be
given in the same way.
- Version parameter: This is an optional parameter. When a NVDrive®
command has been upgraded once or several time, the version to be used can
be selected as an optional parameter specified by the prefix "v=".

**Examples**

```
With 3 compulsory parameters:
Command "My file" 25 z
With 1 compulsory parameter and 3 optional parameters:
Specifying all parameters in order:
Command strpar 1 2 3
Omitting the last optional parameter:
Command strpar 1 2
Omitting the first two optional parameters:
Command strpar p3=3
Specifying all the optional parameters but not in order:
Command strpar p2=2 p1=1 p3=3
With 3 compulsory parameter, 2 optional parameters and 1 version parameter:
Specifying all parameters in order:
Command GetResultEx 6 75 1 0 0 v=4
Special case:
the ExecMacro command
In addition to the compulsory and optional parameters of ExecMacro command,
values can be specified for the macro constants. The macro constants are user defined
in the NVGate® macro editor. For example, to assign a value to the "frequency"
constant, the string "frequency=90" (without quotes) will be added to the parameters.
If no value is specified for a constant, the default value defined in the macro will be
used.
Examples of how to use the anti-slash:
Specify a string type parameter containing a space without using the quotes
LoadProject My\ project can be used instead of
LoadProject "My project"
Use the quotes inside a string already between quotes
"he says \"Hello.\"."
When a character string type parameter beginning with the letter p is specified
without quotes, it must be preceded by the anti-slash. Otherwise, the character
p is interpreted as the start of the key word pi= used to specify the value of an
optional parameter.
```

<!-- page 18 -->
```
LoadProject project1 returns a syntax error.
LoadProject \project1 must be used if you want to load the
project with the name "projet1".
LoadProject "project1" is another possibility.
```

<!-- page 19 -->
```
```

#### 2.3.2 - Server → Client

A 10-character block is systematically returned (header):
Header Data
The first character returned specifies the object type that follows:
0. Acknowledgement of receipt OK. Indicates that the command was completed
without error. The following nine characters indicate the size of the following
data.
1. Command interpretation error (syntax).
2. Consistency error: action possible / impossible.
3. Command run error. The following nine characters indicate the error code
returned by the command at internal language level.
If there is no error, the first character is 0, and the following nine characters indicate
the size of the following data (in number of bytes).
If there is an error, the first character goes from 1 to 3, and the following nine
characters indicate the error code (see below).

### 2.4 - PART LIST OF INTERPRETATION / SYNTAX ERRORS

The following tables contain the 9 code digits

| ??? | ??? | ??? |
|---|---|---|


**Syntax errors**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 001 | 001 | XXX | Generic syntax error. XXX = error position. |
| 001 | 002 | 000 | A rank is specified for one of the optional parameters and is<br>not specified for the following optional parameters. |
| 001 | 003 | XXX | Unexpected line end.<br>XXX = error position (line end). |


**Semantic errors**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 002 | 001 | 000 | Command name unknown. |
| 002 | 002 | XXX | An optional parameter is assigned several times.<br>XXX = rank of the parameter in question. |
| 002 | 003 | 000 | The command does not accept the constants |


**Parameter errors**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 003 | 001 | XXX | Number of compulsory parameters insufficient.<br>XXX = number of parameters expected (minimum). |
| 003 | 002 | XXX | Too many parameters.<br>XXX = maximum number of parameters. |
| 003 | 003 | XXX | Optional parameter rank invalid.<br>XXX = maximum number of optional parameters. |


<!-- page 20 -->

#### 2.4.1 - "GetErrorMessage" command


**Semantics**

Returns the description in English of a header (the header format is defined in
section 2.3.2 - Server → Client).

**Command syntax**

```
GetErrorMessage <header>
```

**Result returned**

Returns a character string coded in ASCII ending in the character \0.

**Consistency errors specific to the GetErrorMessage command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 002 | 001 | 000 | The specified parameter is not a header |
| 002 | 002 | 000 | Code Unknown |


<!-- page 21 -->

## 3 - COMMANDS


### 3.1 - ACTIONS


#### 3.1.1 - "ExecMacro" command


**Semantics**

Used to start the execution of a macro.

**Command syntax**

```
ExecMacro <macro name> [<constant1 name> = <value1>]
[<constant2 name> = <value2>]
[...]
```

**Example**

```
ExecMacro "My Macro" const1=3 "my constant 2"=8
For Boolean type constants, the integer 0 stands for the value FALSE and the
integer 1 stands for the value TRUE.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ExecMacro command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 001 | 001 | 000 | Macro unknown |
| 001 | 002 | XXX | Constant unknown<br>XXX is the rank of the constant in the command.<br>The first constant specified is of rank 1. |
| 001 | 003 | XXX | Type of value for the constant of rank XXX incorrect. |


**Execution errors specific to the ExecMacro command**

| Error code | Meaning |
|---|---|
| 000008000 | Macro loading has failed |
| 000008001 | Recursive macro |


<!-- page 22 -->

#### 3.1.2 - "Run" command


**Semantics**

If no measurement is in the process of acquisition, start a new measurement. The
new measurement is in the "run" mode.
If a measurement is in the process of acquisition:
- If it is in the « pause » mode, reinitialize then restart the measurement.
- If it is in the « run » mode, reinitialize then restart the measurement.

**Command syntax**

```
Run
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Pause command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 013 | 001 | 000 | Measurement is already in process |
| 013 | 002 | 000 | A measurement is saving. |


<!-- page 23 -->

#### 3.1.3 - "Stop" command


**Semantics**

Permanently stops the measurement in the process of acquisition (only one
measurement is possible at a time), which can be in the « run » or « pause » mode.
In this case there is no longer any measurement in the process of acquisition.
If no measurement is in the process of acquisition, the consistency error
014001000 is generated (see the consistency error table).

**Command syntax**

```
Stop
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Stop command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 014 | 001 | 000 | No measurement in the process of acquisition. |


<!-- page 24 -->

#### 3.1.4 - "Pause" command


**Semantics**

If a measurement is in the process of acquisition:
- If the measurement is in the « run » mode, interrupt the measurement. It then
moves to the "pause" mode.
- If the measurement is in the "pause" mode, continue the measurement which
moves to the "run" mode.
If no measurement is in the process of acquisition, the consistency error
015001000 is generated (see the consistency error table).

**Command syntax**

```
Pause
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Pause command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 015 | 001 | 000 | No measurement in the process of acquisition |


<!-- page 25 -->

#### 3.1.5 - "PlayByStep " command


**Semantics**

Play by steps, available only in post-analysis, when the file is played by step. The
command starts a new step or pauses the current step.

**Command syntax**

```
PlayByStep [Action]
[Action] optional parameter. 1 to pause, 0 to play. If this parameter is not set,
the action depends on the current NVGate state.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Pause command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 297 | 001 | 000 | No measurement in the process of acquisition |


<!-- page 26 -->

#### 3.1.6 - "Accept" command


**Semantics**

Do accept the signal blocks in the FFT plug-in.

**Command syntax**

```
Accept
```

**Result returned**

No data follows the header.

<!-- page 27 -->

#### 3.1.7 - "Reject" command


**Semantics**

Do reject the signal blocks in the FFT plug-in.

**Command syntax**

```
Reject
```

**Result returned**

No data follows the header.

<!-- page 28 -->

#### 3.1.8 - "ManualTrigger" command


**Semantics**

Set on the manual trigger.

**Command syntax**

```
ManualTrigger
```

**Result returned**

No data follows the header.

<!-- page 29 -->

#### 3.1.9 - "ShutDown" command


**Semantics**

Allows the user to close the server application.

**Command syntax**

```
ShutDown [Save]
The optional parameter [Save] equals 0 by default.
Entering 0 lets you close the application without saving.
Entering 1 lets you close the application while making the necessary saves.
In this case, the confirmation dialogue boxes corresponding to the various saves
will appear in NVGate.
A value other than 0 or 1 is interpreted as a 0 (no saving).
```

**Result returned**

No data follows the header.

<!-- page 30 -->

#### 3.1.10 - "StandAlone" command


**Semantics**

Allows the user to close the application in standalone mode.

**Command syntax**

```
StandAlone
```

**Result returned**

No data follows the header.

**Consistency errors specific to the StandAlone command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 160 | 1xx | xxx | The depth of the waterfall is too large. Xxxxx indicates the<br>maximum depth that can be stored |
| 160 | 002 | 000 | The analyzer must be stopped before closing the application |
| 160 | 003 | 000 | The recorder cannot record on the PC in standalone mode |


<!-- page 31 -->

#### 3.1.11 - "AbortStandAlone" command


**Semantics**

Allows the user to abort the standalone session for a specific project.

**Command syntax**

```
AbortStandAlone <project name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AbortStandAlone command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 164 | 001 | 000 | The project does not exist. |
| 164 | 002 | 000 | The project is not in standalone. |


<!-- page 32 -->

#### 3.1.12 - "Autorange" command


**Semantics**

Do or stop the auto range according to the NVGate settings.

**Command syntax**

```
Autorange [DoAutorange]
[Master or Slave]
The [DoAutorange] parameter is "1" by default and indicates if the auto range
must be launched (case "1") or stopped (case "0"). It can only be stopped during a
peak auto range.
The [Master or Slave] parameter is "1" by default and indicates if the auto
range must be done on the master inputs (case "1") or on the slave inputs (case
"2") that are only available with a dual configuration.
If a value different from those waited is entered, it is changed in the default value.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Autorange command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 090 | 001 | 000 | The action is already in course. |
| 090 | 002 | 000 | Slave is Selected, but the configuration is not dual. |


<!-- page 33 -->

#### 3.1.13 - "CheckICP" command


**Semantics**

Do the check ICP on the channels whose coupling is ICP.

**Command syntax**

```
CheckICP [Master or Slave]
The [Master or Slave]parameter is "1" by default and indicates if the
checkICP must be done on the master inputs (case "1") or on the slave inputs
(case "2") that are only available with a dual configuration.
If a value different from those waited is entered, it is changed in the default value.
The report of the check ICP is displayed if at least one channel whose coupling is
ICP does not detect an ICP sensor.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CheckICP command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 091 | 001 | 000 | Action not available with OR34 or OR35 |
| 091 | 002 | 000 | Unknown setting |
| 091 | 003 | 000 | The action is already in course. |
| 091 | 004 | 000 | Slave is Selected, but the configuration is not dual. |
| 091 | 005 | 000 | At least one channel whose coupling is ICP does not detect<br>an ICP sensor. The report of the check ICP is returned. |


<!-- page 34 -->

#### 3.1.14 - "CheckTEDS" command


**Semantics**

Do the check TEDS on the channels whose coupling is ICP TEDS.

**Command syntax**

```
CheckTEDS [Master or Slave]
[Input]
[Silent]
All parameters are optional.
The [Master or Slave] parameter is "1" by default and indicates if the
CheckTEDS must be done on the master inputs (case "1") or on the slave inputs
(case "2") that are only available with a dual configuration.
The [Input] parameter is 0 by default, thus checking TEDS on all input. If set
to another value, only the corresponding input is checked.
The [Silent] parameter is 1 by default, using the silent mode, it means that
the "New transducer detected (TEDS)" window is not displayed and the
transducer is automatically added to the transducers database. If set to 0, the silent
mode is not activated.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CheckTEDS command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 191 | 001 | 000 | The action is already in course. |
| 191 | 002 | 000 | Unknown setting |
| 191 | 003 | 000 | At least one channel whose coupling is ICP TEDS does not<br>detect a TEDS sensor. |


<!-- page 35 -->

#### 3.1.15 - "Emergency stop" command


**Semantics**

Do the "emergency stop" action, which cut all the output signals.

**Command syntax**

```
EmergencyStop
```

**Result returned**

No data follows the header.

**Consistency errors specific to the EmergencyStop command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 092 | 001 | 000 | The action is already in course. |
| 092 | 002 | 000 | The emergency stop setting is not found. |


<!-- page 36 -->

#### 3.1.16 - "EditCalibration" command


**Semantics**

Edit the calibration's dialog box, and wait for the user to click on "OK" or
"Cancel".

**Command syntax**

```
EditCalibration
```

**Result returned**

The header is followed by value returned by the edit dialog:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | short | Value returned by the edit dialog:<br>- 1 : OK (if the user press OK)<br>- 2 : CANCEL (if the user press Cancel) |


**Consistency errors specific to the EditCalibration command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 128 | 001 | 000 | NVGate is not in measure mode |
| 128 | 002 | 000 | NVGate is not connected to an analyzer |
| 128 | 003 | 000 | Not all the analyzers are stopped |


<!-- page 37 -->

#### 3.1.17 - "RefreshState" command


**Semantics**

Refresh all NVGate status.

**Command syntax**

```
RefreshState
```

**Result returned**

No data follows the header.

<!-- page 38 -->

#### 3.1.18 - "FormatDisk" command


**Semantics**

Format OR3x internal disk.

**Command syntax**

```
FormatDisk
```

**Result returned**

No data follows the header.

**Consistency errors specific to the FormatDisk command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 177 | 001 | 000 | Format hard disk as failed |


<!-- page 39 -->

### 3.2 - MARKER


#### 3.2.1 - "GetWindowTraces" command


**Semantics**

Allows the user to retrieve the name of the results displayed in a window.

**Command syntax**

```
GetWindowTraces <window name>
```

**Result returned**

A list of result descriptions (see chapter § 3.10 - Result format and description
).
Each result description is separated from the next one by the character minus '-'.

**Consistency errors specific to the GetWindowTraces command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 036 | 001 | 000 | Unknown window |


<!-- page 40 -->

#### 3.2.2 - "GetWindowDisplayZone" command


**Semantics**

Allows the user to retrieve the identifiers of the type of the window display zones.
Those display zones are very useful to handle markers.

**Command syntax**

```
GetWindowDisplayZone <window name>
```

**Result returned**

A list of display zone type identifiers. An identifier is a short (2 bytes).

| Identifier |   | Type of display zone |   |   | Type of window |   |
|---|---|---|---|---|---|---|
| 0 |   | Default display zone |   | Octave - Time - Profile |   |   |
| 1 |   | Imaginary part display zone |   | Spectral - CBT - 2D Waterfall |   |   |
| 2 |   | Real part display zone |   | Spectral - CBT - 2D Waterfall |   |   |
| 3 |   | Phase display zone |   | Spectral - CBT - 2D Waterfall |   |   |
| 4 |   | Module display zone |   | Spectral - CBT - 2D Waterfall |   |   |
| 5 |   | YZ section zone |   | 3D waterfall |   |   |
| 6 |   | XY section zone |   | 3D waterfall |   |   |
| 7 |   | Order section zone |   | 3D waterfall |   |   |
| 8 |   | 3D zone |   | 3D waterfall (warning: this display zone<br>cannot contain markers) |   |   |


**Consistency errors specific to the GetWindowDisplayZone command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 037 | 001 | 000 | Unknown window |


<!-- page 41 -->

#### 3.2.3 - "GetMarkerList" command


**Semantics**

Allows the user to retrieve the markers defined in a display zone of a window.

**Command syntax**

```
GetMarkerList <window name>
[display zone type]
The [display zone type] parameter can be retrieved using the 3.2.2 -
GetWindowDisplayZone command.
It is optional. The default value depends on window type and display type:
In multi-graph mode, all display zones have the type identified by the "display
zone type" parameter (else, the error "Invalid or unavailable display zone" is
returned). So, the markers defined in all the zones are returned in the list.
```

**Result returned**

A list of marker descriptions.
Each marker description is separated from the next one by the minus character '-'.
A marker description consists of the following fields:

|   | Window type |   |   | Display Type |   |   | Default value |   |
|---|---|---|---|---|---|---|---|---|
| 3D waterfall |   |   |   |   |   | 6 (XY section zone) |   |   |
| Octave<br>Time<br>Profile |   |   |   |   |   | 0 (Default display zone) |   |   |
| Spectral<br>CBT<br>2D Waterfall |   |   | Real part mode<br>Real / Imaginary mode |   |   | 2 (Real display zone) |   |   |
|   |   |   | Imaginary part mode |   |   | 1 (Imaginary display zone) |   |   |
|   |   |   | Magnitude mode<br>Magnitude / Phase mode |   |   | 4 (Magnitude display zone) |   |   |
|   |   |   | Phase mode<br>Phase / Magnitude mode |   |   | 3 (Phase display zone) |   |   |


|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | Unsigned short | Marker type |
| 4 |   |   | Unsigned int | Marker number |
| 2 |   |   | Unsigned short | It defines the trace on which the marker is applied :<br>0 : the marker is applied on all traces of the zone<br>1 : the marker is applied on the active trace of the<br>zone<br>2 : the marker is applied on a specific trace, which is<br>described by the result description which follows. |
| X |   |   | Result<br>description<br>(See chapter §<br>3.10 - Result<br>format and<br>description | Only if trace application is 1 or 2.<br>Describes the trace on which the marker is applied |


<!-- page 42 -->
The different types of markers supported by NVDrive® commands are:

| Column 1 | Column 2 | Column 3 |
|---|---|---|
|   | ) |   |


| identifier |   |   | Type of marker |   |
|---|---|---|---|---|
| 0 |   | free |   |   |
| 1 |   | sideband |   |   |
| 2 |   | harmonics |   |   |
| 3 |   | peak |   |   |
| 4 |   | max |   |   |
| 5 |   | powerband |   |   |
| 6 |   | record |   |   |
| 7 |   | Nth octave |   |   |
| 8 |   | period |   |   |
| 9 |   | kinematic |   |   |


**Consistency errors specific to the GetMarkerList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 038 | 001 | 000 | Unknown window |
| 038 | 002 | 000 | Invalid display zone |


<!-- page 43 -->

#### 3.2.4 - "AddFreeMarker" command


**Semantics**

Allows the user to add a free marker on a trace.

**Command syntax**

```
AddFreeMarker <window name>
<position>
[display zone type]
[interpolation type]
[label]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[Display current position]
[color]
[Style line]
[Hide string note]
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The position in S.I. unit of the marker on X axis is defined by the "position"
parameter. There is an exception for the X axis expressed in "Slice number": the
position is the index (for the first value of the X axis (1#), "position" is 0).
The [interpolation type] parameter is one of the following values:
- 0: no interpolation
- 1: X interpolation
- 2: X +Y interpolation
It is an optional parameter. The default value is 0.
[label] is the name of the marker.
The [trace application] defines the trace on which the marker is applied:
- 0: the marker is applied on all traces of the zone (in multi-graph mode, one
marker is added per zone)
- 1: the marker is applied on the active trace of the zone: in multigraph mode,
the marker is associated to the curve which was active when it was created;
in multitrace mode, the marker is associated to the current active curve.
- 2: the marker is applied on a specific trace, defined by the 4 next
parameters, which are the components of a result description.
This parameter is similar to the "Trace application" field returned by the
"3.2.3 - GetMarkerList".
It is an optional parameter and its default value is 1.
```

<!-- page 44 -->
```
[Display current position]: Boolean to decide whether the marker
displays the label or the current position (X: Y).
- 0: displays the label
- 1: displays the current position
It is an optional parameter. Its default value is the default user preference value set
for the free marker.
[color]: line color of the marker
Possible RGB value format :
- #RGB (each of R, G, and B is a single hex digit)
- #RRGGBB
- #RRRGGGBBB
- #RRRRGGGGBBBB
- A name from the list of SVG color names provided by the World Wide Web
Consortium; for example, "steelblue" or "gainsboro".
It is an optional parameter. Its default value is the default user preference value set
for the free marker.
[Style line] : style line of the marker
Possible values :
- 1 = Vertical line
- 2 = Vertical dashed line
- 3 = Vertical with rectangle
- 4 = Cross-hair
- 5 = Vertical + Horizontal
It is an optional parameter. Its default value is the default user preference value set
for the free marker.
[Hide tag note]:Boolean to decide whether the marker displays its tag note
- 0: show tag note
- 1: hide tag note
It is an optional parameter. Its default value is 0.
```

**Example**

```
AddFreeMarker Window1 10000 3 0 "Phase 10kHz" 0
-> Add a free marker to all phase traces of Window1 at 10 kHz.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddFreeMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 039 | 001 | 000 | Unknown window |
| 039 | 002 | 000 | Invalid position |
| 039 | 003 | 000 | Invalid or unavailable display zone type |
| 039 | 004 | 000 | Invalid interpolation type |
| 039 | 005 | 000 | Invalid trace application |
| 039 | 006 | 000 | Unknown trace |


<!-- page 45 -->

#### 3.2.5 - "AddPeakMarker" command


**Semantics**

Allows the user to add a peak marker on a trace.

**Command syntax**

```
AddPeakMarker <window name>
[threshold]
[Absolute threshold]
[Max peak number]
[display zone type]
[interpolation type]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[ValueSortedByFrequency]
[DampingRatio]
[color]
[Style line]
The [threshold],[Absolute threshold] and [Max peak number]
parameters define the peak marker.
The [threshold] parameter is optional, its default value is 5 dB.
The [Absolute threshold] parameter is optional, its default value is -120
dB.
The[Max peak number] parameter is optional, its default value is 5. Its value
must be greater than 0.
The [ValueSortedByFrequency] parameter is optional, its default is 1. It
defines values sort by frequency (1) or by amplitude (0).
The [DampingRatio] parameter is optional, its default value is 0. It adds (1)
the damping ratio in the marker table (since NVGate 9.10).
Others parameters are described in chapter 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddPeakMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 040 | 001 | 000 | Unknown window |
| 040 | 002 | 000 | Invalid max peak number |
| 040 | 003 | 000 | Invalid or unavailable display zone type |
| 040 | 004 | 000 | Invalid interpolation type |
| 040 | 005 | 000 | Invalid trace application |
| 040 | 006 | 000 | Unknown trace |


<!-- page 46 -->

#### 3.2.6 - "AddMaxMarker" command


**Semantics**

Allows the user to add a max marker on a trace.

**Command syntax**

```
AddMaxMarker <window name>
[threshold]
[Absolute threshold]
[Max peak number]
[display zone type]
[interpolation type]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[ValueSortedByFrequency]
[DampingRatio]
[color]
[Style line]
See 3.2.5 - AddPeakMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddMaxMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 041 | 001 | 000 | Unknown window |
| 041 | 002 | 000 | Invalid max peak number |
| 041 | 003 | 000 | Invalid or unavailable display zone type |
| 041 | 004 | 000 | Invalid interpolation type |
| 041 | 005 | 000 | Invalid trace application |
| 041 | 006 | 000 | Unknown trace |


<!-- page 47 -->

#### 3.2.7 - "AddPowerBandMarker" command


**Semantics**

Allows the user to add a power band marker on a trace.

**Command syntax**

```
AddPowerBandMarker <window name>
<Start position>
<Delta>
[display zone type]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[color]
[Style line]
The <Start position> and <Delta> parameters define the power band
marker. They must be specified in S.I. unit.
Others parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddPowerBandMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 042 | 001 | 000 | Unknown window |
| 042 | 002 | 000 | Invalid Start position |
| 042 | 003 | 000 | Invalid Delta (Start position + delta is out of bound) |
| 042 | 004 | 000 | Invalid or unavailable display zone type |
| 042 | 005 | 000 | Invalid trace application |
| 042 | 006 | 000 | Unknown trace |


<!-- page 48 -->

#### 3.2.8 - "AddSideBandMarker" command


**Semantics**

Allows the user to add a side band marker on a trace.

**Command syntax**

```
AddSideBandMarker <window name>
<Start position>
<Delta>
[Number of bands]
[display zone type]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[color]
[Style line]
The <Start position> and <Delta> parameters define the side band
marker. They must be specified in S.I. unit.
By default, the [Number of bands] is set to 3.
Others parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddSideBandMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 142 | 001 | 000 | Unknown window |
| 142 | 002 | 000 | Invalid number of bands |
| 142 | 003 | 000 | Invalid or unavailable display zone type |
| 142 | 004 | 000 | Invalid or unavailable interpolation type |
| 142 | 005 | 000 | Invalid trace application |
| 142 | 006 | 000 | Unknown trace |


<!-- page 49 -->

#### 3.2.9 - "AddHarmonicMarker" command


**Semantics**

Allows the user to add a harmonic marker on a trace.

**Command syntax**

```
AddHarmonicMarker <window name>
<Start position>
[Number of harmonics]
[display zone type]
[trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[color]
[Style line]
The <Start position> parameter defines the harmonic band marker. They
must be specified in S.I. unit.
By default, the [Number of harmonics] is set to 3.
Others parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddHarmonicMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 143 | 001 | 000 | Unknown window |
| 143 | 002 | 000 | Invalid number of harmonics |
| 143 | 003 | 000 | Invalid or unavailable display zone type |
| 143 | 004 | 000 | Invalid or unavailable interpolation type |
| 143 | 005 | 000 | Invalid trace application |
| 143 | 006 | 000 | Unknown trace |


<!-- page 50 -->

#### 3.2.10 - "AddRecordMarker" command


**Semantics**

Allows the user to add a record marker (during recording).

**Command syntax**

```
AddRecordMarker
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddRecordMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 253 | 001 | 000 | No recording |


<!-- page 51 -->

#### 3.2.11 - "AddPeriodMarker" command


**Semantics**

Allows the user to add a period marker on a trace.

**Command syntax**

```
AddPeriodMarker <window name>
<Start position>
[Number of periods]
[Period duration]
[Display zone type]
[Trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[color]
[Style line]
The <Start position> parameter defines the harmonic band marker. They
must be specified in S.I. unit.
By default, the [Number of periods] is set to 3.
The [period duration] parameter defines the length of the period in S.I.
unit.
Others parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddPeriodMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 279 | 001 | 000 | Unknown window |
| 279 | 002 | 000 | Invalid number of periods |
| 279 | 003 | 000 | Invalid or unavailable display zone type |
| 279 | 004 | 000 | Invalid trace application |
| 279 | 005 | 000 | Unknown trace |


<!-- page 52 -->

#### 3.2.12 - "AddKinematicMarker" command


**Semantics**

Allows the user to add a kinematic marker on a trace.

**Command syntax**

```
AddKinematicMarker <window name>
<position>
<kinematic marker type>
<kinematic marker number>
[Display zone type]
[Interpolation type]
[Trace application]
[Module number]
[Process number]
[Channel number]
[Reference channel number]
[color]
[Style line]
The <position> parameter defines the kinematic marker. They must be
specified in S.I. unit.
<kinematic marker type> parameter identifies the kinematic markers
database type index of the kinematic marker you want to add (marker type >= 0).
<kinematic marker number> parameter identifies the kinematic markers
database marker number you want to add (marker number >= 0).
Others parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddKinematicMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 333 | 001 | 000 | Unknown window |
| 333 | 002 | 000 | Invalid position |
| 333 | 003 | 000 | Invalid or unavailable display zone type |
| 333 | 004 | 000 | Invalid interpolation type |
| 333 | 005 | 000 | Invalid trace application |
| 333 | 006 | 000 | Unknown trace |
| 333 | 007 | 000 | Unknown kinematic marker |


<!-- page 53 -->

#### 3.2.13 - "AddNOctaveMarker" command


**Semantics**

Allows the user to add a 1/N octave marker on a trace.

**Command syntax**

```
AddFreeMarker <window name>
[trace application]
[Module number]
[Process number]
[Channel number]
The [trace application] defines the trace on which the marker is applied:
- 0: the marker is applied on all traces of the zone (in multi-graph mode, one
marker is added per zone)
- 1: the marker is applied on the active trace of the zone: in multigraph mode,
the marker is associated to the curve which was active when it was created;
in multitrace mode, the marker is associated to the current active curve.
- 2: the marker is applied on a specific trace, defined by the 3 next
parameters, which are the components of a result description.
This parameter is similar to the "Trace application" field returned by the
"3.2.3 - GetMarkerList".
It is an optional parameter and its default value is 1.
```

**Example**

```
AddNOctaveMarker Window1 0
-> Add a 1/N Octave marker to all traces of the zone of the active trace.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddNOctaveMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 384 | 001 | 000 | Unknown window |
| 384 | 002 | 000 | The window is not compatible with NOctave marker |
| 384 | 003 | 000 | Invalid trace application |
| 384 | 004 | 000 | Unknown trace |


<!-- page 54 -->

#### 3.2.14 - "GetNumberOfRecordMarker" command


**Semantics**

Returns the number of record markers in the current displayed signal.

**Command syntax**

```
GetNumberOfRecordMarker
```

**Result returned**

A short value which is the number of record markers.

<!-- page 55 -->

#### 3.2.15 - "SetRecordMarkerLabel" command


**Semantics**

Allows the user to put a label to a record marker.

**Command syntax**

```
SetRecordMarkerLabel <window name>
<marker number>
<label>
The <window name> parameter identifies a window where the recorded signal is
displayed.
The <marker number> parameter identifies the marker whose label will change.
The first marker corresponds to number 1.
The <label> parameter is the name to affect to the selected record marker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetRecordMarkerLabel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 255 | 001 | 000 | Unknown window |
| 255 | 002 | 000 | Unknown marker |


<!-- page 56 -->

#### 3.2.16 - "RemoveMarker" command


**Semantics**

Allows the user to remove a marker.

**Command syntax**

```
RemoveMarker <window name>
[display zone type]
[marker type]
[marker number]
The [display zone type] parameter is optional. If it is not specified,
"marker type" and "marker number" parameters are ignored. All markers of the
window are removed.
The [marker type] parameter is optional. Its default value is 0 (free marker).
The [marker number] parameter is optional. Its default value is 1.
The number of markers remaining is updated, when the specified marker has been
removed.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveMarker command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 043 | 001 | 000 | Unknown window |
| 043 | 002 | 000 | Invalid or unavailable display zone type |
| 043 | 003 | 000 | Unknown marker type |
| 043 | 004 | 000 | Unknown marker |


<!-- page 57 -->

#### 3.2.17 - "DisplayMarkerProperties" command


**Semantics**

Displays the given marker properties dialog.

**Command syntax**

```
DisplayMarkerProperties <window name>
<display zone type>
<marker type>
<marker number>
<marker type> parameter identifies the type of marker you want to get
parameters (see 3.2.3 - "GetMarkerList" command for the list of marker types).
<marker number> parameter identifies the marker you want to get
parameters.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DisplayMarkerProperties
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 334 | 001 | 000 | Unknown window |
| 334 | 002 | 000 | Invalid or unavailable display zone type |
| 334 | 003 | 000 | Unknown marker type |
| 334 | 004 | 000 | Unknown marker |


<!-- page 58 -->

#### 3.2.18 - "DuplicateMarkerInMultigraphWindow" command


**Semantics**

Duplicate the given marker in the other areas of the window (displayed in a
multigraph mode).

**Command syntax**

```
DuplicateMarkerInMultigraphWindow <window name>
<marker type>
<marker number>
<marker type> parameter identifies the type of marker to duplicate (see 3.2.3
- "GetMarkerList" command for the list of marker types).
<marker number> parameter identifies the marker to duplicate.
```

**Example**

```
DuplicateMarkerInMultigraphWindow Window1 3 1
-> Duplicate the marker number 1, which is a peak marker in the other areas
of Window1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the
DuplicateMarkerInMultigraphWindow command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 383 | 001 | 000 | Unknown window |
| 383 | 002 | 000 | The window is not in a multigraph mode |
| 383 | 003 | 000 | Unknown marker type |
| 383 | 004 | 000 | The marker is unknown in the window |


<!-- page 59 -->

#### 3.2.19 - "SetFreeMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a free marker.

**Command syntax**

```
SetFreeMarkerParameters <window name>
<display zone type>
<marker number>
[position]
[interpolation type]
[label]
[color]
[Style line]
[Hide tag note]
<marker number> parameter identifies the free marker you want to change
parameters.
Other parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetFreeMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 044 | 001 | 000 | Unknown window |
| 044 | 002 | 000 | Invalid or unavailable display zone type |
| 044 | 003 | 000 | Unknown marker |
| 044 | 004 | 000 | Invalid position |
| 044 | 005 | 000 | Invalid interpolation type |


<!-- page 60 -->

#### 3.2.20 - "GetFreeMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a free marker.

**Command syntax**

```
GetFreeMarkerParameters <window name>
<display zone type>
<marker number>
<marker number> parameter identifies the free marker you want to get
parameters.
Other parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | Marker position |   |   |
| X |   |   | string ending in the character \0 |   |   | Marker label |   |   |
| 4 |   |   | Unsigned int |   |   | Interpolation type |   |   |


**Consistency errors specific to the GetFreeMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 045 | 001 | 000 | Unknown window |
| 045 | 002 | 000 | Invalid or unavailable display zone type |
| 045 | 003 | 000 | Unknown marker |


<!-- page 61 -->

#### 3.2.21 - "SetPeakMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a peak marker.

**Command syntax**

```
SetPeakMarkerParameters <window name>
<display zone type>
<marker number>
[threshold]
[Absolute threshold]
[Max peak number]
[interpolation type]
[ValueSortedByFrequency]
(since NVGate 9.10) [Display damping ratio]
[color]
[Style line]
Parameters are described in chapter § 3.2.5 - AddPeakMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPeakMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 046 | 001 | 000 | Unknown window |
| 046 | 002 | 000 | Invalid or unavailable display zone type |
| 046 | 003 | 000 | Unknown marker |
| 046 | 004 | 000 | Invalid max peak number |
| 046 | 005 | 000 | Invalid interpolation type |


<!-- page 62 -->

#### 3.2.22 - "GetPeakMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a peak marker.

**Command syntax**

```
GetPeakMarkerParameters <window name>
<display zone type>
<marker number>
```

**Examples**

```
GetPeakMarkerParameters Window1 4 2 v=1
returns the parameters (including damping ratio) of the second peak marker
displayed in Window1.
GetPeakMarkerParameters Window1 4 2
GetPeakMarkerParameters Window1 4 2 v=0
returns the parameters (but not including damping ratio) of the second peak
marker displayed in Window1.
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | Threshold |   |   |
| 4 |   |   | Float |   |   | Absolute threshold |   |   |
| 4 |   |   | Unsigned<br>int |   |   | Maximum number of peaks per marker |   |   |
| 4 |   |   | Unsigned<br>int |   |   | Interpolation type |   |   |
| 1 |   |   | Boolean |   |   | Sort by frequency or amplitude |   |   |
| If version parameter is >= 1, and NVGate version is 9.10 or upper |   |   |   |   |   |   |   |   |
| 1 |   |   | Boolean |   |   | Display damping ratio |   |   |


**Consistency errors specific to the GetPeakMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 047 | 001 | 000 | Unknown window |
| 047 | 002 | 000 | Invalid or unavailable display zone type |
| 047 | 003 | 000 | Unknown marker |


<!-- page 63 -->

#### 3.2.23 - "SetMaxMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a max marker.

**Command syntax**

```
SetMaxMarkerParameters <window name>
<display zone type>
<marker number>
[threshold]
[Absolute threshold]
[Max peak number]
[interpolation type]
[ValueSortedByFrequency]
(since NVGate 9.10) [Display damping ratio]
[color]
[Style line]
Parameters are described in chapter § 3.2.6 - AddMaxMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetMaxMarkerParameters command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 048 | 001 | 000 | Unknown window |
| 048 | 002 | 000 | Invalid or unavailable display zone type |
| 048 | 003 | 000 | Unknown marker |
| 048 | 004 | 000 | Invalid max peak number |
| 048 | 005 | 000 | Invalid interpolation type |


<!-- page 64 -->

#### 3.2.24 - "GetMaxMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a max marker.

**Command syntax**

```
GetMaxMarkerParameters <window name>
<display zone type>
<marker number>
```

**Result returned**

Data returned is composed of following fields:

| Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|
| 4 |   | Float |   |   | Threshold |   |   |
| 4 |   | Float |   |   | Absolute threshold |   |   |
| 4 |   | Unsigned int |   |   | Maximum number of max per marker |   |   |
| 4 |   | Unsigned int |   |   | Interpolation type |   |   |
| 1 |   | Boolean |   |   | Sort by frequency or amplitude |   |   |
| If version parameter is >= 1, and NVGate version is 9.10 or upper |   |   |   |   |   |   |   |
| 1 |   | Boolean |   |   | Display damping ratio |   |   |


**Consistency errors specific to the GetMaxMarkerParameters command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 049 | 001 | 000 | Unknown window |
| 049 | 002 | 000 | Invalid or unavailable display zone type |
| 049 | 003 | 000 | Unknown marker |


<!-- page 65 -->

#### 3.2.25 - "GetRecordMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a record marker.

**Command syntax**

```
GetRecordMarkerParameters <window name>
<display zone type>
<marker number>
The <display zone type> parameter must be equal to 0.
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | X position (in seconds) |   |   |
| X |   |   | String |   |   | Label ending with '\0' |   |   |


**Consistency errors specific to the GetRecordMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 254 | 001 | 000 | Unknown window |
| 254 | 002 | 000 | Invalid or unavailable display zone type |
| 254 | 003 | 000 | Unknown marker |


<!-- page 66 -->

#### 3.2.26 - "SetPowerBandMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a power band marker.

**Command syntax**

```
SetPowerBandMarkerParameters <window name>
<display zone type>
<marker number>
[Start position]
[Delta]
[color]
[Style line]
Parameters are described in chapter § 3.2.7 - AddPowerBandMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPowerBandMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 050 | 001 | 000 | Unknown window |
| 050 | 002 | 000 | Invalid or unavailable display zone type |
| 050 | 003 | 000 | Unknown marker |
| 050 | 004 | 000 | Invalid Start position |
| 050 | 005 | 000 | Invalid delta (Start position + delta is out of bound) |


<!-- page 67 -->

#### 3.2.27 - "GetPowerBandMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a power band marker.

**Command syntax**

```
GetPowerBandMarkerParameters <window name>
<display zone type>
<marker number>
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|
| 4 |   | Float |   |   | Start position |   |   |
| 4 |   | Float |   |   | Delta |   |   |


**Consistency errors specific to the GetPowerBandMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 051 | 001 | 000 | Unknown window |
| 051 | 002 | 000 | Invalid or unavailable display zone type |
| 051 | 003 | 000 | Unknown marker |


<!-- page 68 -->

#### 3.2.28 - "SetSideBandMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a side band marker.

**Command syntax**

```
SetSideBandMarkerParameters <window name>
<display zone type>
<marker number>
[Start position]
[Delta]
[Number of bands]
[color]
[Style line]
Parameters are described in chapter § 3.2.8 - AddSideBandMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetSideBandMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 145 | 001 | 000 | Unknown window |
| 145 | 002 | 000 | Invalid or unavailable display zone type |
| 145 | 003 | 000 | Unknown marker |
| 145 | 004 | 000 | Invalid Start position |
| 145 | 005 | 000 | Invalid delta (Start position + delta is out of bound) |
| 145 | 006 | 000 | Invalid number of bands (<1 or >128) |


<!-- page 69 -->

#### 3.2.29 - "GetSideBandMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a side band marker.

**Command syntax**

```
GetSideBandMarkerParameters <window name>
<display zone type>
<marker number>
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | Start position |   |   |
| 4 |   |   | Float |   |   | Delta |   |   |
| 4 |   |   | Unsigned int |   |   | Number of Bands |   |   |
| 4 |   |   | Unsigned int |   |   | Interpolation type |   |   |


**Consistency errors specific to the GetSideBandMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 147 | 001 | 000 | Unknown window |
| 147 | 002 | 000 | Invalid or unavailable display zone type |
| 147 | 003 | 000 | Unknown marker |


<!-- page 70 -->

#### 3.2.30 - "SetHarmonicMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a harmonic marker.

**Command syntax**

```
SetHarmonicMarkerParameters <window name>
<display zone type>
<marker number>
[Start position]
[Number of harmonics]
[color]
[Style line]
Parameters are described in chapter § 3.2.9 - AddHarmonicMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetHarmonicMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 146 | 001 | 000 | Unknown window |
| 146 | 002 | 000 | Invalid or unavailable display zone type |
| 146 | 003 | 000 | Unknown marker |
| 146 | 004 | 000 | Invalid Start position |
| 146 | 005 | 000 | Invalid number of harmonics (<1 or >128) |


<!-- page 71 -->

#### 3.2.31 - "SetHarmonicMarkerVisibility" command


**Semantics**

Allows the user to modify the visibility of a harmonic of a harmonic marker.

**Command syntax**

```
SetHarmonicMarkerVisibility <window name>
<display zone type>
<marker number>
<Harmonic number>
[Show/Hide]
<Harmonic number> specified harmonic you want to change its visibility.
[Show/Hide] (1/0) is set by default to 1 (show).
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetHarmonicMarkerVisibility
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 144 | 001 | 000 | Unknown window |
| 144 | 002 | 000 | Invalid or unavailable display zone type |
| 144 | 003 | 000 | Unknown marker |
| 144 | 004 | 000 | Invalid number of harmonics (<2 or >nb max harmonics) |


<!-- page 72 -->

#### 3.2.32 - "GetHarmonicMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a harmonic marker.

**Command syntax**

```
GetHarmonicMarkerParameters <window name>
<display zone type>
<marker number>
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | Start position |   |   |
| 4 |   |   | Unsigned int |   |   | Number of Harmonics |   |   |
| 4 |   |   | Unsigned int |   |   | Interpolation type |   |   |


**Consistency errors specific to the GetHarmonicMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 148 | 001 | 000 | Unknown window |
| 148 | 002 | 000 | Invalid or unavailable display zone type |
| 148 | 003 | 000 | Unknown marker |


<!-- page 73 -->

#### 3.2.33 - "SetPeriodMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a period marker.

**Command syntax**

```
SetPeriodMarkerParameters <window name>
<display zone type>
<marker number>
[Start position]
[Number of periods]
[Period duration]
[color]
[Style line]
Parameters are described in chapter § 3.2.11 - "AddPeriodMarker" command
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPeriodMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 281 | 001 | 000 | Unknown window |
| 281 | 002 | 000 | Invalid or unavailable display zone type |
| 281 | 003 | 000 | Unknown marker |
| 281 | 004 | 000 | Invalid Start position |
| 281 | 005 | 000 | Invalid number of periods |


<!-- page 74 -->

#### 3.2.34 - "SetPeriodMarkerVisibility" command


**Semantics**

Allows the user to modify the visibility of a harmonic of a harmonic marker.

**Command syntax**

```
SetPeriodMarkerVisibility <window name>
<display zone type>
<marker number>
<Period number>
[Show/Hide]
<Period number> specified period you want to change its visibility.
[Show/Hide] (1/0) is set by default to 1 (show).
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPeriodMarkerVisibility
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 280 | 001 | 000 | Unknown window |
| 280 | 002 | 000 | Invalid or unavailable display zone type |
| 280 | 003 | 000 | Unknown marker |
| 280 | 004 | 000 | Invalid period number |


<!-- page 75 -->

#### 3.2.35 - "SetKinematicMarkerParameters" command


**Semantics**

Allows the user to modify the parameters of a kinematic marker.

**Command syntax**

```
SetKinematicMarkerParameters <window name>
<display zone type>
<marker number>
[position]
[color]
[Style line]
<marker number> parameter identifies the free marker you want to change
parameters.
Other parameters are described in chapter § 3.2.4 - AddFreeMarker.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetFreeMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 044 | 001 | 000 | Unknown window |
| 044 | 002 | 000 | Invalid or unavailable display zone type |
| 044 | 003 | 000 | Unknown marker |
| 044 | 004 | 000 | Invalid position |


<!-- page 76 -->

#### 3.2.36 - "GetPeriodMarkerParameters" command


**Semantics**

Allows the user to get the parameters of a period marker.

**Command syntax**

```
GetPeriodMarkerParameters <window name>
<display zone type>
<marker number>
```

**Result returned**

Data returned is composed of following fields:

|   | Size (bytes) |   |   | Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Float |   |   | Start position |   |   |
| 4 |   |   | Unsigned int |   |   | Number of periods |   |   |
| 4 |   |   | Float |   |   | Period |   |   |


**Consistency errors specific to the GetPeriodMarkerParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 282 | 001 | 000 | Unknown window |
| 282 | 002 | 000 | Invalid or unavailable display zone type |
| 282 | 003 | 000 | Unknown marker |


<!-- page 77 -->

#### 3.2.37 - "GetFreeMarkerValue" command


**Semantics**

Allows the user to get the values of free markers defined in a display zone of a
window.

**Command syntax**

```
GetFreeMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows to get the value of one
marker.
The [Get details] flag allows to select the marker's information you want to
retrieve (see free marker info description below). Set the flag to 1 to get all
information. Set to 0 to get only marker value. A value different from 0 or 1 is
interpreted as a 0. This parameter is optional. Its default value is 0.
```

**Result returned**

A list of free marker info. Each free marker info is separated from the next one
by the minus character '-'.
A free marker info consists of the following fields:

|   | Size |   | Type | Description |   |
|---|---|---|---|---|---|
|   | (bytes) |   |   |   |   |
| 4 |   |   | Unsigned int | Marker number |   |
| 2 |   |   | Unsigned short | It defines the trace on which the marker is applied:<br>0: the marker is applied on all traces of the zone<br>1: the marker is applied on the active trace of the<br>zone<br>2: the marker is applied on a specific trace,<br>which is described by the result description which<br>follows. |   |
| X |   |   | String ending in<br>the character \0. | Marker label<br>Only if "Get details" flag is 1. |   |
| 4 |   |   | Float | Position on X Axis (in S.I. unit)<br>Only if "Get details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number of traces on which the marker is applied |   |
| X |   |   | Result<br>description<br>(see chapter §<br>3.10 - Result<br>format and<br>description<br>) | Trace description<br>Only if "Get details" flag is 1. | For each<br>trace on<br>which<br>the<br>marker is<br>applied |
| 4 |   |   | Float | Y Value of the marker (in S.I. unit) |   |


<!-- page 78 -->

**Consistency errors specific to the GetFreeMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 052 | 001 | 000 | Unknown window |
| 052 | 002 | 000 | Invalid or unavailable display zone type |
| 052 | 003 | 000 | Unknown marker |
| 052 | 004 | 000 | No trace in window |


<!-- page 79 -->

#### 3.2.38 - "GetPeakMarkerValue" command


**Semantics**

Allows the user to get the values of peak markers defined in a display zone of a
window.

**Command syntax**

```
GetPeakMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows getting the value of
one marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Examples**

```
GetPeakMarkerValue Window1 4 2 1 v=1
returns the complete information (including damping ratio, if present) about
the second peak marker displayed in Window1.
GetPeakMarkerValue Window1 4 2 1
GetPeakMarkerValue Window1 4 2 1 v=0
returns the complete information (but not including damping ratio) about the
second peak marker displayed in Window1.
```

**Result returned**

A list of peak marker info. Each peak marker info is separated from the next one
by the minus character '-'.
A peak marker info consists of the following fields:

<!-- page 80 -->

|   | Size (bytes) |   |   | Type |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|
| 4 |   |   | Unsigned int |   |   | Marker number |   |   |   |
| 2 |   |   | Unsigned short |   |   | It defines the trace on which the marker is applied:<br>0: the marker is applied on all traces of the zone<br>1: the marker is applied on the active trace of the<br>zone<br>2: the marker is applied on a specific trace,<br>which is described by the result description which<br>follows. |   |   |   |
| 4 |   |   | Float |   |   | Threshold - Only if "Get details" flag is 1. |   |   |   |
| 4 |   |   | Float |   |   | Absolute threshold - Only if "Get details" flag is<br>1. |   |   |   |
| 4 |   |   | Unsigned int |   |   | Maximum number of peak - Only if "Get details"<br>flag is 1. |   |   |   |
| 4 |   |   | Unsigned int |   |   | Number of traces on which the marker is applied |   |   |   |
| X |   |   | Result<br>description<br>(see chapter §<br>3.10 - Result<br>format and<br>description<br>) |   |   | Trace description<br>Only if "Get details" flag is 1. |   | For each<br>trace on<br>which<br>the<br>marker is<br>applied |   |
| 4 |   |   | Unsigned int |   |   | Number of peak |   |   |   |
| 4 *2 *<br>Number of<br>peak |   |   | List of couple<br>of float |   |   | For each peak, one couple composed<br>of position (on X Axis) and value of<br>the peak (on Y axis). |   |   |   |
| If version parameter is >= 1, and NVGate version is 9.10 or upper |   |   |   |   |   |   |   |   |   |
| 1 |   |   | Boolean |   |   | Display damping ratio - Only if "Get details" flag<br>is 1. |   |   |   |
| 4 |   |   | Unsigned int |   |   | Number of damping ratio |   | For each<br>trace on<br>which<br>the<br>marker is<br>applied |   |
| 4*Number<br>of ratio |   |   | List of float |   |   | Damping ratio values |   |   |   |


<!-- page 81 -->

**Consistency errors specific to the GetPeakMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 053 | 001 | 000 | Unknown window |
| 053 | 002 | 000 | Invalid or unavailable display zone type |
| 053 | 003 | 000 | Unknown marker |
| 053 | 004 | 000 | No trace in window |


<!-- page 82 -->

#### 3.2.39 - "GetMaxMarkerValue" command


**Semantics**

Allows the user to get the values of max markers defined in a display zone of a
window.

**Command syntax**

```
GetMaxMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows to get the value of one
marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Examples**

```
GetMaxMarkerValue Window1 4 2 1 v=1
returns the complete information (including damping ratio, if present) about
the second max marker displayed in Window1.
```

**Result returned**

A list of max marker info. Each max marker info is separated from the next one
by the minus character '-'. A max marker info is similar to peak marker info (see
§ 3.2.38 - GetPeakMarkerValue).

**Consistency errors specific to the GetMaxMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 054 | 001 | 000 | Unknown window |
| 054 | 002 | 000 | Invalid or unavailable display zone type |
| 054 | 003 | 000 | Unknown marker |
| 054 | 004 | 000 | No trace in window |


<!-- page 83 -->

#### 3.2.40 - "GetPowerBandMarkerValue" command


**Semantics**

Allows the user to get the values of power band markers defined in a display zone
of a window.

**Command syntax**

```
GetPowerBandMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows to get the value of one
marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Result returned**

A list of power band marker info. Each power band marker info is separated
from the next one by the minus character '-'.
Band marker info consists of the following fields:

| Size<br>(bytes) |   | Type | Description |   |
|---|---|---|---|---|
| 4 |   | Unsigned int | Marker number |   |
| 2 |   | Unsigned short | It defines the trace on which the marker is applied :<br>0 : the marker is applied on all traces of the zone<br>1 : the marker is applied on the active trace of the<br>zone<br>2 : the marker is applied on a specific trace, which<br>is described by the result description which follows. |   |
| 4 |   | Float | Start position - Only if "Get details" flag is 1. |   |
| 4 |   | Float | Delta - Only if "Get details" flag is 1. |   |
| 4 |   | Unsigned int | Number or traces on which the marker is applied |   |
| X |   | Result<br>description<br>(see chapter §<br>3.10 - Result<br>format and<br>description<br>) | Trace description<br>Only if "Get details" flag is 1. | For each<br>trace on<br>which the<br>marker is<br>applied |
| 4 |   | Float | Power (in S.I. unit) |   |


**Consistency errors specific to the GetPowerBandMarkerValue
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 055 | 001 | 000 | Unknown window |
| 055 | 002 | 000 | Invalid or unavailable display zone type |
| 055 | 003 | 000 | Unknown marker |
| 055 | 004 | 000 | No trace in window |


<!-- page 84 -->

#### 3.2.41 - "GetSideBandMarkerValue" command


**Semantics**

Allows the user to get the values of side band markers defined in a display zone of
a window.

**Command syntax**

```
GetSideBandMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows to get the value of one
marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Result returned**

A list of side band marker info. Each side band marker info is separated from
the next one by the minus character '-'.
Band marker info.consists of the following fields:

|   | Size |   | Type | Description |   |
|---|---|---|---|---|---|
|   | (bytes) |   |   |   |   |
| 4 |   |   | Unsigned int | Marker number |   |
| 2 |   |   | Unsigned short | It defines the trace on which the marker is applied<br>:<br>0 : the marker is applied on all traces of the zone<br>1 : the marker is applied on the active trace of the<br>zone<br>2 : the marker is applied on a specific trace,<br>which is described by the result description which<br>follows. |   |
| 4 |   |   | Float | Start position - Only if "Get details" flag is 1. |   |
| 4 |   |   | Float | Delta - Only if "Get details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number of bands- Only if "Get details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number or traces on which the marker is applied |   |
| X |   |   | Result<br>description<br>(see chapter §<br>3.10 - Result<br>format and<br>description<br>) | Trace description<br>Only if "Get details" flag is 1. | For each<br>trace on<br>which the<br>marker is<br>applied |
| 4 |   |   | Float | X Start position |   |
| 4 |   |   | Float | Y Start position |   |
| 4 |   |   | Unsigned int | Number of left bands |   |


<!-- page 85 -->

| 4 *2 *<br>Number<br>of left<br>bands | List of couple of<br>float | For each left band, one couple<br>composed of position (on X Axis)<br>and value of the left band (on Y<br>axis). |   |
|---|---|---|---|
| 4 | Unsigned int | Number of right bands |   |
| 4 *2 *<br>Number<br>of right<br>bands | List of couple of<br>float | For each right band, one couple<br>composed of position (on X Axis)<br>and value of the right band (on Y<br>axis). |   |


**Consistency errors specific to the GetSideBandMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 149 | 001 | 000 | Unknown window |
| 149 | 002 | 000 | Invalid or unavailable display zone type |
| 149 | 003 | 000 | Unknown marker |
| 149 | 004 | 000 | No trace in window |


<!-- page 86 -->

#### 3.2.42 - "GetHarmonicMarkerValue" command


**Semantics**

Allows the user to get the values of harmonic markers defined in a display zone of
a window.

**Command syntax**

```
GetHarmonicMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows to get the value of one
marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Result returned**

A list of harmonic marker info. Each harmonic marker info is separated from
the next one by the minus character '-'.Harmonic marker info consists of the
following fields:

|   | Size |   | Type | Description |   |
|---|---|---|---|---|---|
|   | (bytes) |   |   |   |   |
| 4 |   |   | Unsigned int | Marker number |   |
| 2 |   |   | Unsigned short | It defines the trace on which the marker is<br>applied :<br>0 : the marker is applied on all traces of the<br>zone<br>1 : the marker is applied on the active trace of<br>the zone<br>2 : the marker is applied on a specific trace,<br>which is described by the result description<br>which follows. |   |
| 4 |   |   | Float | Start position - Only if "Get details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number of max harmonics - Only if "Get<br>details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number of max visible harmonics - Only if "Get<br>details" flag is 1. |   |
| 4 |   |   | Unsigned int | Number or traces on which the marker is applied |   |
| X |   |   | Result<br>description<br>(see chapter §<br>3.10 - Result<br>format and<br>description<br>) | Trace description<br>Only if "Get details" flag is 1. | For each<br>trace on<br>which the<br>marker is<br>applied |
| 4 |   |   | Float | X Start position |   |
| 4 |   |   | Float | Y Start position |   |
| 4 |   |   | Unsigned int | Number of harmonics |   |


<!-- page 87 -->

| 4 *2 *<br>Number of<br>harmonics | List of couple<br>of float | For each harmonic, one couple<br>composed of position (on X Axis)<br>and value of the harmonic (on Y<br>axis). |   |
|---|---|---|---|


**Consistency errors specific to the GetHarmonicMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 150 | 001 | 000 | Unknown window |
| 150 | 002 | 000 | Invalid or unavailable display zone type |
| 150 | 003 | 000 | Unknown marker |
| 150 | 004 | 000 | No trace in window |


<!-- page 88 -->

#### 3.2.43 - "GetPeriodMarkerValue" command


**Semantics**

Allows the user to get the values of period markers defined in a display zone of a
window.

**Command syntax**

```
GetPeriodMarkerValue <window name>
<display zone type>
[marker number]
[Get details]
The [marker number] parameter is optional. It allows getting the value of
one marker.
For [Get details] flag description, see § 3.2.37 - GetFreeMarkerValue.
```

**Result returned**

A list of period marker info. Each period marker info is separated from the next
one by the minus character '-'. Period marker info consists of the following
fields:

|   | Size |   | Type |   |   | Description |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
|   | (bytes) |   |   |   |   |   |   |   |   |
| 4 |   |   | Unsigned int |   |   | Marker number |   |   |   |
| 2 |   |   | Unsigned short |   |   | It defines the trace on which the marker is<br>applied :<br>0 : the marker is applied on all traces of the<br>zone<br>1 : the marker is applied on the active trace of<br>the zone<br>2 : the marker is applied on a specific trace,<br>which is described by the result description<br>which follows. |   |   |   |
|   | 4 |   |   | Float |   |   | Start position - Only if "Get details" flag is 1. |   |   |
| 4 | 4 |   | Unsigned int | Unsigned int |   |   | Max number of periods - Only if "Get details" |   |   |
|   |   |   |   |   |   |   | flag is 1. |   |   |
| 4 |   |   | Unsigned int |   |   | Number of traces on which the marker is applied |   |   |   |
| X |   |   |   | Result |   | Trace description<br>Only if "Get details" flag is 1. |   | For each<br>trace on<br>which the<br>marker is<br>applied |   |
|   |   |   |   | description |   |   |   |   |   |
|   |   |   |   | (see chapter § |   |   |   |   |   |
|   |   |   |   | 3.10 - Result |   |   |   |   |   |
|   |   |   |   | format and |   |   |   |   |   |
|   |   |   |   | description |   |   |   |   |   |
|   |   |   |   | ) |   |   |   |   |   |
| 4 |   |   | Float |   |   | X Start position |   |   |   |
| 4 |   |   | Float |   |   | Y Start position |   |   |   |
| 4 |   |   | Unsigned int |   |   | Number of periods |   |   |   |


**Trace description**

| Column 1 |
|---|
| Only if "Get details" flag is 1. |


<!-- page 89 -->

| 4 *2 *<br>Number of<br>periods | List of couple<br>of float | For each period, one couple<br>composed of position (on X Axis)<br>and value on the curve (on Y axis). |   |
|---|---|---|---|


**Consistency errors specific to the GetPeriodMarkerValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 283 | 001 | 000 | Unknown window |
| 283 | 002 | 000 | Invalid or unavailable display zone type |
| 283 | 003 | 000 | Unknown marker |
| 283 | 004 | 000 | No trace in window |


<!-- page 90 -->

### 3.3 - GRAPHICS


#### 3.3.1 - "AddWindowResult" command


**Semantics**

Creates a result window (not 3D waterfall result).

**Command syntax**

```
AddWindowResult <layout name>
<window name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[ArrangeWindow]
[Maximize / minimize]
[2D_Waterfall]
[ExistingResultIsAnError]
The "AddWindowResult" parameters are the <layout name> and the
<window name>, as well as the result description components. If the specified
layout does not exist, it is created. If the specified window does not exist, it is
created.
The "operator" identifiers are described in the Appendix.
The default value for the [Weighting operator] is 0 (no operator).
The default value for the [Time operator] is 0 (no operator).
The default value for the [Display unit] is 0 (no operator).
The tables giving the numbers of the weighting and time operators and the display
units are presented in section 3.10 - Result format and description
.
The optional parameter, [ArrangeWindow], lets you arrange the layout
windows, once the new window has been created. The possible values for this
parameter are listed in section 3.3.28 - "ArrangeWindows" command.
If another value is specified, the parameter is ignored and a consistency error (see
table) is returned. The default value is the user preference.
The optional parameter [Maximize / minimize] lets you maximize or
minimize the window. The possible values are
0 Normal (default value)
1 Minimize
2 Maximize
```

<!-- page 91 -->
```
The optional parameter [2D_Waterfall] lets you determine if the result is a
2D waterfall one (a scalar result displayed in function of time). For a 3D
Waterfall, please use the AddWindowWtfResult command. The possible values
are
0 Normal (default value)
1 2D waterfall result.
The optional parameter [ExistingResultIsAnError] lets you determine
if the selected result already displayed in the selected window is considered as an
error. The possible values are
0 not an error (default value)
1 considered as an error
Choosing 1 for this parameter enables to get the error code = 016015000.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddWindowResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 016 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 016 | 002 | 000 | Number of a module not supplying a result |
| 016 | 003 | 000 | Process number incorrect |
| 016 | 004 | 000 | Channel number incorrect |
| 016 | 005 | 000 | Reference channel number incorrect |
| 016 | 006 | 000 | Weighting operator unknown |
| 016 | 007 | 000 | No weighting for non-spectrum results |
| 016 | 008 | 000 | Result already weighted |
| 016 | 009 | 000 | Time operator unknown |
| 016 | 010 | 000 | Display unit unknown |
| 016 | 011 | 000 | Window cannot be created for the specified result |
| 016 | 012 | 000 | Specified result and window incompatible (when the<br>specified window already exists) |
| 016 | 013 | 000 | Value for the ArrangeWindow parameter incorrect |
| 016 | 014 | 000 |   |
| 016 | 015 | 000 | The specified result is already displayed in the specified<br>window |


<!-- page 92 -->

#### 3.3.2 - "AddWindowPlayerResult" command


**Semantics**

Creates a preview window containing signal file track(s).

**Command syntax**

```
AddWindowPlayerResult <layout name>
<Window name>
<Project name>
<Measurement name>
[Nothing]
[Track]
[ArrangeWindow]
[Maximize / minimize]
The "AddWindowPlayerResult" parameters are the <layout name> and
the <window name>, as well as <Project name> and <Measurement
name> where the signal is located. If the specified layout does not exist, it is
created. If the specified window does not exist, it is created.
The optional parameter, [Nothing], is unused (must be set it to 0 if following
optional parameters are added).
The optional parameter, [Track], lets you select the signal track number to
display. By default, this parameter is set to -1 and all signal tracks are displayed.
The optional parameter, [ArrangeWindow], lets you arrange the layout
windows, once the new window has been created. The possible values for this
parameter are
0 (Horizontal tile)
1 (Vertical tile)
2 (Cascade).
The optional parameter [Maximize / minimize] lets you maximize or
minimize the window. The possible values are
0 Normal
1 Minimize
2 Maximize
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddWindowPlayerResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 105 | 001 | 000 | Window cannot be created |
| 105 | 002 | 000 | The preview window already exists. |
| 105 | 003 | 000 | Unknown Project |
| 105 | 004 | 000 | Unknown Measurement |


<!-- page 93 -->

#### 3.3.3 - "AddWindowSavedResult" command


**Semantics**

Creates a new result window / Add a file result to an already existing window.

**Command syntax**

```
AddWindowSavedResult <layout name>
<window name>
<project name>
<measurement name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[ArrangeWindow]
[Maximize / minimize]
[Waterfall / No waterfall]
The parameters are the same as for the 3.3.1 - AddWindowResult command, plus
the project name, the measurement name and the waterfall type.
The optional parameter [Waterfall] lets you determine if the result to be
displayed is a waterfall one (2D or 3D). The possible values are
-1 Default value, get the first result matching the others parameters
0 Search for a non-waterfall result in the measure
1 Search for a waterfall result in the measure.
The tables giving the numbers of the [Weighting operator, [Time
operator]and the[Display unit] is presented in section 3.10 - Result
format and description
.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddWindowSavedResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 021 | 001 | 000 | Project unknown |
| 021 | 002 | 000 | Measurement unknown |
| 021 | 003 | 000 | Process number incorrect |
| 021 | 004 | 000 | Channel number incorrect |
| 021 | 005 | 000 | Reference channel number incorrect |
| 021 | 006 | 000 | Result unknown |
| 021 | 007 | 000 | Weighting operator unknown |
| 021 | 008 | 000 | Time operator unknown |
| 021 | 009 | 000 | Display unit unknown |
| 021 | 010 | 000 | Window cannot be created for the specified result |


<!-- page 94 -->

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
|   | 011 | 000 | Specified result and window incompatible (when the<br>specified window already exists) |
|   | 012 | 000 | Value for the ArrangeWindow parameter incorrect |
|   | 013 | 000 | Value for Maximize / minimize parameter incorrect |
|   | 014 | 000 | Invalid Waterfall parameter, must be 0 (by default) or 1 |


<!-- page 95 -->

#### 3.3.4 - "AddWindowWtfResult" command


**Semantics**

Creates a 3D waterfall result window.

**Command syntax**

```
AddWindowWtfResult <layout name>
<window name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[ArrangeWindow]
[Maximize / minimize]
The parameters are the same as for the 3.3.1 - AddWindowResult command,
except the 2D_Waterfall parameter.
The <Module number> is the Waterfall source module (not the waterfall
module).
The tables giving the numbers of the [Weighting operator, [Time
operator]and the[Display unit] is presented in section 3.10 - Result
format and description
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddWindowWtfResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 089 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 089 | 002 | 000 | Number of a module not supplying a result |
| 089 | 003 | 000 | Process number incorrect |
| 089 | 004 | 000 | Channel number incorrect |
| 089 | 005 | 000 | Reference channel number incorrect |
| 089 | 006 | 000 | Weighting operator unknown |
| 089 | 007 | 000 | No weighting for non-spectrum results |
| 089 | 008 | 000 | Result already weighted |
| 089 | 009 | 000 | Time operator unknown |
| 089 | 010 | 000 | Display unit unknown |
| 089 | 011 | 000 | Window cannot be created for the specified result |
| 089 | 012 | 000 | Specified result and window incompatible (when the<br>specified window already exists) |
| 089 | 013 | 000 | Value for the ArrangeWindow parameter incorrect |


<!-- page 96 -->

#### 3.3.5 - "AddWindowZoomedSignal" command


**Semantics**

Creates a window displaying a track being recorded or a track from a measurement.
This command is available since NVGate V17.00.

**Command syntax**

```
AddWindowZoomedSignal <layout name>
<Window name>
<Track nb>
<Begin>
<End>
[Project name]
[Measurement name]
The "AddWindowZoomedSignal" parameters are the <layout name> and
the <window name>, as well as <Track nb>, starting from 1 to n if one track
selected, or -1 for all. <Begin> and <End> defined the desired time range, in
seconds. If the specified layout does not exist, it is created. If the specified
window does not exist, it is created.
The optional parameter, [Projet name] and [Measurement name] lets
you select another measurement than the recording one. If they are not used, the
zoom signal come from the recording signal.
When you display a signal being recorded, you must first display the whole signal
with AddWindowResult Layout1 Recorder 3 30 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddWindowZoomedSignal command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 395 | 001 | 000 | Window cannot be created |
| 395 | 002 | 000 | The zoom window already exists. |
| 395 | 003 | 000 | Recorder is not running |
| 395 | 004 | 000 | Unknown recorder state |
| 395 | 005 | 000 | Begin or end cannot be greater than total duration |
| 395 | 006 | 000 | Begin and end are not consistent |
| 395 | 007 | 000 | Zoom impossible on given track |
| 395 | 008 | 000 | Unknown Project |
| 395 | 009 | 000 | Unknown Measurement |
| 395 | 010 | 000 | Project or Measurement inconsistent |


<!-- page 97 -->

#### 3.3.6 - "RenameWindow" command


**Semantics**

Allows the user to rename a window.

**Command syntax**

```
RenameWindow <layout name>
<window name>
<new window name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RenameWindow command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 264 | 001 | 000 | Layout unknown |
| 264 | 002 | 000 | Window unknown |
| 264 | 003 | 000 | New name already used |


<!-- page 98 -->

#### 3.3.7 - "SetLayout" command


**Semantics**

Allows the user to activate a workbook layout for the current project.

**Command syntax**

```
SetLayout <layout name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 011 | 001 | 000 | Layout unknown |


<!-- page 99 -->

#### 3.3.8 - "NewLayout" command


**Semantics**

Creates a new layout

**Command syntax**

```
NewLayout <layout name>
[BecomeCurrent flag]
The name of the new <layout name> is passed as a parameter.
If the [BecomeCurrent flag] flag is set at 1, the new layout will become
the current layout. It is set at 0 by default.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the NewLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 017 | 001 | 000 | Layout already existing |
| 017 | 002 | 000 | Value incorrect for the BecomeCurrent flag (0 or 1<br>expected) |


<!-- page 100 -->

#### 3.3.9 - "RemoveLayout" command


**Semantics**

Creates a new layout

**Command syntax**

```
RemoveLayout <layout name>
The name of the <layout name> to remove is passed as a parameter.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 017 | 001 | 000 | Layout not found |
| 017 | 002 | 000 | There is only one layout in the current workbook |
| 017 | 003 | 000 | Error removing layout |


<!-- page 101 -->

#### 3.3.10 - "RenameLayout" command


**Semantics**

Rename an existing layout

**Command syntax**

```
RenameLayout <current layout name> <new layout name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 317 | 001 | 000 | Layout not found |
| 317 | 002 | 000 | There is already a layout named "new layout name" |
| 317 | 003 | 000 | Unknown Error while renaming layout |


<!-- page 102 -->

#### 3.3.11 - "GetLayoutList" command


**Semantics**

Retrieves the list of the layouts of the current project

**Command syntax**

```
GetLayoutList
```

**Result returned**

The list of project names follows the header. Each name is returned in the form of
an ASCII character string ending in the character \0.

<!-- page 103 -->

#### 3.3.12 - "GetCurrentLayout" command


**Semantics**

Retrieves the name of the current Layout.

**Command syntax**

```
GetCurrentLayout
```

**Result returned**

The header contains the size of the layout name and is followed by the current
layout name.

**Consistency errors specific to the GetCurrentLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 163 | 001 | 000 | There is no layout. |


<!-- page 104 -->

#### 3.3.13 - "MaskAllToolbar" command


**Semantics**

Masks all the toolbars and dockable windows of NVGate.

**Command syntax**

```
MaskAllToolbar [DontMaskToolbar]
[DontMaskDockableWindow]
If the optional parameter [DontMaskToolbar] equals 1, the toolbars are not
masked. Its default value is 0.
If the optional parameter [DontMaskDockableWindow] equals 1, the
dockable windows are not masked. Its default value is 0.
```

**Result returned**

No data follows the header.

<!-- page 105 -->

#### 3.3.14 - "SetActiveWindow" command


**Semantics**

Allows the user to activate a window from a layout for the current project.

**Command syntax**

```
SetActiveWindow <layout name>
<window name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetLayout command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 194 | 001 | 000 | Layout unknown |
| 194 | 002 | 000 | Window unknown |


<!-- page 106 -->

#### 3.3.15 - "GetActiveWindow" command


**Semantics**

Return the name of the active result window.

**Command syntax**

```
GetActiveWindow
```

**Result returned**

The name of the active graphic window (string ending in the character \0.).
If no result window is displayed, no data follows the header.

<!-- page 107 -->

#### 3.3.16 - "GetWindowList" command


**Semantics**

Return names of result windows containing a given result.

**Command syntax**

```
GetWindowList <Module number>
<Process number>
<Channel number >
[Reference channel number]
The GetWindowList parameters are the components of a result description.
The [Reference channel number] is an optional parameter.
```

**Result returned**

A list of strings. Each string ends in the character \0 and is the name of a result
window containing the result specified.
If there is no error, the data block following the header represents a measurement
result. The data are divided into blocks. Section 3.10 - Result format and
description
presents the format of the various result types.

**Consistency errors specific to the GetWindowList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 059 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 059 | 002 | 000 | Number of a module not supplying a result |
| 059 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 059 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 059 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |


<!-- page 108 -->

#### 3.3.17 - "GetWindowNameList" command


**Semantics**

Return names of all windows of the selected layout.

**Command syntax**

```
GetWindowNameList [Layout name]
The [Layout name] is an optional parameter. By default, the current layout is
considered.
```

**Result returned**

A list of strings. Each string ends in the character \0 and is the name of a window.

**Consistency errors specific to the GetWindowNameList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 103 | 001 | 000 | The layout does not exist. |
| 103 | 002 | 000 | Error loading layout |


<!-- page 109 -->

#### 3.3.18 - "GetWindowTraces" command


**Semantics**

Return the list of all traces of the selected window.

**Command syntax**

```
GetWindowTraces <Window name>
The <Window name> parameter specifies the window.
```

**Result returned**

A list of strings. Each string ends in the character \0 and is the trace description.
(see chapter § 3.10 - Result format and description
).

**Consistency errors specific to the GetWindowTraces command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 36 | 001 | 000 | The window does not exist. |


<!-- page 110 -->

#### 3.3.19 - "GetMeasurementWindowTrace" command


**Semantics**

Return project and measurement associated to a specified window trace.

**Command syntax**

```
GetMeasurementWindowTrace <Layout name>
<Window name>
<trace index>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection. The third parameter is an
integer that represents a trace index. The first trace is index 0, the last trace is
<number of traces> - 1.
```

**Result returned**

The header contains the size of the project and measurement name and is followed
by the associated project and measurement name. If the result is not derived from
a saved measurement, it returns empty strings.

**Consistency errors specific to the GetMeasurementWindowTrace
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 378 | 060 1 | 000 | Unknown layout |
| 378 | 002 | 000 | Unknown window |
| 378 | 003 | 000 | Not supported window |
| 378 | 004 | 000 | Bad trace index parameter |


<!-- page 111 -->

#### 3.3.20 - "CloseWindow" command


**Semantics**

Close a result window.

**Command syntax**

```
CloseWindow <layout name>
<window name>
<layout name> and <window name> parameters define the window to
close.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CloseWindow command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 064 | 001 | 000 | Unknown layout |
| 064 | 002 | 000 | Unknown window |


<!-- page 112 -->

#### 3.3.21 - "CloseAllWindows" command


**Semantics**

Close all result windows of a layout.

**Command syntax**

```
CloseAllWindows <layout name>
<layout name> parameters define the layout to empty.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CloseAllWindows command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 161 | 001 | 000 | Unknown layout |


<!-- page 113 -->

#### 3.3.22 - "Autoscale" command


**Semantics**

Autoscale on Y axis or referenced axis of a result window.

**Command syntax**

```
Autoscale <layout name>
<window name>
[axis]
<layout name> and <window name> parameters define the window.
The possible values for [axis] parameter are
- Y Autoscale on Y axis
- Ref Autoscale on referenced axis (X axis for profile and 2D
Waterfall windows, Z axis for 3D waterfall windows)
The values are not case sensitive.
This [axis] parameter is optional; its default value is Y.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Autoscale command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 066 | 001 | 000 | Unknown layout |
| 066 | 002 | 000 | Unknown window |
| 066 | 003 | 000 | Value for "axis" parameter incorrect |


<!-- page 114 -->

#### 3.3.23 - "AutoscaleAllWnd" command


**Semantics**

Autoscale on Y axis or referenced axis of all windows of a layout.

**Command syntax**

```
AutoscaleAllWnd <layout name>
[axis]
<layout name> parameters define the layout.
The possible values for [axis]parameter are
- Y Autoscale on Y axis
- Ref Autoscale on referenced axis (X axis for profile and 2D
Waterfall windows, Z axis for 3D waterfall windows)
The values are not case sensitive.
This [axis] parameter is optional; its default value is Y.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AutoscaleAllWnd command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 108 | 001 | 000 | Unknown layout |
| 108 | 003 | 000 | Value for "axis" parameter incorrect |


<!-- page 115 -->

#### 3.3.24 - "ChangeSpectralWeighting" command


**Semantics**

Change the spectral weighting of a result in a window.

**Command syntax**

```
ChangeSpectralWeighting <layout name>
<window name>
<weighting>
<layout name> and <window name> parameters define the window.
The possible values for <weighting> are detailed in the 3.10.4 - paragraph.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ChangeSpectralWeighting
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 332 | 001 | 000 | Unknown layout |
| 332 | 002 | 000 | Unknown window |
| 332 | 003 | 000 | The weighting cannot be applied to the window |
| 332 | 004 | 000 | The weighting is not valid |


<!-- page 116 -->

#### 3.3.25 - "ChangeDisplayMode" command


**Semantics**

Change the display mode of a window.

**Command syntax**

```
ChangeDisplayMode <layout name>
<window name>
<mode>
<layout name> and <window name> parameters define the window.
The possible values for <mode> parameter are:
```

**Result returned**

No data follows the header.

| Description |   |   | Type of window |   |   | Mode |   |
|---|---|---|---|---|---|---|---|
| Magnitude multitrace |   | Spectrum/Order profile |   |   | 0 |   |   |
| Phase multitrace |   | Spectrum/Order profile |   |   | 1 |   |   |
| Real part multitrace |   | Spectrum/Order profile |   |   | 2 |   |   |
| Imaginary part multitrace |   | Spectrum/Order profile |   |   | 3 |   |   |
| Module phase |   | Spectrum/Order profile |   |   | 4 |   |   |
| Real imaginary |   | Spectrum/Order profile |   |   | 5 |   |   |
| Polar |   | Spectrum |   |   | 6 |   |   |
| Real part 3D |   | Spectrum |   |   | 7 |   |   |
| Imaginary part 3D |   | Spectrum |   |   | 8 |   |   |
| Module 3D |   | Spectrum |   |   | 9 |   |   |
| Phase 3D |   | Spectrum |   |   | 10 |   |   |
| Real part multigraph |   | Spectrum/Order profile |   |   | 11 |   |   |
| Imaginary part multigraph |   | Spectrum/Order profile |   |   | 12 |   |   |
| Module multigraph |   | Spectrum/Order profile |   |   | 13 |   |   |
| Phase multigraph |   | Spectrum/Order profile |   |   | 14 |   |   |
| Phase module |   | Spectrum/Order profile |   |   | 31 |   |   |
| Multitrace |   | Time |   |   | 15 |   |   |
| Multigraph |   | Time |   |   | 16 |   |   |
| 3D |   | Time |   |   | 17 |   |   |
| Multitrace |   | Octave |   |   | 18 |   |   |
| Multigraph |   | Octave |   |   | 19 |   |   |
| Multitrace |   | Profile |   |   | 26 |   |   |
| Multigraph |   | Profile |   |   | 27 |   |   |
| Polar, merged Module + Phase |   | Spectrum/Order profile |   |   | 32 |   |   |
| Viewmeter |   | Scalar |   |   | 50 |   |   |
| Brick |   | Scalar |   |   | 51 |   |   |
| Continuous |   | Scalar |   |   | 52 |   |   |
| Digital |   | Scalar |   |   | 53 |   |   |
| Module + Phase |   | Scalar |   |   | 54 |   |   |


**Consistency errors specific to the ChangeDisplayMode command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 078 | 001 | 000 | Unknown layout |
| 078 | 002 | 000 | Unknown window |
| 078 | 003 | 000 | The mode is not valid for the window |


<!-- page 117 -->

#### 3.3.26 - "GetDisplayMode" command


**Semantics**

Get the current display mode of a window.

**Command syntax**

```
GetDisplayMode <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

An integer that represents a display mode (see Description of displays mode §

#### 3.3.24 - ChangeDisplayMode).


**Consistency errors specific to the GetDisplayMode command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 271 | 001 | 000 | Unknown layout |
| 271 | 002 | 000 | Unknown window |


<!-- page 118 -->

#### 3.3.27 - "GetDisplayModeList" command


**Semantics**

Get the display mode available list of a window.

**Command syntax**

```
GetDisplayModeList <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

A list of ints. Each int represents a display mode (see Description of displays
mode § 3.3.24 - ChangeDisplayMode).

**Consistency errors specific to the GetDisplayModeList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 140 | 001 | 000 | Unknown layout |
| 140 | 002 | 000 | Unknown window |


<!-- page 119 -->

#### 3.3.28 - "ArrangeWindows" command


**Semantics**

Execute a tile of the windows of the current layout.

**Command syntax**

```
ArrangeWindows <Tile Style>
<Tile Style> can have the following values:
```

**Result returned**

No data follows the header.

| Description |   |   | Number |   |
|---|---|---|---|---|
| No tile: the windows keep their positions |   | -1 |   |   |
| Tile horizontally |   | 0 |   |   |
| Tile vertically |   | 1 |   |   |
| Cascade |   | 2 |   |   |
| Automatic tile |   | 3 |   |   |
| Grid |   | 4 |   |   |


**Consistency errors specific to the ArrangeWindows command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 076 | 001 | 000 | Unknown Tile style |


<!-- page 120 -->

#### 3.3.29 - "GroupByMagnitude" command


**Semantics**

Enables to display curves grouped by magnitude when displayed in multi-trace
mode.

**Command syntax**

```
GroupByMagnitude <Layout name>
<Window name>
<Grouped>
<Layout name> and <Window name> parameters define the window.
<Grouped> parameter is 1 for grouping curves or 0 for not grouping curves.
```

**Result returned**

No data follows the header

**Consistency errors specific to the GroupByMagnitude command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 302 | 001 | 000 | Unknown layout |
| 302 | 002 | 000 | Unknown window |


<!-- page 121 -->

#### 3.3.30 - "OpenCloseInfoTrace" command


**Semantics**

Open or close the info trace of the selected window.

**Command syntax**

```
OpenCloseInfoTrace <window name>
<open flag>
The <window name> must be a window of the current project.
The <open flag> defines if the InfoTrace will be opened (flag = 1) or closed
(flag = 0). If a command asks for opening a window which is already opened, the
header will be 0 (= no error) and nothing is done.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the OpenCloseInfoTrace command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 098 | 001 | 000 | Unknown window |


<!-- page 122 -->

#### 3.3.31 - "MemorizeTrace" command


**Semantics**

Memorize the active trace of a result window.

**Command syntax**

```
MemorizeTrace <layout name>
<window name>
<layout name> and <window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the MemorizeTrace command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 121 | 001 | 000 | Unknown layout |
| 121 | 002 | 000 | Unknown window |


<!-- page 123 -->

#### 3.3.32 - "RemoveTrace" command


**Semantics**

Remove a trace of a result window in the current layout.

**Command syntax**

```
RemoveTrace <window name>
<trace number>
<window name> parameter defines the window.
<trace number> defines the signal to remove from the window. For the first
Signal, trace number = 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveTrace command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 138 | 001 | 000 | Unknown window |
| 138 | 002 | 000 | Trace number is not valid (must be between 1 and the<br>number of signals) |


<!-- page 124 -->

#### 3.3.33 - "ClearMemory" command


**Semantics**

Clear all memorized traces of a result window.

**Command syntax**

```
ClearMemory <layout name>
<window name>
<layout name> and <window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ClearMemory command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 209 | 001 | 000 | Unknown layout |
| 209 | 002 | 000 | Unknown window |


<!-- page 125 -->

#### 3.3.34 - "CascadeView" command


**Semantics**

Activate cascade view or return to usual view.

**Command syntax**

```
CascadeView <layout name>
<window name>
<layout name> and <window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CascadeView command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 129 | 001 | 000 | Unknown layout |
| 129 | 002 | 000 | Unknown window |


<!-- page 126 -->

#### 3.3.35 - "AddResultAutoMemorize" command


**Semantics**

Add an existing result of a window to be AutoMemorize

**Command syntax**

```
AddResultAutoMemorize <layout name>
<window name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[2D_Waterfall]
The parameters are the same as for the 3.3.1 - AddWindowResult command.
The tables giving the numbers of the weighting and time operators and
the display units is presented in section 3.10 - Result format and
description
.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddResultAutoMemorize command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 132 | 001 | 000 | Layout unknown |
| 132 | 002 | 000 | Window unknown |
| 132 | 003 | 000 | Module number incorrect |
| 132 | 004 | 000 | Number of a module not supplying a result |
| 132 | 005 | 000 | Process number incorrect |
| 132 | 006 | 000 | Channel number incorrect |
| 132 | 007 | 000 | Reference channel number incorrect |
| 132 | 008 | 000 | Weighting operator unknown |
| 132 | 009 | 000 | No weighting for non-spectrum results |
| 132 | 010 | 000 | Result already weighted |
| 132 | 011 | 000 | Time operator unknown |
| 132 | 012 | 000 | Display unit unknown |
| 132 | 013 | 000 | Window cannot be created for the specified result |
| 132 | 014 | 000 | Result already in AutoMemorize |


<!-- page 127 -->

#### 3.3.36 - "RemoveResultAutoMemorize" command


**Semantics**

Remove an existing result of a window in AutoMemorize

**Command syntax**

```
RemoveResultAutoMemorize <layout name>
<window name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[2D_Waterfall]
The parameters are the same as for the 3.3.35 - AddResultAutoMemorize.
command.
The tables giving the numbers of the weighting and time operators and
the display units is presented in section 3.10 - Result format and
description
.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveResultAutoMemorize
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 133 | 001 | 000 | Layout unknown |
| 133 | 002 | 000 | Window unknown |
| 133 | 003 | 000 | Module number incorrect |
| 133 | 004 | 000 | Number of a module not supplying a result |
| 133 | 005 | 000 | Process number incorrect |
| 133 | 006 | 000 | Channel number incorrect |
| 133 | 007 | 000 | Reference channel number incorrect |
| 133 | 008 | 000 | Weighting operator unknown |
| 133 | 009 | 000 | No weighting for non-spectrum results |
| 133 | 010 | 000 | Result already weighted |
| 133 | 011 | 000 | Time operator unknown |
| 133 | 012 | 000 | Display unit unknown |
| 133 | 013 | 000 | Window cannot be created for the specified result |
| 133 | 014 | 000 | Result not in AutoMemorize |


<!-- page 128 -->

#### 3.3.37 - "EnableAutoMemorize" command


**Semantics**

Add (enable) or remove (disable) a window from the list of windows to memorize
on a stop event.

**Command syntax**

```
EnableAutoMemorize <layout name>
<window name>
[enable]
<layout name> and <window name> parameters define the window.
[enable] is an optional parameter that adds (if = 1) or removes (if = 0) the
described window from the selection of automatic memorization. By default, the
value is set to 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the EnableAutoMemorize command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 134 | 001 | 000 | Unknown layout |
| 134 | 002 | 000 | Unknown window |
| 134 | 003 | 000 | The selected window is already enabled or disabled. |


<!-- page 129 -->

#### 3.3.38 - "AddAutoOperator" command


**Semantics**

Add an automatic operator referenced by an existing result in a window.

**Command syntax**

```
AddAutoOperator <Layout name>
<Window name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[2D_Waterfall]
[Average type]
[Automatic selection type]
[Operator Name]
[Frequency domain]
[Step]
The 10 first parameters are the same as for the 3.3.1 - AddWindowResult
command.
The tables giving the numbers of the weighting and time operators and
the display units is presented in section 3.10 - Result format and
description
. They define the operand source.
[Average type] defines the operator average type. Possible values are:
- 0 for Arithmetic average
- 1 for Quadratic average
By default, the parameter is set to 0.
[Automatic selection type] defines the operator operand type.
Possible values are:
- 0 for memorized traces of the operand source
- 1 for compatible traces of the operand source
By default, the parameter is set to 0.
[Operator Name] defines the operator result name.
[Frequency domain], possible values are:
- 0 for time domain (real/imaginary)
- 1 for frequency domain (module)
By default, the parameter is set to 1.
```

<!-- page 130 -->
```
[Step]defines the step between calculated points if an interpolation is
necessary. By default, it is set to (MaxX- MinX) / (Number of points) of the
operand source.
```

<!-- page 131 -->
```
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddAutoOperator command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 137 | 001 | 000 | Layout unknown |
| 137 | 002 | 000 | Window unknown |
| 137 | 003 | 000 | Module number incorrect |
| 137 | 004 | 000 | Number of a module not supplying a result |
| 137 | 005 | 000 | Process number incorrect |
| 137 | 006 | 000 | Channel number incorrect |
| 137 | 007 | 000 | Reference channel number incorrect |
| 137 | 008 | 000 | Weighting operator unknown |
| 137 | 009 | 000 | No weighting for non-spectrum results |
| 137 | 010 | 000 | Result already weighted |
| 137 | 011 | 000 | Time operator unknown |
| 137 | 012 | 000 | Display unit unknown |
| 137 | 013 | 000 | Window cannot be created for the specified result |
| 137 | 014 | 000 | Operand is not complex, time domain is invalid |


<!-- page 132 -->

#### 3.3.39 - "GetReferenceList" command


**Semantics**

Get the references list of a window with referenced result.

**Command syntax**

```
GetReferenceList <layout name>
<window name>
[display zone type]
<layout name> and <window name> parameters define the window.
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
```

**Result returned**

A list of strings. Each string ends in the character \0 and is the name of a
reference.

**Consistency errors specific to the GetReferenceList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 135 | 001 | 000 | Unknown layout |
| 135 | 002 | 000 | Unknown window |
| 135 | 003 | 000 | Invalid display zone type |


<!-- page 133 -->

#### 3.3.40 - "SetReference" command


**Semantics**

Select the reference for the specified window with referenced result.

**Command syntax**

```
SetReference <layout name>
<window name>
<selected reference name>
[display zone type]
<layout name> and <window name> parameters define the window.
The <selected reference name> defines the wanted reference.
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetReference command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 136 | 001 | 000 | Unknown layout |
| 136 | 002 | 000 | Unknown window |
| 136 | 003 | 000 | Invalid display zone type |
| 136 | 004 | 000 | Invalid reference name |


<!-- page 134 -->

#### 3.3.41 - "GetCurrentReference" command


**Semantics**

Get the current reference for the specified window with referenced result.

**Command syntax**

```
GetCurrentReference <layout name>
<window name>
[display zone type]
<layout name> and <window name> parameters define the window.
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
```

**Result returned**

The name of the current reference ( "Time", "Slice number"...)

**Consistency errors specific to the GetCurrentReference command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 152 | 001 | 000 | Unknown layout |
| 152 | 002 | 000 | Unknown window |
| 152 | 003 | 000 | Invalid display zone type |
| 152 | 004 | 000 | Window cannot handle reference |
| 152 | 005 | 000 | Invalid reference name |


<!-- page 135 -->

#### 3.3.42 - "SetCursorPosition" command


**Semantics**

Position the cursor in specified window.

**Command syntax**

```
SetCursorPosition <Layout name>
<Window name>
<Value>
[Axis Type]
[Cursor number]
[Switch Layout]
[Cursor Start Stop Player]
<Layout name> and <Window name> parameters define the window.
<Value>, expressed in axis current unit, defines the wanted cursor position.
[Axis Type] optional parameter defines X-axis (0), Z-axis (1) or Time
Reference (2). By default it is set to 0 (X-axis).
[Cursor number] optional parameter defines the cursor number (1 or 2). By
default it is set to 1 (cursor1).
[Switch Layout] optional parameter enables (=1) or not (=0) to switch to the
<Layout name> layout if it's not the current one. By default it is set to 1.
[Cursor Start Stop Player] optional parameter, only used in the case
of player window, enables (=1) or not (=0) to set position of start (Cursor
number=1) or Stop (Cursor number=2) cursor. By default it is set to 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetCursorPosition command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 141 | 001 | 000 | Unknown layout |
| 141 | 002 | 000 | Unknown window |
| 141 | 003 | 000 | Incorrect value |
| 141 | 004 | 000 | X-axis does not exist in the specified window |
| 141 | 005 | 000 | Z-axis does not exist in the specified window |
| 141 | 006 | 000 | Time Reference does not exist in the specified window |
| 141 | 007 | 000 | Command not supported by the specified window |


<!-- page 136 -->

#### 3.3.43 - "GetCursorInfo" command


**Semantics**

Get the cursor information from the specified window.

**Command syntax**

```
GetCursorInfo <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

This command returns the cursor information which is displayed in the infotrace
of a window. It has to be noted that the infotrace must be opened to use this
command.
If the command succeeds, the header contains the size of the data, followed by the
string containing all the information.

**Remarks**

The format of the data returned is not fixed and depend of the type of window and
the options that have been selected. Following pictures show different case of
window.
The red circled string indicates the string that can be used to interpret the data
returned. They separate the main sections of the cursor information.
The green circled are specific strings that can be searched to retrieve data that are
displayed once. The dark red square point out strings that are repeated a variable
number of times.
The format of these data is not frozen and may change in the future.

**Consistency errors specific to the GetCursorInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 196 | 001 | 000 | Unknown layout |
| 196 | 002 | 000 | Unknown window |


<!-- page 137 -->

#### 3.3.44 - "CopyData" command


**Semantics**

Copy the data of the active trace from the selected window in the ClipBoard.

**Command syntax**

```
CopyData <Layout name>
<Window name>
<Display zone>
<Layout name> and <Window name> parameters define the window.
<Display zone> must be set to 5 for a YZ, 6 for a XY and 7 for an order
section zone of a waterfall window. It can be any value for other windows
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CopyData command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 156 | 001 | 000 | Unknown layout |
| 156 | 002 | 000 | Unknown window |
| 156 | 003 | 000 | Incorrect display zone |
| 156 | 005 | 000 | The window does not handle the copydata command |


<!-- page 138 -->

#### 3.3.45 - "CopyDataAllTraces" command


**Semantics**

Copy the data of all traces in a specified window in the ClipBoard.

**Command syntax**

```
CopyData <Layout name>
<Window name>
<Display zone>
<Layout name> and <Window name> parameters define the window.
<Display zone> must be set to 5 for a YZ, 6 for a XY and 7 for an order
section zone of a waterfall window. It can be any value for other windows
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CopyDataAllTraces command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 322 | 001 | 000 | Unknown layout |
| 322 | 002 | 000 | Unknown window |
| 322 | 003 | 000 | Incorrect display zone |
| 322 | 005 | 000 | The window does not handle the copydataalltraces<br>command |


<!-- page 139 -->

#### 3.3.46 - "CopyBitmap" command


**Semantics**

Copy the selected window as a bitmap in the ClipBoard.

**Command syntax**

```
CopyBitmap <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CopyData command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 356 | 001 | 000 | Unknown layout |
| 356 | 002 | 000 | Unknown window |
| 356 | 003 | 000 | The window does not handle the copybitmap command |


<!-- page 140 -->

#### 3.3.47 - "CopyGraph" command


**Semantics**

Copy the selected window as a WMF picture in the ClipBoard.

**Command syntax**

```
CopyGraph <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CopyData command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 355 | 001 | 000 | Unknown layout |
| 355 | 002 | 000 | Unknown window |
| 355 | 003 | 000 | The window does not handle the copygraph command |


<!-- page 141 -->

#### 3.3.48 - "SelectWaterfallWindowView" command


**Semantics**

Select the view of a waterfall display

**Command syntax**

```
SelectWaterfallWindowView <Layout name>
<Window name>
<View>
<Layout name> and <Window name> parameters define the window.
<View> one of the following value.
```

**Result returned**

No data follows the header.

| 0 | All view |
|---|---|
| 1 | 3D view |
| 2 | XY View |
| 3 | YZ view |
| 4 | Extraction view |


**Consistency errors specific to the SelectWaterfallWindowView
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 158 | 001 | 000 | Unknown layout |
| 158 | 002 | 000 | Unknown window |
| 158 | 003 | 000 | The window is not a waterfall window |
| 158 | 004 | 000 | The view parameter is incorrect |


<!-- page 142 -->

#### 3.3.49 - "GetScaleInfo" command


**Semantics**

Retrieves information about the selected scale.

**Command syntax**

```
GetScaleInfo <window name>
[display zone type]
[axis]
[bGraduationInfo]
[trace number]
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The [axis] parameter is one of the following values:
- 0: X axis
- 1: Y axis
- 2: Z axis
It is an optional parameter and its default value is 0.
The [bGraduationInfo] parameter determines if information about
graduation will be added to the returned result (0: not added; 1: added). It is an
optional parameter and its default value is 0.
[trace number] defines the signal area.
This parameter is used only if the window is in "Multi-Graph" display mode.
For the first signal area, trace number = 1.
It is an optional parameter and its default value is 1.
```

**Result returned**

The data returned contains the following information:

<!-- page 143 -->

|   | S ize |   | Type | Description |
|---|---|---|---|---|
|   | ( bytes) |   |   |   |
| 4 |   |   | float | Min of the scale |
| 4 |   |   | float | Max of the scale |
| 4 |   |   | Unsigned int | Type (0 = lin; 1 = log; 2 = dB) |
| X |   |   | String ending in<br>the character \0 | Information about graduation. For each graduation of<br>the scale, separated with a tabulation, the following<br>caracters are added :<br>VAL=-10.0\|POS=274\|DRA=0\|STY=-1\|ALI=0\|LEV=-1<br>VAL means the value expressed in the current unit<br>POS means the position in pixel of the graduation on the<br>axis<br>DRA means that the text of the graduation is displayed (if<br>=1) or not (if =0)<br>STY 1 for bold, else -1<br>ALI means alignement : 0 for left, 1 for centered, 2 for<br>right, -1 for not significant<br>LEV 1 means a major graduation, 0 means a minor<br>graduation, -1 for not significant |


**Consistency errors specific to the GetScaleInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 099 | 001 | 000 | Unknown window |
| 099 | 002 | 000 | Invalid display zone type |
| 099 | 003 | 000 | Incoherence between display zone et axis |
| 099 | 004 | 000 | Invalid axis |
| 099 | 005 | 000 | Invalid trace number |


<!-- page 144 -->

#### 3.3.50 - "SetScaleType" command


**Semantics**

Set the type (lin, log or dB) of the selected scale.

**Command syntax**

```
SetScaleType <window name>
<type>
[display zone type]
[axis]
The <type> parameter is one of the following values:
- 0: lin
- 1: log
- 2: dB
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The [axis]parameter is one of the following values:
- 0: X axis
- 1: Y axis
- 2: Z axis
It is an optional parameter and its default value is 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetScaleType command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 100 | 001 | 000 | Unknown window |
| 100 | 002 | 000 | Invalid display zone type |
| 100 | 003 | 000 | Incoherence between display zone and axis |
| 100 | 004 | 000 | Invalid axis |
| 100 | 005 | 000 | Type not authorized |


<!-- page 145 -->

#### 3.3.51 - "SetScaleValues" command


**Semantics**

Set the min and max values of the selected scale.

**Command syntax**

```
SetScaleValues <window name>
<min>
<max>
[display zone type]
[axis]
[lock]
The <min> and <max> values are considered as linear.
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The [axis] parameter is one of the following values:
- 0: X axis
- 1: Y axis
- 2: Z axis
It is an optional parameter and its default value is 0.
The [lock] parameter (available since NVGate V6.10) is one of the following
values:
- 0: the specified axis is no more in a fixed state
- 1: the specified axis is set in a fixed state
It is an optional parameter and its default value is 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetScaleValues command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 101 | 001 | 000 | Unknown window |
| 101 | 002 | 000 | Invalid display zone type |
| 101 | 003 | 000 | Incoherence between display zone et axis |
| 101 | 004 | 000 | Invalid axis |
| 101 | 005 | 000 | Min value upper than max value. |
| 101 | 006 | 000 | Min and max scale values cannot be changed |
| 101 | 007 | 000 | Signal no longer available in the time-to-stop window |


<!-- page 146 -->

#### 3.3.52 - "SendScaleCommand" command


**Semantics**

Send a command to the scale. These commands are usually sent by the buttons of
the toolbars.

**Command syntax**

```
SendScaleCommand <window name>
<axis>
<Command>
[display zone type]
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The <axis> parameter is one of the following values:
- 0: X axis
- 1: Y axis
- 2: Z axis
It is an optional parameter and its default value is 0.
The possible values of the <Command> parameter are :
```

**Result returned**

No data follows the header.

| 1 | Reset zoom , , |
|---|---|
| 2 | Reset min value , , |
| 3 | Reset max , , |
| 4 | Zoom in (from center) , , |
| 5 | Zoom out (from center) , , |
| 6 | Move left , , |
| 7 | Move right , , |
| 8 | Zoom in , |
| 9 | Zoom out , |


**Consistency errors specific to the SendScaleCommand command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 131 | 001 | 000 | Unknown window |
| 131 | 002 | 000 | Invalid display zone type |
| 131 | 003 | 000 | Incoherence between display zone and axis |
| 131 | 004 | 000 | Invalid axis |
| 131 | 005 | 000 | Invalid Command |


<!-- page 147 -->

#### 3.3.53 - "GetAvailableScale" command


**Semantics**

Retrieves available scale for the selected axis of a window's area.

**Command syntax**

```
GetAvailableScale <window name>
[display zone type]
[axis]
For [display zone type] parameter description, see § 3.2.2 -
GetWindowDisplayZone.
The [axis] parameter is one of the following values:
- 0: X axis
- 1: Y axis
- 2: Z axis
It is an optional parameter and its default value is 0.
```

**Result returned**

The data returned is a table of four boolean values:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 1 |   |   | bool | Lin scale available. |
| 1 |   |   | bool | Log scale available. |
| 1 |   |   | bool | db scale available. |
| 1 |   |   | bool | Octave scale available. |


**Consistency errors specific to the GetAvailableScale command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 130 | 001 | 000 | Unknown window |
| 130 | 002 | 000 | Invalid display zone type |
| 130 | 003 | 000 | Incoherence between display zone and axis |
| 130 | 004 | 000 | Invalid axis |


<!-- page 148 -->

#### 3.3.54 - "SetScaleTimeType" command


**Semantics**

Set the type (Absolute, Relative or Auto) of the selected scale.

**Command syntax**

```
SetScaleTimeType <window name>
<type>
[save as user preference]
The <type> parameter is one of the following values:
- 0: Absolute
- 1: Relative
- 2: Auto
The [save as user preference] parameter, set to 1, save the type as
user preference for the window type specified.
It is an optional parameter and its default value is 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetScaleTimeType command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 197 | 001 | 000 | Unknown window |
| 197 | 002 | 000 | Invalid scale |
| 197 | 003 | 000 | Time type not authorized |
| 197 | 004 | 000 | Unknown time type |


<!-- page 149 -->

#### 3.3.55 - "IsScaleTimeInRelative" command


**Semantics**

Return the time type of the selected window (Absolute or Relative) .

**Command syntax**

```
IsScaleTimeInRelative <window name>
```

**Result returned**

The value returned is a boolean (short 2 bytes) :
0 : Scale is absolute
1 : Scale is relative

**Consistency errors specific to the IsScaleTimeInRelative command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 198 | 001 | 000 | Unknown window |
| 198 | 002 | 000 | Scale is not time type |


<!-- page 150 -->

#### 3.3.56 - "GetWindowPosition" command


**Semantics**

Return the position of a window .

**Command syntax**

```
GetWindowPosition <layout name>
<window name>
The parameters identifies the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to retrieve the
values:
```

**Result returned**

If the function succeeded, the header contains the size of the returned data. (16
bytes) and the four coordinates of the window are returned:
- left
- right
- top
- bottom
The reference of the coordinates is the upper left corner of the client area. To
retrieve the size of the client area, call the command using "Client" for the layout
name and "Area" for the window name.
Top
Bottom
Left
Right

**Consistency errors specific to the GetWindowPosition command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 195 | 001 | 000 | Unknown layout |
| 195 | 002 | 000 | Unknown window |


<!-- page 151 -->

#### 3.3.57 - "SetWindowPosition" command


**Semantics**

Set the position of a window .

**Command syntax**

```
SetWindowPosition <layout name>
<window name>
<left>
<right>
<top>
<bottom>
The two first parameters identify the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to set the
position.
The next four parameters define the coordinates of the window, in accordance to
the rules defined in § 3.3.56 - GetWindowPosition command.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetWindowPosition command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 194 | 001 | 000 | Unknown layout |
| 194 | 002 | 000 | Unknown window |
| 194 | 003 | 000 | One of the coordinate is negative |
| 194 | 004 | 000 | Right is lower than left or bottom is lower than top |
| 194 | 005 | 000 | The command failed to move the window |


<!-- page 152 -->

#### 3.3.58 - "GetRotationPreferences" command


**Semantics**

Get the preferences relative to rotation for a window.

**Command syntax**

```
GetRotationPreferences <layout name>
<window name>
The two parameters identify the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to get the
preferences and then restored to its initial selection.
```

**Result returned**

The header contains the size of the returned values is followed by these values.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | int | Direction:<br>0 Counterclockwise,<br>1 Clockwise,<br>-1 Undefined. |
| 4 |   |   | int | X orientation in degree: values among 0, 45,<br>90, 135, 180, 225, 270, 315. |
| 4 |   |   | int | Y orientation in degree. This value is always<br>X orientation plus 90 degrees. |


**Consistency errors specific to the GetRotationPreferences command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 265 | 001 | 000 | Unknown layout |
| 265 | 002 | 000 | Unknown window |
| 265 | 003 | 000 | Not an appropriate window |


<!-- page 153 -->

#### 3.3.59 - "SetRotationPreferences" command


**Semantics**

Set the preferences relative to rotation for a window.

**Command syntax**

```
SetRotationPreferences <layout name>
<window name>
<direction>
<X orientation>
<Y orientation>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to set the
preferences and then restored to its initial selection.
<direction> is either clockwise (1) or counterclockwise (0).
<X orientation> is an integer in degrees among 90, 135, 180, 225, 270 and
315.
<Y orientation> is an integer in degree, and must be X orientation plus 90
degrees.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetRotationPreferences command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 266 | 001 | 000 | Unknown layout |
| 266 | 002 | 000 | Unknown window |
| 266 | 003 | 000 | Not an appropriate window |
| 266 | 004 | 000 | Invalid direction |
| 266 | 005 | 000 | Invalid X orientation |
| 266 | 006 | 000 | Invalid Y orientation |


<!-- page 154 -->

#### 3.3.60 - "SetViewmeterLevels" command


**Semantics**

Set the alarm, low and high levels for a viewmeter window and configure the
display of many levels (low, high, alarm, min, memory, max).

**Command syntax**

```
SetViewmeterLevels <layout name>
<window name>
<low level>
<high level>
<alarm level>
[display low level]
[display high level]
[display alarm level]
[display min]
[display memory]
[display max]
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
<low level> is a floating value in current unit
<high level> is a floating value in current unit
<alarm level> is a floating value in current unit.
The last six optional parameters enable to display ("1") or not ("0") the
corresponding level. Their default value is 0.
```

**Example**

```
SetViewmeterLevels Layout2 Window1 -7 3 7 1 0 1
Set viewmeter levels to -7V 3V and 7V (if current unit is Volt) and display low
level and alarm level in the 1D window "Window1" from layout "Layout2".
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetViewmeterLevels command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 386 | 001 | 000 | Unknown layout |
| 386 | 002 | 000 | Unknown window |
| 386 | 003 | 000 | Not an appropriate window |
| 386 | 004 | 000 | Not 1D graphic window |
| 386 | 005 | 000 | Low > high |
| 386 | 006 | 000 | High > Alarm |


<!-- page 155 -->

#### 3.3.61 - "PinWindow " command


**Semantics**

Set the "always on top" status of a window.

**Command syntax**

```
PinWindow <layout name>
<window name>
<status>
The two first parameters identify the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to set the
position.
The next parameter defines the status of the window: "1" will activate the "always
on top" status, and "0" will deactivate it.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the PinWindow command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 273 | 001 | 000 | Unknown layout |
| 273 | 002 | 000 | Unknown window |


<!-- page 156 -->

#### 3.3.62 - "GetPinStatus" command


**Semantics**

Retrieve the "always on top" status of a window.

**Command syntax**

```
GetPinStatus <layout name>
<window name>
The two parameters identify the window by the <layout name> and the
<window name>. If the layout is not selected, it will be loaded to set the
position.
```

**Result returned**

The header contains the size of the returned values and is followed by these
values.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 1 |   |   | int | Status:<br>1 « Always on top » activated,<br>0 « Always on top » deactivated. |


**Consistency errors specific to the GetPinStatus command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 272 | 001 | 000 | Unknown layout |
| 272 | 002 | 000 | Unknown window |


<!-- page 157 -->

#### 3.3.63 - "SetTachometerPosition" command


**Semantics**

Set the tachometer position preference for a window.

**Command syntax**

```
SetTachometerPosition <layout name>
<window name>
<value>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
<value> is either none or an integer value expressed in degree. The angle is
defined as:
- Positive for a counterclockwise orientation, negative for a clockwise
orientation,
- Origin (value 0) matches the three o'clock position.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetTachometerPosition command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 325 | 001 | 000 | Unknown layout |
| 325 | 002 | 000 | Unknown window |
| 325 | 003 | 000 | Not an appropriate window |


<!-- page 158 -->

#### 3.3.64 - "GetTachometerPosition" command


**Semantics**

Get the tachometer position preference for a window.

**Command syntax**

```
GetTachometerPosition <layout name>
<window name>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
```

**Result returned**

An integer that represents an angle in degree. The angle is defined as:
- Positive for a counterclockwise orientation, negative for a clockwise
orientation,
- Origin (value 0) matches the three o'clock position.

**Consistency errors specific to the GetTachometerPosition command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 327 | 001 | 000 | Unknown layout |
| 327 | 002 | 000 | Unknown window |
| 327 | 003 | 000 | Not an appropriate window |


<!-- page 159 -->

#### 3.3.65 - "AddResultTemplateToWindow" command


**Semantics**

Add a result template to an existing window.

**Command syntax**

```
AddResultTemplateToWindow
<layout name>
<window name>
<project name>
<result template name>
The first two parameters identify the window by the <layout name> and the
<window name>. The last two parameters identify the result template by the
<project name> and the <result template name>.
If the layout is not currently selected, it will be loaded to set the preferences and
then restored to its initial selection.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPhasePreference command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 303 | 001 | 000 | Unknown layout |
| 303 | 002 | 000 | Unknown window |
| 303 | 003 | 000 | Unknown project |
| 303 | 004 | 000 | Unknown result template |
| 303 | 005 | 000 | Result template is not compatible with window |


<!-- page 160 -->

#### 3.3.66 - "SetPhasePreference" command


**Semantics**

Set the preferences relative to rotation for a window.

**Command syntax**

```
SetPhasePreference <layout name>
<window name>
<phase unit>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
< phase unit > is an integer:
- -2 : -180° / +180°
- -1 : 0° / 360°
- X : Number of phase rotations
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPhasePreference command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 298 | 001 | 000 | Unknown layout |
| 298 | 002 | 000 | Unknown window |
| 298 | 003 | 000 | Not an appropriate window |


<!-- page 161 -->

#### 3.3.67 - "SetGraduationDirection" command


**Semantics**

Set the graduation direction for a window with such a concept.

**Command syntax**

```
SetGraduationDirection <layout name>
<window name>
<direction>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
<direction> is either an integer or a string:
- 0 or "CCW" for a counterclockwise direction
- 1 or "CW" for a clockwise direction
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetPhasePreference command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 326 | 001 | 000 | Unknown layout |
| 326 | 002 | 000 | Unknown window |
| 326 | 003 | 000 | Not an appropriate window (no concept of graduation<br>direction is applicable to the window) |
| 326 | 004 | 000 | Invalid direction value. |


<!-- page 162 -->

#### 3.3.68 - "GetGraduationDirection" command


**Semantics**

Get the graduation direction for a window with such a concept.

**Command syntax**

```
GetGraduationDirection <layout name>
<window name>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
```

**Result returned**

An integer that represents a direction:
- 0 for a counterclockwise direction
- 1 for a clockwise direction

**Consistency errors specific to the GetGraduationDirection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 328 | 001 | 000 | Unknown layout |
| 328 | 002 | 000 | Unknown window |
| 328 | 003 | 000 | Not an appropriate window |


<!-- page 163 -->

#### 3.3.69 - "GetActiveTrace" command


**Semantics**

Get the active trace for a window.

**Command syntax**

```
GetActiveTrace <layout name>
<window name>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection.
```

**Result returned**

An integer that represents a trace index. The first trace is index 0, the last trace is
<number of traces> - 1.

**Consistency errors specific to the GetGraduationDirection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 358 | 001 | 000 | Unknown layout |
| 358 | 002 | 000 | Unknown window |
| 358 | 003 | 000 | Not an appropriate window |
| 358 | 004 | 000 | Active trace not found in this window |


<!-- page 164 -->

#### 3.3.70 - "SetActiveTrace" command


**Semantics**

Set the active trace for a window.

**Command syntax**

```
SetActiveTrace <layout name>
<window name>
<trace index>
The first two parameters identify the window by the <layout name> and the
<window name>. If the layout is not currently selected, it will be loaded to set
the preferences and then restored to its initial selection. The third parameter is an
integer that represents a trace index. The first trace is index 0, the last trace is
<number of traces> - 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the GetGraduationDirection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 357 | 001 | 000 | Unknown layout |
| 357 | 002 | 000 | Unknown window |
| 357 | 003 | 000 | Not an appropriate window |
| 357 | 004 | 000 | Unknow trace index |


<!-- page 165 -->

#### 3.3.71 - "ChangeWindowPreferences" command


**Semantics**

Change window preferences.

**Command syntax**

```
ChangeWindowPreferences <layout name>
<window name>
<parameters>
The first two parameters identify the window by the <layout name> and the
<window name>. The third parameter <parameters> is a string describing
new preference values [key=value;]. For example: "background_color=#ff4d4d;".
It can contain several pairs of key=value separated by a ';' character.
```

**Result returned**

No data follows the header.

| Key preferences | Descritption |
|---|---|
| background_color | Modify "Window background" preference. Possible<br>RGB value format :<br>- #RGB (each of R, G, and B is a single hex digit)<br>- #RRGGBB<br>- #RRRGGGBBB<br>- #RRRRGGGGBBBB<br>- A name from the list of SVG color names<br>provided by the World Wide Web Consortium; for<br>example, "steelblue" or "gainsboro". |


**Consistency errors specific to the ChangeWindowPreferences
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 377 | 001 | 000 | Unknown layout |
| 377 | 002 | 000 | Unknown window |
| 377 | 003 | 000 | Unknown key preference |
| 377 | 004 | 000 | Parameters bad format |


<!-- page 166 -->

### 3.4 - PROJECT MANAGER


#### 3.4.1 - "LoadProject" command


**Semantics**

Allows the user to load a project and its last saved workbook. You can also use
"OpenProject".

**Command syntax**

```
LoadProject <project name>
[project database name]
[Save]
The[project database name] parameter is ignored. The project is
always sought for in the current project database.
The optional parameter [Save] equals 1 by default.
Entering 0 lets you load the project without saving the current project.
Entering 1 lets you save the current project. In this case, the confirmation dialogue
boxes corresponding to the various saves will appear in NVGate.
A value other than 0 or 1 is interpreted as a 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the LoadProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 009 | 001 | 000 | Project unknown |
| 009 | 002 | 000 | Error when saving the previous project |
| 009 | 003 | 000 | Error during project loading |
| 009 | 004 | 000 | Error when deleting the default project |
| 009 | 005 | 000 | A recording is running. So no project can be loaded. |


<!-- page 167 -->

#### 3.4.2 - "NewProject" command


**Semantics**

Allows the user to create a new current project with a new name.

**Command syntax**

```
NewProject <Project name>
[Access allowed]
[Workbook]
[Workbook Model]
[Access allowed] : 0 (Administrators only)
1 (All users)
set by default to 0.
[Workbook] : 0 (workbook default empty)
1 (current workbook)
2 (workbook model)
set by default to 0.
[Workbook Model] workbook model name. This parameter is considered
only if [workbook] parameter is set to 2.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the NewProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 290 | 001 | 000 | Project name not allowed |
| 290 | 002 | 000 | Invalid project name |
| 290 | 003 | 000 | Project name already used |
| 290 | 004 | 000 | Error creating project |


<!-- page 168 -->

#### 3.4.3 - "OpenProject" command


**Semantics**

Allows the user to open a project from the project database and load a specific
workbook.

**Command syntax**

```
OpenProject <project name>
<workbook type>
<workbook name>
[Save]
<Workbook type> : 0 (workbook default empty)
1 (project workbook)
2 (workbook model)
3 (measurement workbook)
<Workbook name> : specify the workbook to load.
- If "workbook type" is 0, this parameter is ignored
- If "workbook type" is 1, specify project name containing the workbook
- If "workbook type" is 2, specify model name
- If "workbook type" is 3, specify project name and measurement name like
this "ProjectName\MeasurementName".
The optional parameter [Save] equals 1 by default.
Entering 0 lets you load the project without saving the current project.
Entering 1 lets you save the current project. In this case, the confirmation dialogue
boxes corresponding to the various saves will appear in NVGate.
A value other than 0 or 1 is interpreted as a 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the OpenProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 331 | 001 | 000 | Project unknown |
| 331 | 002 | 000 | Error when saving the previous project |
| 331 | 003 | 000 | Error during project loading |
| 331 | 004 | 000 | Error when deleting the default project |
| 331 | 005 | 000 | A recording is running. So no project can be loaded. |


<!-- page 169 -->

#### 3.4.4 - "SaveProject" command


**Semantics**

Allows the user to save the current project.

**Command syntax**

```
SaveProject [Ask question]
[Access allowed]
[Ask question] must be set to 0 if the action should not be interrupted by
any question (project name selection...) and to 1 to get some choice. Default
value is 0.
[Access allowed] : 0 (Administrators only)
1 (All users)
set by default to 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SaveProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 084 | 001 | 000 | The project is protected and cannot be overwritten |
| 084 | 002 | 000 | Project saving failed |


<!-- page 170 -->

#### 3.4.5 - "SaveProjectAs" command


**Semantics**

Allows the user to save the current project with a new name.

**Command syntax**

```
SaveProjectAs <Project name>
[Access allowed]
[Access allowed] : 0 (Administrators only)
1 (All users)
set by default to 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SaveProjectAs command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 124 | 001 | 000 | Invalid project name |
| 124 | 002 | 000 | Project name already used |
| 124 | 003 | 000 | Error during project copying |
| 124 | 004 | 000 | Error during project saving |
| 124 | 005 | 000 | Error during project opening |


<!-- page 171 -->

#### 3.4.6 - "RemoveProject" command


**Semantics**

Allows the user to remove a project

**Command syntax**

```
RemoveProject <Project name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 274 | 001 | 000 | Cannot remove the current project |
| 274 | 002 | 000 | Project not found |
| 274 | 003 | 000 | Error removing project in StandAlone |
| 274 | 004 | 000 | Error removing measure contained in the project |
| 274 | 005 | 000 | Error removing project directory |


<!-- page 172 -->

#### 3.4.7 - "ImportProject" command


**Semantics**

Import a project in the projects base.

**Command syntax**

```
GetProjectList <Project name>
<Directory>
<Project name> : project name to import
<Directory> : absolute path containing the prajetc name foler
```

**Example**

```
ImportProject MyProject D:\\MyData\\Projects
Imports the project D:\MyData\Projects\MyProject in the current projects base of
NVGate.
```

**Result returned**

The name of the project that has been imported if the import is successful.

**Consistency errors specific to the ImportProject command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 337 | 001 | 000 | Path not exist or bad contain |
| 337 | 002 | 000 | Directory already exist in the project base |
| 337 | 003 | 000 | Error copying project folder |


<!-- page 173 -->

#### 3.4.8 - "GetProjectList" command


**Semantics**

Retrieves the list of project names

**Command syntax**

```
GetProjectList
```

**Result returned**

The list of project names follows the header. Each name is returned in the form of
an ASCII character string ending in the character \0.

**Consistency errors specific to the GetProjectList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 018 | 001 | 000 | File error |


<!-- page 174 -->

#### 3.4.9 - "GetCurrentProjectName" command


**Semantics**

Retrieves the name of the current project.

**Command syntax**

```
GetCurrentProjectName
```

**Result returned**

The header contains the size of the project name and is followed by the current
project name.

<!-- page 175 -->

#### 3.4.10 - "GetProjectProperties" command


**Semantics**

Retrieves the properties of the selected project.

**Command syntax**

```
GetProjectProperties <Project name>
The project must be in the default project base.
```

**Result returned**

The following table described the project properties returned:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| X |   |   | String ending in<br>the character \0. | Name of the project creator |
| X |   |   | String ending in<br>the character \0. | First name of the project creator |
| X |   |   | String ending in<br>the character \0. | Keyword of the project |
| X |   |   | String ending in<br>the character \0. | Comment of the project |
| 4 |   |   | int | Equals 1 if the project is ReadOnly for the<br>external users, else 0 |
| 4 |   |   | int | Equals 1 if the project is ReadOnly, else 0 |
| 4 |   |   | Unsigned int | Year of the project creation |
| 4 |   |   | Unsigned int | Month of the project creation |
| 4 |   |   | Unsigned int | Day of the project creation |
| 4 |   |   | Unsigned int | Year of last modification of the project |
| 4 |   |   | Unsigned int | Month of last modification of the project |
| 4 |   |   | Unsigned int | Day of last modification of the project |


**Consistency errors specific to the GetProjectProperties command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 097 | 001 | 000 | Project not found |


<!-- page 176 -->

#### 3.4.11 - "GetProjectUserPropertiesList" command


**Semantics**

Retrieves the user properties of the selected project (since NVGate V15). This
commande is necessary to get the identifier of a user property, which is needed by
the DeleteProjectUserProperty or ModifyProjectUserProperty commands.

**Command syntax**

```
GetProjectUserPropertiesList <Project name>
```

**Result returned**


**Result returned**

A list of user property info.
A user property info consists of the following fields:

**Consistency errors specific to the
GetProjectUserPropertiesList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 387 | 001 | 000 | Invalid project name |


|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| X |   |   | String ending in<br>the character \0. | The unique identifier of the user property |
| X |   |   | String ending in<br>the character \0. | The title of the user property |
| X |   |   | String ending in<br>the character \0. | The type of the user property (text) |
| X |   |   | String ending in<br>the character \0. | The value of the user property |


<!-- page 177 -->

#### 3.4.12 - "GetMeasurementUserPropertiesList" command


**Semantics**

Retrieves the user properties of the selected measurement (since NVGate V15)

**Command syntax**

```
GetMeasurementUserPropertiesList <Project name>
<Measurement name>
```

**Result returned**


**Result returned**

A list of user property info.
A user property info consists of the following fields:

**Consistency errors specific to the
GetMeasurementUserPropertiesList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 393 | 001 | 000 | Invalid project name |
| 393 | 002 | 000 | Invalid measurement name |


|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| X |   |   | String ending in<br>the character \0. | The unique identifier of the user property |
| X |   |   | String ending in<br>the character \0. | The title of the user property |
| X |   |   | String ending in<br>the character \0. | The type of the user property (text) |
| X |   |   | String ending in<br>the character \0. | The value of the user property |


<!-- page 178 -->

#### 3.4.13 - "AddProjectUserProperty" command


**Semantics**

Add a user property (text type) to the selected project (since NVGate V15).

**Command syntax**

```
AddProjectUserProperty <Project name>
<Property title>
<Property value>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddProjectUserProperty
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 388 | 001 | 000 | Invalid project name |
| 388 | 002 | 000 | Property title already used in this project |


<!-- page 179 -->

#### 3.4.14 - "AddMeasurementUserProperty" command


**Semantics**

Add a user property (text type) to the selected measurement of the project (since
NVGate V15).

**Command syntax**

```
AddMeasurementUserProperty <Project name>
<Measurement name>
<Property title>
<Property value>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the
AddMeasurementUserProperty command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 392 | 001 | 000 | Invalid project name |
| 392 | 002 | 000 | Invalid measurement name |
| 392 | 003 | 000 | Property title already used in this measurement |


<!-- page 180 -->

#### 3.4.15 - "ModifyProjectUserProperty" command


**Semantics**

Modify the value of a user property (text type) into the selected project (since
NVGate V15).

**Command syntax**

```
ModifyProjectUserProperty <Project name>
<Property identifier>
<Property value>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ModifyProjectUserProperty
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 390 | 001 | 000 | Invalid project name |
| 390 | 002 | 000 | Property in a readOnly mode |
| 390 | 003 | 000 | Invalid identifier (see GetProjectUserPropertiesList) |


<!-- page 181 -->

#### 3.4.16 - "ModifyMeasurementUserProperty" command


**Semantics**

Modify the value of a user property (text type) into the selected measurement
(since NVGate V15).

**Command syntax**

```
ModifyMeasurementUserProperty <Project name>
<Measurement name>
<Property identifier>
<Property value>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ModifyMeasurementUserProperty
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 394 | 001 | 000 | Invalid project name |
| 394 | 002 | 000 | Invalid measurement name |
| 394 | 003 | 000 | Invalid identifier (see GetMeasurementUserPropertiesList) |
| 394 | 004 | 000 | Property in a readOnly mode |


<!-- page 182 -->

#### 3.4.17 - "DeleteProjectUserProperty" command


**Semantics**

Remove a user property from the selected project (since NVGate V15).

**Command syntax**

```
DeleteProjectUserProperty <Project name>
<Property identifier>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DeleteProjectUserProperty
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 389 | 001 | 000 | Invalid project name |
| 389 | 002 | 000 | Invalid identifier or property not deletable |


<!-- page 183 -->

#### 3.4.18 - "DeleteMeasurementUserProperty" command


**Semantics**

Remove a user property from the selected measurement (since NVGate V15).

**Command syntax**

```
DeleteMeasurementUserProperty <Project name>
<Measurement name>
<Property identifier>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the
DeleteMeasurementUserProperty command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 391 | 001 | 000 | Invalid project name |
| 391 | 002 | 000 | Measurement name |
| 391 | 003 | 000 | Invalid identifier or property not deletable |


<!-- page 184 -->

#### 3.4.19 - "LoadWorkbook" command


**Semantics**

Allows the user to load a project or measurement workbook.

**Command syntax**

```
LoadWorkbook <project name>
[measurement name]
[Save]
[Settings]
[ControlPanel]
[Layouts]
[Setup]
[PrintSetup]
If no [measurement name] is specified, the project workbook is considered.
The optional parameter [Save] equals 1 by default.
Entering 0 lets you load the workbook without saving the current workbook.
Entering 1 lets you save the current workbook. In this case, the confirmation
dialogue boxes corresponding to the various saves will appear in NVGate.
A value other than 0 or 1 is interpreted as a 1.
The optional parameter [Settings], [ControlPanel], [Layouts],
[Setup], [PrintSetup] let you load only partially the workbook. Set the
parameter to 0 if you do not want to load this part of the workbook. The default
values are 1 so that the whole workbook is loaded if the parameters are not set.
Refer to NVGate reference manual to get the meaning of the partial load.
```

**Example**

```
LoadWorkbook "My Project" p2=0 p3=0 p4=0 p5=1 p6=0 p7=0
Is equivalent to load only the layouts of the project "My Project", without saving
the current workbook.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the LoadWorkbook command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 010 | 001 | 000 | Saving of the previous workbook has failed |
| 010 | 002 | 000 | Workbook loading has failed |
| 010 | 002 | 000 | A recording is running. So no workbook can be loaded. |


<!-- page 185 -->

#### 3.4.20 - "LoadWorkbookModel" command


**Semantics**

Allows the user to load a workbook of the workbook library.

**Command syntax**

```
LoadWorkbookModel <Workbook name>
[Path]
[Save]
[Settings]
[ControlPanel]
[Layouts]
[Setup]
[PrintSetup]
<Workbook name> is the name of the model
[Path] is the relative path in the workbook library. The symbol "\" must be
doubled to be correctly understood.
All the other parameter are used exactly in the same way than the "3.4.19 -
LoadWorkbook" command.
```

**Example**

```
LoadWorkbookModel "StartWorkbook" "User\\SimpleModels"
This load the workbook "StartWorkbook" located in the folder
"User\SimpleModels" of the workbook library
```

**Result returned**

No data follows the header.

**Consistency errors specific to the LoadWorkbookModel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 165 | 001 | 000 | Saving of the previous workbook has failed |
| 165 | 002 | 000 | Workbook loading has failed |
| 165 | 003 | 000 | A recording is running. So no workbook can be loaded. |


<!-- page 186 -->

#### 3.4.21 - "SaveWorkbook" command


**Semantics**

Allows the user to save the current workbook.

**Command syntax**

```
SaveWorkbook
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SaveWorkbook command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 073 | 001 | 000 | Workbook saving failed |
| 073 | 002 | 000 | The workbook is protected and cannot be overwritten |


<!-- page 187 -->

#### 3.4.22 - "SaveWorkbookModel" command


**Semantics**

Allows the user to save the current workbook as a model.

**Command syntax**

```
SaveWorkbookModel <Workbook Model name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SaveWorkbookModel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 166 | 001 | 000 | Workbook saving failed |


<!-- page 188 -->

#### 3.4.23 - "DeleteModel" command


**Semantics**

Delete the specified model. This model cannot be this which has just been loaded.

**Command syntax**

```
DeleteModel <Relative Path>
<Workbook Model name>
<Relative Path> is the relative path in the workbook library. The symbol "\"
must be doubled to be correctly understood. In NVGate, the user models are
stored in a directory called "User".
<Workbook Model name> is the name of the model to delete.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DeleteModel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 167 | 001 | 000 | "Workbook model name" is not a model |
| 167 | 002 | 000 | Deleting model has failed. |


<!-- page 189 -->

#### 3.4.24 - "ReloadCurrentWorkbook" command


**Semantics**

Allows the user to reload the saved workbook of the current project.

**Command syntax**

```
ReloadCurrentWorkbook
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ReloadCurrentWorkbook command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 074 | 001 | 000 | Workbook loading has failed |


<!-- page 190 -->

#### 3.4.25 - "ResetWorkbook" command


**Semantics**

Reset everything in NVGate:
- Settings of the analyzer are set to their default value
- Windows are destroyed
- Control panel and Save setup are emptied

**Command syntax**

```
ResetWorkbook
```

**Result returned**

No data follows the header.

<!-- page 191 -->

#### 3.4.26 - "LoadMeasurement" command


**Semantics**

Allows the user to load a measurement.

**Command syntax**

```
LoaMeasurement <project name>
<measurement name>
[Save]
The parameters <project name> and <measurement name> identify the
measurement to be loaded
The optional parameter [Save] equals 1 by default. If set to 1, the previous
loaded measurement is saved, if set to 0, the previous measurement is not saved
A value other than 0 or 1 is interpreted as a 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the LoadMeasurement command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 153 | 001 | 000 | Measurement unknown |
| 153 | 002 | 000 | Error when saving the previous measurement |
| 153 | 003 | 000 | Error during measurement loading |


<!-- page 192 -->

#### 3.4.27 - "UnloadCurrentMeasurement" command


**Semantics**

Allows the user to unload the current measurement.

**Command syntax**

```
UnloadCurrentMeasurement [Confirmation]
[Save]
The optional parameter [Confirmation] equals 0 by default. If set to 1 and
the loaded measurement need to be saved, a dialog box appears, if set to 0, the
measurement is automatically saved depending of the [Save] parameter.
The [Save] parameter indicates if the loaded measurement must be saved (1) or
not (0). The default value is 0. It is ignored if [Confirmation] is set to 1.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnloadCurrentMeasurement
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 155 | 001 | 000 | Error during measurement saving |


<!-- page 193 -->

#### 3.4.28 - "RemoveMeasurement" command


**Semantics**

Allows the user to remove project's measurements.

**Command syntax**

```
RemoveMeasurement [Project name]
[Measurement name]
If no [Project name] is specified, the current project is considered.
If no [Measurement name] is specified, all of project's measurements are
considered.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveMeasurement command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 123 | 001 | 000 | The directory can't be removed |


<!-- page 194 -->

#### 3.4.29 - "GetMeasureList" command


**Semantics**

Retrieves the list of measurement names of a given project.

**Command syntax**

```
GetMeasureList <project name>
```

**Result returned**

The list of measurement names follows the header. Each name is returned in the
form of an ASCII character string ending in the character \0.

**Consistency errors specific to the GetMeasureList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 019 | 001 | 000 | File error |
| 019 | 002 | 000 | Project unknown |


<!-- page 195 -->

#### 3.4.30 - "GetItemPMTree" command


**Semantics**

Returns the items displayed in the project manager, to mirror the same
presentation.

**Command syntax**

```
GetItemPMTree <project>
<measurement>
The 2 parameters are optional. If no parameter is passed, the whole project
manager items are returned. This operation can take several seconds. If the
<project> parameter is defined, the commands returns all the items below this
project (workbook, measurement, result, signal...). If the <measurement>
parameter is defined, the commands returns only the items below the
measurement. The information returned mirrors exactly what is displayed in the
project manager. For instance, the layout will appear only in the current project.
```

**Result returned**

The command returns a string, with the following rules:
- Items are separated by a tabulation
- Items are preceeded by an identification number corresponding to its type.
This number is delimited by the symbols < and >
- The symbol >> is added after an item when this one is the root of other
items
- The symbol << is added after the last child of an item
The header contains the size of the string

**Example**

```
The command is called on the project "RecordToExport":
GetItemPMTree "RecordToExport"
The result returned is :
0000000196<0>RecordToExport >> <2>Workbook <1>M1024002 >>
<2>Workbook <4>Signal << <1>M1024003 >> <2>Workbook
<4>Signal << <1>M1024001 >> <2>Workbook <4>Signal <<
<1>M102400 >> <2>Workbook <4>Signal << <<
```

<!-- page 196 -->
```
Table of identification number:
```

| Item | Identification number |
|---|---|
| Project | 0 |
| Measurement | 1 |
| Workbook | 2 |
| Layout | 3 |
| Signal | 4 |
| Result group | 5 |
| Result | 6 |
| Template result | 8 |


**Consistency errors specific to the SetFanSpeed command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 206 | 001 | 000 | The item could not be found |


<!-- page 197 -->

#### 3.4.31 - "RefreshPM" command


**Semantics**

Refresh the Project Manager.

**Command syntax**

```
RefreshPM
```

**Result returned**

No data follows the header.

<!-- page 198 -->

#### 3.4.32 - "GetDatabasePath" command


**Semantics**

Retrieves the path of the project database. This path is defined with the
Environment application. The value of the path is stored in the NVGate.ini file.

**Command syntax**

```
GetDatabasePath
```

**Result returned**

The header contains the size of the path name and is followed by the path.

<!-- page 199 -->

#### 3.4.33 - "SwitchBasePath" command


**Semantics**

Switch between common and private base

**Command syntax**

```
SwitchBasePath <SwitchToCommonBase>
<SwitchToCommonBase> switches to the common base (if = 1) or private
base (if = 0).
```

**Result returned**

No data follows the header.

**Consistency errors specific to the WorkspaceTab command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 189 | 001 | 000 | Error during project saving |
| 189 | 002 | 000 | Error during project base loading |


<!-- page 200 -->

#### 3.4.34 - "RemoveSignalFromAnalyzer" command


**Semantics**

This command removes a signal from the disk of the analyzer.

**Command syntax**

```
RemoveSignalFromAnalyzer <Project name>
<Measurement name>
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveMeasurement command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 313 | 001 | 000 | Invalid project name |
| 313 | 002 | 000 | Invalid measurement name |
| 313 | 003 | 000 | No signal in the specified measurement. |
| 313 | 004 | 000 | No signal on analyzer. |
| 313 | 005 | 000 | Failed to remove signal from analyzer. |


<!-- page 201 -->

### 3.5 - GENERAL CONFIGURATION


#### 3.5.1 - "AppliedMode" command


**Semantics**

Allows to change the applied mode (rotating, structural...)

**Command syntax**

```
AppliedMode [mode]
[action]
[mode] can take the following values. The default value is All mode.
[action] can take the following values. The default value is Switch
```

**Result returned**

No data follows the header.

| mode |   | Meaning |   |
|---|---|---|---|
| 1 |   | Rotating mode |   |
| 2 |   | Structural mode |   |
| -1 |   | All mode |   |


| mode |   | Meaning |   |
|---|---|---|---|
| 0 |   | Activate the mode |   |
| 1 |   | Deactivate mode |   |
| 2 |   | Switch the mode |   |


**Consistency errors specific to the AppliedMode command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 079 | 001 | 000 | The mode is not valid |
| 079 | 002 | 000 | The action is not valid |


<!-- page 202 -->

#### 3.5.2 - "AddToControlPanel" command


**Semantics**

Add a setting or a status in the control panel

**Command syntax**

```
AddToControlPanel <Module num>
<Sub-module num>
<Setting num>
[TabActive]
[IsStatus]
[Tab name]
[Name]
<Module num>, <Sub-module num> and <Setting num> describe the
setting or status that is added to the control panel.
[TabActive] must be 1 if the setting must be added to the current active tab.
Default value is 1. If the value is 0, the parameter [Tab name] must be used.
[IsStatus] must be 1 to add a status, 0 for a setting. Default value is 0.
[Tab name] indicates the name of the tab where the setting or status must be
added. If the tab does not exist, it is created.
[Name] allows giving a specific name to the setting or status. If not used, the
usual name in NVGate is used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddToControlPanel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 080 | 001 | 000 | Setting unknown |


<!-- page 203 -->

#### 3.5.3 - "ResetControlPanel" command


**Semantics**

Removes part of or entire control panel

**Command syntax**

```
ResetControlPanel [application]
[TabName]
[application]describes which part of the control panel is to be reset. Default
value is 0 and the available values are :
[TabName] is the name of the tab to reset. It is used only when application = 3.
```

**Result returned**

No data follows the header.

| mode |   | Meaning |   |
|---|---|---|---|
| 0 |   | Complete control panel |   |
| 1 |   | Only the active tab |   |
| 2 |   | Only the status area part of the control panel |   |
| 3 |   | Tab defined by "tab name" |   |


**Consistency errors specific to the ResetControlPanel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 081 | 001 | 000 | Application is not valid |
| 081 | 002 | 000 | The tab " tab name" was not found |


<!-- page 204 -->

#### 3.5.4 - "WorkspaceTab" command


**Semantics**

Selection of 1 of the 3 tabs of the workspace

**Command syntax**

```
WorkspaceTab <Tab>
<Tab> defines the tab to be selected:
```

**Result returned**

No data follows the header.

| Tab |   | Meaning |   |
|---|---|---|---|
| 0 |   | Analyzer Setting Browser |   |
| 1 |   | Control Panel |   |
| 2 |   | Project manager |   |


**Consistency errors specific to the WorkspaceTab command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 082 | 001 | 000 | The "Tab" parameter is not valid |


<!-- page 205 -->

#### 3.5.5 - "SetUser" command


**Semantics**

Lets you load a known user (and its preferences).

**Command syntax**

```
SetUser <user last name>
[user first name]
[password]
The [password] is necessary if the user (who will be the current one) is
declared with a password.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetUser command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 012 | 001 | 000 | User unknown |
| 012 | 002 | 000 | Password not valid |


<!-- page 206 -->

#### 3.5.6 - "SetSilent" command


**Semantics**

This command avoids getting error or warning message box. Command such as
EditCalibration remains active.
This mode can be activated when NVGate is launched with the parameter -
silentex

**Command syntax**

```
SetSilent [nSilent]
[nSilent] must be to 1 to avoid the message boxes, 0 to get them.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetSilent command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 157 | 001 | 000 | The value nSilent is invalid |


<!-- page 207 -->

#### 3.5.7 - "AdministratorMode" command


**Semantics**

Lets you change mode between restricted mode and administrator mode, if the
current user is a restricted user.

**Command syntax**

```
AdministratorMode <Mode on/off>
[User last name]
[User first name]
[Password]
<Mode on/off> must be set to 0 to change to restricted mode. In this case, the
last optional three parameters will not be considered.
<Mode on/off> must be set to 1 to change to administrator mode with the user
specified by the last three optional parameters (see § 3.5.5 - SetUser).
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AdministratorMode command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 125 | 001 | 000 | User unknown |
| 125 | 002 | 000 | Password not valid |
| 125 | 003 | 000 | User is not administrator |
| 125 | 004 | 000 | Current user is not a restricted user |
| 125 | 005 | 000 | Cannot change administrator user in administrator mode |


<!-- page 208 -->

#### 3.5.8 - "SetSaveOption" command


**Semantics**

Sets the preferences relating to creation of a new measurement.

**Command syntax**

```
SetSaveOption [SaveMode flag]
[Keyword]
[AcquisitionSave flag]
[ManualSave flag]
The different values allowed for the [SaveMode flag]are :
- 0 : the measurement is not saved
- 1 : he measurement is saved in default measurement
- 2 : the measurement is saved with name confirmation
- 3 : the measurement is saved without name confirmation
The [SaveMode flag] is an optional parameter. The default value is 2.
If the string [Keyword] is not filled, no keyword is associated to a new
measurement, else, it is associated to the specified keyword.
The different values allowed for the [AcquisitionSave flag] and
[ManualSave flag] are :
- -1. no results are saved
- 0 : only the "static" results are saved
- 1 : only the "dynamic" results are saved
- 2 : both "static" and "dynamic" results are saved
The [AcquisitionSave flag] and [ManualSave flag] are optional
parameters. The default values are the user preferences.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetSaveOption command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 035 | 001 | 000 | Value incorrect for the SaveMode flag |
| 035 | 002 | 000 | Value incorrect for the AcquisitionSave flag |
| 035 | 003 | 000 | Value incorrect for the ManualSave flag |


<!-- page 209 -->

#### 3.5.9 - "SetNewMeasurementParameters" command


**Semantics**

Sets the preferences relating to creation of a new measurement.
Warning: Use the SetSaveOption command instead of this command in the
NVGate 1.30 and later.

**Command syntax**

```
SetNewMeasurementParameters [SaveImmediately flag]
[SkipConfirmation flag]
[Keyword]
If the [SaveImmediately flag] is set to 1, the measurement is saved
immediately when it is stopped.
If the [SkipConfirmation flag] is set to 1, the measurement is saved
without user confirmation being requested
Both flags are set to 0 by default.
If the string [Keyword] is not filled, no keyword is associated to a new
measurement, else, it is associated to the specified keyword.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetNewMeasurementParameters
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 025 | 001 | 000 | Value incorrect for one of the two flags (0 or 1 expected) |


<!-- page 210 -->

#### 3.5.10 - "GetMagnitudeList" command


**Semantics**

Return the list of magnitudes used in NVGate.

**Command syntax**

```
GetMagnitudeList
```

**Result returned**

The list of the magnitude names. Each name is returned in the form of an ASCII
character string ending in the character \0.
There is no specific error for this command. The header contains the size (in
number of bytes) of the result returned.
One magnitude name can be passed in parameter in the GetUnitList command.

<!-- page 211 -->

#### 3.5.11 - "GetUnitList" command


**Semantics**

Return the list of units corresponding to the selected magnitude in NVGate.

**Command syntax**

```
GetUnitList <Magnitude name>
<Magnitude name> defines the magnitude whose units are searched.
```

**Result returned**

The list of unit names corresponding to the magnitude name parameter.
If there is no specific error (magnitude name unknown), the header contains the
size (in number of bytes) of the result returned.

**Consistency errors specific to the GetUnitList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 093 | 001 | 000 | Magnitude name is unknown. |


<!-- page 212 -->

#### 3.5.12 - "SetUnit" command


**Semantics**

Sets the unit which is used for a given magnitude.

**Command syntax**

```
SetUnit <Magnitude identifier>
<Unit identifier>
<Magnitude identifier> can be found in the file « OrosUnit.ini ». Search
for the magnitude you are interested in the section "MAGNITUDE
DEFINITION"and use the value of "Id"
<Unit identifier> can be found in the same file or in the "UserUnit.ini"
file. Use also the "Id" value.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetUnit command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 085 | 001 | 000 | Value incorrect for the Magnitude identifier |
| 085 | 002 | 000 | Value incorrect for the Unit identifier |


<!-- page 213 -->

#### 3.5.13 - "GetCurrentUnit" command


**Semantics**

Return the current unit of a magnitude

**Command syntax**

```
GetCurrentUnit <Magnitude name>
<Magnitude name> defines the magnitude whose unit is searched.
```

**Result returned**

The name of the current unit corresponding to the magnitude name parameter.
If there is no specific error (magnitude name unknown), the header contains the
size (in number of bytes) of the result returned.

**Consistency errors specific to the GetCurrentUnit command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 120 | 001 | 000 | Magnitude name is unknown. |
| 120 | 002 | 000 | Magnitude does not have current unit |


<!-- page 214 -->

#### 3.5.14 - "GetUnitInfo" command


**Semantics**

Retrieves the information from a given unit.

**Command syntax**

```
GetUnitInfo <Magnitude name>
<Unit name>
The <Magnitude name> used by NVGate can be retrieved using the 3.5.10 -
GetMagnitudeList command.
The <Unit name> associated to a magnitude can be retrieved using the 3.5.11 -
GetUnitList command.
```

**Result returned**

The information on the magnitude and unit following the header are as follows (in
order):

|   | Info |   |   | type |   |
|---|---|---|---|---|---|
| Version number allowing structure<br>evolution (the first version is numbered 0) |   |   | 4-byte unsigned integer |   |   |
| SI unit of the magnitude |   |   | Character string ending in the<br>character '\0' |   |   |
| EquaDim information :<br>Returns radians exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns steradians exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns meters exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Kilograms exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Seconds exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Amperes exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Kelvins exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Moles exponent |   |   | 2-byte short |   |   |
| EquaDim information :<br>Returns Candelas exponent |   |   | 2-byte short |   |   |
| Label of the unit |   |   | Character string ending in the<br>character '\0' |   |   |
| Coefficient "A" for SI conversion |   |   | 4-byte float |   |   |
| Coefficient "B" for SI conversion |   |   | 4-byte float |   |   |
| 0dB Reference |   |   | 4-byte float |   |   |
| Factor for dB conversion |   |   | 4-byte float |   |   |


<!-- page 215 -->

**Consistency errors specific to the GetUnitInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 094 | 001 | 000 | Magnitude name unknown |
| 094 | 002 | 000 | Unit name unknown or not associated to the magnitude<br>name. |


<!-- page 216 -->

#### 3.5.15 - "GetMagnitudeInfo" command


**Semantics**

Retrieves the information about a magnitude (Name, name and label of the current
unit) .

**Command syntax**

```
GetMagnitudeInfo <Magnitude key>
The <Magnitude key> is returned by the 3.6.6 - GetSettingValue on the
setting number 204 (Physical setting).
```

**Result returned**

The information on the magnitude and unit following the header are as follows (in
order):
- Name of the magnitude
- Name of the current unit
- Label of the current unit

**Example**

```
getsettingvalue 1 2 204: 0000000028
Enumerated
Angular_Velocity
getmagnitudeinfo Angular_Velocity: 0000000039
Angular velocity
Rotation / minute
RPM
```

**Consistency errors specific to the GetMagnitudeInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 122 | 001 | 000 | Magnitude not found. The key is invalid |
| 122 | 002 | 000 | The magnitude does not have current unit |


<!-- page 217 -->

#### 3.5.16 - "SetPreferedWtfReference" command


**Semantics**

Sets the preference (choosing magnitude) for the reference of waterfall or profiles.

**Command syntax**

```
SetPreferedWtfReference <Magnitude identifier>
<Magnitude identifier> can be found in the file « OrosUnit.ini ». (see §
```

#### 3.10.3 - Unit ID table).


**Result returned**

No data follows the header.

**Consistency errors specific to the SetPreferedWtfReference
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 151 | 001 | 000 | Value incorrect for the Magnitude identifier |
| 151 | 002 | 000 | Magnitude not authorized |


<!-- page 218 -->

#### 3.5.17 - "GetPreferedWtfReference" command


**Semantics**

Returns the preference (chosen magnitude) for the reference of waterfall or
profiles.

**Command syntax**

```
GetPreferedWtfReference
```

**Result returned**

The header is followed by the identifier of the magnitude chosen as preference.
Magnitude identifier can be found in the file « OrosUnit.ini ». (see § 3.10.3 - Unit
ID table).

<!-- page 219 -->

#### 3.5.18 - "GetPermission" command


**Semantics**

Indicates whether an external application is authorized to be run, according to the
NVGate key (hardware or dongle).

**Command syntax**

```
GetPermission <Application name>
The external applications currently listed are
- SoundPower
- ServoAnalyzer
- TPASRC
- TPAEMI
- Balancing3
- ORBIGate
```

**Result returned**

A short (2 bytes) equal to 1 if the application can be run, else 0.
Contact OROS for registration of your application in the NVGate® key.

**Consistency errors specific to the GetPermission command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 034 | 001 | 000 | Unlisted external application |


<!-- page 220 -->

#### 3.5.19 - "ChangeMode" command


**Semantics**

Switch between on-line and post-analysis mode.

**Command syntax**

```
ChangeMode <Mode>
Set <Mode> parameter to 1 to switch on post-analysis mode. Set to 0 to switch
off.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ChangeMode command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 062 | 001 | 000 | Wrong value for "Mode" parameter |
| 062 | 002 | 000 | When "Mode" parameter is set to 1 and post-analysis mode<br>is already activated. |
| 062 | 003 | 000 | When "Mode" parameter is set to 0 and post-analysis mode<br>is already disabled. |


<!-- page 221 -->

#### 3.5.20 - "GetAnalyzerModes" command


**Semantics**

Returns the analyzer's modes.

**Command syntax**

```
GetAnalyzerModes
```

**Result returned**

The result returned is as follows:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | short | Equals 0 if the analyzer is On-line<br>Equals 1 if the analyzer is in the Result mode<br>Equals 2 if the analyzer is in post-analysis |
| 2 |   |   | short | Equals 0 if no analyzer is connected (office mode)<br>Equals 1 if one or more analyzers are connected<br>Equals 2 if a frontend device is connected (OR10) |


<!-- page 222 -->

#### 3.5.21 - "GetUserList" command


**Semantics**

Retrieves the list of users.

**Command syntax**

```
GetUserList
```

**Result returned**

The command returns a list of strings pairs (User last name and User first name),
each string ending by character \0.

<!-- page 223 -->

#### 3.5.22 - "GetCurrentUserName" command


**Semantics**

Retrieves the current user name.

**Command syntax**

```
GetCurrentUserName
```

**Result returned**

The command returns a pair (User last name and User first name), ending by
character \0.

<!-- page 224 -->

#### 3.5.23 - "GetPreferenceGeneral" command


**Semantics**

Retrieves the user preferences specified in the "general" tab.

**Command syntax**

```
GetPreferenceGeneral
```

**Result returned**

The result returned is given as follow:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 1 |   |   | Boolean | Confirm Identity |
| 1 |   |   | Boolean | Beep when error |
| 4 |   |   | Unsigned int | Refresh rate |
| 4 |   |   | int | Project to start with (0:Default; 1: Last project; 2:<br>"NVGAte start" window) |
| 1 |   |   | Boolean | Start with default workbook |
| X |   |   | string | Model workbook to start with |
| 1 |   |   | Boolean | Confirm before stopping analysis |
| 4 |   |   | int | Scale font size |
| 4 |   |   | int | Info trace font size |
| 1 |   |   | Boolean | Rotating |
| 1 |   |   | Boolean | Structural |
| 4 |   |   | int | Tab for the "NVGate start" window (0: Quick; 1:<br>Application; 2: Project) |
| 4 |   |   | int | Selected date format (0 : mm-dd-yy, 1 : locale<br>dependent |


<!-- page 225 -->

#### 3.5.24 - "SetPreferenceGeneral" command


**Semantics**

Set a user preference specified in the "general" tab.

**Command syntax**

```
SetPreferenceGeneral < Preference Identifier >
< Preference value >
The <Preference identifier> and <Preference value> are
described in the following table.
No data follows the header.
```

|   | Identifier |   |   | Value Type |   |   | Description |   |
|---|---|---|---|---|---|---|---|---|
| 0 |   |   | Boolean |   |   | Confirm Identity |   |   |
| 2 |   |   | Boolean |   |   | Beep when error |   |   |
| 3 |   |   | Unsigned int |   |   | Refresh rate (0 to 30) |   |   |
| 4 |   |   | int |   |   | Project to start with (0:Default; 1: Last project; 2:<br>"NVGAte start" window) |   |   |
| 5 |   |   | Boolean |   |   | Start with default workbook |   |   |
| 6 |   |   | string |   |   | Model workbook to start with |   |   |
| 1 |   |   | Boolean |   |   | Confirm before stopping analysis |   |   |
| 7 |   |   | int |   |   | Scale font size (6,7,8,9,10,11,12,14,20) |   |   |
| 8 |   |   | int |   |   | Info trace font size (6,7,8,9,10,11,12,14,20) |   |   |
| 9 |   |   | Boolean |   |   | Rotating |   |   |
| 10 |   |   | Boolean |   |   | Structural |   |   |
| 11 |   |   | int |   |   | Tab for the "NVGate start" window (0: Quick; 1:<br>Application; 2: Project) |   |   |
| 12 |   |   | int |   |   | Selected Led bar Size (0: small; 1: large) obsolete |   |   |
| 13 |   |   | Int |   |   | Selected date format (0: mm-dd-yy, 1: locale<br>dependent) |   |   |


**Consistency errors specific to the SetPreferenceGeneral command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 256 | 001 | 000 | Wrong value for "identifier" parameter |
| 256 | 002 | 000 | Wrong value for "value" parameter |


<!-- page 226 -->

#### 3.5.25 - "GetFanInfo" command


**Semantics**

Retrieves the information about fan and hardware temperature.

**Command syntax**

```
GetFanInfo
```

**Result returned**

The result returned is given as follow:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | long | Status of the fan (0: on; 1: auto; 2: off) |
| 4 |   |   | long | Speed of the fan (0 to 2 for the OR34/35 hardware; 0 to 10<br>for the OR36/38 hardware) |
| 4 |   |   | long | Temperature value (expressed in the displayed unit) |


**Consistency errors specific to the GetFanInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 174 | 001 | 000 | Hardware is not connected |
| 174 | 002 | 000 | Error reading hard status |


<!-- page 227 -->

#### 3.5.26 - "SetFanStatus" command


**Semantics**

Set the status of the fan (on / off / automatic).

**Command syntax**

```
SetFanStatus <status>
The <status> can have the following values:
- 0: on, the fan runs with a speed value > 0
- 1: auto, the fan runs if necessary (depends on temperature)
- 2: off, the fan is stopped and the speed value is set to 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetFanStatus command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 176 | 001 | 000 | Hardware is not connected |
| 176 | 002 | 000 | Status value is not valid |
| 176 | 003 | 000 | Error reading hard status |


<!-- page 228 -->

#### 3.5.27 - "SetFanSpeed" command


**Semantics**

Set the speed of the fan (The status of the fan must be "On").

**Command syntax**

```
SetFanSpeed <speed>
The <speed>can have the following values:
- From 1 to 2 for an OR34/35
- From 1 to 10 for an OR36/38
The 0 value cannot be affected because it is reserved to the "Off" status.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetFanSpeed command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 175 | 001 | 000 | Hardware is not connected |
| 175 | 002 | 000 | Error reading hard status |
| 175 | 003 | 000 | Status value is not valid for an OR36/38 |
| 175 | 004 | 000 | Status value is not valid for an OR34/35 |
| 175 | 005 | 000 | Error reading hard type (OR3x). |


<!-- page 229 -->

#### 3.5.28 - "GetMacroList" command


**Semantics**

Get the list of macros.

**Command syntax**

```
GetMacroList
```

**Result returned**

Return a list of strings. Each string ends in the character \0 and is the name of a
macro.

<!-- page 230 -->

#### 3.5.29 - "GetCurrentNVGatePath" command


**Semantics**

Get the path folder of current NVGate.exe

**Command syntax**

```
GetCurrentNVGatePath
```

**Result returned**

Return a string ended in the character \0.

<!-- page 231 -->

#### 3.5.30 - "SetBandState" command


**Semantics**

Open or close the band (at the top of the NVGate main window).

**Command syntax**

```
SetBandState <action>
<action>can have the following values:
- "open" to unfold the band
- "close" or "closed" to fold (minimize) the band
- "toggle" to toggle its state
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetFanSpeed command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 364 | 001 | 000 | Unknown action |


<!-- page 232 -->

#### 3.5.31 - "LogWarning" command


**Semantics**

Display a message in log window warning tab.

**Command syntax**

```
LogWarning <message>
<message> user message to display.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the LogWarning command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 000 | 000 | 000 | No error |


<!-- page 233 -->

### 3.6 - SETTINGS AND STATES CONFIGURATION


#### 3.6.1 - Identification number setting (setting IDN)

The NVGate settings located in the Analyzer setting browser tree are identified by
a specific number called IDN.
An IDN is a text such as:
frontEnd.input2.label
recorder.track6.inputFilter
fft1.channel5.active
tda.892:1.418
frontEnd.input129
fft3
In previous NVGate versions, an IDN was specified as a triplet of numbers:
<Module num>.<Sub-module num>.<Setting num>
This old, number-based way of specifying an IDN is still supported and is
perfectly backward-compatible, with the caveat that it is limited to 32 channels.
Thus, it is advised to use the new text-based of IDNs to leverage the NVGate
ability to deal with a large number of channels.
You can retrieve the IDN of any setting from NVGate software using the
"Shift + Right Click" combination on the required setting. Both the old and new
form of the IDN are provided:

<!-- page 235 -->

#### 3.6.2 - Identification number state (state IDN)

The NVGate states are also identified by an IDN number. Both the new text-based
IDN and the old number-based IDN are supported.
These states are not visible in the Analyzer Setting Browser, but can be added in
the Control Panel.
You may retrieve the IDN of any state from NVGate software clicking on the
Customize Control Panel button while holding pressed the "Shift" key.
In the Customize Control Panel dialog, the status tab displays a tree with all the
states available. The identification number is added to the name of the states, as
shown on next picture.

#### 3.6.3 - Specifying IDNs in NVDrive commands

In order to maintain full backward-compatibility of NVDrive commands, many commands
require three parameters:
<Module num>
<Sub-module num>

<!-- page 236 -->
<Setting num>
Such commands can be invoked with an old number-based IDN, but they can be called with a
new text-based IDN just as well. Here are several examples that are all valid and semantically
equivalent:
SetSettingValue 1 3 1 example
SetSettingValue frontEnd input3 label example
SetSettingValue frontEnd.input3.label "" "" example
SetSettingValue 1.3.1 "" "" example
We just used "" as a way to let a parameter empty, ensuring that the correct number of
parameters are always provided. In this way, the IDN can be expressed as a unique parameter.
Sometimes, instead of three parameters, only one or two are required. It is the case when the
command needs to identify a module (FFT1, SOA2 etc...) or a submodule (channel1 of FFT1,
channel4 of TDA, etc...). In these cases the same principle is applied:
SetToDefaultCollection 11 501
SetToDefaultCollection fft2 channel1
SetToDefaultCollection fft2.channel1 ""
GetAnalyzerState 11
GetAnalyzerState fft2
Some NVDrive command have specificities, in which case they are described in the command
documentation.

#### 3.6.4 - Teamwork IDN

NVGate Teamwork manages several OR3x analyzers as if there was only one, using a chain
of analyzers. For example, using NVGate Teamwork with 3 x OR38 of 32 channels each will
present 96 channels to the user.
NVDrive can access these 96 channels in the classical way:
SetSettingValue frontEnd input1 label inputA1
SetSettingValue frontEnd input32 label inputA32
SetSettingValue frontEnd input33 label inputB1
SetSettingValue frontEnd input96 label inputC32
However, it is sometimes usefull to know the physical channel associated to each of these
channel. For example, channel 96 matches the channel 32 of the third analyzer in the chain.
NVDrive can convert this "channel 96" to "third analyzer channel 32" and back, using a
setting named xref (cross-reference).
For example, the following command will return "slave2.frontEnd.input32":
GetSettingValue frontEnd input96 xref
And the following command will return "frontEnd.input96":
GetSettingValue slave2.frontEnd input32 xref

<!-- page 237 -->
As shown above, an IDN can be prefixed with the identification of the analyzer in the chain,
when such a concept makes sense. For example, the following IDN are all valid, and all point
to different settings:
frontEnd.input2.xref
master.frontEnd.input2.xref
slave1.frontEnd.input2.xref
slave2.frontEnd.input2.xref
Furthermore, most NVDrive commands can be invoked with an IDN including the analyzer
identifier, as well as with the classical unprefixed IDN. For example, these call are all
equivalent, and the caller can choose the most convenient way:
SetSettingValue frontEnd input96 label inputC32
SetSettingValue slave2.frontEnd input32 label inputC32
Finally, some settings are accessible in NVGate Teamwork to get information about specific
analyzers in the chain. For example, to get the activation, serial number, system short name,
system long name, system model, and disk used space of the third system in the chain:
GetSettingValue frontEnd system3 active
GetSettingValue frontEnd system3 482
GetSettingValue frontEnd system3 483
GetSettingValue frontEnd system3 484
GetSettingValue frontEnd system3 485
GetSettingValue slave2.frontEnd inputSettings 494

<!-- page 238 -->

#### 3.6.5 - "GetSettingValues" command


**Semantics**

Returns the possible values of a setting

**Command syntax**

```
GetSettingValues <Module num>
<Sub-module num>
<Setting num>
The 3 parameters identifying the IDN setting (see § 3.6.3 - ).
```

**Result returned**

The header is followed by the type of setting, in the form of a character string
ending in the character \0. Possible types are:
- Boolean
- String
- Scalar
- Signal file
- Enumerated
- Action
- ActionBis
- Equation
- MultiSources
For the enumerated types, the list of possible values follows the type. This list
comes in the form of a series of pairs <key, value>. Each key is a string ending in
the character \0 identifying a possible setting value. This is the key that is passed
as a parameter of the SetSettingValue command. The associated value is a string
ending in the character \0 indicating the value corresponding to the key.
For the multisources type, the number of selected channels (short) and a set of
channel number (short) follow the type.

**Consistency errors specific to the GetSettingValues command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 027 | 001 | 000 | Setting unknown |
| 027 | 002 | 000 | Type of setting not managed by the command |


<!-- page 239 -->

#### 3.6.6 - "GetSettingValue" command


**Semantics**

Returns the setting value

**Command syntax**

```
GetSettingValue <Module num>
<Sub-module num>
<Setting num>
[Line num]
[Column num]
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting (see § 3.6.3 - ).
The 2 optional parameters identify a setting in an array. The [Line num] varies
from 0 to 7. The [Column num] varies from 0 to 2. The settings in array are
Boolean (column 0) or Scalar (column 1 and 2).
```

**Result returned**

The header is followed by the type of setting, in the form of a character string
ending in the character \0. Possible types are:
- Boolean
- String
- Scalar
- Signal file
- Enumerated
- ActionBis
- Matrix
- Equation
- MultiSources
The type of setting is followed by the setting value:

| Setting type | Value returned |
|---|---|
| Boolean | short (2 bytes) equal to 0 or 1 |
| String | character string ending in the character \0 |
| Scalar | float (4 bytes) |
| Signal file | character string ending in the character \0 representing the name<br>of the signal file |
| Enumerated | character string ending in the character \0 representing the value<br>key |
| ActionBis | short (2 bytes) equal to 0 or 1 |
| Matrix | character string ending in the character \0 representing the list of<br>couples selected in the matrix (ex: 1;2\|5;7\|3;8) |
| Equation | character string ending in the character \0. Line endings are<br>replaced by a "\|" character. |
| MultiSources | Set of short (2 bytes) representing the list of selected channels<br>[1..32] |


<!-- page 240 -->
The parameters of the virtual tach can be read thanks to this command. The
Virtual tach setting has the identification number 304. It cannot be interrogated
directly. Replace this number by one of the following to get the value of a
parameter. The value return is of type "Scalar".
Ex : GetSettingValue 6 171 302
This command get the tach ratio of the first virtual tach.
NB : Do not use those identifiers with the SetSettingValue command. The "3.6.12
- SetVirtualTachoSettingValue" must be used to modify the parameters of the
virtual tach.

| Error code | Meaning |
|---|---|
| Numerator1 | 298 |
| Denominator1 | 300 |
| Numerator2 | 299 |
| Denominator2 | 301 |
| Tach ratio | 302 |


**Consistency errors specific to the GetSettingValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 032 | 001 | 000 | Setting unknown |
| 032 | 002 | 000 | Type of setting not managed by the command |
| 032 | 003 | 000 | Incorrect line num or column num. |


<!-- page 241 -->

#### 3.6.7 - "SetSignalFileSettingValue" command


**Semantics**

Assigns a value to a signal file type setting.

**Command syntax**

```
SetSignalFileSettingValue <Module num>
<Sub-module num>
<Setting num>
[Project name]
[Measurement name]
[PerformCheck]
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ). The IDN of the player signal in NVGate
is 4.90.233.
The first 2 optional parameters are the [Project name] and the
[Measurement name] of the signal file. Omitting those parameters enables
to do a "Set to Defaut" on this setting (in order to setup that no signal is connected
to the player). But it is better to use the "SetToDefault" command.
[PerformCheck] parameter enables to skip the project and measurement
existence checking. This check can be time consuming, and may not be necessary
if the project and measurement name are valid. The default value is 1
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetSignalFileSettingValue
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 029 | 001 | 000 | Setting unknown |
| 029 | 002 | 000 | The setting is not of the signal file type: use the<br>SetSettingValue command |
| 029 | 003 | 000 | Project unknown |
| 029 | 004 | 000 | Measurement unknown |
| 029 | 005 | 000 | No signal file in the specified measurement |
| 029 | 006 | 000 | PerformCheck value is not correct |
| 029 | 008 | 000 | Real time is not guaranted for current analysis setting (since<br>NVGate V6.20) |
| 029 | 009 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (since NVGate V6.20) |


<!-- page 242 -->

#### 3.6.8 - "SetSettingValue" command


**Semantics**

Assigns a value to a simple type (Boolean, string, scalar), enumerated type
(enumerated), matrix type setting, action type, actionbis type or multisources type.

**Command syntax**

```
SetSettingValue <Module num>
<Sub-module num>
<Setting num>
<Value>
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting (see § 3.6.3 - ).
For enumerated types, the value is defined by a key, obtained via the 3.6.5 -
GetSettingValues command.
For matrix type, the value is a string defined as follow:
Each couple consists of a channel number + ";" + the other channel number (the
order is not important between response and reference). The separation between
two couples is a "|". There is no space in this string.
Example: SetSettingValue 10 363 205 1;2|5;7|3;8
This means that the FFT1 cross-spectrum is activated for Channel1 * Channel2
and for Channel5 * Channel7 and for Channel3 * Channel8.
For equation type, the value is a formula, which can be multi-line. Lines must be
separated using "|" character.
For multiSources type, the value is a set of channel number [1..32] separated by
";".
Example: SetSettingValue 23 879 446 1;2;7;32
To change the value of a signal file type setting, the 3.6.7 -
SetSignalFileSettingValue command must be used.
To change the value of a virtual tach type setting, the 3.6.12 -
SetVirtualTachoSettingValue command must be used.
Submodules inside a collection use a special hidden boolean setting, "State",
which can be used to activate/desactivate the submodule. "State" setting number
is 2.
```

**Example**

```
"SetSettingValue 7 225 2 1" activates Sine 1 (old number-based IDN)
"SetSettingValue generator 225:1 state 1" activates Sine 1 (new text-based IDN).
"SetSettingValue 1 1 2 0" desactivates Input 1 (old number-based IDN)
"SetSettingValue frontEnd input1 state 1" activates Input 1 (new text-based IDN)
```

<!-- page 243 -->
```
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetSettingValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 028 | 001 | 000 | Setting unknown |
| 028 | 002 | 000 | Value incorrect |
| 028 | 003 | 000 | Signal file or virtual tach type setting: use the<br>SetSignalFileSettingValue or<br>SetVirtualTachoSettingValue command. |
| 028 | 004 | 000 | Other type of setting not managed by the command |
| 028 | 005 | 000 | The action is already in course |
| 028 | 006 | 000 | Real time is not guaranted for current analysis setting (since<br>NVGate V6.20) |
| 028 | 007 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (since NVGate V6.20) |
| 028 | 008 | 000 | Too many sources for "multisources" setting (limited to 12) |


<!-- page 244 -->

#### 3.6.9 - "GetSettingInfo" command


**Semantics**

Returns various information about a setting

**Command syntax**

```
GetSettingInfo <Module num>
<Sub-module num>
<Setting num>
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ).
```

**Result returned**

The header contains the size of the data returned
The command returns 5 strings, ending by the character \0.
- The first string contains the name of the setting displayed in NVGate.
- The second string contains the value of the setting, displayed in NVGate
Analyzer Setting Browser. This string should be used only for information,
use GetSettingValue if you need to handle the value of a setting, taking care
its specific format.
- The third string describes the style of a setting: it can be one of these 3
values:
- "Not visible": This setting is not currently visible in NVGate. Its value
should not be read or used.
- "Fixed": The setting cannot be modified. It is represented with the
symbol "i" in the analyzer setting brower.
- "Normal": The setting is accessible in the ASB.
- The fourth string contains information about the effect of the setting and
should not be of any interest for external applications.
- The fifth string indicates that the setting is actually visible in NVGate. The
reasons a setting cannot be seen are:
- Its style is invible (setting 1 1 2 that drives the activation of the input 1)
- It belongs to an inactive sub-module (setting 1 1 1 representing the label
of the input 1, is visible once input1 is activated
- It is hidden because unsignificant at this moment (setting of the Front-
end while the analyzer is in post-analysis mode)

**Consistency errors specific to the GetSettingInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 188 | 001 | 000 | Setting unknown |


<!-- page 245 -->

#### 3.6.10 - "GetSubModuleList" command


**Semantics**

Returns idn string list of a specified collection.

**Command syntax**

```
GetSubModuleList <Sub-module string>
The <Sub-module string> parameter identify the setting IDN (see § 3.6.3 -
).
```

**Result returned**

The header contains the size of the data returned
The string "Version 1.0\n".
The command returns all idn strings, each of them is ending by the character \n.
Ending by the character \0.
For example:
GetSubModuleList frontEnd.input1
Returns:
- The size of string returned
- Version 1.0\n
- frontEnd.input1\nfrontEnd.input2\n.frontEnd.input3 ...

**Consistency errors specific to the GetSubModuleList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 340 | 001 | 000 | Module unknown |


<!-- page 246 -->

#### 3.6.11 - "GetSignalFileSettingValues" command


**Semantics**

Retrieve the list of available measures that could be affected to a signal file type
setting.

**Command syntax**

```
GetSignalFileSettingValues <Module num>
<Sub-module num>
<Setting num>
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ). The IDN of the player signal in NVGate
is 4.90.233.
```

**Result returned**

The header contains the number of pairs: project name - measure name.
The command returns a list of strings pairs (project name and measure name),
each string ending by character \0.

**Consistency errors specific to the GetSignalFileSettingValues
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 201 | 001 | 000 | Setting unknown |
| 201 | 002 | 000 | The setting is not of the signal file type: use the<br>SetSettingValue command |


<!-- page 247 -->

#### 3.6.12 - "SetVirtualTachoSettingValue" command


**Semantics**

Assigns the 4 values which determine the tach ratio setting.

**Command syntax**

```
SetVirtualTachoSettingValue <Tach number>
<Numerator1>
<Denominator1>
<Numerator2>
<Denominator2>
The <Tach number> parameter identifies the number of the virtual tach (from
1 to 4).
The following parameters are the values which determine the tach ratio.
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
The tach ratio value must be lower or equal to 2, and higher or equal to 0.001.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetVirtualTachoSettingValue
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 116 | 001 | 000 | Setting unknown |
| 116 | 002 | 000 | The values are not available (the ratio value must be<br>between 0.001 and 2). |


<!-- page 248 -->

#### 3.6.13 - "SetForceSettings" command


**Semantics**

Modify settings of response setting.

**Command syntax**

```
SetForceSettings [Window start]
[Window stop]
The 2 parameters are optional. If a parameter is not specified, the corresponding
setting is not modified. The values must be specified in percent and must be in
range [0,100].
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetForceSettings command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 056 | 001 | 000 | Setting not available |
| 056 | 002 | 000 | Values are not consistent |


<!-- page 249 -->

#### 3.6.14 - "SetResponseSettings" command


**Semantics**

Modify settings of response setting.

**Command syntax**

```
SetResponseSettings [Window stop]
[Flat top start]
[Flat top stop]
[Decreasing point X-coordinate]
[Decreasing point Y-coordinate]
All parameters are optional. If a parameter is not specified, the corresponding
setting is not modified. The values must be specified in percent and must be in
range [0,100].
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetResponseSettings command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 057 | 001 | 000 | Setting not available |
| 057 | 002 | 000 | Values are not consistent |


<!-- page 250 -->

#### 3.6.15 - "SetDualExponentialSettings" command


**Semantics**

Modify settings of response setting.

**Command syntax**

```
SetDualExponentialSettings [Window start]
[Window stop]
[Flat top start]
[Flat top stop]
[Decreasing point X-coordinate]
[Decreasing point Y-coordinate]
[Rising point X-coordinate]
[Rising point Y-coordinate]
All parameters are optional. If a parameter is not specified, the corresponding
setting is not modified. The values must be specified in percent and must be in
range [0,100].
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetDualExponentialSettings
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 058 | 001 | 000 | Setting not available |
| 058 | 002 | 000 | Values are not consistent |


<!-- page 251 -->

#### 3.6.16 - "AddArrayLine" command


**Semantics**

Add a new line to the selected array.

**Command syntax**

```
AddArrayLine <Module num>
<Sub-module num>
<Setting num>
<Line number>
<State value>
<Order number>
[Bandwidth]
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - )..
This command must be applied to an Array. Arrays in NVGate contain a state
value (On/Off), an order number, and a bandwidth (for arrays in FFT plug-in).
The <Line number> parameter is ignored. The new line is always added
at the end of the array.
The <State value> parameter identifies the state of the order: 0 = Off and 1 =
On.
The <Order number> parameter identifies the order number, which is a float.
The [Bandwidth] optional parameter can be used for the FFT order arrays. It
identifies the bandwidth to apply to this order. It is a float that will be adjusted to
an available value. If this parameter is missing, the default value of the bandwidth
is applied.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddArrayLine command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 075 | 001 | 000 | Setting unknown |
| 075 | 002 | 000 | Line number incorrect |
| 075 | 003 | 000 | State value incorrect |
| 075 | 004 | 000 | Order value incorrect |
| 075 | 005 | 000 | Bandwidth value incorrect |
| 075 | 006 | 000 | The setting is not an array |
| 075 | 007 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 075 | 008 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 252 -->

#### 3.6.17 - "ModifyArrayLine" command


**Semantics**

Modify a specified line to the selected array.

**Command syntax**

```
ModifyArrayLine <Module num>
<Sub-module num>
<Setting num>
<Line number>
<State value>
<Order number>
[Bandwidth]
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ).
This command must be applied to an Array. Arrays in NVGate contain a state
value (On/Off), an order number, and a bandwidth (for arrays in FFT plug-in).
The <Line number> parameter specified the line number. If this line does not
exist, a new line is added at the end of the array and modified by the next
parameters.
The <State value> parameter identifies the state of the order: 0 = Off and 1 =
On.
The <Order number> parameter identifies the order number, which is a float.
The [Bandwidth] optional parameter can be used for the FFT order arrays. It
identifies the bandwidth to apply to this order. It is a float that will be adjusted to
an available value. If this parameter is missing, the default value of the bandwidth
is applied.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ModifyArrayLine command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 287 | 001 | 000 | Setting unknown |
| 287 | 002 | 000 | Line number incorrect |
| 287 | 003 | 000 | State value incorrect |
| 287 | 004 | 000 | Order value incorrect |
| 287 | 005 | 000 | Bandwidth value incorrect |
| 287 | 006 | 000 | The setting is not an array |


<!-- page 253 -->

#### 3.6.18 - "RemoveArrayLine" command


**Semantics**

Remove a line of the selected array.

**Command syntax**

```
RemoveArrayLine <Module num>
<Sub-module num>
<Setting num>
<Line number>
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ).
This command must be applied to an Array.
The <Line number> parameter identifies the position of the line to delete. It
varies from 0 to 7.
If the value is set to -1, all the lines are removed.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveArrayLine command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 077 | 001 | 000 | Setting unknown |
| 077 | 002 | 000 | The line number is not valid |
| 077 | 003 | 000 | The setting is not an array |
| 077 | 004 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 077 | 005 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 254 -->

#### 3.6.19 - "EditSetting" command


**Semantics**

Edit in a dialog, the specified setting's properties.

**Command syntax**

```
EditSetting <Module num>
<Sub-module num>
<Setting num>
[EditCollection]
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ).
[EditCollection] must be set to 1 to edit the collection of a sub-module
specified by the first 3 parameters.
```

**Result returned**

The header is followed by value returned by the edit dialog :

| Size<br>(bytes) |   | Type | Description |
|---|---|---|---|
|   |   | short | Value returned by the edit dialog :<br>- 1 : OK<br>- 2 : CANCEL<br>- 10 : The collection have no child so the dialog was not open<br>- 11 : The setting's value is fixed so the dialog was not open |


**Consistency errors specific to the EditSetting command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 126 | 001 | 000 | Setting unknown |
| 126 | 002 | 000 | Setting not present in the ASB |
| 126 | 003 | 000 | Setting is not a sub-module (with EditCollection sets to 1) |
| 126 | 004 | 000 | No collection associated (with EditCollection sets to 1) |


<!-- page 255 -->

#### 3.6.20 - "SetToDefault" command


**Semantics**

Set the specified element to its default value. The element may be a setting, a sub-
module or a module.
In the case of module or sub-module, all the settings of this element are set to
their default value.

**Command syntax**

```
SetToDefault <Module num>
<Sub-module num>
<Setting num>
The <Module num>.<Sub-module num>.<Setting num> parameters
identify the setting IDN (see § 3.6.3 - ).
Ex: SetToDefault 10 0 0 -> is applied to the FFT1 module
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetToDefault command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 139 | 001 | 000 | Setting unknown |
| 139 | 002 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |


<!-- page 256 -->

#### 3.6.21 - "SetToDefaultCollection" command


**Semantics**

Set the specified element to its default value. The element may be a setting, a sub-
module or a module.
In the case of module or sub-module, all the settings of this element are set to
their default value.

**Command syntax**

```
SetToDefaultCollection <Module num>
<Sub-module num>
The <Module num>.<Sub-module num> parameters identify the IDN of
the first submodule in the collection (see § 3.6.3 - ).
Ex: SetToDefaultCollection frontEnd input1 -> is applied to the Front-End
Input collection
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetToDefaultCollection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 267 | 001 | 000 | Collection unknown |


<!-- page 257 -->

#### 3.6.22 - "GetInputInfo" command


**Semantics**

Get information about front end inputs (dynamic inputs, DC inputs, Ext Sync...).

**Command syntax**

```
GetInputInfo <Sub-module num>
The <Sub-module num> parameters identify the IDN of the first submodule
in the collection (see § 3.6.3 - ).
Ex: GetInputInfo input1 -> is applied to the Front-End Input collection
GetInputInfo 33 -> is applied to the Front-End DC Input collection
```

**Result returned**

The header contains the size of the data returned
The command returns 2 short :
- Number of input available : short
- Sub-Module number of the first input : short

**Consistency errors specific to the GetInputInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 291 | 001 | 000 | Collection unknown |


<!-- page 258 -->

#### 3.6.23 - "ConnectInput" command


**Semantics**

Connects a front-end input (or player track, in post-analysis mode) to an analyzer
channel.

**Command syntax**

```
ConnectInput <Input number>
<Module number>
<Channel number>
<Input number> is the number of the front-end input / player track to
connect.
<Analyzer number> is the number of the target analyzer (see § 3.6.3 - ).
<Analyzer channel number> is the number of the target analyzer channel.
```

**Examples**

```
ConnectInput 1 10 3
-> Connect Input1 (or player track1) on FFT1 Channel3.
ConnectInput frontEnd.input1 ff1 channel3
-> Connect Input1 on FFT1 Channel3.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ConnectInput command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 030 | 001 | 000 | Invalid Input / track number |
| 030 | 002 | 000 | Analyzer number unknown |
| 030 | 003 | 000 | Channel number not valid |
| 030 | 004 | 000 | Connection has failed |
| 030 | 005 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 030 | 006 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 259 -->

#### 3.6.24 - "DisconnectInput" command


**Semantics**

Disconnect a front-end input in on-line mode, a player track in post-analysis
mode.

**Command syntax**

```
DisconnectInput [Input number]
[Input number] is the number of the front-end input / player track to
disconnect.
It is an optional parameter. If it's not specified, all front-end inputs / player tracks
are disconnected.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DisconnectInput command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 065 | 001 | 000 | Invalid front-end input / player track number |
| 065 | 002 | 000 | Front-end input / player track already disabled |
| 065 | 003 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 065 | 004 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 260 -->

#### 3.6.25 - "SelectWtfChannels" command


**Semantics**

Connect the selected result to a waterfall channel.

**Command syntax**

```
SelectWtfChannels <Process number>
<Module number>
<Response channel number>
[Reference channel number]
The <Process number>, <Module number>, <Response channel
number> and [Reference channel number] determines a result. To
connect a result to a waterfall channel, the result must already exist (Response and
Reference channels must be connected to the result).
The [Reference channel number] is an optional parameter (it may or
may not exist according to the result type).
Some results cannot be individually connected to the Waterfall. Specific Process
numbers include those special cases.
For example, the command SelectWtfChannels 2 10 1 connect the result
AVERAGE SPECTRUM on channel no 1 of the FFT1 module.
```

**Result returned**

No data follows the header.

| Specific Processes | Process<br>number | Included processes |
|---|---|---|
| Overall Levels<br>(obsolete) | 29 | DC, RMS, Min, Max, Skew, Kurtosis |
| Orders | 44 | Order 1 to 8 and Overall. |
| OVA | 46 |   |
| 1/Nth Octave | 131 | Min, Max, Avg |


**Consistency errors specific to the SelectWtfChannels command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 086 | 001 | 000 | Process number incorrect (not included in the process<br>number table) |
| 086 | 002 | 000 | Response channel number incorrect (number not included<br>between 1 and 32) |
| 086 | 003 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 086 | 004 | 000 | The selected Process and Module are not compatible. |
| 086 | 005 | 000 | The selected result is already connected to the waterfall. |
| 086 | 006 | 000 | The Response channel is not connected to the selected<br>result. |
| 086 | 007 | 000 | The Reference channel is not connected to the selected<br>result. |


<!-- page 261 -->

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
|   | 008 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
|   | 009 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 262 -->

#### 3.6.26 - "UnSelectWtfChannels" command


**Semantics**

Disconnect the selected result from a waterfall channel.

**Command syntax**

```
UnSelectWtfChannels <Process number>
<Module number>
<Response channel number>
[Reference channel number]
The <Process number>, <Module number>, <Response channel
number> and [Reference channel number] determines the result to
disconnect from the waterfall. To disconnect a result from a waterfall channel, the
result must already exist (Response and Reference channels must be connected to
the result).
The [Reference channel number] is an optional parameter (it may or
may not exist according to the result type).
For example, the command UnSelectWtfChannels 2 10 1 disconnect the result
AVERAGE SPECTRUM on channel no 1 of the FFT1 module.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SelectWtfChannels command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 086 | 001 | 000 | Process number incorrect (not included in the process<br>number table) |
| 086 | 002 | 000 | Response channel number incorrect (number not included<br>between 1 and 32) |
| 086 | 003 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 086 | 004 | 000 | The selected Process and Module are not compatible. |
| 086 | 005 | 000 | The selected result is not connected to the waterfall. |
| 086 | 006 | 000 | The Response channel is not connected to the selected<br>result. |
| 086 | 007 | 000 | The Reference channel is not connected to the selected<br>result. |
| 086 | 008 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 086 | 009 | 000 | Limits of DSP power have been reached. The previous valid<br>configuration has been restored (from the version 6.20) |


<!-- page 263 -->

#### 3.6.27 - "GetTEDSContentOnInput" command


**Semantics**

Retrieve the data buffer included in the TEDS transducer of the specified input.

**Command syntax**

```
GetTEDSContentOnInput <input number>
<input number> is the number of the front-end input.
Before using this command, ensure you called CheckTEDS command to have an
updated buffer.
```

**Result returned**

The returned value is the size of the TEDS buffer sent after it. This buffer includes
the whole of TEDS data (basic TEDS included).

**Consistency errors specific to the GetTEDSContentOnInput command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 193 | 001 | 000 | Input number incorrect |
| 193 | 002 | 000 | No transducer on selected input. |
| 193 | 003 | 000 | The transducer on the input is not a TEDS. |
| 193 | 004 | 000 | TEDS buffer is empty. |


<!-- page 264 -->

#### 3.6.28 - "GetTEDSContent" command


**Semantics**

Retrieve the data buffer included in the specified TEDS transducer.

**Command syntax**

```
GetTEDSContent <transducer identifier>
The <transducer identifier> parameter enables to identify the
transducer whose information is searched.
Before using this command, ensure you called CheckTEDS command to have an
updated buffer.
```

**Result returned**

The returned value is the size of the TEDS buffer sent after it. This buffer includes
the whole of TEDS data (i.e. basic TEDS - as described in IEE1451.4 - included).

**Consistency errors specific to the GetTEDSContent command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 192 | 001 | 000 | Unknown transducer. |
| 192 | 002 | 000 | The selected transducer is not a TEDS. |
| 192 | 003 | 000 | TEDS buffer is empty. |


<!-- page 265 -->

#### 3.6.29 - "GetTransducerList" command


**Semantics**

Retrieves the list of identifiers of transducers of a given type.

**Command syntax**

```
GetTransducerList [Transducer type number]
The [Transducer type number] is an optional parameter. If it is not
entered, the identifiers of all the transducers are returned, in type distinction.
The transducer type is represented by a number:
```

**Result returned**

The header contains the number of pairs : identifier - name.
Returns a list of pairs <identifier,name>
The identifier is a character string ending in the character \0.
The name is a character string ending in the character \0.
There is no specific error for this command. The header contains the size (in
number of bytes) of the result returned.
An identifier can be passed as a parameter of the 3.6.30 - GetTransducerInfo
command, to retrieve information on a specific transducer.

|   | Transducer type |   |   | Number |   |
|---|---|---|---|---|---|
| Microphone |   |   | 1 |   |   |
| Accelerometer |   |   | 2 |   |   |
| Voltmeter |   |   | 3 |   |   |
| Ammeter |   |   | 4 |   |   |
| Velocity sensor |   |   | 5 |   |   |
| Tachometer |   |   | 6 |   |   |
| Displacement sensor |   |   | 7 |   |   |
| Pressure sensor |   |   | 8 |   |   |
| Force sensor |   |   | 9 |   |   |


<!-- page 266 -->

#### 3.6.30 - "GetTransducerInfo" command


**Semantics**

Retrieves the information from a given transducer.

**Command syntax**

```
GetTransducerInfo <transducer identifier>
[Version]
The <transducer identifier> parameter enables to identify the
transducer whose information is searched.
A transducer identifier can be retrieved using the 3.6.29 - GetTransducerList
command.
If the optional [Version] parameter is set to one, the commands return
additional information about the last calibration of the transducer. If the optional
Version parameter is set to two, the commands return additional information
about the last calibration of the transducer and the applied sensitivity during a
connection to an input (factory or last calibration).
```

**Result returned**

The information on the transducer following the header is as follows (in order):

|   | Info |   |   | type |   |
|---|---|---|---|---|---|
| Transducer name |   |   | Character string ending in the character<br>'\0' |   |   |
| Manufacturer's name |   |   | Character string ending in the character<br>'\0' |   |   |
| Model name |   |   | Character string ending in the character<br>'\0' |   |   |
| Serial number |   |   | Character string ending in the character<br>'\0' |   |   |
| Coupling type |   |   | Character string ending in the character<br>'\0' |   |   |
| Sensitivity supplied by manufacturer and<br>given in the current unit |   |   | 4-byte float |   |   |
| Abbreviation of the sensitivity current unit |   |   | Character string ending in the character<br>'\0' |   |   |
| Offset supplied by manufacturer and given<br>in the current unit |   |   | 4-byte float |   |   |
| Abbreviation of the offset current unit |   |   | Character string ending in the character<br>'\0' |   |   |
| Year of last calibration |   |   | 4-byte unsigned integer<br>Equals 0 if no calibration has been<br>performed |   |   |
| Number of month of last calibration |   |   | 4-byte unsigned integer<br>Equals 0 if no calibration has been<br>performed |   |   |
| Number of day of last calibration |   |   | 4-byte unsigned integer<br>Equals 0 if no calibration has been<br>performed |   |   |


<!-- page 267 -->
If Version = 1:
If Version = 2:

| Comments | Character string ending in the character<br>'\0' |
|---|---|


| Info |   |   | type |   |
|---|---|---|---|---|
| Last calibration sensitivity |   | 4-byte float |   |   |
| Last calibration Offset |   | 4-byte float |   |   |
| User who has done the last calibration |   | Character string ending in the character<br>'\0' |   |   |
| Analyzer used for the last calibration |   | Character string ending in the character<br>'\0' |   |   |
| Input used for the last calibration |   | Character string ending in the character<br>'\0' |   |   |
| Name of the calibrator used for the last<br>calibration |   | Character string ending in the character<br>'\0' |   |   |


| Info |   |   | type |   |
|---|---|---|---|---|
| Applied sensitivity |   | 1-byte Boolean<br>Equals 1 for factory sensitivity<br>Equals 0 for last calibration sensitivity |   |   |


**Consistency errors specific to the GetTransducerInfo command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 031 | 001 | 000 | Transducer unknown |


<!-- page 268 -->

#### 3.6.31 - "AddCalibration" command


**Semantics**

Add new values for calibration.

**Command syntax**

```
AddCalibration <Transducer Identifier>
<Sensitivity>
<Offset>
<Calibration type>
<Input name>
[User name]
[Calibrator name]
The <Transducer Identifier> is described in the 3.6.29 -
GetTransducerList command.
The <Sensitivity> parameter corresponds to the transducer sensitivity
expressed in the current unit.
The <Offset> parameter corresponds to the transducer offset expressed in the
current unit.
The <Calibration type> is an integer corresponding to the following cases:
- Manual calibration 0
- Acoustic calibration 1
- Accelerometer calibration 2
- A * x + B calibration 3
- Frequency calibration 4
- Initial factory calibration 5
- Update factory calibration 6
The <Input name> parameter is the name of the input on which the
transducer is connected to during the calibration.
The [User name] parameter is optional and indicates the name of the user.
The [Calibrator name]parameter is optional and indicates the name of the
calibrator.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddCalibration command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 095 | 001 | 000 | Transducer unknown |
| 095 | 002 | 000 | Sensitivity value not valid |
| 095 | 003 | 000 | Offset value not valid |
| 095 | 004 | 000 | Calibration type not valid |


<!-- page 269 -->

#### 3.6.32 - "SetTransducerAppliedSensitivity" command


**Semantics**

Specify the applied sensitivity (factory or last calibration).

**Command syntax**

```
SetTransducerAppliedSensitivity <Transducer Identifier>
<Factory/Current>
The <Transducer Identifier> is described in the 3.6.29 -
GetTransducerList command.
The <Factory/Current> parameter will be factory sensitivity (if = 1) or last
calibration sensitivity (if = 0) will be applied during a connection to an input.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the SetTransducerAppliedSensitivity
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 190 | 001 | 000 | Transducer unknown |


<!-- page 270 -->

#### 3.6.33 - "GetEvent" command


**Semantics**

Informs you whether an event has appeared since its last consultation or since the
start of the connection if this event has not yet been consulted. Event state is
memorized on the server. An event is reset to "not appeared" as from when the
user consults its value with GetEvent.

**Command syntax**

```
GetEvent <Event name>
The following <Event name> are defined:
```

**Result returned**

Returns a short (2 bytes) which equals 1 if the event has appeared, else 0.

| Event name |   | Semantics |
|---|---|---|
| MeasureStarted | Trigged on launching a measurement |   |
| MeasureStopped | Trigged on stopping a measurement |   |


**Consistency errors specific to the GetEvent command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 003 | 001 | 000 | Event unknown |


<!-- page 271 -->

#### 3.6.34 - "ResetEvents" command


**Semantics**

Initializes all the events to « not appeared ».

**Command syntax**

```
ResetEvents
```

**Result returned**

No data follows the header.

<!-- page 272 -->

#### 3.6.35 - "GetStatus" command


**Semantics**

Returns the application status.

**Command syntax**

```
GetStatus
```

**Result returned**

The result returned is as follows:

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | short | Equals 1 if a measurement is in progress, else 0 |
| 2 |   |   | short | Equals 0 if no analyzer is connected (office mode)<br>Equals 1 if one or more analyzers are connected<br>Equals 2 if a frontend device is connected (OR10) |


<!-- page 273 -->

#### 3.6.36 - "GetGeneralAnalyzerState" command


**Semantics**

Returns the state of NVGate analyzer.

**Command syntax**

```
GetGeneralAnalyzerState
The possible states are:
```

**Result returned**

The result returned is given as follow:

| value | State name | Description |
|---|---|---|
| 0 | Unknown |   |
| 3 | Running | Include recording and triggering |
| 4 | Stopped |   |
| 6 | Paused |   |
| 9 | Calibrating |   |
| 11 | Armed | Armed while waiting for a recording |


|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | short | Status of the analyzer |


<!-- page 274 -->

#### 3.6.37 - "GetAnalyzerState" command


**Semantics**

Returns the state of the selected plug-in.

**Command syntax**

```
GetAnalyzerState <Module number>
[State name]
The default value of StateName is "Trigger State". The different State Names are
defined in the following Array.
```

**Result returned**

The header is followed by the state value, in form of a float (4 bytes), an unsigned
int (4 bytes), or a character string ending in the character \0.

| State name |   | Type of value |   | Possible values |
|---|---|---|---|---|
|   |   | returned |   |   |
| Trigger state | String |   |   | Running<br>Recording (for recorder only)<br>Triggering<br>Bloc triggering<br>Waiting<br>Paused<br>Stopped |
| Count | Float |   |   | number |
| Real-time | String |   |   | Ok : (real-time presently)<br>- : (no real-time in the past<br>and real-time presently)<br>No : (no real-time presently) |
| Block overload | String |   |   | No overload<br>Overload on channel: x |
| Analysis overload | String |   |   | No overload<br>Overload on channel: x |
| Record counter | Unsigned int |   |   | number |
| Time to stabilization | Float |   |   | number |
| % Block lost | Float |   |   | number |
| % Block transfered | Float |   |   | number |


**Consistency errors specific to the GetAnalyzerState command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 033 | 001 | 000 | Module unknown or not managed by the command |
| 033 | 002 | 000 | State unknown for the specified module |


<!-- page 275 -->

#### 3.6.38 - "ExportTransducerDB" command


**Semantics**

Exports a transducer database file to a text file.

**Command syntax**

```
ExportTransducerDB <file>
The <file> indicates the full path to the file to export to (including ".txt"
extension), from the NVGate's computer point of view.
```

**Example**

```
ExportTransducerDB C:\\myTransducers.txt
This command exports the transducers database to the file
"C:\myTransducers.txt".
```

**Result returned**

No data follows the header.

<!-- page 276 -->

#### 3.6.39 - "MergeTransducerDB " command


**Semantics**

Merges a transducer database file (CDB or TXT) into NVGate's transducer
database.

**Command syntax**

```
MergeTransducerDB <file> <operation>
The <file> indicates the full path to the file to import (including ".cdb" or ".txt"
extension), from the NVGate's computer point of view. This file corresponds to
the "theirs" column in the NVGate's merge dialog.
The <operation> instructs the operation to perform when a conflict occurs.
```

**Example**

```
MergeTransducerDB C:\\myTransducers.cdb 2
This command merges the file "C:\myTransducers.cdb" into the transducers
database of NVGate, overwriting NVGate's version with the version of the file in
case of conflicts.
```

**Result returned**

No data follows the header.

| Operation value |   |   | Effect |   |
|---|---|---|---|---|
| 0 (do nothing) |   | When a conflict occurs, keep the NVGate<br>version intact and do not perform any<br>merge.<br>Calibration history is not merged. |   |   |
| 1 (use mine) |   | When a conflict occurs, keep the NVGate<br>version of the conflicted fields, and import<br>other fields if the NVGate's field is empty.<br>Calibration history is merged. |   |   |
| 2 (use theirs) |   | When a conflict occurs, use the version of<br>the file.<br>Calibration history is merged. |   |   |


**Consistency errors specific to the MergeTransudcerDB command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 275 | 001 | 000 | Invalid operation. |


<!-- page 277 -->

#### 3.6.40 - "GetStateValue" command


**Semantics**

Returns a state value

**Command syntax**

```
GetStateValue <Module num>
<Sub-module num>
<State num>
The <Module num>.<Sub-module num>.<State num> parameters
identify the setting IDN (see § 3.6.3 - ).
```

**Result returned**

The header contains the size of a string, followed by the string itself.
Every state is returned as a string.
Ex : GetStateValue 10 89 64
This command returns the number of average of the FFT1 analyzer
Ex : GetStateValue 7 209 330
This command returns the frequency status of the Advanced Sine Generator

**Consistency errors specific to the GetStateValue command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 171 | 001 | 000 | Status unknown |


<!-- page 278 -->

#### 3.6.41 - "WizardBegin" command


**Semantics**

Warning : This command is deprecated. Please consider using
TransactionBegin instead.
This command and the command "WizardEnd" can be used to speed up the
setting of the analyzer. When connecting inputs to analyzer plug-ins and/or
changing the settings, this command avoid sending the new configuration to the
hardware after each modification. WizardBegin must be called before sending the
first configuration command and the command WizardEnd must be called after
the last configuration command.

**Command syntax**

```
WizardBegin
Ex:
WizardBegin
( ConnectInput or SetSettingValue command(s)...)
WizardEnd
```

**Result returned**

No data follows the header.

**Consistency errors specific to the WizardBegin command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 000 | 000 | 000 | No error |


<!-- page 279 -->

#### 3.6.42 - "WizardEnd" command


**Semantics**

Warning : This command is deprecated. Please consider using
TransactionEnd instead.
The command "WizardBegin" and this command can be used to speed up the
setting of the analyzer. After connecting inputs to analyzer plug-ins and/or
changing the settings, this command allows sending the new configuration to the
hardware. WizardBegin must be called before sending the first configuration
command and the command WizardEnd must be called after the last configuration
command.

**Command syntax**

```
WizardEnd
Ex:
WizardBegin
( ConnectInput or SetSettingValue command(s)...)
WizardEnd
```

**Result returned**

No data follows the header.

**Consistency errors specific to the WizardEnd command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 226 | 001 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 226 | 002 | 000 | Limits of DSP power have been reached. The previous<br>valid configuration has been restored (from the version<br>6.20) |


<!-- page 280 -->

#### 3.6.43 - "TransactionBegin" command


**Semantics**

This command and the command "TransactionEnd" can be used to speed up the
setting of the analyzer. When connecting inputs to analyzer plug-ins and/or
changing the settings, this command avoid sending the new configuration to the
hardware after each modification. TransactionBegin must be called before sending
the first configuration command and the command TransactionEnd must be called
after the last configuration command.

**Command syntax**

```
TransactionBegin
Ex:
TransactionBegin
( ConnectInput or SetSettingValue command(s)...)
TransactionEnd
```

**Result returned**

No data follows the header.

**Consistency errors specific to the TransactionBegin command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 000 | 000 | 000 | No error |


<!-- page 281 -->

#### 3.6.44 - "TransactionEnd" command


**Semantics**

The command "TransactionBegin" and this command can be used to speed up the
setting of the analyzer. After connecting inputs to analyzer plug-ins and/or
changing the settings, this command allows sending the new configuration to the
hardware. TransactionBegin must be called before sending the first configuration
command and the command TransactionEnd must be called after the last
configuration command.

**Command syntax**

```
TransactionEnd
Ex:
TransactionBegin
( ConnectInput or SetSettingValue command(s)...)
TransactionEnd
```

**Result returned**

No data follows the header.

**Consistency errors specific to the TransactionEnd command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 361 | 001 | 000 | Real time is not guaranted for current analysis setting (from<br>the version 6.20) |
| 361 | 002 | 000 | Limits of DSP power have been reached. The previous<br>valid configuration has been restored (from the version<br>6.20) |


<!-- page 282 -->

#### 3.6.45 - "WaitGUI" command


**Semantics**

The command "WaitGUI" waits for the user interface to be available, then
returns.

**Command syntax**

```
WaitGUI
```

**Result returned**

No data follows the header.

**Consistency errors specific to the WaitGUI command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 382 | 001 | 000 | Unspecified error |


<!-- page 283 -->

### 3.7 - SIGNAL AND RESULT MANAGEMENT


#### 3.7.1 - Results specificity

The operations on results concern 4 types of results:
- Result which is displayed in NVGate.
- Result which is saved in a measurement.
- Result which is not displayed in NVGate, but that can be computed with the
current NVGate configuration.
- TCP result which can be created and modified with no reference to the
current configuration.
Results acquired or analyzed by the OR3x analyzer can be retrieved thought
NVDrive®.
Results collection must comply with the following rules:
- The corresponding windows (which contain the results to be collected) must
exist prior to any data collection, except for saved results (see
GetSavedResult)
- Data values are forced to SI unit (can be different from display).
- Spectral operations are not applied to collected results (No
integration/Differentiation, no unit modifications, can be different from
display).
- The data windows must be located in the 2 latest activated layouts. For
example after displaying Layout 1, Layout 2, Layout 3, the data in the
layout 1 are not available since Layout 1 is activated (see SetLayout)
Data refresh depends on NVGate® displays. Fast polling may block NVGate® display
operations causing a dead-lock. For applications that run on the same computer be
careful to let some computation power to NVGate® (Sleep, Pause, Nop Function) in
the polling sequence.
The TCP results are used to inject new data in an external result channel. The data and
properties of theses channels can be defined and modified by an external application.
The TCP channels can be displayed with the 3.3.1 - AddWindowResult command.
with "TCP" module value. For the result value, you must notice the NVD value
corresponding to your result type. You cannot inject a Waterfall 2D result, you have to
inject it as Referenced Vector result.

<!-- page 284 -->

#### 3.7.2 - "IsResultWaterfallisable" command


**Semantics**

Return if the selected process can be added to the waterfall module.

**Command syntax**

```
IsResultWaterfallisable <Module ID> <Process ID>
The Module ID is one of the 3.10.1 - Module ID table
The Process ID is one of the 3.10.5 - Process ID table.
```

**Result returned**

The result returned 1 (true) if the process can be added as a channel to the
waterfall module, 0 (false) otherwise.

<!-- page 285 -->

#### 3.7.3 - "GetSignalProperties" command


**Semantics**

Retrieves the properties of the selected signal.

**Command syntax**

```
GetSignalProperties <Project name>
<Measurement name>
The project must be in the default base.
```

**Result returned**

The signal properties data returned are :

|   | Size<br>(bytes) | Type | Description |
|---|---|---|---|
| X |   | String ending in<br>the character \0. | Creation time |
| X |   | String ending in<br>the character \0. | Type (= Signal) |
| X |   | String ending in<br>the character \0. | Sampling frequency 1 |
| X |   | String ending in<br>the character \0. | Sampling frequency 2 |
| X |   | String ending in<br>the character \0. | Sampling frequency of slow inputs |
| X |   | String ending in<br>the character \0. | Inform if the signal is on analyzer |
| X |   | String ending in<br>the character \0. | Inform if the signal is on computer |
| X |   | String ending in<br>the character \0. | Size of the signal in bytes |
| X |   | String ending in<br>the character \0. | Signal duration in hour / minute / second |
| X |   | String ending in<br>the character \0. | Number of tracks in the signal |
| X |   | String ending in<br>the character \0. | Format (normal / compacted) |
| X |   | String ending in<br>the character \0. | Signal duration in seconds |


**Consistency errors specific to the GetSignalProperties command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 106 | 001 | 000 | Project not found |
| 106 | 002 | 000 | Measurement not found |


<!-- page 286 -->

#### 3.7.4 - "GetRecordDate" command


**Semantics**

Return the start date of a record of the signal file loaded in player.

**Command syntax**

```
GetRecordDate <Record Number>
The <Record Number> is 1 based index (for signal files which contain one
record, you must set "Record Number" parameter to 1).
```

**Result returned**

The start date of the record.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | Unsigned int | Year |
| 4 |   |   | Unsigned int | Month (1 to 12) |
| 4 |   |   | Unsigned int | Day (1 to 31) |
| 4 |   |   | Unsigned int | Hour |
| 4 |   |   | Unsigned int | Minute |
| 4 |   |   | Unsigned int | Second |
| 4 |   |   | Unsigned int | Milliseconds |


**Consistency errors specific to the GetRecordDate command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 060 | 001 | 000 | The player is not in the configuration |
| 060 | 002 | 000 | No signal file is loaded in player |
| 060 | 003 | 000 | No record has the number specified in parameter |
| 060 | 004 | 000 | Get record date failed. |


<!-- page 287 -->

#### 3.7.5 - "ChangeSignalDate" command


**Semantics**

Change the start date of a signal in a measurement of a project. The signal must
not be loaded in the player.

**Command syntax**

```
ChangeSignalDate <Project Name>
<Measurement Name>
<Year>
<Month>
<Day>
<Hour>
<Minute>
<Second>
The parameters are self-explanatory.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ChangeSignalDate command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 200 | 001 | 000 | Project not found |
| 200 | 002 | 000 | Measurement not found |
| 200 | 003 | 000 | Signal not found |
| 200 | 004 | 000 | Signal loaded in the player |
| 200 | 005 | 000 | Loading the file has failed |
| 200 | 006 | 000 | Saving the new date has failed |


<!-- page 288 -->

#### 3.7.6 - "Download" command


**Semantics**

Download signal file from OR3x to PC.

**Command syntax**

```
Download <Project name>
<Measure name>
[Remove file from OR3x]
<Project name> and <Measure name> define the location of signal file
to download.
Set [Remove file from OR3x] flag to 0 to leave the signal file on OR3x
after download. Set to 1 to remove it. This parameter is optional; its default value
is 0.
A value different from 0 and 1, the default value is taken.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DownLoad command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 063 | 001 | 000 | The specified measure has no signal |
| 063 | 002 | 000 | OR3X is not connected |
| 063 | 003 | 000 | Signal is already on PC disk |
| 063 | 004 | 000 | Signal is not on OR3X disk |
| 063 | 005 | 000 | There is not enough space on the PC to download the signal |


<!-- page 289 -->

#### 3.7.7 - "Upload" command


**Semantics**

Upload signal file from PC to OR3x.

**Command syntax**

```
Upload <Project name>
<Measure name>
[Remove file from PC]
<Project name> and <Measure name> define the location of signal file
to upload.
Set [Remove file from PC] flag to 0 to leave the signal file on PC after
upload. Set to 1 to remove it. This parameter is optional; its default value is 0.
A value different from 0 and 1, the default value is taken.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the Upload command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 107 | 001 | 000 | The specified measure has no signal |
| 107 | 002 | 000 | OR3X is not connected |
| 107 | 003 | 000 | Signal is already on OR3x disk |
| 107 | 004 | 000 | Signal is not on PC disk |
| 107 | 005 | 000 | There is not enough space on OR3x to upload the signal |


<!-- page 290 -->

#### 3.7.8 - "ImportFile" command


**Semantics**

Import or convert signal or result file.

**Command syntax**

```
ImportFile <ImportType>
<File>
<Directory>
[Project]
[Delete]
The <ImportType> defines the type of the file to import:
<File> is the name (without the extension) of the file to import.
<Directory> is the name of the directory where the file is located.
[Project] is an optional parameter to select the name of the project in which
the file will be imported. The default value is the current project.
[Delete] is an optional parameter to delete the original file after import (only
available for an OR10 signal file)
```

**Example**

```
ImportFile 1 MyWavFile D:\\MyData\\WavFiles
Imports the file D:\MyData\WaveFiles\MyWaveFile.wav in the current
project of NVGate.
```

**Result returned**

The name of the measurement that has been created if the import is successful.

| 0 | OR2X result (*.ae2) |
|---|---|
| 1 | OR2X signal (*.wav) |
| 2 | OR3X result (*.res) |
| 3 | OR3X signal legacy (*.oxf) |
| 4 | UFF signal file (*.uff) |
| 5 | TXT signal file (*.txt) |
| 6 | OR10 signal file (*.or10) |
| 7 | OROS Signal (*.osfh) |


**Consistency errors specific to the ImportFile command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 118 | 001 | 000 | The import failed. Refer to the log wnd for details |
| 118 | 002 | 000 | The type of import is invalid |
| 118 | 003 | 000 | The project does not exist |
| 118 | 004 | 000 | The directory where the file is located does not exist |
| 118 | 005 | 000 | The file to import does not exist |
| 118 | 006 | 000 | The delete parameter in invalid |


<!-- page 291 -->

#### 3.7.9 - "Export" command


**Semantics**

Export results or signal in standard format.

**Command syntax**

```
Export <ExportType>
<Project>
<Measurement>
<ExportDirectory>
[FileName]
[Option1]
The <ExportType> defines the format of the exported file.
The export type "Results in txt (as OR2x txt export)" is available since NVGate
V6.01, but is limitated to the following results: FFT averaged spectrum, FFT
Instant spectrum, FRF H1, FRF H2, Coherence, Avg.1/3 octave, SOA Order
Profile.
<Project> is the name of the project.
<Measurement> is the name of the measurement.
<ExportDirectory> is the name of the directory that will receive the file(s).
[FileName] (optional) is the name that will take the exported file. The default
value is the name of the measurement.
[Option1] is used only for Export in AudioWav. It indicates the preferred
frequency to export to. Values can be 44100, 48000 or 96000. The default value
used is the one define in the preferences.
```

**Result returned**

No data follows the header.

| 0 | Results in UFF |
|---|---|
| 1 | Results in Matlab |
| 2 | Results in txt (NVGate txt export) |
| 3 | Results in txt (as OR2x txt export) |
| 4 | Results in ASAM ODS ATFX. |
| 10 | Signal in SDF |
| 11 | Signal in Wav |
| 12 | Signal in Matlab |
| 13 | Signal in Audio Wav |
| 14 | Signal in UFF |
| 15 | Signal in Txt |
| 16 | Signal in ASAM ODS ATFX |


<!-- page 292 -->

**Consistency errors specific to the Export command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 119 | 001 | 000 | The export failed. Refer to the log wnd for details |
| 119 | 002 | 000 | The type of export is invalid |
| 119 | 003 | 000 | The project does not exist |
| 119 | 004 | 000 | The measurement does not exist |
| 119 | 005 | 000 | The ExportDirectory does not exist |


<!-- page 293 -->

#### 3.7.10 - "AddResultToSetup" command


**Semantics**

Adds a result to the save setup list

**Command syntax**

```
AddResultToSetup <Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[IsWaterfall]
The tables giving the numbers of the weighting and time operators and
the display units are presented in section 3.10 - Result format and
description
.
The IsWaterfall optional parameter enables to indicate that the result is a
Waterfall (if = 1) or not (if = 0). The default value is 0.
```

**Examples**

```
AddResultToSetup 10 2 1 0 0 0 0 0
enables to put the result FFT1 Avg Spectrum Ch1 in the save setup list
AddResultToSetup 10 2 1 0 0 0 0 1
enables to put the result Wtf FFT1 Avg Spectrum Ch1 in the save setup list
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddResultToSetup command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 022 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 022 | 002 | 000 | Number of a module not supplying a result |
| 022 | 003 | 000 | Process number incorrect |
| 022 | 004 | 000 | Channel number incorrect |
| 022 | 005 | 000 | Reference channel number incorrect |
| 022 | 006 | 000 | Weighting operator unknown |
| 022 | 007 | 000 | No weighting for non-spectrum results |
| 022 | 008 | 000 | Result already weighted |
| 022 | 009 | 000 | Time operator unknown |
| 022 | 010 | 000 | Display unit unknown |
| 022 | 011 | 000 | Result already present in the list |
| 022 | 012 | 000 | IsWaterfall parameter incorrect |


<!-- page 294 -->

#### 3.7.11 - "RemoveSetupResult" command


**Semantics**

Removes a result from the save setup list

**Command syntax**

```
RemoveSetupResult <Module number>
<Process number>
<Channel number >
[Reference channel number]
[Weighting operator]
[Time operator]
[Display unit]
[IsWaterfall]
The tables giving the numbers of the weighting and time operators and
the display units are presented in section 3.10 - Result format and
description
.
The IsWaterfall optional parameter enables to indicate that the result is a
Waterfall (if = 1) or not (if = 0). The default value is 0.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveSetupResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 023 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 023 | 002 | 000 | Number of a module not supplying a result |
| 023 | 003 | 000 | Process number incorrect |
| 023 | 004 | 000 | Channel number incorrect |
| 023 | 005 | 000 | Reference channel number incorrect |
| 023 | 006 | 000 | Weighting operator unknown |
| 023 | 007 | 000 | No weighting operator for non spectal result |
| 023 | 008 | 000 | The result is already weighted |
| 023 | 009 | 000 | Time operator unknown |
| 023 | 010 | 000 | Display unit unknown |
| 023 | 011 | 000 | Result not present in the save setup list |
| 023 | 012 | 000 | IsWaterfall parameter incorrect |


<!-- page 295 -->

#### 3.7.12 - "ClearSetupList" command


**Semantics**

Clears the save setup result list

**Command syntax**

```
ClearSetupList
```

**Result returned**

No data follows the header.

<!-- page 296 -->

#### 3.7.13 - "SetSetupParameters" command


**Semantics**

Sets the parameters [Measurement database name] and [Increment
type] of the save setup.

**Command syntax**

```
SetSetupParameters [Measurement database name]
[Increment type]
The [Increment type] is specified by a number:
```

**Result returned**

No data follows the header.

| Increment type |   |   | Number |   |
|---|---|---|---|---|
| By number |   | 0 |   |   |
| By date |   | 1 |   |   |


**Consistency errors specific to the SetSetupParameters command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 024 | 001 | 000 | Increment unknown |
| 024 | 002 | 000 | Measurement database name incorrect as it contains one of<br>the following characters: \ /: * ? " < > \| . |


<!-- page 297 -->

#### 3.7.14 - "SetAutomaticExportSetup" command


**Semantics**

Enable automatic export of the next saved results into the specified format
<ExportType>. The exported files will be created in the specified directory.

**Command syntax**

```
SetAutomaticExportSetup <ExportType>
<ExportDirectory>
The <ExportType> defines the format of the exported file.
The export type "Results in txt (as OR2x txt export)" is available since NVGate
V6.01, but is limitated to the following results: FFT averaged spectrum, FFT
Instant spectrum, FRF H1, FRF H2, Coherence, Avg.1/3 octave, SOA Order
Profile.
<ExportDirectory> is the name of the directory that will receive the file(s).
It must exist.
```

**Result returned**

No data follows the header.

| 0 | Results in UFF |
|---|---|
| 1 | Results in Matlab |
| 2 | Results in txt (NVGate txt export) |
| 3 | Results in txt (as OR2x txt export) |
| 4 | Results in ASAM ODS ATFX. |
| 10 | Signal in SDF |
| 11 | Signal in Wav |
| 12 | Signal in Matlab |
| 13 | Signal in Audio Wav |
| 14 | Signal in UFF |
| 15 | Signal in Txt |
| 16 | Signal in ASAM ODS ATFX |


**Consistency errors specific to the SetAutomaticExportSetup
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 368 | 001 | 000 | The ExportDirectory does not exist |


<!-- page 298 -->

#### 3.7.15 - "SetNoAutomaticExport" command


**Semantics**

Disable automatic export of results.

**Command syntax**

```
SetNoAutomaticExport
```

**Result returned**

No data follows the header.

<!-- page 299 -->

#### 3.7.16 - "AddToResultSelection" command


**Semantics**

Add the results of a window in the selection of the save setup.

**Command syntax**

```
AddToResultSelection <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Remark**

For waterfall window or window with memorized traces, the selection dialog is
skipped. All traces are selected.

**Result returned**

No data follows the header.

**Consistency errors specific to the AddToResultSelection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 159 | 001 | 000 | Unknown layout |
| 159 | 002 | 000 | Unknown window |


<!-- page 300 -->

#### 3.7.17 - "RemoveToResultSelection" command


**Semantics**

Remove the results of a window in the selection of the save setup.

**Command syntax**

```
RemoveToResultSelection <Layout name>
<Window name>
<Layout name> and <Window name> parameters define the window.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveToResultSelection command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 284 | 0 01 | 000 | Unknown layout |
| 284 | 002 | 000 | Unknown window |


<!-- page 301 -->

#### 3.7.18 - "SaveResults" command


**Semantics**

Save the results that have been selected in the Save Setup in a new measurement

**Command syntax**

```
SaveResults [Confirm name]
[ReturnMeasurementName]
[Confirm name] must be set to 0 if the name of the new measurement should
not be confirmed or 1 to get the dialog requesting the name of the measurement as
well as the keyword and the comment. Default value is 0.
[ReturnMeasurementName] must be set to 1 to get the name of the
measurement saved in the return result. Default value is 0. In this case, the
command only return an error code.
```

**Result returned**

No result is returned except for any errors if "ReturnMeasurementName" is set to
0. If set to 1, the header contains the size of the string followed by the name of the
new measurement

**Consistency errors specific to the SaveResults command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 096 | 001 | 000 | There is no result selected in the save setup |
| 096 | 002 | 000 | Results are not ready (Analyzer is running, or a setting has<br>been changed since the last stop ) |
| 096 | 003 | 000 | There is a default measurement in the project manager. It<br>must be saved before calling this command. |
| 096 | 004 | 000 | Value incorrect for the parameter confirm name (0 or 1<br>expected) |
| 096 | 005 | 000 | Value incorrect for the parameter ReturnMeasurementName<br>(0 or 1 expected) |
| 096 | 006 | 000 | No measurement was created. |


<!-- page 302 -->

#### 3.7.19 - "GetResultList" command


**Semantics**

Allows the user to retrieve the list of available results. This list corresponds to the
displayed signals and results.

**Command syntax**

```
GetResultList
```

**Result returned**

A list of result descriptions (see chapter § 3.10 - Result format and description
).
Each result description is separated from the next one by the character minus '-'.

<!-- page 303 -->

#### 3.7.20 - "GetWTFResultList" command


**Semantics**

Allows the user to retrieve the list of available waterfall results. This list
corresponds to the displayed signals and results.

**Command syntax**

```
GetWTFResultList
```

**Result returned**

A list of waterfall result descriptions (see chapter § 3.10 - Result format and
description
).
Each result description is separated from the next one by the character minus '-'.

<!-- page 304 -->

#### 3.7.21 - "GetResultCaption" command


**Semantics**

Allows the user to retrieve the name of an available result, from the description of
this result.

**Command syntax**

```
GetResultCaption <Module number>
<Process number>
<Channel number >
[Reference channel number]
The GetResultCaption parameters are the components of a result description. The
[Reference channel number] is an optional parameter (it may or may
not exist according to the result type).
```

**Result returned**

A character string coded in ASCII ending in \0.

**Consistency errors specific to the GetResultCaption command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 004 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 004 | 002 | 000 | Number of a module not supplying a result |
| 004 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 004 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 004 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 004 | 006 | 000 | Result not available |


<!-- page 305 -->

#### 3.7.22 - "GetSavedResultList" command


**Semantics**

Returns the list of result descriptions saved in a project measurement.

**Command syntax**

```
GetSavedResultList <measurement name>
[project name]
The [project name] is optional. If the project name is not specified, the
measurement will be sought in the default project.
```

**Result returned**

List of result descriptions.
The format of a result description is described in section 3.10 - Result format and
description

**Consistency errors specific to the GetSavedResultList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 006 | 001 | 000 | Project / measurement unknown |


<!-- page 306 -->

#### 3.7.23 - "GetSavedResultCaption" command


**Semantics**

Allows the user to retrieve the name of a result saved in a project measurement.

**Command syntax**

```
GetSavedResultCaption <project name>
<measurement name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Waterfall / No Waterfall]
The GetSavedResultCaption parameters are the <project name> and the
<measurement name>, as well as the result description components. The
[Reference channel number] is an optional parameter (it may or may
not exist according to the result type).
The optional parameter [Waterfall] lets you determine if the result to be
searched is a waterfall one (2D or 3D). The possible values are
-1 Default value, get the first result matching the others parameters
0 Search for a non waterfall result in the measure
1 Search for a waterfall result in the measure.
```

**Result returned**

A character string coded in ASCII ending in \0.

**Consistency errors specific to the GetSavedResultCaption command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 007 | 001 | 000 | Project / measurement unknown |
| 007 | 002 | 000 | Process number incorrect (not included in the process<br>number table) |
| 007 | 003 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 007 | 004 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 007 | 005 | 000 | Result not available |


<!-- page 307 -->

#### 3.7.24 - "CreateResultEx" command


**Semantics**

Prepare a result to be retrieved with the command GetResultEx.

**Command syntax**

```
CreateResultEx <Module number>
<Process number>
<Channel number >
[Reference channel number]
[Waterfall Flag]
Refer to 3.7.24 - GetResultEx command for the meaning of the parameters
```

**Remarks**

This command must be called before calling the GetResultEx command. It
prepares NVGate to get the results. Once the result is not used any longer, call the
DeleteResultEx or DeleteAllResultEx to free the memory. The command needs to
be called every time the result has been destroyed. (Disconnection of a channel,
of an input... )
If very big results should be managed (Waterfall 3D), it can be useful to maintain
only one result at the time.

**Result returned**

No data follows the header.

**Consistency errors specific to the CreateResultEx command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 112 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 112 | 002 | 000 | Number of a module not supplying a result |
| 112 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 112 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 112 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 112 | 006 | 000 | Result could not be created. |
| 112 | 007 | 000 | Process not managed by the plug-in |
| 112 | 008 | 000 | Response not managed by the plug-in |
| 112 | 009 | 000 | Reference not managed by the plug-in |
| 112 | 010 | 000 | Result already created |


<!-- page 308 -->

#### 3.7.25 - "GetResultEx" command


**Semantics**

Allows the user to retrieve a result, which has been created thanks to the
CreateResultEx command.

**Command syntax**

```
GetResultEx <Module number>
<Process number>
<Channel number >
[Reference channel number]
[Waterfall Flag]
The GetResultEx command replaces the GetResult and GetWTFResult
commands from Version 2.2 of NVGate. It simplifies the result access. Also it is
recommended to call it with the "version parameter" (see chap 2.3 - Exchange
format). If omitted, the version parameter used is 2.
Getting results (since NVGate V5): use version parameter = 3 to get BlockInfo
data on top of that.
This command enables to retrieve results without displaying the windows in
NVGate.
The [Reference channel number] is an optional parameter. Its defaults
value is 0 and it is interpreted as No Reference.
The [Waterfall Flag] indicates that the result is in the waterfall. Default
value is 0 and means that the result expected is the one furnished by the plug-in. If
set to 1, then it is the waterfall result.
```

**Examples**

```
GetResultEx 12 24 1 v=3
returns the octave average spectrum of the channel1
GetResultEx 1 9 1 v=3
returns the DC level of the slow input 1
GetResultEx 1 9 1 0 1 v=3
returns the waterfall of the DC level of the slow input 1
GetResultEx 10 6 2 1 1 v=3
returns the waterfall of the average cross spectrum 2-1
```

**Reminder**

Before calling this command, the result must have been created with the
CreateResultEx command. The result is refreshed when the GetResultEx
command is received. If the analyzer is stopped, the last valid result is sent.

<!-- page 309 -->

**Result returned**

If there is no error, the data block following the header represents a measurement
result. The data are divided into blocks. Section 3.10 - Result format and
description
presents the format of the various result types.

**Consistency errors specific to the GetResultEx command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 111 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 111 | 002 | 000 | Number of a module not supplying a result |
| 111 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 111 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 111 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 111 | 006 | 000 | Result not found. Call CreateResultEx before |
| 111 | 007 | 000 | Result not valid. |


<!-- page 310 -->

#### 3.7.26 - "GetSavedResultEx" command


**Semantics**

Allows the user to retrieve a result saved in a project measurement.

**Command syntax**

```
GetSavedResult <project name>
<measurement name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[Waterfall Flag]
The GetSavedResultEx replaces the GetSavedResult command from Version 2.2
of NVGate, and enable to get a waterfall result. It simplifies the saved result
access.
The GetSavedResultEx parameters are the <project name> and the
<measurement name>, as well as the result description components.
The [Reference channel number] is an optional parameter. Its defaults
value is 0 and it is interpreted as No Reference.
The [Waterfall Flag] indicates that the result is in the waterfall. Default
value is 0 and means that the result expected is the one furnished by the plug-in. If
set to 1, then it is the waterfall result.
```

**Result returned**

If there are no errors, the data block following the header represents a
measurement result. The data are divided into blocks. Section 3.10 - Result
format and description
presents the format of the various result types.

**Consistency errors specific to the GetSavedResultEx command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 115 | 001 | 000 | Module number incorrect (not included in the module<br>number table) |
| 115 | 002 | 000 | Process number incorrect (not included in the process<br>number table) |
| 115 | 003 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 115 | 004 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 115 | 005 | 000 | Result not available |
| 115 | 006 | 000 | Project / measurement unknown |


<!-- page 311 -->

#### 3.7.27 - "DeleteResultEx" command


**Semantics**

Delete a result created with the command CreateResultEx.

**Command syntax**

```
DeleteResultEx <Module number>
<Process number>
<Channel number >
[Reference channel number]
[Waterfall Flag]
Refer to 3.7.24 - GetResultEx command for the meaning of the parameters
```

**Remarks**

This command must be called when the result is not used anymore.

**Result returned**

No data follows the header.

**Consistency errors specific to the DeleteResultEx command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 113 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 113 | 002 | 000 | Number of a module not supplying a result |
| 113 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 113 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 113 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 113 | 006 | 000 | Result could not be found |


<!-- page 312 -->

#### 3.7.28 - "DeleteAllResultEx" command


**Semantics**

Delete all the results created with the command CreateResultEx.

**Command syntax**

```
DeleteAllResultEx
```

**Remarks**

This command must be called to delete all the results created.

**Result returned**

No result is returned

<!-- page 313 -->

#### 3.7.29 - "GetResult" command


**Semantics**

Allows the user to retrieve a result, which is displayed in a window.
Warning: Use the 3.7.25 - GetResultEx command instead of this command in
the NVGate 3.10 and later.

**Command syntax**

```
GetResult <Module number>
<Process number>
<Channel number >
[Reference channel number]
[GetGlobalLevel Flag]
[GetPondGlobalLevel Flag]
[Version number]
The GetResult parameters are the components of a result description.
The[Reference channel number] is an optional parameter.
The [GetGlobalLevel Flag] and [GetPondGlobalLevel Flag] are
optional parameters designed, for results of the AVERAGE N OCTAVE or N OCTAVE
type, to retrieve respectively the unweighted and weighted global levels. For results
other than AVERAGE N OCTAVE or N OCTAVE, these parameters are ignored.
It is found in the queue of the Data field of the CVEC / RVEC data block, in float
form (4 bytes.). When both values are retrieved, the weighted global level follows the
unweighted global level.
The default value of the flags is 0. A value upper than 1 is considered as 0.
The [Version number] parameter enables to select the version (0, 1 or later) of
the result blocks (see chapter § 3.10 - Result format and description
). Its default value is 0.
Warning: Since version 1 all results are return in EU format. With version 0, some
results are returned in EU² (to be compatible with the NVGate version 1.5x).
Reminder: if you wish to retrieve the global level for a result without a reference
channel, you must specify the value of the [GetGlobalLevel Flag] parameter
and not specify a value for the reference channel parameter. To do this, use the syntax
pi=.
For example, the command GetResult 12 24 1 p2=1 lets you retrieve the result
AVERAGE N OCTAVE on channel no. 1 of the 1/n octave module. The retrieved result
will contain the global level.
```

<!-- page 314 -->
```
```

**Result returned**

If there is no error, the data block following the header represents a measurement
result. The data are divided into blocks. Section 3.10 - Result format and
description
presents the format of the various result types.

**Consistency errors specific to the GetResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 005 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 005 | 002 | 000 | Number of a module not supplying a result |
| 005 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 005 | 004 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 005 | 005 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 005 | 006 | 000 | Result not available |
| 005 | 007 | 000 | Result not valid |


<!-- page 315 -->

#### 3.7.30 - "GetWTFResult" command


**Semantics**

Allows the user to retrieve a waterfall result, which is displayed in a window.
Warning: Use the 3.7.25 - GetResultEx command instead of this command in
the NVGate 3.10 and later.

**Command syntax**

```
GetWTFResult <Module number>
<Process number>
<Channel number >
[Reference channel number]
[GetGlobalLevel Flag]
[GetPondGlobalLevel Flag]
[Version number]
[Start Index]
[Wanted Size]
The GetWTFResult parameters are the components of a result description.
The <Module number> defines the module which is the source of the
Waterfall.
The <Channel number > goes from 501 to 532 for channel 1 to 32.
The [Reference channel number] is an optional parameter.
The [GetGlobalLevel Flag] and [GetPondGlobalLevel Flag] are
optional parameters designed, for results of the WATERFALL AVERAGE N OCTAVE
or WATERFALL N OCTAVE type, to retrieve respectively the unweighted and
weighted global levels. For other results, these parameters are ignored.
The [Version number] parameter enables to select the version (0, 1 or later)
of the result blocks (see chapter § 3.10 - Result format and description
). Its default value is 0.
The [Start Index] number is optional. It is the index from which you want
the waterfall values.
The [Wanted Size] number is optional. It is the number of waterfall values
wanted, if there is less values available, they are transmitted with the Request
status member of the DWTF block set to 1.
For example, the command GetWTFResult 10 2 501 lets you retrieve the result
WATERFALL FFT1 AVERAGE SPECTRUM on channel n°1.
```

<!-- page 316 -->
```
```

**Result returned**

If there is no error, the data block following the header represents a measurement
result. The data are divided into blocks. Section 3.10 - Result format and
description
presents the format of the various result types.

**Consistency errors specific to the GetWTFResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 071 | 001 | 000 | Module number incorrect (not included in the module<br>number table) or number of a module not existing in the<br>configuration. |
| 071 | 002 | 000 | Number of a module not supplying a result |
| 071 | 003 | 000 | Process number incorrect (not included in the process<br>number table) |
| 071 | 004 | 000 | Channel number incorrect (number not included between<br>501 and 532) |
| 071 | 005 | 000 | Reference channel number incorrect (number not included<br>between 501 and 532) |
| 071 | 006 | 000 | Result not available |
| 071 | 007 | 000 | Result not valid |


<!-- page 317 -->

#### 3.7.31 - "GetSavedResult" command


**Semantics**

Allows the user to retrieve a result saved in a project measurement.
Attention: Use the 3.7.26 - GetSavedResultEx command instead of this
command in the NVGate 3.10 and later.

**Command syntax**

```
GetSavedResult <project name>
<measurement name>
<Module number>
<Process number>
<Channel number >
[Reference channel number]
[GetGlobalLevel flag]
[GetPondGlobalLevel flag]
[Version number]
The GetSavedResult parameters are the project name and the measurement name,
as well as the result description components.
For the [GetGlobalLevel flag], [GetPondGlobalLevel flag] and
[Version number] parameters, refer to the GetResult command.
```

**Result returned**

If there are no errors, the data block following the header represents a
measurement result. The data are divided into blocks. Section 3.10 - Result
format and description
presents the format of the various result types.

**Consistency errors specific to the GetSavedResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 008 | 001 | 000 | Project / measurement unknown |
| 008 | 002 | 000 | Process number incorrect (not included in the process<br>number table) |
| 008 | 003 | 000 | Channel number incorrect (number not included between 1<br>and 32) |
| 008 | 004 | 000 | Reference channel number incorrect (number not included<br>between 1 and 32) |
| 008 | 005 | 000 | Result not available |


<!-- page 318 -->

#### 3.7.32 - "CreateTCPResultChannel" command


**Semantics**

Allows the user to create a TCP channel to send result into NVGate

**Command syntax**

```
CreateTCPResultChannel <Binary Param>
The <Binary Param> structure is:
```

**Result returned**

An id to identify the created channel. This id will be used with all commands to
modify, display, and send data to this channel.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | long | Size of the rest of the bloc |
| 2 |   |   | Unsigned Short | Module ID = 498 |
| 4 |   |   | Unsigned int | Process ID (ex: NVC SCALAR = 182) |
| 4 |   |   | Unsigned int | Channel number = 0 |
| 4 |   |   | Unsigned int | Reference channel number = 0 |
| x |   |   | String | Name of the input connected to the channel<br>The string ends in the character '\0' |
| x |   |   | Result (series of<br>blocks) | The result according to the result format. The<br>blocks that compose this result (HEAD + ...) must<br>be of the version 1 and above, to have precision<br>fields. See "3.10 - Result format and description<br>" section for details. |


|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | long | >= 0 if the creation is done, else -1 |


**Consistency errors specific to the CreateTCPResultChannel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 067 | 001 | 000 | Unable to create |
| 067 | 002 | 000 | Unable to decrypt binary param (since NVGate V6.10) |


<!-- page 319 -->

#### 3.7.33 - "RemoveTCPResultChannel" command


**Semantics**

Allows the user to remove a TCP channel.

**Command syntax**

```
RemoveTCPResultChannel <TCP channel id>
The <TCP channel id> is the identifier of the TCP channel to destroy. If its
value is -1, all the TCP channels are destroyed
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RemoveTCPResultChannel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 069 | 001 | 000 | TCP generator not found |
| 069 | 002 | 000 | TCP channel not found |
| 069 | 003 | 000 | Channel id invalid |


<!-- page 320 -->

#### 3.7.34 - "NewDataForTCPResultChannel" command


**Semantics**

Allows the user to modify the data of a TCP channel to send result into NVGate.
For SCAL block: Value (4 bytes) = Scalar value
For XREF block: Data (Size*4 bytes) = Reference values
For CVEC block: Data (Size*2*4 bytes) = Complex values (list of pairs)
For RVEC block: Data (Size*4 bytes) = Real values
For RWTF block: Data (Vectorsize*Depth*4 bytes) = List of real vectors
For CWTF block: Data (Vectorsize*Depth*2*4 bytes) = List of complex
vectors

**Command syntax**

```
NewDataForTCPResultChannel <Binary Param>
The <Binary Param> structure is:
```

**Result returned**

No data follows the header.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | long | Size of the rest of the bloc |
| 4 |   |   | long | TCP channel id |
| X |   |   | Result (series of<br>blocks) | A RegVector, RefVector, Waterfall 3D or Scalar<br>result, depending of the channel type. The blocks<br>that compose this result (HEAD + ...) must be of<br>the version 1 and above, to have precision fields.<br>See "3.10 - Result format and description<br>" section for details |


**Consistency errors specific to the NewDataForTCPResultChannel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 068 | 001 | 000 | Unable to transfer data |
| 068 | 002 | 000 | Unable to decrypt binary param (since NVGate V6.10) |


<!-- page 321 -->

#### 3.7.35 - "AddDataToTCPResultChannel" command


**Semantics**

Allows the user to add new data at the end of a TCP Result Channel (only for
profile 2D type, for the other result types this command do the same as
NewDataForTCPResultChannel command).

**Command syntax**

```
AddDataToTCPResultChannel <Binary Param>
The <Binary Param> structure is as described in 3.7.34 -
NewDataForTCPResultChannel.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddDataToTCPResultChannel
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 259 | 001 | 000 | Unable to transfer data |
| 259 | 002 | 000 | Unable to decrypt binary param (since NVGate V6.10) |


<!-- page 322 -->

#### 3.7.36 - "SetTCPResultChannel" command


**Semantics**

Allows the user to modify the parameters (as name and others) and data of a TCP
channel. This action includes the "NewDataForTCPResultChannel" action.

**Command syntax**

```
SetTCPResultChannel <Binary Param>
The <Binary Param> structure is:
```

**Result returned**

No data follows the header.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 4 |   |   | long | Size of the rest of the bloc |
| 4 |   |   | long | TCP channel id |
| X |   |   | Result (series of<br>blocks) | A RegVector, RefVector, Waterfall 3D or<br>Scalar result, depending of the channel type. The<br>blocks that compose this result (HEAD + ...) must<br>be of the version 1 and above, to have precision<br>fields. See "3.10 - Result format and description<br>" section for details. |


**Consistency errors specific to the SetTCPResultChannel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 070 | 001 | 000 | Unable to set the channel |
| 070 | 002 | 000 | Unable to decrypt binary param (since NVGate V6.10) |


<!-- page 323 -->

#### 3.7.37 - "GetTCPResultChannelList" command


**Semantics**

Returns the list of all the TCP result channel, with their description

**Command syntax**

```
GetTCPResultChannelList
```

**Result returned**

The header contains the size of the data returned, followed by the number of
descriptors to be read and the list of result descriptions (see chapter § 3.10 -
Result format and description
).
Each result description is separated from the next one by the character minus '-'.

**Consistency errors specific to the RemoveTCPResultChannel command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 172 | 001 | 000 | TCP generator not found |


<!-- page 324 -->

#### 3.7.38 - "GetTCPResult" command


**Semantics**

Allows the user to retrieve a result, which has been created thanks to the
CreateTCPResultChannel command

**Command syntax**

```
GetTCPResult <TCP channel ID>
<TCP channel ID> identifies the channel. Its value was returned during the
creation process.
```

**Result returned**

This command use the same format than the GetSavedResult Command

**Consistency errors specific to the GetTCPResultcommand**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 173 | 001 | 000 | TCP generator not found |
| 173 | 002 | 000 | TCP channel not found |


<!-- page 325 -->

#### 3.7.39 - "ChangeTCPResultName" command


**Semantics**

Change result name of a TCP result.

**Command syntax**

```
ChangeTCPResultName <TCP channel ID>
<ResultName>
<TCP channel ID> identifies the channel. Its value was returned during the
creation process.
<Result Name> identifies the new result name.
```

**Result returned**


**Consistency errors specific to the ChangeTCPResultName command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 286 | 001 | 000 | TCP generator not found |
| 286 | 002 | 000 | TCP channel not found |


<!-- page 326 -->

#### 3.7.40 - "CreateResultRecordSignal" command


**Semantics**

Prepare the signal from the recorder to be retrieved as a signal result with the
command GetResultRecordSignalBlock or
GetResultRecordSignalZoom.

**Command syntax**

```
CreateResultRecordSignal <Track number>
The <Track number> parameter indicates the track to read the signal from.
```

**Remarks**

This command must be called before calling the GetResultRecordSignalBlock
command or the GetResultRecordSignalZoom command. Once the signal result
is not used any longer, call the DeleteResultRecordSignal free the memory.

**Result returned**

No data follows the header.

**Consistency errors specific to the CreateResultRecordSignal
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 398 | 001 | 000 | Recorder module not existing in the configuration. |
| 398 | 002 | 000 | Unknown track number. |
| 398 | 003 | 000 | A signal result has already been created for this track<br>number. |


<!-- page 327 -->

#### 3.7.41 - "DeleteResultRecordSignal" command


**Semantics**

Delete a signal result created with CreateResultRecordSignal.

**Command syntax**

```
DeleteResultRecordSignal <Track number>
The <Track number> parameter indicates the track to read the signal from.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CreateResultRecordSignal
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 400 | 001 | 000 | Recorder module not existing in the configuration. |
| 400 | 002 | 000 | Unknown track number. |
| 400 | 003 | 000 | No signal result created for this track number. |


<!-- page 328 -->

#### 3.7.42 - "DeleteAllResultRecordSignal" command


**Semantics**

Delete all the signal results created with CreateResultRecordSignal.

**Command syntax**

```
DeleteAllResultRecordSignalBlock
No parameter.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the CreateResultRecordSignal
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 400 | 001 | 000 | Configuration not found. |
| 400 | 002 | 000 | Recorder module not existing in the configuration. |


<!-- page 329 -->

#### 3.7.43 - "GetResultRecordSignalBlock" command


**Semantics**

Allows the user to retrieve a signal result, which has been created thanks to the
CreateResultRecordSignal command.

**Command syntax**

```
GetResultRecordSignalBlock <Track number>
<Sample number>
<Size>
<Details>
[Record number]
This command reads samples from the track <Track number> of [Record
number] (Record 1 by default).
<Size> is the number of samples to read from the position <Sample number>.
When <Details> is 1, it returns all the metadata, when it it 0 it only returns minimal
metadata.
```

**Examples**

```
GetResultRecordSignalBlock 2 1024 512 1 3
Reads 512 samples in track 2 of the record 3 starting from the sample 1024.
```

**Reminder**

Before calling this command, the signal result must have been created with the
CreateResultRecordSignal command.

**Result returned**

If there is no error, the data block following the header contains the signal. The
data are divided into blocks. The format is RecordSignal. Section 3.10 - Result
format and description
presents the format of the various result types.
When <Details> is 1 in the request, it returns the complete RecordSignal
format, otherwise the HEAD and XREG blocks are omitted.

**Consistency errors specific to the GetResultRecordSignalBlock
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 398 | 001 | 000 | Recorder module not existing in the configuration. |
| 398 | 002 | 000 | No result created for this track number. |
| 398 | 003 | 000 | The signal cannot be read. |
| 398 | 004 | 000 | The record didn't start |


<!-- page 330 -->

#### 3.7.44 - "GetResultRecordSignalZoom" command


**Semantics**

Allows the user to retrieve a part of zoomed signal, which has been created thanks
to the CreateResultRecordSignal command.

**Command syntax**

```
GetResultRecordSignalZoom <Track number>
<t0>
<t1>
<Size>
<Details>
[Record number]
This command reads samples from the track <Track number> of [Record
number] (Record 1 by default).
The signal is compressed from position <t0> to <t1> in seconds. The signal is
decomposed into <Size>/2 parts then the result is created from the minimum and the
maximum value of each part, hence <Size> values.
When <Details> is 1, it returns all the metadata, when 0 it only returns minimal
metadata.
```

**Examples**

```
GetResultRecordSignalZoom 2 0.5 7.5 50 1
Create 25 (50/2) pairs of (min, max) from position 0.5 second to 7.5 seconds of
track 2. The result is a vector of 50 values.
```

**Reminder**

Before calling this command, the result must have been created with the
CreateResultRecordSignal command.

**Result returned**

If there is no error, the data block following the header contains the signal. The
data are divided into blocks. The format is RecordSignal. Section 3.10 - Result
format and description
presents the format of the various result types.
When <Details> is 1 in the request, it returns the complete RecordSignal
format, otherwise the HEAD and XREG blocks are omitted.

**Consistency errors specific to the GetResultRecordSignalBlock
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 400 | 001 | 000 | Recorder module not existing in the configuration. |
| 400 | 002 | 000 | No result created for this track number. |
| 400 | 003 | 000 | The signal cannot be read. |
| 400 | 004 | 000 | The record didn't start |


<!-- page 331 -->

### 3.8 - REPORTS


#### 3.8.1 - "PrintReport" command


**Semantics**

Prints a report.

**Command syntax**

```
PrintReport <Template name>
[ReturnFileName]
[AutoCloseQuery]
<Template name> defines the template that must be selected.
The default value of [ReturnFileName] is 0. If it is set to 1, the command
returns the name of the file created.
The optional parameter [AutoCloseQuery] enable to close the queries of a
template without any action. The default value is 1. The value to skip the queries
validation is 0
```

**Result returned**

If [ReturnFileName] is set to 1, the command returns the name of the file
that has been created. The header contains the size of the string returned. If no file
was created, it returns the error 004.

**Consistency errors specific to the PrintReport command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 026 | 001 | 000 | Print loading has failed |
| 026 | 002 | 000 | No printer available |
| 026 | 003 | 000 | Printing has failed |
| 026 | 004 | 000 | No file created (only when ReturnFileName is set to 1) |


<!-- page 332 -->

#### 3.8.1 - "ReportRefreshPrint" command


**Semantics**

Trigger the Refresh and/or Print report command.

**Command syntax**

```
ReportRefreshPrint <doRefresh> <doPrint>
<doRefresh> defines the triggering of the Refresh command. If set to 1,
Refresh command will be triggered. If set to 0 or all other values, Refresh
command will not be triggered.
<doPrint> defines the triggering of the Print command. If set to 1, Print
command will be triggered. If set to 0 or all other values, Print command will not
be triggered.
```

**Result returned**

No data follows the header.

<!-- page 333 -->

#### 3.8.2 - "ReportGetInteractiveDocumentList" command


**Semantics**

Search and return the list of documents that are selectable for an interactive report.
After calling this command, the first document in the list is the current interactive
report document.

**Command syntax**

```
ReportGetInteractiveDocumentList
```

**Result returned**

Returns a UTF-8 character string encoded in ending in the character \0.
It is a \r\n separated list of paths.

**Consistency errors specific to the
ReportGetInteractiveDocumentList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 371 | 001 | 000 | Interactive Report is not available. |


<!-- page 334 -->

#### 3.8.3 - "ReportSelectInteractiveDocument" command


**Semantics**

Select an interactive report document. Beware that you should call
ReportGetInteractiveDocumentList before calling this command so that
NVGate searches for currently open documents.

**Command syntax**

```
ReportSelectInteractiveDocument <documentIndex>
<documentIndex> Index (1-based) of the document to select in the list
returned by the command
ReportGetInteractiveDocumentList. For
example, use 0 to select the first document in the list.
```

**Result returned**


**Consistency errors specific to the
ReportSelectInteractiveDocument command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 372 | 001 | 000 | Interactive Report is not available |
| 372 | 002 | 000 | The specified document does not exist |


<!-- page 335 -->

### 3.9 - TCP CLIENT TO SCAN STATE, SETTING, USER INTERFACE

NOTIFICATION, COMMAND AND RESULT EVENTS

#### 3.9.1 - "ConnectToTCPClient" command


**Semantics**

Creates a TCP socket connection between NVGate and the NVDrive® client
application. This application must have a TCP server running on the specified
port. The call of this command is necessary to use NVGate's notification system.
Each NVDrive® client application should only send this command once.

**Command syntax**

```
ConnectToTCPClient <IP address>
<Port number>
The parameters are the <IP address> and <Port number> of the client's
application TCP server.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ConnectToTCPClient command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 168 | 001 | 000 | Unable to connect to server |


<!-- page 336 -->

#### 3.9.2 - "DisconnectFromTCPClient" command


**Semantics**

Disconnect NVGate from the NVDrive® client application.

**Command syntax**

```
DisconnectFromTCPClient
```

**Result returned**

No data follows the header.

**Consistency errors specific to the DisconnectFromTCPClient
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 179 | 001 | 000 | Error during disconnection |


<!-- page 337 -->

#### 3.9.3 - "RegisterState" command


**Semantics**

Allows an NVDrive® client application to be notified when the specified state
changed. The application must be connected with NVGate thru
"ConnectToTCPClient" before using this function. Due to refreshing state period
inside NVGate, some changes may not be received.

**Command syntax**

```
RegisterState <Module number>
<Sub-module number>
<State number>
The <Module number>.<Sub-module number>.<State number>
parameters define the state to register.
Generic value -1 could be used for each parameter. For examples:
RegisterState -1 -1 -1
register the client for all states notification
RegisterState 10 -1 -1
register for all FFT1 states notification.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterState command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 181 | 001 | 000 | Unable to find the specified state. |
| 181 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 338 -->

#### 3.9.4 - "UnregisterState" command


**Semantics**

Unregister the specified state from the notification system.

**Command syntax**

```
UnregisterState <Module number>
<Sub-module number>
<State number>
The <Module number>.<Sub-module number>.<State number>
parameters define the unregistered state.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterState command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 182 | 001 | 000 | Unable to find the specified state. |
| 182 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 339 -->

#### 3.9.5 - "RegisterSetting" command


**Semantics**

Allows an NVDrive® client application to be notified when the specified setting
changed. The application must be connected with NVGate thru
"ConnectToTCPClient" before using this function.

**Command syntax**

```
RegisterSetting <Module number>
<Sub-module number>
<Setting number>
The <Module number>.<Sub-module number>.<Setting number>
parameters define the setting to register.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterSetting command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 178 | 001 | 000 | Unable to find the specified setting. |
| 178 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 340 -->

#### 3.9.6 - "UnregisterSetting" command


**Semantics**

Unregister the specified setting from the notification system.

**Command syntax**

```
UnregisterSetting <Module number>
<Sub-module number>
<Setting number>
The <Module number>.<Sub-module number>.<Setting number>
parameters define the unregister setting.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterSetting command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 180 | 001 | 000 | Unable to find the specified setting. |
| 180 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 341 -->

#### 3.9.7 - "RegisterUINotification" command


**Semantics**

Allows an NVDrive® client application to be notified when the specified User
Interface Notification changed. The application must be connected with NVGate
thru "ConnectToTCPClient" before using this function.

**Command syntax**

```
RegisterUINotification <UI Notification>
[Mode]
The first parameter defines the <UI Notification> identifier to register.
The second parameter [Mode] is optional: 0 means that the action corresponding
to the user interface notification is executed, 1 means it is not executed.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterUINotification command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 183 | 001 | 000 | Unable to find the specified UI Notification |
| 183 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 342 -->

#### 3.9.8 - "ExecUINotification" command


**Semantics**

Allows an NVDrive® client application to execute a User Interface Notification if
it has not been executed before (i.e., if the [Mode] parameter of the
"RegisterUINotification" command is set to 1). The application must be
connected with NVGate thru "ConnectToTCPClient" before using this function.

**Command syntax**

```
ExecUINotification
No parameter is required. The function executes the last User Interface
Notification received.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ExecUINotification command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 185 | 001 | 000 | Unable to execute the command. |


<!-- page 343 -->

#### 3.9.9 - "UnregisterUINotification" command


**Semantics**

Unregister the specified User Interface Notification from the notification system.

**Command syntax**

```
UnregisterUINotification <UINotification number>
The parameter defines the <UINotification number> unregister.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterUINotification
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 184 | 001 | 000 | Unable to find the specified UI Notification |
| 184 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 344 -->

#### 3.9.10 - "RegisterCommand" command


**Semantics**

Allows an NVDrive® client application to be notified when the specified
command is sent. The application must be connected with NVGate thru
"ConnectToTCPClient" before using this function.

**Command syntax**

```
RegisterCommand <Command number>
The parameter defines the <Command number> to register.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterCommand command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 186 | 001 | 000 | Unable to find the specified command |
| 186 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 345 -->

#### 3.9.11 - "UnregisterCommand" command


**Semantics**

Unregister the specified Command from the notification system.

**Command syntax**

```
UnregisterCommand <Command number>
The parameter defines the unregister command.
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterCommand command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 187 | 001 | 000 | Unable to find the specified command |
| 187 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 346 -->

#### 3.9.12 - "RegisterNewResult" command


**Semantics**

Allows an NVDrive® client application to be notified when new results from the
specified Module are available for transfer. New results are not computed for
transfer until the command UnblockNewResult is sent (see next page). The
application must be connected with NVGate thru "ConnectToTCPClient" before
using this function.

**Command syntax**

```
RegisterNewResult <Module ID>
The first parameter defines the <Module ID> identifier to register.
(See 3.10.1 - Module ID table).
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterNewResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 202 | 001 | 000 | Unable to find the specified Module ID |
| 202 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 347 -->

#### 3.9.13 - "UnblockNewResult" command


**Semantics**

Allows an NVDrive® client application unblocks new results transfer from the
specified Module. The application must be connected with NVGate thru
"ConnectToTCPClient" before using this function.

**Command syntax**

```
UnblockNewResult <Module ID>
The first parameter defines the <Module ID> identifier to register.
(See 3.10.1 - Module ID table).
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnblockNewResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 204 | 001 | 000 | Unable to find the specified Module ID |
| 204 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 348 -->

#### 3.9.14 - "UnregisterNewResult" command


**Semantics**

Unregister the new results computed from the specified Module from the
notification system.

**Command syntax**

```
UnregisterNewResult <Module Id>
The first parameter defines the <Module ID> identifier to register.
(See 3.10.1 - Module ID table).
As with RegisterState command, generic value -1 can be used.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterNewResult command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 203 | 001 | 000 | Unable to find the specified Module ID |
| 203 | 002 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 349 -->

#### 3.9.15 - "RegisterNewMeasurement" command


**Semantics**

Allows an NVDrive® client application to be notified when a new measurement
is created in the current project. The application must be connected with NVGate
thru "ConnectToTCPClient" before using this function.

**Command syntax**

```
RegisterNewMeasurement
```

**Result returned**

No data follows the header.

**Consistency errors specific to the RegisterNewMeasurement command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 299 | 001 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 350 -->

#### 3.9.16 - "UnregisterNewMeasurement" command


**Semantics**

Unregister the "new measurement" event from the notification system.

**Command syntax**

```
UnregisterNewMeasurement
```

**Result returned**

No data follows the header.

**Consistency errors specific to the UnregisterSetting command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 300 | 001 | 000 | Need to call ConnectToTCPClient before. |


<!-- page 351 -->

### 3.10 - RESULT FORMAT AND DESCRIPTION

A result description consists of the following fields:
The term process refers to the type of processing applied to the signal.
The term channel refers to a module input.
The term input refers to an analyzer channel.
For TCP result channel, the channel number contains the channel identifier and
can be therefore higher than 32. The reference channel is 0.

|   | Size |   | Type | Description |
|---|---|---|---|---|
|   | (bytes) |   |   |   |
| 2 |   |   | Unsigned Short | Module ID |
| 4 |   |   | Unsigned int | Process ID |
| 4 |   |   | Unsigned int | Channel number (1 to 32) |
| 4 |   |   | Unsigned int | Reference channel number (1 to 32)<br>Equals 0 if there is no reference channel |
| x |   |   | String | Name of the input connected to the channel<br>The string ends in the character '\0' |
| x |   |   | String | Name of the input connected to the reference channel.<br>The string ends in the character '\0'<br>This field does not exist if there is no reference channel |


<!-- page 352 -->

#### 3.10.1 - Module ID table


#### 3.10.2 - Time operator ID table

In case of missing parameter, the default value is 0

#### 3.10.3 - Unit ID table

In case of missing parameter, the default value is 0

|   | Module name |   |   | ID |   |
|---|---|---|---|---|---|
| FRONT END |   |   | 1 |   |   |
| MONITOR |   |   | 2 |   |   |
| RECORDER |   |   | 3 |   |   |
| PLAYER |   |   | 4 |   |   |
| EVENT |   |   | 5 |   |   |
| TACHOMETER |   |   | 6 |   |   |
| GENERATOR |   |   | 7 |   |   |
| FILTER |   |   | 8 |   |   |
| WEIGTING WINDOW |   |   | 9 |   |   |
| FFT1 |   |   | 10 |   |   |
| FFT2 |   |   | 11 |   |   |
| FFT3 |   |   | 18 |   |   |
| FFT4 |   |   | 19 |   |   |
| TIME DOMAIN ANALYSIS |   |   | 22 |   |   |
| 1/N OCTAVE |   |   | 12 |   |   |
| OVERALL ACOUSTIC |   |   | 21 |   |   |
| SYNCHRONOUS ORDER 1 |   |   | 14 |   |   |
| SYNCHRONOUS ORDER 2 |   |   | 17 |   |   |
| WATERFALL |   |   | 16 |   |   |
| TCP |   |   | 498 |   |   |


|   | Operation |   |   | ID |   |
|---|---|---|---|---|---|
| Normal |   |   | 0 |   |   |
| dt integration |   |   | 1 |   |   |
| dt² double integration |   |   | 2 |   |   |
| 1/dt differentiation |   |   | 3 |   |   |
| 1/dt² double differentiation |   |   | 4 |   |   |


|   | Unit |   |   | ID |   |
|---|---|---|---|---|---|
| Normal |   |   | 0 |   |   |
| RMS Root mean square |   |   | 1 |   |   |
| Peak |   |   | 2 |   |   |
| Peak-Peak |   |   | 3 |   |   |
| EU² engineering unit squared |   |   | 4 |   |   |
| PSD Power spectral density |   |   | 5 |   |   |
| ESD Energetic spectral density |   |   | 6 |   |   |
| RMS-PSD root mean squared Energetic spectral<br>density |   |   | 7 |   |   |


<!-- page 353 -->

#### 3.10.4 - Weighting operator ID table

In case of missing parameter, the default value is 0

#### 3.10.5 - Process ID table


|   | Weighting |   |   | ID |   |
|---|---|---|---|---|---|
| No Weighting |   |   | 0 |   |   |
| A |   |   | 1 |   |   |
| B |   |   | 2 |   |   |
| C |   |   | 3 |   |   |
| D |   |   | 4 |   |   |
| 1/A |   |   | 5 |   |   |
| 1/(A*D) |   |   | 6 |   |   |
| A*D |   |   | 7 |   |   |
| A*D 200-500Hz |   |   | 8 |   |   |
| Wc (ISO 2631-1) |   |   | 9 |   |   |
| Wd (ISO 2631-1) |   |   | 10 |   |   |
| Wk (ISO 2631-1) |   |   | 11 |   |   |
| Wb (ISO 2631-4) |   |   | 12 |   |   |
| We (ISO 2631-1) |   |   | 15 |   |   |
| Wf (ISO 2631-1) |   |   | 16 |   |   |
| Wg (BSI 6841) |   |   | 17 |   |   |
| Wh (ISO 5349-1) |   |   | 18 |   |   |
| Wj (ISO 2631-1) |   |   | 19 |   |   |
| Wm (ISO 2631-2) |   |   | 20 |   |   |


|   | Process name |   |   | Description |   |   | ID |   |
|---|---|---|---|---|---|---|---|---|
| INSTANT TRIGGER |   |   | Front end instantaneous time bloc |   |   | 1 |   |   |
| AVERAGED TRIGGER |   |   | Front end averaged time bloc |   |   | 3 |   |   |
| GAP |   |   | Shaft centerline |   |   | 8 |   |   |
| DC |   |   | Monitor averaged DC value |   |   | 9 |   |   |
| RMS |   |   | Monitor Averaged and filtered RMS value |   |   | 10 |   |   |
| RMS FRONT END |   |   | Front end RMS value |   |   | 220 |   |   |
| SKEW |   |   | Monitor Averaged and filtered |   |   | 12 |   |   |
| KURTOSIS |   |   | Monitor Averaged and filtered |   |   | 13 |   |   |
| MAX |   |   | Monitor Averaged and filtered |   |   | 14 |   |   |
| MIN |   |   | Monitor Averaged and filtered |   |   | 15 |   |   |
| SCALAR PROFILE |   |   | Scalar Time profile |   |   | 43 |   |   |
| AVERAGE SPECTRUM |   |   | FFTx Averaged spectrum |   |   | 2 |   |   |
| INSTANT SPECTRUM |   |   | FFTx Instantaneous spectrum |   |   | 4 |   |   |
| INSTANT CROSS SPECTRUM |   |   | FFTx Instantaneous cross spectrum |   |   | 5 |   |   |
| AVERAGE CROSS SPECTRUM |   |   | FFTx Averaged cross spectrum |   |   | 6 |   |   |
| SPECTRUM |   |   | FFTx time domain averaged Spectrum |   |   | 17 |   |   |
| WEIGHTED |   |   | FFTx Weighted time bloc |   |   | 20 |   |   |
| TRIGGERED |   |   | FFTx Triggered time bloc |   |   | 21 |   |   |
| FRF H1 |   |   | FFTx averaged H1 frequency response function |   |   | 31 |   |   |
| FRF H2 |   |   | FFTx averaged H2 frequency response function |   |   | 32 |   |   |
| COHERENCE |   |   | FFTx coherence function |   |   | 33 |   |   |
| LISSAJOUX |   |   | Lissajoux |   |   | 16 |   |   |
| CEPSTRUM |   |   | Cepstrum |   |   | 221 |   |   |
| CEPSTRUM ZOOM |   |   | Zoomed Cepstrum |   |   | 222 |   |   |
| AUTO CORR INST |   |   | Instantaneous auto-correlation |   |   | 223 |   |   |
| AUTO CORR AVG |   |   | Averaged instantaneous auto-correlation |   |   | 224 |   |   |
| AUTO CORRELATION |   |   | Auto-correlation |   |   | 225 |   |   |
| CROSS CORR INST |   |   | Instantaneous cross-correlation |   |   | 226 |   |   |
| CROSS CORR AVG |   |   | Averaged instantaneous cross-correlation |   |   | 227 |   |   |
| CROSS CORRELATION |   |   | Cross-correlation |   |   | 228 |   |   |


<!-- page 354 -->

| Column 1 | Column 2 | Column 3 |
|---|---|---|
| PEAK LEVEL | Peak level | 250 |
| PEAK LEVEL | Peak-Peak level | 251 |
| PEAK FACTOR LEVEL | Peak factor level | 252 |
| 1/N OCTAVE | 1/n Octave instantaneous spectrum | 18 |
| AVERAGE 1/N OCTAVE | 1/n Octave averaged spectrum | 24 |
| AVERAGE 1/N OCTAVE MIN | Min of 1/n Octave spectrum | 132 |
| AVERAGE 1/N OCTAVE MAX | Max of 1/n Octave spectrum | 133 |
| ANGULAR SPEED | RPM speed from input based tacho | 42 |
| DIGIT ANGULAR SPEED | RPM speed from ext. sync. Based tach | 75 |
| VIRTUAL ANGULAR SPEED | RPM speed from fractional tach | 88 |
| DIGIT PROFILE | RPM Profile from ext. sync. Based tach | 76 |
| SCALAR RPM PROFILE | RPM Profile from input-based tach | 77 |
| VIRTUAL RPM PROFILE | RPM Profile from fractional tach | 89 |
| SIMULATED ANGULAR SPEED | RPM Speed from simulated Tach | 253 |
| SIMULATED PROFILE | RPM Speed profile from simulated Tach | 254 |
| TACH DC ANGULAR SPEED | RPM Speed from DC Tach | 255 |
| TACH DC PROFILE | RPM Speed profile from DC Tach | 256 |
| CBT ORDER 1 | Constant Band Tracking order 1 profile | 109 |
| CBT ORDER 2 | Constant Band Tracking order 2 profile | 110 |
| CBT ORDER 3 | Constant Band Tracking order 3 profile | 111 |
| CBT ORDER 4 | Constant Band Tracking order 4 profile | 112 |
| CBT ORDER 5 | Constant Band Tracking order 5 profile | 113 |
| CBT ORDER 6 | Constant Band Tracking order 6 profile | 114 |
| CBT ORDER 7 | Constant Band Tracking order 7 profile | 115 |
| CBT ORDER 8 | Constant Band Tracking order 8 profile | 116 |
| FFT OVERALL BAND TRACKING | Overall band tracking profile | 117 |
| ORDER 1 | Constant Band Tracking order 1 (SOA, FFT) | 100 |
| ORDER 2 | Constant Band Tracking order 2 (SOA, FFT) | 101 |
| ORDER 3 | Constant Band Tracking order 3 (SOA, FFT) | 102 |
| ORDER 4 | Constant Band Tracking order 4 (SOA, FFT) | 103 |
| ORDER 5 | Constant Band Tracking order 5 (SOA, FFT) | 104 |
| ORDER 6 | Constant Band Tracking order 6 (SOA, FFT) | 105 |
| ORDER 7 | Constant Band Tracking order 7 (SOA, FFT) | 106 |
| ORDER 8 | Constant Band Tracking order 8 (SOA, FFT) | 107 |
| OVERALL LEVEL | Overall level (SOA, FFT) | 108 |
| PRE FILTERING | Filtered signal (SOA, FFT) | 19 |
| ORDER INSTANT SPECTRUM | Synchronous Order x Instantaneous spectrum | 80 |
| ORDER AVERAGE SPECTRUM | Synchronous Order x Averaged spectrum | 81 |
| ORDER SPECTRUM | Synchronous Order x time domain averaged<br>Spectrum | 82 |
| SOA TRIGGER BLOCK | Synchronous Order x Trigger block | 83 |
| SOA WEIGHTED BLOCK | Synchronous Order x Weighted block | 87 |
| SOA AVERAGED SIGNAL | Synchronous Order x Averaged signal (time<br>averaging) | 86 |
| ZOOM INSTANT SPECTRUM | FFTx zoomed instant spectrum | 90 |
| ZOOM AVERAGE SPECTRUM | FFTx averaged zoomed spectrum | 91 |
| ZOOM CROSS SPECTRUM | FFTx zoomed cross spectrum | 170 |
| AVERAGE ZOOM CROSS SPECTRUM | FFTx averaged zoomed cross spectrum | 171 |
| ZOOM FRF H1 | FFTx zoomed averaged H1 frequency response<br>function | 172 |
| ZOOM FRF H2 | FFTx zoomed averaged H2 frequency response<br>function | 173 |
| COHERENCE | FFTx zoomed coherence function | 174 |
| TRIGGER ENV | Envelope trigger block | 197 |
| AVG SPECTRUM ENV | Envelope spectrum | 198 |
| WEIGHT WINDOW ENV | Weighted envelope trigger block | 200 |
| OCTAVE OVERALL LIN | 1/n Octave Global level | 193 |
| OCTAVE OVERALL WEIGHTED | 1/n Octave Global level weighted | 194 |
| OVA SHORT LPK | Short Leq for peak detector | 47 |
| OVA INSTANT LEQ 1 | Instant Leq for detector 1 | 48 |


<!-- page 355 -->
(*) Commands "GetResult" and "GetSavedResult" does not apply to this type of
result.

| OVA INSTANT LEQ 2 | Instant Leq for detector 2 | 49 |
|---|---|---|
| OVA INSTANT LEQ 3 | Instant Leq for detector 3 | 50 |
| OVA SHORT LEQ 1 | Short Leq for detector 1 | 51 |
| OVA SHORT LEQ 2 | Short Leq for detector 2 | 52 |
| OVA SHORT LEQ 3 | Short Leq for detector 3 | 53 |
| OVA LEQ 1 | Leq for detector 1 | 54 |
| OVA LEQ 2 | Leq for detector 2 | 55 |
| OVA LEQ 3 | Leq for detector 3 | 56 |
| OVA MAX LPK | Max Leq for peak detector | 201 |
| OVA MIN LPK | Min Leq for peak detector | 202 |
| OVA MAX LEQ 1 | Max Leq for detector 1 | 203 |
| OVA MAX LEQ 2 | Max Leq for detector 2 | 204 |
| OVA MAX LEQ 3 | Max Leq for detector 3 | 205 |
| OVA MIN LEQ 1 | Min Leq for detector 1 | 206 |
| OVA MIN LEQ 2 | Min Leq for detector 2 | 207 |
| OVA MIN LEQ 3 | Min Leq for detector 3 | 208 |
| PREVIEW SIGNAL (*) | Preview signal | 191 |
| COMPRESSED SIGNAL (*) | Player signal | 25 |
| COMPRESSED MONITORING SIGNAL (*) | Recorder signal | 30 |
| NVD TIME | Time signal created thru NVDrive® | 175 |
| NVD ROTATION | Rotation signal created thru NVDrive® | 176 |
| NVD REAL SPECTRUM | Real spectrum created thru NVDrive® | 177 |
| NVD COMPLEX SPECTRUM | Complex spectrum created thru NVDrive® | 178 |
| NVD REAL ORDER SPECTRUM | Real order spectrum created thru NVDrive® | 179 |
| NVD COMPLEX ORDER SPECTRUM | Complex order spectrum created thru NVDrive® | 180 |
| NVD COHERENCE | Coherence created thru NVDrive® | 181 |
| NVD SCALAR | Scalar created thru NVDrive® | 182 |
| NVD NTH OCTAVE | Nth Octave created thru NVDrive® | 183 |
| NVD REAL PROFILE | Real Profile created thru NVDrive® | 185 |
| NVD COMPLEX PROFILE | Complex Profile created thru NVDrive® | 186 |
| NVD REAL WTF SPECTRUM | Real waterfall spectrum created thru NVDrive® | 187 |
| NVD COMPLEX WTF SPECTRUM | Complex waterfall spectrum created thru NVDrive® | 192 |
| NVD WTF TIME | Waterfall Time signal created thru NVDrive® | 189 |
| NVD WTF OCTAVE | Waterfall Nth Octave created thru NVDrive® | 188 |
| NVD CEPSTRUM | Cepstrum created thru NVDrive® | 300 |
| NVD AUTO CORR INST | Instantaneous auto-correlation created thru<br>NVDrive® | 301 |
| NVD AUTO CORR AVG | Averaged instantaneous auto-correlation created thru<br>NVDrive® | 302 |
| NVD AUTO CORRELATION | Auto-correlation created thru NVDrive® | 303 |
| NVD CROSS CORR INST | Instantaneous cross-correlation created thru<br>NVDrive® | 304 |
| NVD CROSS CORR AVG | Averaged instantaneous cross-correlation created thru<br>NVDrive® | 305 |
| NVD CROSS CORRELATION | Cross-correlation created thru NVDrive® | 306 |
| NVD_GAP | Shaft centerline thru NVDrive® | 309 |


<!-- page 356 -->

#### 3.10.6 - Corresponding table Process Id <=> NVD process Id


| INSTANT TRIGGER<br>AVERAGED TRIGGER<br>WEIGHTED<br>TRIGGERED<br>TRIGGER ENV<br>PRE FILTERING | NVD TEMPOREL |
|---|---|
| DC<br>RMS<br>RMS FRONT END<br>SKEW<br>KURTOSIS<br>MAX<br>MIN<br>PEAK LEVEL<br>PEAK PEAK LEVEL<br>PEAK FACTOR LEVEL<br>ANGULAR SPEED<br>DIGIT ANGULAR SPEED<br>VIRTUAL ANGULAR SPEED<br>SIMULATED ANGULAR SPEED<br>TACH DC ANGULAR SPEED<br>ORDER 1<br>ORDER 2<br>ORDER 3<br>ORDER 4<br>ORDER 5<br>ORDER 6<br>ORDER 7<br>ORDER 8<br>OVERALL LEVEL<br>OVA MAX LPK<br>OVA MIN LPK<br>OVA MAX LEQ 1<br>OVA MAX LEQ 2<br>OVA MAX LEQ 3<br>OVA MIN LEQ 1<br>OVA MIN LEQ 2<br>OVA MIN LEQ 3<br>OVA SHORT LPK<br>OVA INSTANT LEQ 1<br>OVA INSTANT LEQ 2<br>OVA INSTANT LEQ 3<br>OVA SHORT LEQ 1<br>OVA SHORT LEQ 2<br>OVA SHORT LEQ 3<br>OVA LEQ 1<br>OVA LEQ 2<br>OVA LEQ 3 | NVD SCALAR |
| 1/N OCTAVE<br>AVERAGE 1/N OCTAVE<br>AVERAGE 1/N OCTAVE MIN<br>AVERAGE 1/N OCTAVE MAX | NVD NTH OCTAVE |


<!-- page 357 -->

| SCALAR PROFILE<br>SCALAR RPM PROFILE<br>DIGIT PROFILE<br>SIMULATED PROFILE<br>TACH DC PROFILE<br>CBT ORDER 1<br>CBT ORDER 2<br>CBT ORDER 3<br>CBT ORDER 4<br>CBT ORDER 5<br>CBT ORDER 6<br>CBT ORDER 7<br>CBT ORDER 8<br>FFT OVERALL BAND TRACKING | NVD PROFILE |
|---|---|
| AVERAGE SPECTRUM<br>AVERAGE CROSS SPECTRUM<br>ORDER AVERAGE SPECTRUM<br>AVG SPECTRUM ENV | NVD REAL SPECTRUM |
| INSTANT SPECTRUM<br>INSTANT CROSS SPECTRUM<br>ORDER SPECTRUM<br>ORDER INSTANT SPECTRUM<br>SPECTRUM<br>FRF H2<br>FRF H1 | NVD COMPLEX SPECTRUM |
| COHERENCE | NVD COHERENCE |
| SOA TRIGGER BLOCK<br>SOA WEIGHTED BLOCK<br>SOA AVERAGED SIGNAL | NVD ROTATION |
| CEPSTRUM<br>CEPSTRUM ZOOM | NVD CEPSTRUM |
| AUTO CORR INST | NVD AUTO CORR INST |
| AUTO CORR AVG | NVD AUTO CORR AVG |
| AUTO CORRELATION | NVD AUTO CORRELATION |
| CROSS CORR INST | NVD CROSS CORR INST |
| CROSS CORR AVG | NVD CROSS CORR AVG |
| CROSS CORRELATION | NVD CROSS CORRELATION |
| GAP | NVD_GAP |
| LISSAJOUS<br>COMPRESSED SIGNAL<br>COMPRESSED MONITORING SIGNAL | Unavailable |


<!-- page 358 -->

#### 3.10.7 - Result format

The result format for each process type is described in the following table:

|   | Process name |   |   | Result format |   |
|---|---|---|---|---|---|
| DC<br>RMS<br>RMS FRONT END<br>SKEW<br>KURTOSIS<br>MAX<br>MIN<br>PEAK LEVEL<br>PEAK PEAK LEVEL<br>PEAK FACTOR LEVEL<br>OCTAVE OVERALL LIN<br>OCTAVE OVERALL WEIGHTED<br>OVA SHORT LPK<br>OVA INSTANT LEQ 1<br>OVA INSTANT LEQ 2<br>OVA INSTANT LEQ 3<br>OVA SHORT LEQ 1<br>OVA SHORT LEQ 2<br>OVA SHORT LEQ 3<br>OVA LEQ 1<br>OVA LEQ 2<br>OVA LEQ 3<br>OVA MAX LPK<br>OVA MIN LPK<br>OVA MAX LEQ 1<br>OVA MAX LEQ 2<br>OVA MAX LEQ 3<br>OVA MIN LEQ 1<br>OVA MIN LEQ 2<br>OVA MIN LEQ 3<br>ANGULAR SPEED<br>DIGIT ANGULAR SPEED<br>VIRTUAL ANGULAR SPEED<br>SIMULATED ANGULAR SPEED<br>TACH DC ANGULAR SPEED<br>NVD SCALAR |   |   | Scalar |   |   |
| INSTANT<br>PRE FILTERING<br>AVERAGE SPECTRUM<br>INSTANT SPECTRUM<br>INSTANT CROSS SPECTRUM<br>AVERAGE CROSS SPECTRUM<br>SPECTRUM<br>WEIGHTED<br>TRIGGERED<br>FRF H1<br>FRF H2<br>COHERENCE<br>1/N OCTAVE<br>AVERAGE 1/N OCTAVE<br>AVERAGE 1/N OCTAVE MIN<br>AVERAGE 1/N OCTAVE MAX<br>ORDER INSTANT SPECTRUM<br>ORDER AVERAGE SPECTRUM |   |   | RegVector |   |   |


<!-- page 359 -->

**ORDER SPECTRUM
ORDER INSTANT SPECTRUM
ORDER AVERAGE SPECTRUM
ORDER SPECTRUM
SOA TRIGGER BLOCK
SOA WEIGHTED BLOCK
SOA AVERAGED SIGNAL
ZOOM INSTANT SPECTRUM
ZOOM AVERAGE SPECTRUM
ZOOM CROSS SPECTRUM
AVERAGE ZOOM CROSS SPECTRUM
ZOOM FRF H1
ZOOM FRF H2
COHERENCE
TRIGGER ENV
AVG SPECTRUM ENV
CEPSTRUM
CEPSTRUM ZOOM
AUTO CORR INST
AUTO CORR AVG
AUTO CORRELATION
CROSS CORR INST
CROSS CORR AVG
CROSS CORRELATION
NVD TIME
NVD ROTATION
NVD REAL SPECTRUM
NVD COMPLEX SPECTRUM
NVD REAL ORDER SPECTRUM
NVD COMPLEX ORDER SPECTRUM
NVD COHERENCE
NVD NTH OCTAVE
NVD CEPSTRUM
NVD AUTO CORR INST
NVD AUTO CORR AVG
NVD AUTO CORRELATION
NVD CROSS CORR INST
NVD CROSS CORR AVG
NVD CROSS CORRELATION**

| DIGIT PROFILE<br>SCALAR RPM PROFILE<br>VIRTUAL RPM PROFILE<br>SIMULATED PROFILE<br>TACH DC PROFILE<br>CBT ORDER 1<br>CBT ORDER 2<br>CBT ORDER 3<br>CBT ORDER 4<br>CBT ORDER 5<br>CBT ORDER 6<br>CBT ORDER 7<br>CBT ORDER 8<br>ORDER 1<br>ORDER 2<br>ORDER 3<br>ORDER 4<br>ORDER 5<br>ORDER 6<br>ORDER 7<br>ORDER 8<br>OVERALL LEVEL<br>NVD REAL PROFILE<br>NVD COMPLEX PROFILE | RefVector |
|---|---|


<!-- page 360 -->
- Result with x regular values :
RegVector:
- Result with one or more reference on x / z axis :
RefVector:
- Waterfall 3D Result:
Waterfall 3D:
- Waterfall 2D Result :
Waterfall 2D:
- Result composed of one single value:
Scalar:
- Signal from recorder:
RecordSignal:
(*) If the Complex field of the HEAD block equals 1, then CVEC block.
If this field equals 0, then RVEC block.
(**) If the Complex field of the HEAD block equals 1, then the SCAL block
(since version 2) contains an "Imag" field.
(***) Presence of the block depends on the command behavior.
(Grayed) Info block is only available if the GetResult version number (or version
parameter used with GetResultEx command) is equal to or greater than 3.

**SCALAR PROFILE
VIRTUAL RPM PROFILE
FFT OVERALL BAND TRACKING
GAP
NVD_GAP**

| WATERFALL<br>NVD REAL WTF SPECTRUM<br>NVD COMPLEX WTF SPECTRUM<br>NVD WTF TIME<br>NVD WTF OCTAVE | Waterfall |
|---|---|


| HEAD | XREG | CVEC / RVEC (*) |   | INFO |   |
|---|---|---|---|---|---|


| HEAD | XREF | CVEC / RVEC (*) |   | INFO |   |
|---|---|---|---|---|---|


| HEAD | DWTF | XREF | XREG | CWTF / RWTF(*) |   | INFO |   |
|---|---|---|---|---|---|---|---|


| HEAD | DWTF | XREF | CVEC / RVEC(*) |   | INFO |   |
|---|---|---|---|---|---|---|


| HEAD | SCAL(**) |   | INFO |   |
|---|---|---|---|---|


| HEAD<br>*** | XREG<br>*** | RVEC | RNFO |
|---|---|---|---|


<!-- page 361 -->

#### 3.10.8 - Generic Header

Each block consists of a generic header:
The header is grayed in the blocks described below.

#### 3.10.9 - HEAD block

HEAD block is the first block of data for each type of result.
For version = 1 or 2, additional fields:
In version 3, those fields are no more present. This information is transferred in the
INFO block.
For version >= 4, additional field:

| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | Key identifying the type of block that follows |   |
| 2 | 2 |   | Short | Short |   | Version | Version |   |   | Version number allowing structure evolution (the first version |   |
|   |   |   |   |   |   |   |   |   |   | is numbered 0) |   |
|   | 4 |   |   | long |   |   | BlockSize |   |   | Size of rest of block |   |


| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | Value: HEAD |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 5 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 2 |   |   | Short |   |   | ResultType |   |   | The "Result Type" represents the result format. The different<br>values are:<br>1 : Scalar result<br>2 : RegVector<br>3 : RefVector<br>8 : Waterfall<br>15 : RecordSignal |   |   |
| 4 |   |   | Long |   |   | Size |   |   | Number of data lines |   |   |
| 2 |   |   | Short |   |   | Dimension |   |   | 1 for 1 1D / 2 for 2D / 3 for 3D |   |   |
| 2 |   |   | Short |   |   | Complex |   |   | 1 if the result contains complex data, other values meaning<br>real data. |   |   |
| 2 |   |   | Short |   |   | MeasureStatus |   |   | 0 if no measurement has been taken (in this case, Size = 0),<br>1 if a measurement is in progress, 2 if measurement finished |   |   |
| X |   |   | String |   |   | PhysicalQuantity |   |   | Quantity name |   |   |
| X |   |   | String |   |   | UnitName |   |   | Unit name |   |   |
| X |   |   | String |   |   | UnitLabel |   |   | Unit symbol |   |   |
| X |   |   | String |   |   | Name |   |   | Result name |   |   |


| 2 | Short | OverallLevelStatus | 1 if the Overall Level must be added to the Data<br>Array of a RegVector Result. |
|---|---|---|---|
| 2 | Short | WeigtedOLStatus | 1 if the Weighted Overall Level must be added to<br>the Data Array of a RegVector Result. |


<!-- page 362 -->
For version >= 5, additional field:
Important note: When the field is a character string, this string ends in '\0' (except
for the ID field where the number of characters is equal to 4). The characters are
coded in ASCII.

| 2 | Unsigned<br>Short | WeightingWindow | For previous versions, this field is set to Hanning.<br>WW_UNIFORM = 316,<br>WW_HANNING = 333,<br>WW_HAMMING = 334,<br>WW_KAISER_BESSEL = 335,<br>WW_FLATTOP = 336,<br>W W_EXPONENTIAL = 337 |
|---|---|---|---|


| X | String | MagnitudeKey | The key that identifies the PhysicalQuantity (ex:<br>P otential_Difference, see OrosUnit.ini file) |
|---|---|---|---|


<!-- page 363 -->

#### 3.10.10 - XREG block

Regular X axis: XREG block defines the step, min and max value on X axis for a
RegVector result.
Example: spectrum.
For version >= 1, additional fields:
For version >= 3, additional fields:

| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | XREG |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 3 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 4 |   |   | Float |   |   | Start |   |   | Start value |   |   |
| 4 |   |   | Float |   |   | Stop |   |   | End value |   |   |
| 2 |   |   | Short |   |   | N-Octave |   |   | Step |   |   |
| x |   |   | String |   |   | PhysicalQuantity |   |   | Quantity name |   |   |
| x |   |   | String |   |   | UnitName |   |   | Unit name |   |   |
| x |   |   | String |   |   | UnitLabel |   |   | Unit symbol |   |   |


| 4 | Float | RelPrecision | Relative precision |
|---|---|---|---|
| 4 | Float | AbsPrecision | Absolute precision |


| X | String | MagnitudeKey | The key that identifies the PhysicalQuantity (ex: Frequency,<br>see OrosUnit.ini file) |
|---|---|---|---|


<!-- page 364 -->

#### 3.10.11 - XREF block

Referenced X-axis: XREF bloc contains the values of the references of a
RefVector result. These references can be on X-axis (2D result) or Z axis (3D
result).
Example of 3D result: spectrum waterfall.
Example of 2D result: tacho profile.
For version >= 1, each reference description has some additional fields:
For version >= 2, each reference description has some additional fields:
For version >= 3, additional fields:
Important note: If the "result process id" is equal to GAP or NVD_GAP, the
Y vector value is also a reference. The list of references is given in this order:
- All tag references values,
- Y vector values,
- X vector values.

| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | XREF |   |   |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 3 |   |   |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |   |   |
| 2 |   |   | Short |   |   | NbRef |   |   | Number of references |   |   |   |   |
| x |   |   | String |   |   | VecName |   |   | Reference name |   |   | NbRef times |   |
| x |   |   | String |   |   | PhysicalQuantity |   |   | Quantity name |   |   |   |   |
| x |   |   | String |   |   | UnitName |   |   | Unit name |   |   |   |   |
| x |   |   | String |   |   | UnitLabel |   |   | Unit symbol |   |   |   |   |
|   | Size * 4 |   |   | float |   |   | Data |   |   | Reference values (float list) |   |   |   |


| 4 | Float | RelPrecision | Relative precision | NbRef times |
|---|---|---|---|---|
| 4 | Float | AbsPrecision | Absolute precision |   |


| 4 | Float | Min | Minimum value | NbRef times |
|---|---|---|---|---|
| 4 | Float | Max | Maximum value |   |


| X | String | MagnitudeKey | The key that identifies the PhysicalQuantity (ex:<br>Slice_Number, see OrosUnit.ini file) |
|---|---|---|---|


<!-- page 365 -->

#### 3.10.12 - CVEC block

Complex vector: CVEC contains Y-axis complex values.
Example: FFT instant spectrum.
For version >= 1, additional fields:

| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | CVEC |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 4 |   |   | Float |   |   | RealMin |   |   | Real part min value |   |   |
| 4 |   |   | Float |   |   | RealMax |   |   | Real part max value |   |   |
| 4 |   |   | Float |   |   | ImMin |   |   | Imaginary part min value |   |   |
| 4 |   |   | Float |   |   | ImMax |   |   | Imaginary part max value |   |   |
| Size*2*4 |   |   | float |   |   | Data |   |   |   | List of pairs (real part, imaginary part). The « Size » |   |
|   |   |   |   |   |   |   |   |   |   | value comes from the HEAD block. It takes into account |   |
|   |   |   |   |   |   |   |   |   |   | the overall levels, if selected in the HEAD block. |   |


| 4 | Float | RealRelPrecision | Real part relative precision |
|---|---|---|---|
| 4 | Float | RealAbsPrecision | Real part absolute precision |
| 4 | Float | ImRelPrecision | Imaginary part relative precision |
| 4 | Float | ImAbsPrecision | Imaginary part absolute precision |


<!-- page 366 -->

#### 3.10.13 - RVEC block

Real vector: RVEC contains Y-axis real values.
Example: Octave spectrum
For version >= 1, additional fields:

| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | RVEC |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 4 |   |   | Float |   |   | RealMin |   |   | Real part min value |   |   |
| 4 |   |   | Float |   |   | RealMax |   |   | Real part max value |   |   |
| Size * 4 |   |   | Float |   |   | Data |   |   |   | The « Size » value comes from the HEAD block. It |   |
|   |   |   |   |   |   |   |   |   |   | takes into account the overall levels, if selected in the |   |
|   |   |   |   |   |   |   |   |   |   | HEAD block. |   |


| 4 | Float | RealRelPrecision | Real part relative precision |
|---|---|---|---|
| 4 | Float | RealAbsPrecision | Real part absolute precision |


<!-- page 367 -->

#### 3.10.14 - SCAL block

Scalar: SCAL contains minimum, maximum and current value of the scalar
result.
Example: RPM speed.
For version >= 1, additional fields:
For version >= 2, additional fields for complex scalar:
Note that the Imaginary part is available only if the HEAD Complex value is 1.
In this case the Scalar value is the Real part.

| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | SCAL |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 2 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   | 24 for version 2 |   |
| 4 |   |   | Float |   |   | Min |   |   | Min value |   |   |
| 4 |   |   | Float |   |   | Max |   |   | Max value |   |   |
|   | 4 |   |   | Float |   |   | Value |   |   | Scalar value |   |


| 4 | Float | RelPrecision | Relative precision |
|---|---|---|---|
| 4 | Float | AbsPrecision | Absolute precision |


| 4 | Float | Imag | Imaginary part |
|---|---|---|---|


<!-- page 368 -->

#### 3.10.15 - DWTF block

DWTF block is the block that describes a 2D or 3D Waterfall result

#### 3.10.16 - RWTF block

Real waterfall vector: RWTF contains Y-axis real values of the oldest vector first
and the newest vector is at the end of the data block.
For version >= 1, additional fields:

| Size<br>(bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | Value: DWTF |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 0 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   | 12 for version 0 |   |
| 2 |   |   | Short |   |   | Process Number |   |   | Identification number of the process |   |   |
| 4 |   |   | Long |   |   | FirstIndex |   |   | Index of the oldest Waterfall scalar or vector transmitted |   |   |
| 4 |   |   | Long |   |   | LastIndex |   |   | Index of the newest Waterfall scalar or vector transmitted |   |   |
| 2 |   |   | Short |   |   | RequestStatus |   |   | 0 if everything is alright,<br>1 if there is less values than asked<br>2 if the StartIndex asked is not available yet |   |   |


| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | RWTF |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 4 |   |   | Float |   |   | RealMin |   |   | Real part min value |   |   |
| 4 |   |   | Float |   |   | RealMax |   |   | Real part max value |   |   |
|   | 4 |   |   | Long |   |   | VectorSize |   |   | Size of one vector |   |
|   | 4 |   |   | Long |   |   | Depth |   |   | Number of vectors |   |
|   | VectorSize* |   | Float | Float |   | Data | Data |   |   | First vector : the oldest |   |
|   | Depth * 4 |   |   |   |   |   |   |   |   | Last vector : the newest |   |


| 4 | Float | RelPrecision | Relative precision |
|---|---|---|---|
| 4 | Float | AbsPrecision | Absolute precision |


<!-- page 369 -->

#### 3.10.17 - CWTF block

Complex waterfall vector: CWTF contains Y-axis complex values of the oldest
vector first and the newest vector is at the end of the data block.
For version >= 1, additional fields:

| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | CWTF |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   |   |   |
| 4 |   |   | Float |   |   | RealMin |   |   | Real part min value |   |   |
| 4 |   |   | Float |   |   | RealMax |   |   | Real part max value |   |   |
| 4 |   |   | Float |   |   | ImMin |   |   | Imaginary part min value |   |   |
| 4 |   |   | Float |   |   | ImMax |   |   | Imaginary part max value |   |   |
|   | 4 |   |   | Long |   |   | VectorSize |   |   | Size of one vector |   |
|   | 4 |   |   | Long |   |   | Depth |   |   | Number of vectors |   |
| VectorSize*<br>Depth * 4 *2 | VectorSize* |   | Float | Float |   | Data | Data |   |   | List of pairs( real part, imaginary part) |   |
|   | Depth * 4 *2 |   |   |   |   |   |   |   |   | First vector : the oldest |   |
|   |   |   |   |   |   |   |   |   |   | Last vector : the newest |   |


| 4 | Float | RealRelPrecision | Imaginary part relative precision |
|---|---|---|---|
| 4 | Float | RealAbsPrecision | Imaginary part absolute precision |
| 4 | Float | ImRelPrecision | Imaginary part relative precision |
| 4 | Float | ImAbsPrecision | Imaginary part absolute precision |


<!-- page 370 -->

#### 3.10.18 - INFO block

INFO block contains current date, and tacho value of the result.
This type of block exists since NVGate V5.0.
The InfoMask can be a combination of the following bit values:
- 0x1 : Global level filled.
- 0x2 : Weighted global level filled.
- 0x4 : Tacho reference filled.
- 0x8 : Date is filled.
If the info block si sent, the global levels are not included in the other blocks.
The date is a 64 bits value, representing the number of 100-nanosecond intervals
since January 1, 1601.

#### 3.10.19 - RNFO block

RECORD SIGNAL INFO block contains information about the samples read.
This type of block exists since NVGate V17.00.

| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | INFO |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   | 24 for version 1 |   |
| 4 |   |   | long |   |   | InfoMask |   |   | Indicates which fields are available |   |   |
| 4 |   |   | Float |   |   | GlobalLevel |   |   | Global level value |   |   |
| 4 |   |   | Float |   |   | WeightedGlobalLevel |   |   | Weighted global level value |   |   |
| 4 |   |   | Float |   |   | Tacho |   |   | Tacho value |   |   |
|   | 8 |   |   | 2*Long |   |   | Date |   |   | Result date value |   |


| Size (bytes) |   |   | Type |   |   | Field name |   |   | Description |   |   |
|---|---|---|---|---|---|---|---|---|---|---|---|
|   | 4 |   |   | String |   |   | ID |   |   | INFO |   |
|   | 2 |   |   | Short |   |   | Version |   |   | Last version = 1 |   |
|   | 4 |   |   | Long |   |   | BlockSize |   |   | 24 for version 1 |   |
| 2 |   |   | Int |   |   | Samples |   |   | Number of read samples |   |   |
| 4 |   |   | Float |   |   | Duration |   |   | Duration of the signal read |   |   |
| 2 |   |   | Short |   |   | State |   |   | 0 if all the requested samples have been read<br>1 if not enough data was available in the record<br>and the recording is running<br>2 if not enough data was available in the record<br>and the recording is stopped |   |   |


<!-- page 371 -->

### 3.11 - RECORDER SETUP (OPTION)

The following commands are only available for analyzers with Recorder setup option,
and NVGate since V6.12.

#### 3.11.1 - "AddCurrentSetup" command


**Semantics**

Used to generate and upload a configuration on the analyzer. Only Front-end,
Recorder, and Event are present in this configuration.

**Command syntax**

```
AddCurrentSetup [config name]
The optional parameter config name enables to give a name to this setup. If
missing, NVGate forces a default name using the number of channels, the
sampling frequency and the record duration (if "start to time").
Ex: 32_Ch_51200_kSps
```

**Result returned**

A list of strings. Each string ends in the character \0. The first string is the name
of the setup generated and the rest is a list of idns that have an invalid value for
recorder setup.

#### 3.11.2 - "RemoveRecorderSetup" command


**Semantics**

Remove a configuration on the analyzer.

**Command syntax**

```
RemoveRecorderSetup <config name>
The parameter config name is the name of the configuration to remove from
analyzer.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the AddCurrentSetup command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 305 | 001 | 000 | Command unavailable |
| 305 | 002 | 000 | Too many configurations on the hard (max = 12). |
| 305 | 003 | 000 | Error while creating setup |


**Consistency errors specific to the RemoveRecorderSetup command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 307 | 001 | 000 | Command unavailable |
| 307 | 002 | 000 | Error while removing file |


<!-- page 372 -->

#### 3.11.3 - "GetRecorderSetupList" command


**Semantics**

Get the list of recorder setup names that are present on the analyzer.

**Command syntax**

```
GetRecorderSetupList
```

**Result returned**

A list of strings. Each string ends in the character \0 and is the name of a setup.

**Consistency errors specific to the GetRecorderSetupList command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 306 | 001 | 000 | Command unavailable |
| 306 | 002 | 000 | Error reading disk |


<!-- page 373 -->

#### 3.11.4 - "GetDefaultRecorderSetup" command


**Semantics**

Get the name of the configuration present on the analyzer that will be loaded by
default.

**Command syntax**

```
GetDefaultRecorderSetup
```

**Result returned**

The name of the recorder setup that is loaded by default (string ending in the
character \0.).

#### 3.11.5 - "SetDefaultRecorderSetup" command


**Semantics**

Affects the name of the default recorder configuration on the analyzer.

**Command syntax**

```
SetDefaultRecorderSetup <config name>
The parameter config name is the name of the configuration that will be
loaded by default.
Warning : there is no check that the config name exists.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the GetDefaultRecorderSetup
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 309 | 001 | 000 | Command unavailable |
| 309 | 002 | 000 | Error while reading config name |


**Consistency errors specific to the SetDefaultRecorderSetup
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 308 | 001 | 000 | Command unavailable |
| 308 | 002 | 000 | Error while writing ini file on analyzer (that memorizes the<br>default config name) |


<!-- page 374 -->

#### 3.11.6 - "ExportRecorderConfigAsText" command


**Semantics**

Export a recorder configuration in a text file.

**Command syntax**

```
ExportRecorderConfigAsText <config name>
<txt path>
The parameter config name is the name of the configuration that will be
exported.
The parameter txt path is the path of the txt file (path + file name + ".txt")
that will be created.
Warning : if the file already exists, it will be replaced.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ExportRecorderConfigAsText
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 311 | 001 | 000 | Command unavailable |
| 311 | 002 | 000 | Error while transferring data from Analyzer to PC |
| 311 | 003 | 000 | Error while creating txt file |


<!-- page 375 -->

#### 3.11.7 - "ImportRecorderConfigInASB" command


**Semantics**

Import a recorder configuration in the Analyzer setting browser of NVGate.

**Command syntax**

```
ImportRecorderConfigInASB <config name>
The parameter config name is the name of the configuration that will be
exported.
```

**Result returned**

No data follows the header.

**Consistency errors specific to the ImportRecorderConfigInASB
command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 315 | 001 | 000 | Command unavailable |
| 315 | 002 | 000 | Error while transferring data from Analyzer to PC |
| 315 | 003 | 000 | Error while importing config file |


<!-- page 376 -->

### 3.12 - EV/HV (OPTION)

The following commands are related to the EV/HV NVGate option.

#### 3.12.1 - "GetEvhvCurrentSpatiogramMeasurement"

command

**Semantics**

Returns the currently selected EV/HV measurement selected as current
measurement for Spatiogram calculation.

**Command syntax**

```
GetEvhvCurrentSpatiogramMeasurement
This command has no parameter.
```

**Result returned**

Path to the measurement, ending with a zero-byte (\0).
By default, the string is returned in the current code page (default Windows 8-bits
encoding).

**Consistency errors specific to the AddCurrentSetup command**

| Code (1) | Code (2) | Code (3) | Meaning |
|---|---|---|---|
| 379 | 001 | 000 | EV/HV option is not available |
| 379 | 002 | 000 | There is no current measurement at this time. |


<!-- page 378 -->

## 4 - APPENDIXES


### 4.1 - LAUNCHING NVGATE® FROM COMMAND LINE

NVGate® software can be launched by the NVDrive® application directly from the
windows command line. The command line may contain optional parameters that
define the analyzer mode and/or default preferences.

#### 4.1.1 - Connected / office mode

You can select the mode of NVGate and skip the the connection dialog
Use the following command line option to:
Launch NVGate® in office mode:
NVGate -offline
Launch NVGate® in connected mode with one OR3x real-time analyzer:
NVGate -online -or3xip=223.255.253.50
NVGate -online -ListHardIpAddr=223.255.253.50
Launch NVGate® in connected teamwork mode with 2 chained OR3x analyzers:
NVGate -online -teamwork -ListHardIpAddr=223.255.253.50,223.255.253.51
Launch NVGate® in frontend mode with an OR10:
NVGate -frontend=FE80::204:F3FF:FE07:8F7C%12
Note: replace the IP addresses by your device configuration. (The OR10 IP
address can be obtained by clicking on "DHCP Server" in the NVGate connection
dialog)
Launch NVGate® in frontend mode with an O4:
NVGate -ConnectToDAQ -USB_Device_Index=1

<!-- page 379 -->
Note: replace the USB index by your device configuration. (The index is the same
as the order in the NVGate connection dialog)

#### 4.1.2 - User profiles set

NVGate® software preferences are saved in user profiles files with .usr type. That
file contains a set of user profiles plus windows and toolbar arrangement of the
last NVGate® execution.
You can create one set of user plus a specific windows and toolbar arrangement
from a NVGate® running session. The result will be saved in the default
NVGate.usr file. This file can be renamed using windows explorer.
NVGate -usr=XXX l launch NVGate® with the user file XXX.usr
If the -usr option is not specified, the user file NVGate.usr is used by default.
Note: user file contains a set of user preferences and NVGate® windows and
toolbars arrangement.

#### 4.1.3 - User selection

You can select the user's name inside a selected user file by using the following
command line:
NVGate -user=username

#### 4.1.4 - Client application name

When you launch NVGate® from an external application, you can display the
name of your application in the NVGate® Splash screen. Use the following
command line:
NVGate -ExternalAppName=YourApplicationName

#### 4.1.5 - Splash screen

To avoid the splash screen being displayed when launching NVGate®, use the
following command line:
NVGate -silent

#### 4.1.6 - MessageBox

If you want to use NVGate® without any user interaction (monitoring, long
measurement...), you can disable all the jumping message box (Warning,
questions...) that would stop the analysis by using the following command line:
NVGate -silentex

<!-- page 380 -->

#### 4.1.7 - Start and Go Dialog

You can avoid the "Start and Go" dialog
Use the following command line:
NVGate -StartAndGoOff

#### 4.1.8 - Project base

You can select your project base and skip the default one by using the following
command line:
NVGate -ProjectBase=YourProjectBasePath

#### 4.1.9 - Analyzer IP address

You can select the IP address of the analyzer by using the following command
line:
NVGate -online -or3xip=AAA.BBB.CCC.DDD
To start NVGate in multi-analyzer mode (two or more OR3x):
NVGate -online -teamwork -ListHardIpAddr=X.X.X.X,Y.Y.Y.Y,Z.Z.Z
To start NVGate in frontend mode with an OR10:
NVGate -frontend=FE80::204:A:B:C%D (IPV6 random address)
NVGate -frontend=192.168.150.28 (IPV4 fixed address)
Note: For IPV6, replace the IP addresses by your device configuration. (The
OR10 IP address can be obtained by clicking on "DHCP Server" in the NVGate
connection dialog).
And for IPV4, don't forget to put your PC with IP address compatible to
"192.168.150.28".

<!-- page 381 -->

#### 4.1.10 - NVDrive® Disabled

If you do not want NVGate® to be accessible through NVDrive®, you can disable
it by using the following command line:
NVGate -DisableNVD

#### 4.1.11 - NVDrive® Port

The default port for NVDrive® is 3000. You can modify this default value by
using the following command line:
NVGate -NVDrivePort=YourPortNumber

#### 4.1.12 - Default project

You can force NVGate® to start with the default project, whatever the user
preferences are, by using the following command line:
NVGate -default

#### 4.1.13 - Band

You can force the NVGate® Band to be open or closed at start up
(folder/undolded):
NVGate -band=open
NVGate -band=close
NVGate -band=closed

<!-- page 383 -->

## 5 - COMMANDS INDEX

AbortStandAlone, 31 ConnectInput, 258
Accept, 26 ConnectToTCPClient, 335
AddArrayLine, 251 CopyBitmap, 139
AddAutoOperator, 129 CopyData, 137
AddCalibration, 268 CopyDataAllTraces, 138
AddCurrentSetup, 371 CopyGraph, 140
AddDataToTCPResultChannel, 321 CreateResultEx, 307
AddFreeMarker, 43 CreateTCPResultChannel, 318
AddHarmonicMarker, 49 DeleteAllResultEx, 312
AddKinematicMarker, 52 DeleteMeasurementUserProperty, 183
AddMaxMarker, 46 DeleteModel, 188
AddMeasurementUserProperty, 179 DeleteProjectUserProperty, 182
AddNOctaveMarker, 53 DeleteResultEx, 311
AddPeakMarker, 45 DisconnectFromTCPClient, 336
AddPeriodMarker, 51, 73 DisconnectInput, 259
AddPowerBandMarker, 47 DisplayMarkerProperties, 57
AddProjectUserProperty, 178 Download, 288
AddRecordMarker, 50 DuplicateMarkerInMultigraphWindow, 58
AddResultAutoMemorize, 126 EditCalibration, 36
AddResultTemplateToWindow, 159 EditSetting, 254
AddResultToSetup, 293 Emergency stop, 35
AddSideBandMarker, 48 EnableAutoMemorize, 128
AddToControlPanel, 202 ExecMacro, 21
AddToResultSelection, 299 ExecUINotification, 342
AddWindowPlayerResult, 92, 96 Export, 291
AddWindowResult, 90 ExportRecorderConfigAsText, 374
AddWindowSavedResult, 93 ExportTransducerDB, 275
AddWindowWtfResult, 95 FormatDisk, 38
AdministratorMode, 207 GetActiveTrace, 163
AppliedMode, 201 GetActiveWindow, 106
ArrangeWindows, 90, 119 GetAnalyzerModes, 221
Autorange, 32 GetAnalyzerState, 274
Autoscale, 113 GetAvailableScale, 147
AutoscaleAllWnd, 114 GetCurrentLayout, 103
CascadeView, 125 GetCurrentNVGatePath, 230
ChangeDisplayMode, 116 GetCurrentProjectName, 174
ChangeMode, 220 GetCurrentReference, 134
ChangeSignalDate, 287 GetCurrentUnit, 213
ChangeSpectralWeighting, 115 GetCurrentUserName, 223
ChangeTCPResultName, 325, 329, 330 GetCursorInfo, 136
ChangeWindowPreferences, 165 GetDatabasePath, 198
CheckICP, 33 GetDefaultRecorderSetup, 373
CheckTEDS, 34 GetDisplayMode, 117
ClearMemory, 124 GetDisplayModeList, 118
ClearSetupList, 295 GetErrorMessage, 20
CloseAllWindows, 112 GetEvent, 270
CloseWindow, 111

<!-- page 384 -->
GetEvhvCurrentSpatiogramMeasurement, GetSideBandMarkerParameters, 69
376 GetSideBandMarkerValue, 84
GetFanInfo, 226 GetSignalFileSettingValue, 246
GetFreeMarkerParameters, 60 GetSignalProperties, 285
GetFreeMarkerValue, 77 GetStateValue, 277
GetGeneralAnalyzerState, 273 GetStatus, 272
GetGraduationDirection, 162 GetSubModuleList, 245
GetHarmonicMarkerParameters, 72 GetTachometerPosition, 158
GetHarmonicMarkerValue, 86 GetTCPResult, 324
GetInputInfo, 257 GetTCPResultChannelList, 323
GetItemPMTree, 195 GetTEDSContent, 264
GetLayoutList, 102 GetTEDSContentOnInput, 263
GetMacroList, 229 GetTransducerInfo, 266
GetMagnitudeInfo, 216 GetTransducerList, 265
GetMagnitudeList, 210 GetUnitInfo, 214
GetMarkerList, 41, 57, 58 GetUnitList, 211
GetMaxMarkerParameters, 64 GetUserList, 222
GetMaxMarkerValue, 82 GetWindowDisplayZone, 40
GetMeasureList, 194 GetWindowList, 107
GetMeasurementUserPropertiesList, 177 GetWindowNameList, 108
GetMeasurementWindowTrace, 110 GetWindowPosition, 150
GetNumberOfRecordMarker, 54 GetWindowTraces, 39, 109
GetPeakMarkerParameters, 62 GetWTFResult, 315
GetPeakMarkerValue, 79 GetWTFResultList, 303
GetPeriodMarkerParameters, 76 GroupByMagnitude, 120
GetPeriodMarkerValue, 88 ImportFile, 290
GetPermission, 219 ImportProject, 172
GetPinStatus, 156 ImportRecorderConfigInASB, 375
GetPowerBandMarkerParameters, 67 IsResultWaterfallisable, 284
GetPowerBandMarkerValue, 83 IsScaleTimeInRelative, 149
GetPreferedWtfReference, 218 LoadMeasurement, 191
GetPreferenceGeneral, 224 LoadProject, 166
GetProjectList, 173 LoadWorkbook, 184
GetProjectProperties, 175 LoadWorkbookModel, 185
GetProjectUserPropertiesList, 176 LogWarning, 232
GetRecordDate, 286 ManualTrigger, 28
GetRecorderSetupList, 372 MaskAllToolbar, 104
GetRecordMarkerParameters, 65 MemorizeTrace, 122
GetReferenceList, 132 MergeTransducerDB, 276
GetResult, 313 ModifyArrayLine, 252
GetResultCaption, 304 ModifyMeasurementUserProperty, 181
GetResultEx, 308, 326, 327, 328 ModifyProjectUserProperty, 180
GetResultList, 302 NewDataForTCPResultChannel, 320
GetRotationPreferences, 152 NewLayout, 99
GetSavedResult, 317 NewProject, 167
GetSavedResultCaption, 306 OpenCloseInfoTrace, 121
GetSavedResultEx, 310 OpenProject, 168
GetSavedResultList, 305 Pause, 24
GetScaleInfo, 142 PinWindow, 155
GetSettingInfo, 244 PlayByStep, 25
GetSettingValue, 239 PrintReport, 331
GetSettingValues, 238 RefreshPM, 197

<!-- page 385 -->
RefreshState, 37 SetKinematicMarkerParameters, 75
RegisterCommand, 344 SetLayout, 98
RegisterNewMeasurement, 349 SetMaxMarkerParameters, 63
RegisterNewResult, 346 SetNewMeasurementParameters, 209
RegisterSetting, 339 SetNoAutomaticExport, 298
RegisterState, 337 SetPeakMarkerParameters, 61
RegisterUINotification, 341 SetPeriodMarkerParameters, 73
Reject, 27 SetPeriodMarkerVisibility, 74
ReloadCurrentWorkbook, 189 SetPhasePreference, 160
RemoveArrayLine, 253 SetPowerBandMarkerParameters, 66
RemoveLayout, 100 SetPreferedWtfReference, 217
RemoveMarker, 56 SetPreferenceGeneral, 225
RemoveMeasurement, 193 SetRecordMarkerLabel, 55
RemoveProject, 171 SetReference, 133
RemoveRecorderSetup, 371 SetResponseSettings, 249
RemoveResultAutoMemorize, 127 SetRotationPreferences, 153
RemoveSetupResult, 294 SetSaveOption, 208
RemoveSignalFromAnalyzer, 200 SetScaleTimeType, 148
RemoveTCPResultChannel, 319 SetScaleType, 144
RemoveToResultSelection, 300 SetScaleValues, 145
RemoveTrace, 123 SetSettingValue, 242
RenameLayout, 101 SetSetupParameters, 296
RenameWindow, 97 SetSideBandMarkerParameters, 68
ReportGetInteractiveDocumentList, 333 SetSignalFileSettingValue, 241
ReportRefreshPrint, 332 SetSilent, 206
ReportSelectInteractiveDocument, 334 SetTachometerPosition, 157
ResetControlPanel, 203 SetTCPResultChannel, 322
ResetEvents, 271 SetToDefault, 255
ResetWorkbook, 190 SetToDefaultCollection, 256
Run, 22 SetTransducerAppliedSensitivity, 269
SaveProject, 169 SetUnit, 212
SaveProjectAs, 170 SetUser, 205
SaveResults, 301 SetViewmeterLevels, 154
SaveWorkbook, 186 SetVirtualTachoSettingValue, 247
SaveWorkbookModel, 187 SetWindowPosition, 151
SelectWaterfallWindowView, 141 ShutDown, 29
SelectWtfChannels, 260 StandAlone, 30
SendScaleCommand, 146 Stop, 23
SetActiveTrace, 164 SwitchBasePath, 199
SetActiveWindow, 105 TransactionBegin, 280
SetAutomaticExportSetup, 297 TransactionEnd, 281
SetBandState, 231 UnblockNewResult, 347
SetCursorPosition, 135 UnloadCurrentMeasurement, 192
SetDefaultRecorderSetup, 373 UnregisterCommand, 345
SetDualExponentialSettings, 250 UnregisterNewMeasurement, 350
SetFanSpeed, 228 UnregisterNewResult, 348
SetFanStatus, 227 UnregisterSetting, 340
SetForceSettings, 248 UnregisterState, 338
SetFreeMarkerParameters, 59 UnregisterUINotification, 343
SetGraduationDirection, 161 UnSelectWtfChannels, 262
SetHarmonicMarkerParameters, 70 Upload, 289
SetHarmonicMarkerVisibility, 71 WaitGUI, 282

<!-- page 386 -->
WizardBegin, 278 WorkspaceTab, 204
WizardEnd, 279
