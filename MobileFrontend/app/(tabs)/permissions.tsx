import { router } from "expo-router";
import React, { useEffect } from "react";
import { Button, View } from "react-native";

const permissions = () => {
  const tempAlerts = ["Camera", "Call", "Contacts"];

  useEffect(() => {
    router.replace("/permissions");
    function alerts() {
      for (let i = 0; i < tempAlerts.length; i++) {
        alert(`Do you want to allow ${tempAlerts[i]} permission?`);
      }
    }
    setTimeout(() => {
      alerts();
    }, 1000);
  }, []);

  return (
    <View
      style={{ display: "flex", height: "100%", justifyContent: "flex-end" }}
    >
      <Button title="Continue" onPress={() => router.replace("/chatUI")} />
    </View>
  );
};

export default permissions;
