ECHO OFF
::This batch file runs setup_project_CLI.py
::It was configured for running on a single Windows machine
TITLE bw2preagg setup_project on Windows machine

::Get variables from params.txt
::Make sure you update this file before running the code
for /F "tokens=1,2,3" %%i in ('findstr /v /c:"//" params.txt') do set %%i %%j %%k

::Display variable
ECHO(
ECHO Using the following variables:
ECHO -----------------------------------
ECHO(
ECHO project_name = %project_name%
ECHO database_name = %database_name%
ECHO result_dir = %result_dir%
ECHO database_dir = %database_dir%
ECHO overwrite_project = %overwrite_project%
ECHO overwrite_database = %overwrite_database%
ECHO force_write_common_files = %force_write_common_files%
ECHO save_det_lci = %save_det_lci%
ECHO default_bw2setup = %default_bw2setup%
ECHO(

:PROMPT
SET /P AREYOUSURE=Proceed (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" EXIT

cd ../scripts
ECHO(
python setup_project_CLI.py --project_name=%project_name% --database_name=%database_name% --result_dir=%result_dir% --database_dir=%database_dir% --overwrite_project=%overwrite_project% --overwrite_database=%overwrite_database% --save_det_lci=%save_det_lci% --force_write_common_files=%force_write_common_files% --default_bw2setup=%default_bw2setup%
ECHO(
ECHO Done
cd ../single_windows_machine