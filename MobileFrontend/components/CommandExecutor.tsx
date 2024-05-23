import { Alert, Linking, Platform } from 'react-native';

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
    }
    try {
        if (action !== '')  await Linking.openURL(action);
    } catch (e) {
        console.log('Some Error Occurred');
    }
}

export default execute_command;
