ECHO OFF
::This batch file runs balancing_presamples_CLI.py
::It was configured for running on a single Windows machine
TITLE bw2preagg balancing_presamples on Windows machine

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
ECHO iterations = %iterations%
ECHO samples_batch = %samples_batch%
ECHO overwrite_ps = %overwrite_ps%
ECHO balance_water = %balance_water%
ECHO balance_land = %balance_land%
ECHO ecoinvent_version = %ecoinvent_version%
ECHO ps_base_name = %ps_base_name%
ECHO expect_base_presamples = %expect_base_presamples%
ECHO(
:PROMPT
SET /P AREYOUSURE=Proceed (Y/[N])?
IF /I "%AREYOUSURE%" NEQ "Y" EXIT

cd ../scripts
ECHO(
python balancing_presamples_CLI.py --project_name=%project_name% --database_name=%database_name% --result_dir=%result_dir% --iterations=%iterations% --samples_batch=%samples_batch% --overwrite_ps=%overwrite_ps% --balance_water=%balance_water% --balance_land=%balance_land% --ecoinvent_version=%ecoinvent_version% --expect_base_presamples=%expect_base_presamples%
ECHO(
ECHO Done
cd ../single_windows_machine