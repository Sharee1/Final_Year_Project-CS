// DishDetails.js
import React from "react";
import { View, Text, StyleSheet } from "react-native";

export default function DishDetails({ route }) {
  const { name, description, ingredients } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.name}>{name}</Text>
      <Text style={styles.description}>{description}</Text>
      <Text style={styles.ingredients}>{ingredients}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  name: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 8,
  },
  description: {
    fontSize: 18,
    marginBottom: 8,
  },
  ingredients: {
    fontSize: 16,
  },
});
