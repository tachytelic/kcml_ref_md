Key (menuitem control property)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<tbody>
<tr>
<td>Design<br />
time</td>
<td>Run<br />
time</td>
<td>Appears in<br />
browser</td>
<td>KCML<br />
5.03+</td>
</tr>
</tbody>
</table>

\
<img src="/bitmaps/browsetool21.png" data-border="0" width="16" height="15" alt="property icon" /> Integer property

**Specifies the accelerator key for the menu item**

The **Key** property is used to define a short cut key for a menu item. It is more powerful than the use of '&' to denote accelerators on controls as it can be used to specify most of the keys on the keyboard, together with the Shift, Ctrl and Alt key status (at least one of these must be included. The text of the menu item is changed to reflect the short-cut key available. It can be set at design time using the menu editor or it can be set programmatically during the enter event.

The value is set using the integer form of the two byte hex string 0xkkss, where kk is the virtual-key code and ss is the shift status. This is the same format as used to specify a windows key in the KCML 5.03 enhanced [\$KEYBOARD](mk:@MSITStore:kcmlrefman.chm::/$KEYBOARD.htm) statement.

A similar property is available for [buttons](PROP_BUTTON_KEY.htm).

To set a menu item to be accelerated by the End key a programmer might code in the Enter() event


    .menu.PrintButton.key=0x2300

The following table lists most of the likely needed values. <span id="vk"></span>

Virtual-Key Code Definitions

The following table includes the virtual-key codes that are defined for Windows. The key code values 0x00 and 0xFF are not used.

<table data-cellspacing="20">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr data-valign="top">
<th>First byte</th>
<th>Second byte</th>
</tr>
</thead>
<tbody>
<tr>
<td><table data-cellpadding="3" data-cellspacing="3">
<thead>
<tr data-valign="top">
<th>Name</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td>VK_BACK</td>
<td>0x08</td>
</tr>
<tr>
<td>VK_TAB</td>
<td>0x09</td>
</tr>
<tr>
<td>VK_CLEAR</td>
<td>0x0C</td>
</tr>
<tr>
<td>VK_RETURN</td>
<td>0x0D</td>
</tr>
<tr>
<td>VK_PAUSE</td>
<td>0x13</td>
</tr>
<tr>
<td>VK_ESCAPE</td>
<td>0x1B</td>
</tr>
<tr>
<td>VK_SPACE</td>
<td>0x20</td>
</tr>
<tr>
<td>VK_PRIOR Page up</td>
<td>0x21</td>
</tr>
<tr>
<td>VK_NEXTPage down</td>
<td>0x22</td>
</tr>
<tr>
<td>VK_END</td>
<td>0x23</td>
</tr>
<tr>
<td>VK_HOME</td>
<td>0x24</td>
</tr>
<tr>
<td>VK_LEFT</td>
<td>0x25</td>
</tr>
<tr>
<td>VK_UP</td>
<td>0x26</td>
</tr>
<tr>
<td>VK_RIGHT</td>
<td>0x27</td>
</tr>
<tr>
<td>VK_DOWN</td>
<td>0x28</td>
</tr>
<tr>
<td>VK_INSERT</td>
<td>0x2D</td>
</tr>
<tr>
<td>VK_DELETE</td>
<td>0x2E</td>
</tr>
<tr>
<td>VK_HELP</td>
<td>0x2F</td>
</tr>
<tr>
<td>VK_0</td>
<td>0x30</td>
</tr>
<tr>
<td>VK_1</td>
<td>0x31</td>
</tr>
<tr>
<td>VK_2</td>
<td>0x32</td>
</tr>
<tr>
<td>VK_3</td>
<td>0x33</td>
</tr>
<tr>
<td>VK_4</td>
<td>0x34</td>
</tr>
<tr>
<td>VK_5</td>
<td>0x35</td>
</tr>
<tr>
<td>VK_6</td>
<td>0x36</td>
</tr>
<tr>
<td>VK_7</td>
<td>0x37</td>
</tr>
<tr>
<td>VK_8</td>
<td>0x38</td>
</tr>
<tr>
<td>VK_9</td>
<td>0x39</td>
</tr>
<tr>
<td>VK_A</td>
<td>0x41</td>
</tr>
<tr>
<td>VK_B</td>
<td>0x42</td>
</tr>
<tr>
<td>VK_C</td>
<td>0x43</td>
</tr>
<tr>
<td>VK_D</td>
<td>0x44</td>
</tr>
<tr>
<td>VK_E</td>
<td>0x45</td>
</tr>
<tr>
<td>VK_F</td>
<td>0x46</td>
</tr>
<tr>
<td>VK_G</td>
<td>0x47</td>
</tr>
<tr>
<td>VK_H</td>
<td>0x48</td>
</tr>
<tr>
<td>VK_I</td>
<td>0x49</td>
</tr>
<tr>
<td>VK_J</td>
<td>0x4A</td>
</tr>
<tr>
<td>VK_K</td>
<td>0x4B</td>
</tr>
<tr>
<td>VK_L</td>
<td>0x4C</td>
</tr>
<tr>
<td>VK_M</td>
<td>0x4D</td>
</tr>
<tr>
<td>VK_N</td>
<td>0x4E</td>
</tr>
<tr>
<td>VK_O</td>
<td>0x4F</td>
</tr>
<tr>
<td>VK_P</td>
<td>0x50</td>
</tr>
<tr>
<td>VK_Q</td>
<td>0x51</td>
</tr>
<tr>
<td>VK_R</td>
<td>0x52</td>
</tr>
<tr>
<td>VK_S</td>
<td>0x53</td>
</tr>
<tr>
<td>VK_T</td>
<td>0x54</td>
</tr>
<tr>
<td>VK_U</td>
<td>0x55</td>
</tr>
<tr>
<td>VK_V</td>
<td>0x56</td>
</tr>
<tr>
<td>VK_W</td>
<td>0x57</td>
</tr>
<tr>
<td>VK_X</td>
<td>0x58</td>
</tr>
<tr>
<td>VK_Y</td>
<td>0x59</td>
</tr>
<tr>
<td>VK_Z</td>
<td>0x5A</td>
</tr>
<tr>
<td>VK_NUMPAD0</td>
<td>0x60</td>
</tr>
<tr>
<td>VK_NUMPAD1</td>
<td>0x61</td>
</tr>
<tr>
<td>VK_NUMPAD2</td>
<td>0x62</td>
</tr>
<tr>
<td>VK_NUMPAD3</td>
<td>0x63</td>
</tr>
<tr>
<td>VK_NUMPAD4</td>
<td>0x64</td>
</tr>
<tr>
<td>VK_NUMPAD5</td>
<td>0x65</td>
</tr>
<tr>
<td>VK_NUMPAD6</td>
<td>0x66</td>
</tr>
<tr>
<td>VK_NUMPAD7</td>
<td>0x67</td>
</tr>
<tr>
<td>VK_NUMPAD8</td>
<td>0x68</td>
</tr>
<tr>
<td>VK_NUMPAD9</td>
<td>0x69</td>
</tr>
<tr>
<td>VK_MULTIPLY</td>
<td>0x6A</td>
</tr>
<tr>
<td>VK_ADD</td>
<td>0x6B</td>
</tr>
<tr>
<td>VK_SUBTRACT</td>
<td>0x6D</td>
</tr>
<tr>
<td>VK_DECIMAL</td>
<td>0x6E</td>
</tr>
<tr>
<td>VK_DIVIDE</td>
<td>0x6F</td>
</tr>
<tr>
<td>VK_F1</td>
<td>0x70</td>
</tr>
<tr>
<td>VK_F2</td>
<td>0x71</td>
</tr>
<tr>
<td>VK_F3</td>
<td>0x72</td>
</tr>
<tr>
<td>VK_F4</td>
<td>0x73</td>
</tr>
<tr>
<td>VK_F5</td>
<td>0x74</td>
</tr>
<tr>
<td>VK_F6</td>
<td>0x75</td>
</tr>
<tr>
<td>VK_F7</td>
<td>0x76</td>
</tr>
<tr>
<td>VK_F8</td>
<td>0x77</td>
</tr>
<tr>
<td>VK_F9</td>
<td>0x78</td>
</tr>
<tr>
<td>VK_F10</td>
<td>0x79</td>
</tr>
<tr>
<td>VK_F11</td>
<td>0x7A</td>
</tr>
<tr>
<td>VK_F12</td>
<td>0x7B</td>
</tr>
<tr>
<td>VK_F13</td>
<td>0x7C</td>
</tr>
<tr>
<td>VK_F14</td>
<td>0x7D</td>
</tr>
<tr>
<td>VK_F15</td>
<td>0x7E</td>
</tr>
<tr>
<td>VK_F16</td>
<td>0x7F</td>
</tr>
<tr>
<td>VK_F17</td>
<td>0x80</td>
</tr>
<tr>
<td>VK_F18</td>
<td>0x81</td>
</tr>
<tr>
<td>VK_F19</td>
<td>0x82</td>
</tr>
<tr>
<td>VK_F20</td>
<td>0x83</td>
</tr>
<tr>
<td>VK_F21</td>
<td>0x84</td>
</tr>
<tr>
<td>VK_F22</td>
<td>0x85</td>
</tr>
<tr>
<td>VK_F23</td>
<td>0x86</td>
</tr>
<tr>
<td>VK_F24</td>
<td>0x87</td>
</tr>
<tr>
<td>VK_ATTN</td>
<td>0xF6</td>
</tr>
</tbody>
</table></td>
<td><table data-cellpadding="3" data-cellspacing="3">
<thead>
<tr>
<th>Shift keys</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr>
<td> </td>
<td>0x00</td>
</tr>
<tr>
<td>Shift</td>
<td>0x01</td>
</tr>
<tr>
<td>Ctrl</td>
<td>0x02</td>
</tr>
<tr>
<td>Shift-Ctrl</td>
<td>0x03</td>
</tr>
<tr>
<td>Alt</td>
<td>0x04</td>
</tr>
<tr>
<td>Shift-Alt</td>
<td>0x05</td>
</tr>
<tr>
<td>Ctrl-Alt</td>
<td>0x06</td>
</tr>
<tr>
<td>Shift-Ctrl-Alt</td>
<td>0x07</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

##### See also:

Other [menuitem](menuitem.htm) properties, methods and events, [menu](menu.htm) properties, methods and events\
and [generic](generic.htm) properties and methods.
