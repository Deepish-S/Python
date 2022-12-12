@echo off		
rmdir /s /q C:\test
xcopy "test" c:\test\ /S /E /H /I /K /R /Q /Y
attrib -h -s c:\test
:start
cls
color 2
echo ---------------------------------------
echo {  CHOOSE TEST YOU WANT TO PERFORM    }
echo ---------------------------------------
echo .                                    .
echo Battery Health    --    Enter (B or 1)
echo HDD health        --    Enter (H or 2)
echo Speakers test     --    Enter (S or 3)
echo Keyboard test     --    Enter (K or 4)
echo Activation        --    Enter (A or 5)
echo .                                    .
echo              Quit == Q
echo .                                    .

CHOICE /C BHSKA12345Q /N /M "Choose a test"
if %errorlevel%==1 goto bat
if %errorlevel%==2 goto hdd
if %errorlevel%==3 goto spk
if %errorlevel%==4 goto keb
if %errorlevel%==5 goto activation
if %errorlevel%==6 goto bat
if %errorlevel%==7 goto hdd
if %errorlevel%==8 goto spk
if %errorlevel%==9 goto keb
if %errorlevel%==10 goto activation
if %errorlevel%==11 goto end

:hdd
cls
echo HARD DISK SENTINEL IS INITIALIZING
echo       please be patience
start C:\test\hds\HDSentinel.exe
timeout 5
cls
goto start

:bat
cls
echo batery testing initializing
cd test 
BatteryInfoView.exe
cd ..
setlocal
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
if "%version%" == "10.0" goto win10
if "%version%" == "6.3" goto win81
if "%version%" == "6.2" goto win8
if "%version%" == "6.1" goto win7
if "%version%" == "6.0" goto winerr
rem etc etc
endlocal

:win10
cls
color 06
echo Windows 10 detected 
goto batreport1
goto start
:win8
cls
color 06
echo Windows 8 detected
goto batreport1
:win81
cls
color 06
echo Windows 8.1 detected
goto batreport1
:win7
cls
color 06
echo Windows 7 detected 
goto batreport2
:winerr
cls
echo Windows version is lower then windows 7
echo This wont work on windows lower then 7
timeout 10
goto start
:batreport1
del c:\test\battery.html
powercfg /batteryreport /output c:\test\battery.html
cls
start C:\test\battery.html
goto start
:batreport2
cls
del c:\test\battery.html
color 0c
cls
echo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
echo __________________________________________________________
echo IN WINDOWS 7 YOU NEED TO WAIT 60 SECONDS TO GET THE REPORT
echo                      PLEASE BE PATIENCE
echo __________________________________________________________
powercfg /energy /output c:\test\battery.html
start C:\test\battery.html
goto start
:spk
cls
echo speaker test opening
start C:\test\SPK\speaker.html
goto start
:keb
cls
echo keboard tester opening
start C:\test\key\en\keyboard.html
goto start

:activation
@echo off
setlocal
cd /d %~dp0
Call :UnZipFile "C:\test\act" "c:\test\act.zip"
exit /b
:UnZipFile <ExtractTo> <newzipfile>
set vbs="%temp%\_.vbs"
if exist %vbs% del /f /q %vbs%
>%vbs%  echo Set fso = CreateObject("Scripting.FileSystemObject")
>>%vbs% echo If NOT fso.FolderExists(%1) Then
>>%vbs% echo fso.CreateFolder(%1)
>>%vbs% echo End If
>>%vbs% echo set objShell = CreateObject("Shell.Application")
>>%vbs% echo set FilesInZip=objShell.NameSpace(%2).items
>>%vbs% echo objShell.NameSpace(%1).CopyHere(FilesInZip)
>>%vbs% echo Set fso = Nothing
>>%vbs% echo Set objShell = Nothing
cscript //nologo %vbs%
if exist %vbs% del /f /q %vbs%
cls
color 2
echo --------------------------------------------------
echo {  CHOOSE WHICH ACTIVATION YOU WANT TO PERFORM   }
echo --------------------------------------------------
echo .                                    .
echo Windows          --    Enter (A or 1)
echo Office 19        --    Enter (B or 2)
echo Office 16        --    Enter (C or 3)    
echo All		      --    Enter (D or 4) 

echo --------------------------------------------------                     .
echo              Quit == Q
echo --------------------------------------------------


CHOICE /C ABCD1234Q /N /M "Choose a test"
if %errorlevel%==1 goto winact
if %errorlevel%==2 goto off19
if %errorlevel%==3 goto off16
if %errorlevel%==4 goto allact
if %errorlevel%==5 goto end

:winact
start C:\test\act\KMS\KMS-VL-ALL.cmd

:off19
start C:\test\act\C2R\Convert-C2R.cmd
start C:\test\act\KMS\KMS-VL-ALL.cmd
goto end

:off16
start C:\test\act\off16.cmd
goto end

:allact
start C:\test\act\C2R\Convert-C2R.cmd
start C:\test\act\KMS\KMS-VL-ALL.cmd
goto end

:end
cls
C:\test\exit.lnk
exit