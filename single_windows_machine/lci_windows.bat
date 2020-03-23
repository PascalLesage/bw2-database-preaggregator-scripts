ECHO OFF
::This batch file runs lci_CLI.py
::It was configured for running on a single Windows machine
TITLE bw2preagg lci on Windows machine

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
ECHO samples_batch = %samples_batch%
ECHO parallel_jobs = %parallel_jobs%

ECHO(
:PROMPT
SET /P AREYOUSURE=Proceed (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" EXIT

cd ../scripts
ECHO(
python lci_CLI.py --project_name=%project_name% --database_name=%database_name% --result_dir=%result_dir% --samples_batch=%samples_batch% --parallel_jobs=%parallel_jobs%
ECHO(
ECHO Done
cd ../single_windows_machine