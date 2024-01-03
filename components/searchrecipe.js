// SearchRecipe.js
import React, { useState } from "react";
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
  TextInput,
  Alert,
} from "react-native";

export default function SearchRecipe({ navigation }) {
  const [searchText, setSearchText] = useState("");
  const [showDetails, setShowDetails] = useState(false);
  const [foundDish, setFoundDish] = useState(null);

  const dishes = [
    {
      id: 1,
      name: "Pasta",
      description: "Delicious pasta dish",
      ingredients: "Pasta, sauce, cheese",
    },
    // Add more dishes as needed
  ];

  const navigateToDetails = (dish) => {
    navigation.navigate("DishDetails", dish);
  };

  const handleSearch = () => {
    const searchedDish = dishes.find(
      (dish) => dish.name.toLowerCase() === searchText.toLowerCase()
    );

    if (searchedDish) {
      navigateToDetails(searchedDish);
      setShowDetails(true);
      setFoundDish(searchedDish);
    } else {
      // Handle case when dish is not found
      setShowDetails(false);
      setFoundDish(null);
      Alert.alert(
        "Dish Not Found",
        "Sorry, the dish you searched for is not in our database."
      );
    }
  };

  return (
    <View style={styles.container}>
      <TextInput
        style={styles.searchBar}
        placeholder="Search for a dish..."
        onChangeText={(text) => setSearchText(text)}
        value={searchText}
      />

      {!showDetails ? (
        <TouchableOpacity style={styles.button} onPress={handleSearch}>
          <Text style={styles.buttonText}>Search</Text>
        </TouchableOpacity>
      ) : null}

      {showDetails ? (
        <View>
          {dishes.map((dish) => (
            <TouchableOpacity
              key={dish.id}
              onPress={() => navigateToDetails(dish)}
            >
              <Text style={styles.dishItem}>{dish.name}</Text>
            </TouchableOpacity>
          ))}
        </View>
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
  },
  searchBar: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 16,
    paddingLeft: 8,
  },
  button: {
    backgroundColor: "blue",
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    margin: 16,
  },
  buttonText: {
    color: "white",
    fontSize: 16,
    textAlign: "center",
  },
  dishItem: {
    fontSize: 18,
    marginBottom: 8,
    color: "blue",
  },
});
