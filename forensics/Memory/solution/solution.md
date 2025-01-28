# {Solution : }
to analyse this RAM we must use volatilty3 package that contains different plugins and options to manupilate a RAM dump 
to get the user account name after installing the volatility3 package from the original website: 
```bash
python3 volatility3/vol.py -f Downloads/memdmp.dmp windows.registry.printkey  --key "SAM\Domains\Account\Users\Names"
```
we use the windows.registry.printkey plugin to get the registry keys under the specific key value which is "SAM\Domains\Account\Users\Names" it's the default path of the credential informations in Windows os so you must search for  the path first to get the username :1sl3m

## The machine name : 
we should see the content of the specific hive which is the "\ControlSet001\Control\ComputerName\ActiveComputerName" 
```bash
python3 volatility3/vol.py -f Downloads/memdmp.dmp windows.registry.printkey  --key "ControlSet001\Control\ComputerName\ActiveComputerName"
```

