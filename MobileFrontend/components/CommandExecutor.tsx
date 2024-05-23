import { Linking, Platform } from 'react-native';

const execute_command = (cmd: string) => {
    if (cmd === 'camera') {
        let cameraAppScheme;
        if (Platform.OS === 'android') {
            // Use the appropriate URI scheme for Android
            cameraAppScheme = 'package://com.android.camera';
        } else if (Platform.OS === 'ios') {
            // Use the appropriate URI scheme for iOS
            cameraAppScheme = 'cameraplus://';
        } else {
            // For other platforms, you might handle differently
            console.log('Unsupported platform');
            return;
        }

        Linking.openURL(cameraAppScheme)
            .catch(err => console.error('An error occurred', err));
    }
}

export default execute_command;
