// Default.js
import React from "react";
import { View, Text, StyleSheet, TouchableOpacity } from "react-native";

export default function Default({ navigation }) {
  const navigateToModule = (moduleName) => {
    // Use navigation to navigate to the specific module based on the module name
    // For simplicity, assuming module names match the screen names
    navigation.navigate(moduleName);
  };

  return (
    <View style={styles.container}>
      <View style={styles.grid}>
        {/* Scan Item */}
        <TouchableOpacity
          style={styles.module}
          onPress={() => navigateToModule("scanner")}
        >
          <Text style={styles.moduleText}>Scan Item</Text>
        </TouchableOpacity>

        {/* Search Recipe */}
        <TouchableOpacity
          style={styles.module}
          onPress={() => navigateToModule("searchrecipe")}
        >
          <Text style={styles.moduleText}>Search Recipe</Text>
        </TouchableOpacity>

        {/* Substitute */}
        <TouchableOpacity
          style={styles.module}
          onPress={() => navigateToModule("subs")}
        >
          <Text style={styles.moduleText}>Substitute</Text>
        </TouchableOpacity>

        {/* Schedule */}
        <TouchableOpacity
          style={styles.module}
          onPress={() => navigateToModule("schedule")}
        >
          <Text style={styles.moduleText}>Schedule</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  grid: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "center",
  },
  module: {
    width: 150,
    height: 150,
    backgroundColor: "blue",
    margin: 16,
    justifyContent: "center",
    alignItems: "center",
    borderRadius: 8,
  },
  moduleText: {
    color: "white",
    fontSize: 16,
    textAlign: "center",
  },
});
