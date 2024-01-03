// Subs.js
import React, { useState } from "react";
import {
  View,
  Text,
  TextInput,
  TouchableOpacity,
  Alert,
  StyleSheet,
} from "react-native";

export default function Subs() {
  const [ingredient, setIngredient] = useState("");
  const substitutesData = {
    tomato: "bell pepper",
    onion: "green onion",
    garlic: "shallot",
    cilantro: "parsley",
    sugar: "honey",
    flour: "almond flour",
    butter: "coconut oil",
    milk: "soy milk",
    eggs: "applesauce",
    chocolate: "cocoa nibs",
    garlic: "garlic powder",
    oliveoil: "avocado oil",
    salt: "sea salt",
    pepper: "cayenne pepper",
    bakingpowder: "yeast",
    yogurt: "coconut yogurt",
    onions: "shallots",
    lemonjuice: "white vinegar",
    brownsugar: "maple syrup",
    vanillaextract: "almond extract",
    cinnamon: "nutmeg",
    cilantro: "parsley",
    sourcream: "greek yogurt",
    shrimp: "tofu",
    beef: "turkey",
    mayonnaise: "greek yogurt",
    soysauce: "tamari",
    mustard: "dijon mustard",
    thyme: "rosemary",
    basil: "oregano",
    paprika: "cayenne pepper",
    heavycream: "coconut cream",
    rice: "quinoa",
    pasta: "zucchini noodles",
    cornstarch: "arrowroot powder",
    chicken: "turkey",
    cheese: "nutritional yeast",
    coconutmilk: "almond milk",
    peanutbutter: "almond butter",
    maplesyrup: "agave nectar",
    dill: "tarragon",
    cheddarcheese: "monterey jack cheese",
    broccoli: "cauliflower",
    cranberries: "raisins",
    cumin: "coriander",
    cayennepepper: "paprika",
    honey: "sugar",
    almondflour: "flour",
    soymilk: "milk",
    applesauce: "eggs",
    cocoanibs: "chocolate",
    sundriedtomatoes: "tomatoes",
    garlicpowder: "garlic",
    avocadooil: "olive oil",
    seasalt: "salt",
    cayennepepper: "pepper",
    yeast: "baking powder",
    coconutyogurt: "yogurt",
    shallots: "onions",
    whitevinegar: "lemon juice",
    maplesyrup: "brown sugar",
    almondextract: "vanilla extract",
    nutmeg: "cinnamon",
    parsley: "cilantro",
    greekyogurt: "sour cream",
    tofu: "shrimp",
    groundturkey: "ground beef",
    greekyogurt: "mayonnaise",
    tamari: "soysauce",
    dijonmustard: "mustard",
    rosemary: "thyme",
    oregano: "basil",
    cayennepepper: "paprika",
    coconutcream: "heavy cream",
    quinoa: "rice",
    zucchininoodles: "pasta",
    arrowrootpowder: "cornstarch",
    cherrytomatoes: "bell peppers",
    groundturkey: "ground chicken",
    chives: "green onions",
    nutritionalyeast: "parmesan cheese",
    almondmilk: "coconut milk",
    almondbutter: "peanut butter",
    agavenectar: "maple syrup",
    tarragon: "dill",
    cauliflower: "broccoli",
    raisins: "cranberries",
    coriander: "cumin",
    paprika: "cayenne pepper",

    // Add more ingredients and their substitutes as needed
  };
  const findSubstitute = () => {
    const formattedIngredient = ingredient.trim().toLowerCase(); // Remove extra spaces and convert to lowercase
    const substitute = substitutesData[formattedIngredient];

    if (substitute) {
      Alert.alert(
        "Substitute Found",
        `For ${ingredient}, you can use ${substitute}.`
      );
    } else {
      Alert.alert(
        "Substitute Not Found",
        `Sorry, no substitute found for ${ingredient}.`
      );
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Find Ingredient Substitute</Text>

      <TextInput
        style={styles.input}
        placeholder="Enter an ingredient..."
        onChangeText={(text) => setIngredient(text)}
        value={ingredient}
      />

      <TouchableOpacity style={styles.button} onPress={findSubstitute}>
        <Text style={styles.buttonText}>Find Substitute</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  heading: {
    fontSize: 20,
    marginBottom: 16,
  },
  input: {
    height: 40,
    width: 200,
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
  },
  buttonText: {
    color: "white",
    fontSize: 16,
    textAlign: "center",
  },
});
