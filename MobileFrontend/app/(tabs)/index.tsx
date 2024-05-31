import React, { useState } from "react";
import { router } from "expo-router";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Button,
  useColorScheme,
  StyleSheet,
} from "react-native";

interface Intents {
  [key: string]: boolean;
}

interface RequiredFields {
  [key: string]: { title: string; placeholder: string };
}

const HomePage: React.FC = () => {
  const colorScheme = useColorScheme();
  const [intents, setIntents] = useState<Intents>({
    music: true,
    weather: false,
    internet: true,
    volume: true,
    calls: true,
    Brightness: true,
    Notes: true,
  });

  const [requiredFields, setRequiredFields] = useState<RequiredFields>({
    weather: {
      title: "You can get API key from www.ABC.com",
      placeholder: "Enter weather details...",
    },
  });

  const handleIntentToggle = (intent: string) => {
    setIntents({ ...intents, [intent]: !intents[intent] });
  };

  const handleFieldChange = (intent: string, value: string) => {
    setRequiredFields({
      ...requiredFields,
      [intent]: { ...requiredFields[intent], title: value },
    });
  };

  const handleSubmit = () => {
    const hasEmptyRequiredOption = Object.entries(intents).some(
      ([intent, checked]) =>
        checked && requiredFields[intent]?.title.trim() === ""
    );

    if (!hasEmptyRequiredOption) {
      console.log("Proceeding to next page...");
      // router.replace("/privacyPolicy");
      router.push('/chatUI');
    } else {
      console.log("Please fill in the required fields.");
    }
  };

  return (
    <View
      style={[
        styles.container,
        { backgroundColor: colorScheme === "dark" ? "#000" : "#fff" },
      ]}
    >
      <View style={styles.introNote}>
        <Text
          style={[
            styles.heading,
            { color: colorScheme === "dark" ? "#fff" : "#000" },
          ]}
        >
          Welcome to NOVA
        </Text>
        <Text
          style={[
            styles.subHeading,
            { color: colorScheme === "dark" ? "#fff" : "#000" },
          ]}
        >
          Nextgen Offline Voice Assistant
        </Text>
      </View>
      <View style={styles.intentsContainer}>
        <View>
          <Text
            style={[
              styles.intentsLabel,
              { color: colorScheme === "dark" ? "#fff" : "#000" },
            ]}
          >
            Please enter your name:
          </Text>
          <TextInput
            style={[
              styles.requiredFieldInput,
              {
                backgroundColor: colorScheme === "dark" ? "#333" : "#f4f4f4",
                color: colorScheme === "dark" ? "#fff" : "#000",
              },
            ]}
            onChangeText={(value) => handleFieldChange("name", value)}
            placeholder="Enter your name..."
            placeholderTextColor={colorScheme === "dark" ? "#aaa" : "#666"}
          />
        </View>

        <Text
          style={[
            styles.intentsLabel,
            { color: colorScheme === "dark" ? "#fff" : "#000" },
          ]}
        >
          Select the intents you want:
        </Text>
        {Object.keys(intents).map((intent) => (
          <View key={intent} style={styles.intentItem}>
            <View style={styles.intentWrapper}>
              <TouchableOpacity
                style={[
                  styles.checkbox,
                  colorScheme === "dark"
                    ? {
                        backgroundColor: "#fff",
                        borderColor: "rgb(230,230,230)",
                      }
                    : { backgroundColor: "#000", borderColor: "rgb(20,20,20)" },
                  intents[intent] ? styles.checked : null,
                ]}
                onPress={() => handleIntentToggle(intent)}
              >
                {intents[intent] && <View style={styles.innerCheckbox} />}
              </TouchableOpacity>
              <Text style={{ color: colorScheme === "dark" ? "#fff" : "#000" }}>
                {intent}
              </Text>
            </View>
            {intents[intent] && requiredFields[intent] && (
              <View style={styles.requiredField}>
                <Text
                  style={[
                    styles.requiredFieldTitle,
                    { color: colorScheme === "dark" ? "#fff" : "#000" },
                  ]}
                >
                  {requiredFields[intent].title}
                </Text>
                <TextInput
                  style={[
                    styles.requiredFieldInput,
                    {
                      backgroundColor:
                        colorScheme === "dark" ? "#333" : "#f4f4f4",
                      color: colorScheme === "dark" ? "#fff" : "#000",
                    },
                  ]}
                  value={""}
                  onChangeText={(value) => handleFieldChange(intent, value)}
                  placeholder="Enter details..."
                  placeholderTextColor={
                    colorScheme === "dark" ? "#aaa" : "#666"
                  }
                />
              </View>
            )}
          </View>
        ))}
      </View>
      <Button title="Next" onPress={handleSubmit} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    justifyContent: "center",
    overflow: "scroll",
  },
  introNote: {
    marginBottom: 20,
  },
  heading: {
    fontSize: 34,
    fontWeight: "bold",
    marginBottom: 5,
  },
  subHeading: {
    fontSize: 24,
  },
  intentsContainer: {
    marginBottom: 20,
    gap: 20,
  },
  intentsLabel: {
    fontSize: 18,
    marginBottom: 10,
  },
  intentItem: {
    flexDirection: "column",
    alignItems: "flex-start",
    paddingLeft: 20,
    marginBottom: 10,
  },
  checkbox: {
    width: 20,
    height: 20,
    borderRadius: 10,
    borderWidth: 2,
    marginRight: 10,
    justifyContent: "center",
    alignItems: "center",
  },
  innerCheckbox: {
    width: 12,
    height: 12,
    borderRadius: 6,
    backgroundColor: "rgb(20,20,200)",
  },
  checked: {
    backgroundColor: "rgb(20,20,200)",
  },
  intentWrapper: {
    flexDirection: "row",
    flex: 1,
    alignContent: "flex-start",
    justifyContent: "flex-start",
    alignItems: "flex-start",
  },
  requiredField: {
    marginLeft: 30,
    marginTop: 10,
  },
  requiredFieldTitle: {
    marginBottom: 5,
  },
  requiredFieldInput: {
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
    padding: 5,
    marginTop: 5,
  },
});

export default HomePage;
