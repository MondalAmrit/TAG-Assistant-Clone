import { router } from "expo-router";
import React, { useState } from "react";
import {
  View,
  ScrollView,
  Text,
  StyleSheet,
  Pressable,
  Button,
} from "react-native";
import Checkbox from "expo-checkbox";

const PrivacyPolicyScreen = () => {
  const [isChecked, setIsChecked] = useState(false);

  const handleNextPress = () => {
    if (isChecked) {
      router.replace("/permissions");
    } else {
      alert("Please agree to the privacy policy to proceed.");
    }
  };

  const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: "center",
    },
    scrollView: {
      // Define your styles here
    },
    title: {
      // Define your styles here
    },
    content: {
      // Define your styles here
    },
  });

  return (
    <View style={styles.container}>
      <ScrollView style={styles.scrollView}>
        <Text style={styles.title}>Privacy Policy</Text>
        <Text style={styles.content}>
          Welcome to our AI Assistant app. Your privacy is critically important
          to us.
          {"\n\n"}
          It is our policy to respect your privacy regarding any information we
          may collect while operating our app. This Privacy Policy applies to
          all data collected through our app.
          {"\n\n"}
          Information We Collect
          {"\n\n"}
          We may collect different types of information in order to provide and
          improve our services:
          {"\n\n"}
          1. Personal Data
          {"\n"}- Email address
          {"\n"}- First name and last name
          {"\n"}- Phone number
          {"\n"}- Address, State, Province, ZIP/Postal code, City
          {"\n\n"}
          2. Usage Data
          {"\n\n"}
          Personal Data
          {"\n\n"}
          While using our app, we may ask you to provide us with certain
          personally identifiable information that can be used to contact or
          identify you. This may include:
          {"\n\n"}- Email address
          {"\n"}- First name and last name
          {"\n"}- Phone number
          {"\n"}- Address, State, Province, ZIP/Postal code, City
          {"\n\n"}
          We collect this information for the purpose of providing and improving
          our services. We will not use or share your information with anyone
          except as described in this Privacy Policy.
          {"\n\n"}
          By using our app, you consent to the collection and use of your
          personal information as outlined in this Privacy Policy.
        </Text>
        <View
          style={{
            flex: 1,
            flexDirection: "row",
            gap: 8,
            marginTop: 12,
            marginBottom: 12,
          }}
        >
          <Checkbox
            value={isChecked}
            onValueChange={() => setIsChecked(!isChecked)}
          />
          <Text>I Agree</Text>
        </View>
        <Button title="Next" onPress={handleNextPress} />
      </ScrollView>
    </View>
  );
};

export default PrivacyPolicyScreen;
