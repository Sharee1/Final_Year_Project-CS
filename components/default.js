import React from "react";
import { View, Text, Button, StyleSheet } from "react-native";

const HomePage = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Welcome to Your Meal Planner</Text>

      <View style={styles.buttonContainer}>
        {}
        <Button
          title="Search Recipe"
          onPress={() => navigation.navigate("searchrecipe")}
          color="#FFD700"
        />
      </View>

      {}
      <View style={styles.buttonSpacer} />

      <View style={styles.buttonContainer}>
        {}
        <Button
          title="Substitute"
          onPress={() => navigation.navigate("subs")}
          color="#FFD700"
        />
      </View>

      {}
      <View style={styles.buttonSpacer} />

      <View style={styles.buttonContainer}>
        {}
        <Button
          title="Weekly Schedule"
          onPress={() => navigation.navigate("schedule")}
          color="#FFD700"
        />
      </View>

      {}
      <View style={styles.buttonSpacer} />

      <View style={styles.buttonContainer}>
        {/* Button 4: Scan Your Meal */}
        <Button
          title="Scan Your Meal"
          onPress={() => navigation.navigate("scanner")}
          color="#FFD700" // Yellow color
        />
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
    backgroundColor: "White", // Yellow background
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 140,
  },
  buttonContainer: {
    flexDirection: "row",
    justifyContent: "center",
    marginBottom: 10, // Added marginBottom for spacing
  },
  buttonSpacer: {
    height: 20, // Adjusted height for vertical spacing
  },
});

export default HomePage;
