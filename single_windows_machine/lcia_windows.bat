ECHO OFF
::This batch file runs lcia_CLI.py
::It was configured for running on a single Windows machine
TITLE bw2preagg lcia on Windows machine

::Get variables from params.txt
::Make sure you update that file before running the code
for /F "tokens=1,2,3" %%i in ('findstr /v /c:"//" params.txt') do set %%i %%j %%k

::Display variable
ECHO(
ECHO Using the following variables:
ECHO -----------------------------------
ECHO(

ECHO project_name = %project_name%
ECHO result_dir = %result_dir%
ECHO samples_batch = %samples_batch%
ECHO method_list_file_path = %method_list_file_path%
ECHO method_idx = %method_idx%
ECHO result_type = %result_type%
ECHO samples_batch = %samples_batch%
ECHO method_idx = %method_idx%
ECHO dtype = %dtype%
ECHO return_total = %return_total%
ECHO return_per_exchange = %return_per_exchange%
ECHO ignore_missing = %ignore_missing%
ECHO project_name = %project_name%
ECHO(
:PROMPT
SET /P AREYOUSURE=Proceed (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" EXIT

cd ../scripts
ECHO(
python lcia_CLI.py --result_dir=%result_dir% --method_list_file_path=%method_list_file_path% --method_idx=%method_idx% --result_type=%result_type% --samples_batch=%samples_batch% --dtype=%dtype% --return_total=%return_total% --return_per_exchange=%return_per_exchange% --ignore_missing=%ignore_missing% --project_name=%project_name%

ECHO(
ECHO Done
cd ../single_windows_machine