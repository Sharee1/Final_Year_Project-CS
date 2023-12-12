import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const Substitute = ({ navigation }) => {
  const [searchText, setSearchText] = useState('');

  const handleSearch = () => {
    // Implement your logic to search substitutes based on the searchText
    // For now, let's just log the search text to the console
    console.log(`Searching for substitutes with name: ${searchText}`);
  };

  const goBack = () => {
    navigation.goBack();
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Substitute Ingredients</Text>

      <TextInput
        style={styles.input}
        placeholder="Enter ingredient name"
        value={searchText}
        onChangeText={(text) => setSearchText(text)}
      />

      {/* Change button color to yellow */}
      <Button title="Search" onPress={handleSearch} color="#FFD700" />

      {/* Add your substitute results or other content here */}
      
      {/* Add spacing */}
      <View style={styles.buttonSpacer} />

      {/* Change button color to yellow */}
      <Button title="Go Back" onPress={goBack} color="#FFD700" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
    backgroundColor: '#FFF', // White background
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  input: {
    height: 40,
    width: '100%',
    borderColor: 'gray',
    borderWidth: 1,
    marginBottom: 10,
    paddingHorizontal: 10,
  },
  buttonSpacer: {
    height: 10,
  },
});

export default Substitute;