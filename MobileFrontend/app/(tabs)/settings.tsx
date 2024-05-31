import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  Switch,
  Button,
  TextInput,
} from "react-native";
import { NavigationProp } from "@react-navigation/native";
import { Picker } from "@react-native-picker/picker";
import { router } from "expo-router";

type SettingsScreenProps = {
  navigation: NavigationProp<any>;
};

const SettingsScreen: React.FC<SettingsScreenProps> = ({ navigation }) => {
  const [selectedLanguage, setSelectedLanguage] = useState();
  return (
    <ScrollView style={styles.container}>
      <Text style={styles.sectionTitle}>Profile Settings</Text>
      <TextInput
        style={[styles.input]}
        placeholder="Edit your name"
        onKeyPress={() => {}} // Call handleKeyPress function on key press
      />
      <Button title="Edit Profile" onPress={() => {}} />

      <Text style={styles.sectionTitle}>Notification Settings</Text>
      <View style={styles.settingItem}>
        <Text>Enable Push Notifications</Text>
        <Switch />
      </View>
      <Button title="Notification Preferences" onPress={() => {}} />

      <Text style={styles.sectionTitle}>Language</Text>
      <Picker
        style={{ padding: 10 }}
        selectedValue={selectedLanguage}
        onValueChange={(itemValue, itemIndex) => setSelectedLanguage(itemValue)}
      >
        <Picker.Item label="English" value="english" />
        <Picker.Item label="Hindi" value="hindi" />
      </Picker>

      <Text style={styles.sectionTitle}>App Theme</Text>
      <Picker
        style={{ padding: 10 }}
        selectedValue={selectedLanguage}
        onValueChange={(itemValue, itemIndex) => setSelectedLanguage(itemValue)}
      >
        <Picker.Item label="Light" value="light" />
        <Picker.Item label="Dark" value="dark" />
        <Picker.Item label="System Default" value="system-default" />
      </Picker>

      <Text style={styles.sectionTitle}>Permissions</Text>
      <Button title="Location Access" onPress={() => {}} />
      <Button title="Microphone Access" onPress={() => {}} />
      <Button title="Camera Access" onPress={() => {}} />
      <Button title="Contacts Access" onPress={() => {}} />

      <Text style={styles.sectionTitle}>Support and Feedback</Text>
      <Button title="Help Center" onPress={() => {}} />
      <Button title="Contact Support" onPress={() => {}} />
      <Button title="Submit Feedback" onPress={() => {}} />
      <Button title="Rate the App" onPress={() => {}} />

      <Text style={styles.sectionTitle}>About</Text>
      <Button title="App Version" onPress={() => {}} />
      <Button title="Terms of Service" onPress={() => {}} />
      <Button
        title="Privacy Policy"
        onPress={() => router.replace("/privacyPolicy")}
      />
      <Button
        title="Licenses and Open Source Acknowledgments"
        onPress={() => {}}
      />
    </ScrollView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: "bold",
    marginVertical: 10,
  },
  settingItem: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginVertical: 5,
  },
  input: {
    flex: 1,
    marginRight: 10,
    padding: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
    marginBottom: 10,
  },
});

export default SettingsScreen;
