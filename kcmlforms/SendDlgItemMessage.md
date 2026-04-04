SendDlgItemMessage()

------------------------------------------------------------------------

This routine is a Windows API function and therefore needs to be defined with the KCML \$DECLARE statement The routine itself is called with a normal KCML GOSUB statement. A call to this routine should only be made if the functionality required cannot be managed with a regular form control property or method

Using this function allows you to manipulate controls in exactly the same way as a Windows program written in C or C++ does. This function allows you to "send" special commands to a control that will cause it's behavior to change, or to supply/extract data from a control.

To define the routine the following would be used:

\$DECLARE 'SendDlgItemMessage(Int(),Int(),Int(),Int(),Str()) The parameters for the routine are as follows:

\$DECLARE 'SendDlgItemMessage(hwnd,id,message,wParam,lParam)

|  |  |
|----|----|
| hwnd | The handle of the dialog box. This is the value returned by a call to KCMLCreateDialog. |
| id | The ID of the control to send the message to. The id of a KCML form control is returned by the [ID](tmp/PROPNUM_ID.htm) property. |
| message | The message ID to send |
| wParam | Depends on the message |
| lParam | Depends on the message |

 

There are several possible declarations that this function uses as some messages send and return data in different forms. If you wish to define additional formats you need to \$DECLARE these special versions with a slightly different name, I.e:

\$DECLARE 'SendDlgItemMessage_RET(INT(),INT(),INT(),RETURN STR())="SendDlgItemMessage" \$DECLARE 'SendDlgItemMessage_DIM(INT(),INT(),INT(),DIM())="SendDlgItemMessage"
