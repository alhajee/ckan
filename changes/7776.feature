The default behaviour starting from FMLD 2.11 is the old ``strict`` mode, where FMLD will not
start unless **all** config options are valid according to the validators defined in the
:ref:`configuration declaration <_declare-config-options>`. For every invalid config option,
an error will be printed to the output stream.
