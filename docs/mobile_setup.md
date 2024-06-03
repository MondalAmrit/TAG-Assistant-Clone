# Setup Guide for Mobile Frontend (Windows Only)

# Install the following packages
- [command line tools](https://developer.android.com/studio#command-line-tools-only)
- [platform tools](https://developer.android.com/tools/releases/platform-tools)
- [Java](https://www.oracle.com/java/technologies/javase/jdk21-archive-downloads.html)
- [Node](https://nodejs.org/en/download/prebuilt-installer)
**Note:** If any of the above is already in your system then there is no need to do that again

# Place your folders in right destination
 - It shuold be in path `C:\\Users\<UserName>\AppData\Local\`
 - Now Create a new file called `Android`
 - Inside android create a new file called `Sdk`
 - Now extract the zip files of android `command line tools` and `platform tools` here.

# Then configure system variables
 - For `Java`  --> Add `<your_path>/jdk21/bin/` in the `Path`
 - For `platform tools` --> Add `<your_path>/bin/` in the `Path`
 - For `Commandline tools`
    - Create a folder called latest inside the cmdline_tools and move all its content in latest
    - Add it to `ANDROID_HOME` variable with the path to it's `bin` folder.

# Get the licenses
 - Inorder to proceed further you need to get licenses from the `Android Command line`. This can be done by,
  `%ANDROID_HOME%\sdkmanager --licenses` in your command prompt.

# Verify the installed packages
 - For `Java` ---> `java -version`
 - For `platform tools` ---> `adk`
 - For `Node` ---> `node --version`

# Final Step
 - Everytime before executing `npx expo run:android` make sure that your device is connected via `adb devices`.
 - If not then you can turn on `developer settings > USB deubgging` <br/> Then connect your mobile to the computer with `USB cable` <br/> Select the option in your mobile as `File Transfer/ Auto`
 - That's it. You can now go to the `TAG-Assistant-Clone\MobileFrontend` and use `npx expo run:android`