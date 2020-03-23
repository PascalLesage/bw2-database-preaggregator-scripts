ECHO OFF
::This batch file runs concat_CLI.py
::It was configured for running on a single Windows machine
TITLE bw2preagg concat on Windows machine

::Get variables from params.txt
::Make sure you update that file before running the code
for /F "tokens=1,2,3" %%i in ('findstr /v /c:"//" params.txt') do set %%i %%j %%k

::Display variable
ECHO(
ECHO Using the following variables:
ECHO -----------------------------------
ECHO(

ECHO result_dir = %result_dir%
ECHO concat_result_type = %concat_result_type%
ECHO method_list_file_path = %method_list_file_path%
ECHO method_idx = %method_idx%
ECHO concat_totals_or_per_exchanges = %concat_totals_or_per_exchanges%
ECHO sim_name = %sim_name%
ECHO dest=%dest%
ECHO fail_if_samples_batches_different=%fail_if_samples_batches_different%
ECHO ignore_missing_concat=%ignore_missing_concat%
ECHO project_name = %project_name%
ECHO(
:PROMPT
SET /P AREYOUSURE=Proceed (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" EXIT

cd ../scripts
ECHO(
python concat_CLI.py --result_dir=%result_dir% --concat_result_type=%concat_result_type% --method_list_file_path=%method_list_file_path% --method_idx=%method_idx% --concat_totals_or_per_exchanges=%concat_totals_or_per_exchanges% --sim_name=%sim_name% --dest=%dest% --fail_if_samples_batches_different=%fail_if_samples_batches_different% --ignore_missing_concat=%ignore_missing_concat% --project_name=%project_name%

ECHO(
ECHO Done
cd ../single_windows_machine