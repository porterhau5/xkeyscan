#!/usr/bin/python
# -*- coding: utf-8 -*-

# Tom Porter (@porterhau5)

import optparse
import os
import sys

def main():
    usage = ("Usage: python [-u] %prog [LOGFILE]"
          "\n\nA simple script for converting xinput output to legible "
          "keystokes."
          "\nCan process a log file directly when passed as an argument, or can"
          "\nconvert keystrokes in near real-time if tailing a log file."
          "\nIf tailing a log file, use python's -u switch to avoid buffering."
          "\n\nExamples:\n  python %prog xkey.log (post process log file)"
          "\n  cat xkey.log | python %prog (accepts logs from stdin)"
          "\n  tail -f -n +1 xkey.log | python -u %prog (tail log file)"
          "\n\nType -h or --help for a full listing of options.")
    parser = optparse.OptionParser(usage=usage)

    (options, args) = parser.parse_args()

    # verify positional argument is set (INFILE)
    if len(args) == 0:
        stdin = True
    else:
        file_path = args[0]
        # verify input file exists
        if not os.path.isfile(file_path):
            parser.error("%s - file does not exist" % file_path)
            exit(1)
        stdin = False

    codes = {}
    codes["9"] = [" <Esc> ", "NoSymbol", " <Esc> "]
    #codes["9"] = ["Escape", "NoSymbol", "Escape"]
    codes["10"] = ["1", "!", "1", "!"]
    #codes["10"] = ["1", "exclam", "1", "exclam"]
    codes["11"] = ["2", "@", "2", "@"]
    #codes["11"] = ["2", "at", "2", "at"]
    codes["12"] = ["3", "#", "3", "#"]
    #codes["12"] = ["3", "numbersign", "3", "numbersign"]
    codes["13"] = ["4", "$", "4", "$"]
    #codes["13"] = ["4", "dollar", "4", "dollar"]
    codes["14"] = ["5", "%", "5", "%"]
    #codes["14"] = ["5", "percent", "5", "percent"]
    codes["15"] = ["6", "^", "6", "^"]
    #codes["15"] = ["6", "asciicircum", "6", "asciicircum"]
    codes["16"] = ["7", "&", "7", "&"]
    #codes["16"] = ["7", "ampersand", "7", "ampersand"]
    codes["17"] = ["8", "*", "8", "*"]
    #codes["17"] = ["8", "asterisk", "8", "asterisk"]
    codes["18"] = ["9", "(", "9", "("]
    #codes["18"] = ["9", "parenleft", "9", "parenleft"]
    codes["19"] = ["0", ")", "0", ")"]
    #codes["19"] = ["0", "parenright", "0", "parenright"]
    codes["20"] = ["-", "_", "-", "_"]
    #codes["20"] = ["minus", "underscore", "minus", "underscore"]
    codes["21"] = ["=", "+", "=", "+"]
    #codes["21"] = ["equal", "plus", "equal", "plus"]
    codes["22"] = [" <Back> ", " <Back> ", " <Back> ", " <Back> "]
    #codes["22"] = ["BackSpace", "BackSpace", "BackSpace", "BackSpace"]
    codes["23"] = [" <Tab> ", "ISO_Left_Tab", " <Tab> ", "ISO_Left_Tab"]
    #codes["23"] = ["Tab", "ISO_Left_Tab", "Tab", "ISO_Left_Tab"]
    codes["24"] = ["q", "Q", "q", "Q"]
    codes["25"] = ["w", "W", "w", "W"]
    codes["26"] = ["e", "E", "e", "E"]
    codes["27"] = ["r", "R", "r", "R"]
    codes["28"] = ["t", "T", "t", "T"]
    codes["29"] = ["y", "Y", "y", "Y"]
    codes["30"] = ["u", "U", "u", "U"]
    codes["31"] = ["i", "I", "i", "I"]
    codes["32"] = ["o", "O", "o", "O"]
    codes["33"] = ["p", "P", "p", "P"]
    codes["34"] = ["[", "{", "[", "{"]
    #codes["34"] = ["bracketleft", "braceleft", "bracketleft", "braceleft"]
    codes["35"] = ["]", "}", "]", "}"]
    #codes["35"] = ["bracketright", "braceright", "bracketright", "braceright"]
    codes["36"] = ["\r\n", "NoSymbol", "\r\n"]
    #codes["36"] = ["Return", "NoSymbol", "Return"]
    codes["37"] = [" <LCtl> ", "NoSymbol", " <LCtl> "]
    #codes["37"] = ["Control_L", "NoSymbol", "Control_L"]
    codes["38"] = ["a", "A", "a", "A"]
    codes["39"] = ["s", "S", "s", "S"]
    codes["40"] = ["d", "D", "d", "D"]
    codes["41"] = ["f", "F", "f", "F"]
    codes["42"] = ["g", "G", "g", "G"]
    codes["43"] = ["h", "H", "h", "H"]
    codes["44"] = ["j", "J", "j", "J"]
    codes["45"] = ["k", "K", "k", "K"]
    codes["46"] = ["l", "L", "l", "L"]
    codes["47"] = [";", ":", ";", ":"]
    #codes["47"] = ["semicolon", "colon", "semicolon", "colon"]
    codes["48"] = ["'", "\"", "'", "\""]
    #codes["48"] = ["apostrophe", "quotedbl", "apostrophe", "quotedbl"]
    codes["49"] = ["`", "~", "`", "~"]
    #codes["49"] = ["grave", "asciitilde", "grave", "asciitilde"]
    codes["50"] = [" <LShift> ", "NoSymbol", " <LShift> "]
    #codes["50"] = ["Shift_L", "NoSymbol", "Shift_L"]
    codes["51"] = ["\\", "|", "\\", "|"]
    #codes["51"] = ["backslash", "bar", "backslash", "bar"]
    codes["52"] = ["z", "Z", "z", "Z"]
    codes["53"] = ["x", "X", "x", "X"]
    codes["54"] = ["c", "C", "c", "C"]
    codes["55"] = ["v", "V", "v", "V"]
    codes["56"] = ["b", "B", "b", "B"]
    codes["57"] = ["n", "N", "n", "N"]
    codes["58"] = ["m", "M", "m", "M"]
    codes["59"] = [",", "<", ",", "<"]
    #codes["59"] = ["comma", "less", "comma", "less"]
    codes["60"] = [".", ">", ".", ">"]
    #codes["60"] = ["period", "greater", "period", "greater"]
    codes["61"] = ["/", "?", "/", "?"]
    #codes["61"] = ["slash", "question", "slash", "question"]
    codes["62"] = [" <RShift> ", "NoSymbol", " <RShift> "]
    #codes["62"] = ["Shift_R", "NoSymbol", "Shift_R"]
    codes["63"] = ["*", "*", "*", "*", "*", "*", "<XF86ClearGrab>"]
    #codes["63"] = ["KP_Multiply", "KP_Multiply", "KP_Multiply", "KP_Multiply", "KP_Multiply", "KP_Multiply", "XF86ClearGrab"]
    codes["64"] = [" <LAlt> ", " <Meta_L> ", " <LAlt> ", " <Meta_L> "]
    #codes["64"] = ["Alt_L", "Meta_L", "Alt_L", "Meta_L"]
    codes["65"] = [" ", "NoSymbol", " "]
    #codes["65"] = ["space", "NoSymbol", "space"]
    codes["66"] = [" <Caps_Lock> ", "NoSymbol", " <Caps_Lock> "]
    #codes["66"] = ["Caps_Lock", "NoSymbol", "Caps_Lock"]
    codes["67"] = [" <F1> ", " <F1> ", " <F1> ", " <F1> ", " <F1> ", " <F1> ", "XF86Switch_VT_1"]
    #codes["67"] = ["F1", "F1", "F1", "F1", "F1", "F1", "XF86Switch_VT_1"]
    codes["68"] = [" <F2> ", " <F2> ", " <F2> ", " <F2> ", " <F2> ", " <F2> ", "XF86Switch_VT_2"]
    #codes["68"] = ["F2", "F2", "F2", "F2", "F2", "F2", "XF86Switch_VT_2"]
    codes["69"] = [" <F3> ", " <F3> ", " <F3> ", " <F3> ", " <F3> ", " <F3> ", "XF86Switch_VT_3"]
    #codes["69"] = ["F3", "F3", "F3", "F3", "F3", "F3", "XF86Switch_VT_3"]
    codes["70"] = [" <F4> ", " <F4> ", " <F4> ", " <F4> ", " <F4> ", " <F4> ", "XF86Switch_VT_4"]
    #codes["70"] = ["F4", "F4", "F4", "F4", "F4", "F4", "XF86Switch_VT_4"]
    codes["71"] = [" <F5> ", " <F5> ", " <F5> ", " <F5> ", " <F5> ", " <F5> ", "XF86Switch_VT_5"]
    #codes["71"] = ["F5", "F5", "F5", "F5", "F5", "F5", "XF86Switch_VT_5"]
    codes["72"] = [" <F6> ", " <F6> ", " <F6> ", " <F6> ", " <F6> ", " <F6> ", "XF86Switch_VT_6"]
    #codes["72"] = ["F6", "F6", "F6", "F6", "F6", "F6", "XF86Switch_VT_6"]
    codes["73"] = [" <F7> ", " <F7> ", " <F7> ", " <F7> ", " <F7> ", " <F7> ", "XF86Switch_VT_7"]
    #codes["73"] = ["F7", "F7", "F7", "F7", "F7", "F7", "XF86Switch_VT_7"]
    codes["74"] = [" <F8> ", " <F8> ", " <F8> ", " <F8> ", " <F8> ", " <F8> ", "XF86Switch_VT_8"]
    #codes["74"] = ["F8", "F8", "F8", "F8", "F8", "F8", "XF86Switch_VT_8"]
    codes["75"] = [" <F9> ", " <F9> ", " <F9> ", " <F9> ", " <F9> ", " <F9> ", "XF86Switch_VT_9"]
    #codes["75"] = ["F9", "F9", "F9", "F9", "F9", "F9", "XF86Switch_VT_9"]
    codes["76"] = [" <F10> ", " <F10> ", " <F10> ", " <F10> ", " <F10> ", " <F10> ", "XF86Switch_VT_10"]
    #codes["76"] = ["F10", "F10", "F10", "F10", "F10", "F10", "XF86Switch_VT_10"]
    codes["77"] = [" <NumLock> ", "NoSymbol", " <NumLock> "]
    #codes["77"] = ["Num_Lock", "NoSymbol", "Num_Lock"]
    codes["78"] = [" <ScrollLock> ", "NoSymbol", " <ScrollLock> "]
    #codes["78"] = ["Scroll_Lock", "NoSymbol", "Scroll_Lock"]
    codes["79"] = [" <KP_Home> ", " <KP_7> ", " <KP_Home> ", " <KP_7> "]
    #codes["79"] = ["KP_Home", "KP_7", "KP_Home", "KP_7"]
    codes["80"] = [" <KP_Up> ", " <KP_8> ", " <KP_Up> ", " <KP_8> "]
    #codes["80"] = ["KP_Up", "KP_8", "KP_Up", "KP_8"]
    codes["81"] = [" <KP_Prior> ", " <KP_9> ", " <KP_Prior> ", " <KP_9> "]
    #codes["81"] = ["KP_Prior", "KP_9", "KP_Prior", "KP_9"]
    codes["82"] = ["-", "-", "-", "-", "-", "-", " <XF86Prev_VMode> "]
    #codes["82"] = ["KP_Subtract", "KP_Subtract", "KP_Subtract", "KP_Subtract", "KP_Subtract", "KP_Subtract", "XF86Prev_VMode"]
    codes["83"] = [" <KP_Left> ", " <KP_4> ", " <KP_Left> ", " <KP_4> "]
    #codes["83"] = ["KP_Left", "KP_4", "KP_Left", "KP_4"]
    codes["84"] = [" <KP_Begin> ", " <KP_5> ", " <KP_Begin> ", " <KP_5> "]
    #codes["84"] = ["KP_Begin", "KP_5", "KP_Begin", "KP_5"]
    codes["85"] = [" <KP_Right> ", " <KP_6> ", " <KP_Right> ", " <KP_6> "]
    #codes["85"] = ["KP_Right", "KP_6", "KP_Right", "KP_6"]
    codes["86"] = ["+", "+", "+", "+", "+", "+", " <XF86Next_VMode> "]
    #codes["86"] = ["KP_Add", "KP_Add", "KP_Add", "KP_Add", "KP_Add", "KP_Add", "XF86Next_VMode"]
    codes["87"] = [" <KP_End> ", " <KP_1> ", " <KP_End> ", " <KP_1> "]
    #codes["87"] = ["KP_End", "KP_1", "KP_End", "KP_1"]
    codes["88"] = [" <KP_Down> ", " <KP_2> ", " <KP_Down> ", " <KP_2> "]
    #codes["88"] = ["KP_Down", "KP_2", "KP_Down", "KP_2"]
    codes["89"] = [" <KP_Next> ", " <KP_3> ", " <KP_Next> ", " <KP_3> "]
    #codes["89"] = ["KP_Next", "KP_3", "KP_Next", "KP_3"]
    codes["90"] = [" <KP_Insert> ", " <KP_0> ", " <KP_Insert> ", " <KP_0> "]
    #codes["90"] = ["KP_Insert", "KP_0", "KP_Insert", "KP_0"]
    codes["91"] = [" <KP_Delete> ", " <KP_Decimal> ", " <KP_Delete> ", " <KP_Decimal> "]
    #codes["91"] = ["KP_Delete", "KP_Decimal", "KP_Delete", "KP_Decimal"]
    codes["92"] = [" <ISO_Level3_Shift> ", "NoSymbol", " <ISO_Level3_Shift> "]
    #codes["92"] = ["ISO_Level3_Shift", "NoSymbol", "ISO_Level3_Shift"]
    codes["94"] = [" <less> ", " <greater> ", " <less> ", " <greater> ", " <bar> ", " <brokenbar> ", " <bar> "]
    #codes["94"] = ["less", "greater", "less", "greater", "bar", "brokenbar", "bar"]
    codes["95"] = [" <F11> ", " <F11> ", " <F11> ", " <F11> ", " <F11> ", " <F11> ", "XF86Switch_VT_11"]
    #codes["95"] = ["F11", "F11", "F11", "F11", "F11", "F11", "XF86Switch_VT_11"]
    codes["96"] = [" <F12> ", " <F12> ", " <F12> ", " <F12> ", " <F12> ", " <F12> ", "XF86Switch_VT_12"]
    #codes["96"] = ["F12", "F12", "F12", "F12", "F12", "F12", "XF86Switch_VT_12"]
    codes["98"] = ["Katakana", "NoSymbol", "Katakana"]
    codes["99"] = ["Hiragana", "NoSymbol", "Hiragana"]
    codes["100"] = ["Henkan_Mode", "NoSymbol", "Henkan_Mode"]
    codes["101"] = ["Hiragana_Katakana", "NoSymbol", "Hiragana_Katakana"]
    codes["102"] = ["Muhenkan", "NoSymbol", "Muhenkan"]
    codes["104"] = [" <KP_Enter> ", "NoSymbol", " <KP_Enter> "]
    #codes["104"] = ["KP_Enter", "NoSymbol", "KP_Enter"]
    codes["105"] = [" <RCtl> ", "NoSymbol", " <RCtl> "]
    #codes["105"] = ["Control_R", "NoSymbol", "Control_R"]
    codes["106"] = ["/", "/", "/", "/", "/", "/", "XF86Ungrab"]
    #codes["106"] = ["KP_Divide", "KP_Divide", "KP_Divide", "KP_Divide", "KP_Divide", "KP_Divide", "XF86Ungrab"]
    codes["107"] = [" <Print> ", " <Sys_Req> ", " <Print> ", " <Sys_Req> "]
    #codes["107"] = ["Print", "Sys_Req", "Print", "Sys_Req"]
    codes["108"] = ["Multi_key", "Multi_key", "Multi_key", "Multi_key"]
    codes["109"] = ["Linefeed", "NoSymbol", "Linefeed"]
    codes["110"] = [" <Home> ", "NoSymbol", " <Home> "]
    #codes["110"] = ["Home", "NoSymbol", "Home"]
    codes["111"] = [" <Up> ", "NoSymbol", " <Up> "]
    #codes["111"] = ["Up", "NoSymbol", "Up"]
    codes["112"] = [" <Prior> ", "NoSymbol", " <Prior> "]
    #codes["112"] = ["Prior", "NoSymbol", "Prior"]
    codes["113"] = [" <Left> ", "NoSymbol", " <Left> "]
    #codes["113"] = ["Left", "NoSymbol", "Left"]
    codes["114"] = [" <Right> ", "NoSymbol", " <Right> "]
    #codes["114"] = ["Right", "NoSymbol", "Right"]
    codes["115"] = [" <End> ", "NoSymbol", " <End> "]
    #codes["115"] = ["End", "NoSymbol", "End"]
    codes["116"] = [" <Down> ", "NoSymbol", " <Down> "]
    #codes["116"] = ["Down", "NoSymbol", "Down"]
    codes["117"] = [" <Next> ", "NoSymbol", " <Next> "]
    #codes["117"] = ["Next", "NoSymbol", "Next"]
    codes["118"] = [" <Insert> ", "NoSymbol", " <Insert> "]
    #codes["118"] = ["Insert", "NoSymbol", "Insert"]
    codes["119"] = [" <Delete> ", "NoSymbol", " <Delete> "]
    #codes["119"] = ["Delete", "NoSymbol", "Delete"]
    codes["121"] = ["XF86AudioMute", "NoSymbol", "XF86AudioMute"]
    codes["122"] = ["XF86AudioLowerVolume", "NoSymbol", "XF86AudioLowerVolume"]
    codes["123"] = ["XF86AudioRaiseVolume", "NoSymbol", "XF86AudioRaiseVolume"]
    codes["124"] = ["XF86PowerOff", "NoSymbol", "XF86PowerOff"]
    codes["125"] = [" <KP_Equal> ", "NoSymbol", " <KP_Equal> "]
    #codes["125"] = ["KP_Equal", "NoSymbol", "KP_Equal"]
    codes["126"] = ["plusminus", "NoSymbol", "plusminus"]
    codes["127"] = [" <Pause> ", " <Break> ", " <Pause> ", " <Break> "]
    #codes["127"] = ["Pause", "Break", "Pause", "Break"]
    codes["128"] = ["XF86LaunchA", "NoSymbol", "XF86LaunchA"]
    codes["129"] = [" <KP_Decimal> ", " <KP_Decimal> ", " <KP_Decimal> ", " <KP_Decimal> "]
    #codes["129"] = ["KP_Decimal", "KP_Decimal", "KP_Decimal", "KP_Decimal"]
    codes["130"] = ["Hangul", "NoSymbol", "Hangul"]
    codes["131"] = ["Hangul_Hanja", "NoSymbol", "Hangul_Hanja"]
    codes["133"] = [" <Super_L> ", "NoSymbol", " <Super_L> "]
    #codes["133"] = ["Super_L", "NoSymbol", "Super_L"]
    codes["134"] = [" <Super_R> ", "NoSymbol", " <Super_R> "]
    #codes["134"] = ["Super_R", "NoSymbol", "Super_R"]
    codes["135"] = [" <Menu> ", "NoSymbol", " <Menu> "]
    #codes["135"] = ["Menu", "NoSymbol", "Menu"]
    codes["136"] = [" <Cancel> ", "NoSymbol", " <Cancel> "]
    #codes["136"] = ["Cancel", "NoSymbol", "Cancel"]
    codes["137"] = [" <Redo> ", "NoSymbol", " <Redo> "]
    #codes["137"] = ["Redo", "NoSymbol", "Redo"]
    codes["138"] = [" <SunProps> ", "NoSymbol", " <SunProps> "]
    #codes["138"] = ["SunProps", "NoSymbol", "SunProps"]
    codes["139"] = [" <Undo> ", "NoSymbol", " <Undo> "]
    #codes["139"] = ["Undo", "NoSymbol", "Undo"]
    codes["140"] = [" <SunFront> ", "NoSymbol", " <SunFront> "]
    #codes["140"] = ["SunFront", "NoSymbol", "SunFront"]
    codes["141"] = ["XF86Copy", "NoSymbol", "XF86Copy"]
    codes["142"] = ["XF86Open", "NoSymbol", "XF86Open"]
    codes["143"] = ["XF86Paste", "NoSymbol", "XF86Paste"]
    codes["144"] = [" <Find> ", "NoSymbol", " <Find> "]
    #codes["144"] = ["Find", "NoSymbol", "Find"]
    codes["145"] = ["XF86Cut", "NoSymbol", "XF86Cut"]
    codes["146"] = [" <Help> ", "NoSymbol", " <Help> "]
    #codes["146"] = ["Help", "NoSymbol", "Help"]
    codes["147"] = ["XF86MenuKB", "NoSymbol", "XF86MenuKB"]
    codes["148"] = ["XF86Calculator", "NoSymbol", "XF86Calculator"]
    codes["150"] = ["XF86Sleep", "NoSymbol", "XF86Sleep"]
    codes["151"] = ["XF86WakeUp", "NoSymbol", "XF86WakeUp"]
    codes["152"] = ["XF86Explorer", "NoSymbol", "XF86Explorer"]
    codes["153"] = ["XF86Send", "NoSymbol", "XF86Send"]
    codes["155"] = ["XF86Xfer", "NoSymbol", "XF86Xfer"]
    codes["156"] = ["XF86Launch1", "NoSymbol", "XF86Launch1"]
    codes["157"] = ["XF86Launch2", "NoSymbol", "XF86Launch2"]
    codes["158"] = ["XF86WWW", "NoSymbol", "XF86WWW"]
    codes["159"] = ["XF86DOS", "NoSymbol", "XF86DOS"]
    codes["160"] = ["XF86ScreenSaver", "NoSymbol", "XF86ScreenSaver"]
    codes["162"] = ["XF86RotateWindows", "NoSymbol", "XF86RotateWindows"]
    codes["163"] = ["XF86Mail", "NoSymbol", "XF86Mail"]
    codes["164"] = ["XF86Favorites", "NoSymbol", "XF86Favorites"]
    codes["165"] = ["XF86MyComputer", "NoSymbol", "XF86MyComputer"]
    codes["166"] = ["XF86Back", "NoSymbol", "XF86Back"]
    codes["167"] = ["XF86Forward", "NoSymbol", "XF86Forward"]
    codes["169"] = ["XF86Eject", "NoSymbol", "XF86Eject"]
    codes["170"] = ["XF86Eject", "XF86Eject", "XF86Eject", "XF86Eject"]
    codes["171"] = ["XF86AudioNext", "NoSymbol", "XF86AudioNext"]
    codes["172"] = ["XF86AudioPlay", "XF86AudioPause", "XF86AudioPlay", "XF86AudioPause"]
    codes["173"] = ["XF86AudioPrev", "NoSymbol", "XF86AudioPrev"]
    codes["174"] = ["XF86AudioStop", "XF86Eject", "XF86AudioStop", "XF86Eject"]
    codes["175"] = ["XF86AudioRecord", "NoSymbol", "XF86AudioRecord"]
    codes["176"] = ["XF86AudioRewind", "NoSymbol", "XF86AudioRewind"]
    codes["177"] = ["XF86Phone", "NoSymbol", "XF86Phone"]
    codes["179"] = ["XF86Tools", "NoSymbol", "XF86Tools"]
    codes["180"] = ["XF86HomePage", "NoSymbol", "XF86HomePage"]
    codes["181"] = ["XF86Reload", "NoSymbol", "XF86Reload"]
    codes["182"] = ["XF86Close", "NoSymbol", "XF86Close"]
    codes["185"] = ["XF86ScrollUp", "NoSymbol", "XF86ScrollUp"]
    codes["186"] = ["XF86ScrollDown", "NoSymbol", "XF86ScrollDown"]
    codes["187"] = [" <parenleft> ", "NoSymbol", " <parenleft> "]
    #codes["187"] = ["parenleft", "NoSymbol", "parenleft"]
    codes["188"] = [" <parenright> ", "NoSymbol", " <parenright> "]
    #codes["188"] = ["parenright", "NoSymbol", "parenright"]
    codes["189"] = ["XF86New", "NoSymbol", "XF86New"]
    codes["190"] = [" <Redo> ", "NoSymbol", " <Redo> "]
    #codes["190"] = ["Redo", "NoSymbol", "Redo"]
    codes["191"] = ["XF86Tools", "NoSymbol", "XF86Tools"]
    codes["192"] = ["XF86Launch5", "NoSymbol", "XF86Launch5"]
    codes["193"] = ["XF86Launch6", "NoSymbol", "XF86Launch6"]
    codes["194"] = ["XF86Launch7", "NoSymbol", "XF86Launch7"]
    codes["195"] = ["XF86Launch8", "NoSymbol", "XF86Launch8"]
    codes["196"] = ["XF86Launch9", "NoSymbol", "XF86Launch9"]
    codes["198"] = ["XF86AudioMicMute", "NoSymbol", "XF86AudioMicMute"]
    codes["199"] = ["XF86TouchpadToggle", "NoSymbol", "XF86TouchpadToggle"]
    codes["200"] = ["XF86TouchpadOn", "NoSymbol", "XF86TouchpadOn"]
    codes["201"] = ["XF86TouchpadOff", "NoSymbol", "XF86TouchpadOff"]
    codes["203"] = [" <Mode_switch> ", "NoSymbol", " <Mode_switch> "]
    #codes["203"] = ["Mode_switch", "NoSymbol", "Mode_switch"]
    codes["204"] = ["NoSymbol", "Alt_L", "NoSymbol", "Alt_L"]
    codes["205"] = ["NoSymbol", "Meta_L", "NoSymbol", "Meta_L"]
    codes["206"] = ["NoSymbol", "Super_L", "NoSymbol", "Super_L"]
    codes["207"] = ["NoSymbol", "Hyper_L", "NoSymbol", "Hyper_L"]
    codes["208"] = ["XF86AudioPlay", "NoSymbol", "XF86AudioPlay"]
    codes["209"] = ["XF86AudioPause", "NoSymbol", "XF86AudioPause"]
    codes["210"] = ["XF86Launch3", "NoSymbol", "XF86Launch3"]
    codes["211"] = ["XF86Launch4", "NoSymbol", "XF86Launch4"]
    codes["212"] = ["XF86LaunchB", "NoSymbol", "XF86LaunchB"]
    codes["213"] = ["XF86Suspend", "NoSymbol", "XF86Suspend"]
    codes["214"] = ["XF86Close", "NoSymbol", "XF86Close"]
    codes["215"] = ["XF86AudioPlay", "NoSymbol", "XF86AudioPlay"]
    codes["216"] = ["XF86AudioForward", "NoSymbol", "XF86AudioForward"]
    codes["218"] = [" <Print> ", "NoSymbol", " <Print> "]
    #codes["218"] = ["Print", "NoSymbol", "Print"]
    codes["220"] = ["XF86WebCam", "NoSymbol", "XF86WebCam"]
    codes["223"] = ["XF86Mail", "NoSymbol", "XF86Mail"]
    codes["224"] = ["XF86Messenger", "NoSymbol", "XF86Messenger"]
    codes["225"] = ["XF86Search", "NoSymbol", "XF86Search"]
    codes["226"] = ["XF86Go", "NoSymbol", "XF86Go"]
    codes["227"] = ["XF86Finance", "NoSymbol", "XF86Finance"]
    codes["228"] = ["XF86Game", "NoSymbol", "XF86Game"]
    codes["229"] = ["XF86Shop", "NoSymbol", "XF86Shop"]
    codes["231"] = [" <Cancel> ", "NoSymbol", " <Cancel> "]
    #codes["231"] = ["Cancel", "NoSymbol", "Cancel"]
    codes["232"] = ["XF86MonBrightnessDown", "NoSymbol", "XF86MonBrightnessDown"]
    codes["233"] = ["XF86MonBrightnessUp", "NoSymbol", "XF86MonBrightnessUp"]
    codes["234"] = ["XF86AudioMedia", "NoSymbol", "XF86AudioMedia"]
    codes["235"] = ["XF86Display", "NoSymbol", "XF86Display"]
    codes["236"] = ["XF86KbdLightOnOff", "NoSymbol", "XF86KbdLightOnOff"]
    codes["237"] = ["XF86KbdBrightnessDown", "NoSymbol", "XF86KbdBrightnessDown"]
    codes["238"] = ["XF86KbdBrightnessUp", "NoSymbol", "XF86KbdBrightnessUp"]
    codes["239"] = ["XF86Send", "NoSymbol", "XF86Send"]
    codes["240"] = ["XF86Reply", "NoSymbol", "XF86Reply"]
    codes["241"] = ["XF86MailForward", "NoSymbol", "XF86MailForward"]
    codes["242"] = ["XF86Save", "NoSymbol", "XF86Save"]
    codes["243"] = ["XF86Documents", "NoSymbol", "XF86Documents"]
    codes["244"] = ["XF86Battery", "NoSymbol", "XF86Battery"]
    codes["245"] = ["XF86Bluetooth", "NoSymbol", "XF86Bluetooth"]
    codes["246"] = ["XF86WLAN", "NoSymbol", "XF86WLAN"]

    # 0 - shift not active, 1 - shift active
    shift = 0
    # 50:LShift, 62:RShift
    shift_set = set(['50','62'])

    # 37:LCtl, 64:LAlt, 105:RCtl, 133:Super_L, 134:Super_R
    mod_set = set(['37','64', '105', '133', '134'])

    if stdin:
        print "reading from stdin"
        while True:
            line = sys.stdin.readline()
            line = line.rstrip()
            state = line.split()[1]
            code = line.split()[2]
            # determine state of shift modifier
            if code in shift_set:
                if state == "press":
                    shift = 1
                else:
                    shift = 0
            # register modifier on key press instead of release
            elif code in mod_set:
                if state == "press":
                    out = codes[code][shift]
                    if out == "NoSymbol":
                        sys.stdout.write(codes[code][0])
                    else:
                        sys.stdout.write(out)
            # register all other keys on release
            elif state == "release":
                    out = codes[code][shift]
                    if out == "NoSymbol":
                        sys.stdout.write(codes[code][0])
                    else:
                        sys.stdout.write(out)
    else:
        with open(file_path) as f:
            for line in f:
                line = line.rstrip()
                state = line.split()[1]
                code = line.split()[2]
                # determine state of shift modifier
                if code in shift_set:
                    if state == "press":
                        shift = 1
                    else:
                        shift = 0
                # register modifier on key press instead of release
                elif code in mod_set:
                    if state == "press":
                        out = codes[code][shift]
                        if out == "NoSymbol":
                            sys.stdout.write(codes[code][0])
                        else:
                            sys.stdout.write(out)
                # register all other keys on release
                elif state == "release":
                        out = codes[code][shift]
                        if out == "NoSymbol":
                            sys.stdout.write(codes[code][0])
                        else:
                            sys.stdout.write(out)


if __name__ == '__main__':
    main()
