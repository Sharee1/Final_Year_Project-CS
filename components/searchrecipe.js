import React, { useState } from "react";
import { View, Text, TextInput, Button, StyleSheet } from "react-native";

const SearchRecipe = ({ navigation }) => {
  const [searchText, setSearchText] = useState("");

  const handleSearch = () => {
    console.log("Searching for recipes with name: ${searchText}");
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Search Recipe</Text>

      <TextInput
        style={styles.input}
        placeholder="Enter recipe name here"
        value={searchText}
        onChangeText={(text) => setSearchText(text)}
      />

      <Button title="Search" onPress={handleSearch} />

      {/* Add your search results or other content here */}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 16,
    backgroundColor: "#FFF",
  },
  title: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 20,
  },
  input: {
    height: 40,
    width: "100%",
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
});

export default SearchRecipe;
