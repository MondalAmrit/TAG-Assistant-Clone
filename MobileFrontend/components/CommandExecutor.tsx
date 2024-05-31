import { Alert, Linking, Platform } from 'react-native';


/////////////////////////////////////////////////////
// Better to add things :
// 1. File Handling ... (File System)
// 2. Torch control
// 3. Clock Settings
// 4. Bluetooth and Wifi

const execute_command = async (cmd: string) => {
    let action: string = '';
    if (cmd === 'whatsapp') {
        action = 'whatsapp://send?text=' + encodeURI('Hi, This message is generated from the NOVA Assistant');
        // Whatsapp format : whatsapp://send?phone=<encodeURI()>&text=<encodeURI()>
    } else if (cmd === 'email') {
        let recipent: string = 'example@email.com'
        action = 'mailto:'+recipent+'?subject=Subject%20Here&body=Body%20Here';
    } else if (cmd === 'call') {
        action = 'tel:+91-1234567890';
    } else if (cmd === 'sms') {
        action = 'sms:+91-9315946948';
    } else if (cmd === 'camera') {
        action = 'android.media.action.IMAGE_CAPTURE';
    } else if (cmd === 'contacts') {
        action = 'content://contacts/people/';
    } else if (cmd === 'battery') {
        action = 'android.intent.action.POWER_USAGE_SUMMARY';
    } else if (cmd === 'maps') {
        action = 'geo:';
    } else if (cmd === 'play store') {
        action = 'market://details?id=';
    } else if (cmd === 'calendar') {action = 'content://com.android.calendar/time/';}
    else if (cmd === 'call logs') {action = 'content://call_log/calls';}
    else if (cmd === 'media') {action = 'content://media/external/images/media';}
    else if (cmd === 'video') {action = 'android.media.action.VIDEO_CAPTURE';}
    // else if (cmd === 'torch') {action = 'android.intent.action.TORCH';}
    else if (cmd === 'settings') {action = 'android.settings.SETTINGS';}
    else if (cmd === 'downloads') {action = 'android.intent.action.VIEW_DOWNLOADS';}
    else if (cmd === 'bluetooth') {
        // action = 'android.bluetooth.adapter.action.REQUEST_ENABLE';
    }
    try {
        if (action !== '')  {
            if (action.split('.')[0] != 'android') await Linking.openURL(action);
            else await Linking.sendIntent(action);
        }
    } catch (e) {
        console.log(e);
    }
}

export default execute_command;
