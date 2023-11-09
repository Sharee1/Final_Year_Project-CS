import pymongo

def insert_recipe(recipe_info):
    client = pymongo.MongoClient("localhost", 27017)
    db = client["recipe-database"]
    collection = db.recipe_table

    recipe_id = collection.insert_one(recipe_info).inserted_id
    print(f"Recipe with id {recipe_id} has been created.")

# def visualize_data():
#     client = pymongo.MongoClient("localhost", 27017)
#     db = client["recipe-database"]
#     collection = db.recipe_table

#     recipes = collection.find()

#     for recipe in recipes:
#         print(f"Recipe ID: {recipe['_id']}")
#         print(f"Name: {recipe['name']}")
#         print("Total Ingredients:")
#         for ingredient in recipe['total_ingredients']:
#             print(f"  - {ingredient}")
        
#         print("Ingredients Required:")
#         for required in recipe['ingredients_required']:
#             print(f"  - Item: {required['item']}, Quantity: {required['quantity']}, Notes: {required.get('notes', '')}")

#         print(f"Description: {recipe['description']}")
#         print("\n" + "="*30 + "\n")

if __name__ == '__main__':
    # Add Recipe 1
    recipe1_info = {
        "name": "BOMBAY BIRYANI",
        "total_ingredients": [
            "Salt",
            "Red Chili",
            "Paprika",
            "Turmeric",
            "Coriander",
            "Green Cardamom",
            "Carom",
            "Fenugreek Leaves",
            "Dried Mango Powder",
            "Black Pepper",
            "Clove",
            "Garlic",
            "Acid: Citric Acid",
            "Maltodextrin"
        ],
        "ingredients_required": [
            {"item": "MEAT ON BONES", "quantity": "1 kg / 2.2 lbs", "notes": "small portions"},
            {"item": "RICE, BASMATI", "quantity": "750g / 3 ½ cups", "notes": "washed & soaked"},
            {"item": "ONIONS", "quantity": "300g / 3 medium", "notes": "finely sliced"},
            {"item": "TOMATOES", "quantity": "300g / 3-4 medium", "notes": "diced"},
            {"item": "POTATOES", "quantity": "250g / 2 medium", "notes": "peeled and quartered"},
            {"item": "GARLIC PASTE", "quantity": "2 tablespoons"},
            {"item": "GINGER PASTE", "quantity": "2 tablespoons"},
            {"item": "YOGURT, PLAIN", "quantity": "200g / 1 cup", "notes": "whipped"},
            {"item": "COOKING OIL", "quantity": "175ml / 1 cup"},
            {"item": "SHAN SPECIAL BOMBAY BIRYANI MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"},
        ],
        "description": "Fry onions in hot oil until golden. Add tomatoes and fry until oil separates. Add meat, garlic paste, ginger paste, yogurt, potatoes, and Shan Special Bombay Biryani Mix. Stir fry for 10 minutes. Add water (Beef/Lamb 4 cups, Chicken 2 cups). Cover and cook on low heat until meat is tender. Then increase heat and stir fry until oil separates from gravy. Separately: In 15 cups / 3 liters of boiling water, stir in tablespoons of Shan Salt and soaked rice. Boil rice until ¾ cooked. Remove and drain thoroughly. Spread half rice in pot and pour meat curry. Top with remaining rice. Cover pot and cook on low heat until rice is fully cooked (5-10 minutes). Mix before serving. Tips: For meat, use breast, ribs & shoulder cuts."
    }
    insert_recipe(recipe1_info)

    recipe2_info = {
    "name": "DALEEM",
    "total_ingredients": [
        "Grains Mix Powder",
        "Ground Flours of Wheat",
        "Barley",
        "Split Yellow Pea",
        "Split Mung Beans",
        "Skinless Black Gram",
        "Red Lentil",
        "Spice Mix Powder:",
        "Salt",
        "Red Chili",
        "Paprika",
        "Turmeric",
        "Black Pepper",
        "Curry Leaf",
        "Coriander",
        "Nigella",
        "Cumin",
        "Green Cardamom",
        "Bay Leaf",
        "Caraway",
        "Clove",
        "Ginger",
        "Dehydrated Onion",
        "Garlic",
        "Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide",
        "Dried Papaya Powder"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "250g", "notes": "Boneless"},
        {"item": "BONES", "quantity": "500g", "notes": "Small portions"},
        {"item": "OIL / GHEE", "quantity": "1 cup / 175ml"},
        {"item": "ONION", "quantity": "1 medium", "notes": "Finely sliced"},
        {"item": "SHAN SPECIAL SHAHI HALEEM MIX", "quantity": "Contains 2 sachets: Shan pulses & grain mix, Shan Shahi Haleem Masala"}
    ],
    "description": "Heat half cup oil/ghee. Add meat, bones, and Shan Special Haleem Masala. Stir-fry for a few minutes. Then add 15 cups of water. Cover the pot or use a pressure cooker and cook until the meat is tender. Remove from heat. Separate meat and gravy. Discard the bones. Grind the mixture for one minute in a blender to shred the meat. In the gravy add Shan’s grains and pulses mix and meat. Stir and add 1-2 cups of water. Cook on medium heat for 30 minutes. Stir occasionally. Heat remaining oil/ghee. Fry the onions until golden. Then pour over Haleem. Cover and cook on low heat for 10 - 15 minutes."
}

insert_recipe(recipe2_info)


recipe3_info = {
    "name": "BIHARI KABAB",
    "total_ingredients": [
        "Coriander",
        "Red Chili",
        "Paprika",
        "Salt",
        "Ginger",
        "Garlic",
        "Muskmelon",
        "Dehydrated Onion",
        "Long Pepper",
        "Carom",
        "Bay Leaf",
        "Black Cumin",
        "Black Pepper",
        "Green Cardamom",
        "Cumin",
        "Dill Seed",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "1 kg", "notes": "boneless small cubes"},
        {"item": "FRIED ONIONS", "quantity": "3 tablespoons", "notes": "finely crushed"},
        {"item": "GINGER PASTE", "quantity": "2 tablespoons"},
        {"item": "GARLIC PASTE", "quantity": "2 tablespoons"},
        {"item": "PLAIN YOGURT", "quantity": "½ cup", "notes": "whipped"},
        {"item": "OIL/GHEE", "quantity": "3-4 tablespoons"},
        {"item": "SHAN BIHARI KABAB MIX", "quantity": "1 packet"}
    ],
    "description": "Mix Shan Bihari Kabab Mix, fried onions, ginger, garlic, yogurt and ghee/oil. Apply on meat. Set aside for 3-4 hours or overnight. Thread meat on skewers and grill on very low heat until the Kababs are well done and brown on all sides. Turn the skewers periodically to grill evenly. If kababs fall, wrap a thread around them.\n\nServing Suggestion: Serve with Tamarind chutney and onion rings rinsed in cold water.\n\nNote for frying onions: Deep fry the onions in hot oil until golden. Remove from ghee/oil and spread on an absorbent paper. Allow to cool then crush coarsely.\n\nChicken: Use meat on bone for chicken.\n\nFried Bihari Kababs: Use additional 1 cup ghee / butter in the above recipe. Follow the above recipe until step No. 1. Heat ghee/butter and add meat mixture. Fry on high heat until oil separates from meat. Stir frequently. Place a small piece of red hot coal in a small utensil and keep it inside meat pot. Pour a tablespoon of ghee over coal and cover pot for few minutes. Then remove coal."
}

insert_recipe(recipe3_info)

recipe4_info = {
    "name": "TIKKA BOTI",
    "total_ingredients": [
        "Paprika",
        "Red Chili",
        "Salt",
        "Muskmelon",
        "Cumin",
        "Coriander",
        "Black Pepper",
        "Cinnamon",
        "Brown Cardamom",
        "Ginger",
        "Garlic",
        "Leavening Agent: Sodium Bicarbonate",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide",
        "Dried Papaya Powder"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "1 – 1½ kg", "notes": "thin small cubes"},
        {"item": "GARLIC PASTE", "quantity": "2-3 tablespoons"},
        {"item": "OIL / BUTTER", "quantity": "½ cup", "notes": "melted for basting"},
        {"item": "SHAN TIKKA MIX1", "quantity": "1 packet"}
    ],
    "description":"Mix Shan Tikka Mix in half cup of water, garlic and 2 tablespoons oil. Apply to meat. Leave to marinate for 3-4 hours. *(Remove and discard the raw papaya slices from the meat, if used). Sew meat onto skewers. Place on very low heat of coal/gas fire. Grill lightly on all sides. Lightly brush meat with butter/oil and rotate the skewers until meat is tender. Serve with Shan Tamarind Chutney, salad, and lemon juice. * To tenderize the meat further, add ½ cup thinly sliced papaya."
}

insert_recipe(recipe4_info)

recipe5_info = {
    "name": "CHICKEN TIKKA",
    "total_ingredients": [
        "Salt",
        "Red Chili",
        "Paprika",
        "Turmeric",
        "Aniseed",
        "Cinnamon",
        "Cumin",
        "Brown Cardamom",
        "Black Pepper",
        "Star Aniseed",
        "Ginger",
        "Dried Papaya Powder",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Citric Acid",
        "Sodium Phosphate",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN SKINLESS", "quantity": "1½ kgs / 3.3 lbs", "notes": "8-10 portions, make 2-3 slits on each"},
        {"item": "LEMON JUICE", "quantity": "8-10 tablespoons"},
        {"item": "COOKING OIL/ MELTED BUTTER", "quantity": "6 tablespoons"},
        {"item": "SHAN CHICKEN TIKKA MIX", "quantity": "1 packet", "notes": "do not mix in water"}
    ],
    "description": "Mix together Shan Chicken Tikka Mix, lemon juice, and 2 tablespoons oil. Apply on chicken pieces and marinate for 3 hours +. Put each portion of chicken on skewer and place it on low heat of charcoal / gas grill. Grill evenly on each side until meat is tender and done. Apply butter before removing from heat.\n\nServing Suggestions: Serve hot Chicken Tikka with fresh green salad, sliced onion, tomatoes, and Shan Tamarind / BBQ / Green Chutney.\n\nGrilled Chicken Tikka: Follow the above Chicken Tikka recipe up to step No. 1. Place chicken pieces in a frying pan and grill on high heat for 3 minutes on each side. Apply butter, cover and cook on low heat for 10 minutes."
}

insert_recipe(recipe5_info)

recipe6_info = {
    "name": "SEEKH KABAB",
    "total_ingredients": [
        "Paprika",
        "Red Chili",
        "Salt",
        "Coriander",
        "Muskmelon",
        "Ginger",
        "Allspice",
        "Long Pepper",
        "Black Pepper",
        "Cumin",
        "Clove",
        "Bay Leaf",
        "Garlic",
        "Roasted Chickpea",
        "Carom",
        "Dried Papaya Powder",
        "Citric Acid",
        "Maltodextrin",
        "Sodium Phosphate",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "GROUND / MINCED MEAT", "quantity": "1kg / 2.2lbs & 200g fat/suet", "notes": "minced twice"},
        {"item": "GREEN CHILIES", "quantity": "2-3 tablespoons", "notes": "coarsely grounded"},
        {"item": "ONION", "quantity": "1 small / 75g", "notes": "finely diced (squeeze to remove liquid)"},
        {"item": "CILANTRO/FRESH CORIANDER", "quantity": "2 tablespoons", "notes": "chopped"},
        {"item": "GARLIC PASTE", "quantity": "2 tablespoons"},
        {"item": "BUTTER", "quantity": "2-3 tablespoons"},
        {"item": "SHAN SEEKH KABAB MIX", "quantity": "1 packet"}
    ],
    "description": "Mix all the above ingredients except butter and run in a chopper for 1 minute. Set aside for about 2-3 hours. Add butter and mix well. Make small round meat balls. Thread each through a skewer. Flatten the grounded meat in a thin layer around each skewer with wet Barbeque on low heat of coal/gas grill (or in a hot oven 275°F). Periodically turn skewer, until the kababs change color. Do not over grill / brown the kabab.\n\nServing Suggestions: Serve with Shan Tamarind / BBQ / Green Chutney and onion salad."
}

insert_recipe(recipe6_info)

recipe7_info = {
    "name": "TANDOORI MASALA",
    "total_ingredients": [
        "Paprika",
        "Salt",
        "Red Chili",
        "Ginger",
        "Black Pepper",
        "Cumin",
        "Brown Cardamom",
        "Garlic",
        "Aniseed",
        "Cinnamon",
        "Dried Papaya Powder",
        "Maltodextrin",
        "Sugar",
        "Hydrolyzed Soy Protein",
        "Citric Acid",
        "Sodium Phosphate",
        "Canola Oil",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN SKINLESS", "quantity": "1½ kg /3.3 lbs", "notes": "8-12 portions, make slits on each"},
        {"item": "PLAIN YOGURT", "quantity": "1 cup/200g", "notes": "whipped & strained"},
        {"item": "LEMON JUICE", "quantity": "5-6 tablespoons"},
        {"item": "RED FOOD COLOR No. 6", "quantity": "½ teaspoon"},
        {"item": "COOKING OIL/ MELTED BUTTER", "quantity": "4-6 tablespoons"},
        {"item": "SHAN TANDOORI MASALA MIX", "quantity": "1 packet", "notes": "do not mix in water"}
    ],
    "description": "Mix lemon juice, food color, Shan Tandoori Masala Mix, and 2 tablespoons oil / butter. Apply to chicken pieces. Prick all over the meat. Set aside for 30 minutes. Apply strained yogurt and set aside for 3 hours +. Arrange the pieces in a tray and discard the marinade. Bake in a preheated oven, (350°F) for 25 minutes. Apply remaining oil / melted butter on chicken and place the tray under high setting of grill until lightly brown or barbecue.\n\nServing Suggestion: Serve hot Chicken Tandoori with Shan Tamarind / Green Chutney."
}

insert_recipe(recipe7_info)


recipe8_info = {
    "name": "LAHORI FISH",
    "total_ingredients": [
        "Wheat/Corn/Gram Flour",
        "Salt",
        "Red Chili",
        "Dehydrated Onion",
        "Garlic",
        "Ginger",
        "Bay Leaf",
        "Citric Acid",
        "Black Cumin",
        "Clove",
        "Black Pepper",
        "Cinnamon",
        "Carom",
        "Turmeric",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Silicon Dioxide",
        "Dried Mango Powder",
        "Sodium Bicarbonate"
    ],
    "ingredients_required": [
        {"item": "SHAN LAHORI FISH MASALA MIX", "quantity": "1 packet"}
    ],
    "description": "Mix half cup of water in Shan Lahori Fish Mix and make a smooth batter. Apply on fish.Deep fry fish until golden and crisp."
}

insert_recipe(recipe8_info)

recipe9_info = {
    "name": "FRIED FISH",
    "total_ingredients": [
        "Red Chili",
        "Paprika",
        "Coriander",
        "Salt",
        "Dehydrated Onion",
        "Garlic",
        "Ginger",
        "Fenugreek Leaves",
        "Cinnamon",
        "Carom",
        "Clove",
        "Turmeric",
        "Brown Cardamon",
        "Cumin",
        "Black Pepper",
        "Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide",
        "Dried Mango Power",
        "Wheat Flour"
    ],
    "ingredients_required": [
        {"item": "FISH", "quantity": "1 KG", "notes": "whole/sliced"},
        {"item": "GARLIC PASTE", "quantity": "2-3 tablespoons"},
        {"item": "COOKING OIL", "quantity": "2-3 cups for shallow frying"}
    ],
    "description": "Mix garlic paste, Shan Fried Fish Mix, and one tablespoon oil. Apply on the fish. Set aside for 2-3 hours. Fry fish in hot oil until lightly golden. Enjoy tasty Fried Fish with Shan Chaat Masala and lime juice."
}

insert_recipe(recipe9_info)

recipe10_info = {
    "name": "KOFTA",
    "total_ingredients": [
        "Coriander",
        "Red Chili",
        "Salt",
        "Paprika",
        "Roasted Chickpea",
        "Cinnamon",
        "Dehydrated Onion",
        "Ginger",
        "Black Pepper",
        "Cumin",
        "Green Cardamom",
        "Garlic",
        "Fenugreek Leaves",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide",
        "Dried Papaya Powder"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "1 kg", "notes": "finely grounded to a paste"},
        {"item": "ONIONS", "quantity": "300g", "notes": "grounded"},
        {"item": "PLAIN YOGURT", "quantity": "1½ cups/300g", "notes": "whipped"},
        {"item": "GARLIC PASTE", "quantity": "1 tablespoon"},
        {"item": "FRESH CILANTRO", "quantity": "2 tablespoons", "notes": "chopped"},
        {"item": "OIL / GHEE", "quantity": "175-250g"},
        {"item": "SHAN KOFTA MIX", "quantity": "1 packet"}
    ],
    "description": "In the minced meat, add half grounded onions, half yogurt, green coriander, and 2 tablespoons Shan Kofta Mix. Knead to make a smooth dough. Make about 40 small round meat balls. Heat ghee and fry the remaining onions paste until golden. Add garlic, the remaining yogurt, and Shan Kofta Mix. Stir fry for a few minutes and then add 2-3 glasses of water. Boil for about 15 minutes on medium heat. Add meat balls and reduce the heat. Cook until meat balls are tender; about 20-30 minutes. Do not stir with a spoon."
}

insert_recipe(recipe10_info)

recipe11_info = {
    "name": "CHICKEN WHITE KORMA",
    "total_ingredients": [
        "Salt",
        "Coriander",
        "Red Chilli",
        "Garlic",
        "Ginger",
        "Black Pepper",
        "White Pepper",
        "Turmeric",
        "Cumin",
        "Acid: Citric Acid",
        "Cinnamon",
        "Dried Onion",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "1 kg", "notes": "small portions"},
        {"item": "ONIONS", "quantity": "4 medium/400g", "notes": "finely diced"},
        {"item": "GARLIC PASTE", "quantity": "1 tablespoon"},
        {"item": "GINGER PASTE", "quantity": "2 tablespoons"},
        {"item": "GREEN CHILIES", "quantity": "2-4 tablespoons", "notes": "grounded"},
        {"item": "LEMON JUICE", "quantity": "4 tablespoons"},
        {"item": "PLAIN YOGURT", "quantity": "1 cup/200g", "notes": "whipped"},
        {"item": "OIL/GHEE", "quantity": "½-1 cup / 180ml"},
        {"item": "SHAN CHICKEN WHITE KORMA MIX", "quantity": "1 packet"}
    ],
    "description": "Mix together green chili paste, garlic paste, ginger paste, and Shan Chicken White Korma Mix. Apply to the chicken and set aside for 30-45 minutes. Heat oil and fry onions until light brown. Remove onions from oil and grind with yogurt. Keep aside. In the same oil, add marinated chicken and stir fry for 4-5 minutes. Add onion and yogurt mixture. Cook for 15 minutes or until oil separates from the gravy. (For a thinner gravy, add half to one cup milk). Add lemon juice and remove from heat. Garnish with a few blanched and peeled almonds."
}

insert_recipe(recipe11_info)

recipe12_info = {
    "name": "KORMA",
    "total_ingredients": [
        "Red Chili",
        "Salt",
        "Coriander",
        "Paprika",
        "Cinnamon",
        "Fennel",
        "Turmeric",
        "Cumin",
        "Muskmelon",
        "Bay Leaf",
        "Black Pepper",
        "Green Cardamom",
        "Cloves",
        "Garlic",
        "Ginger",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Natural & Artificial Food Flavor",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "BONES", "quantity": "1 kg / 2.2 lbs", "notes": "small portions"},
        {"item": "ONIONS", "quantity": "3 medium / 300g", "notes": "finely sliced"},
        {"item": "PLAIN YOGURT", "quantity": "1 ½ cups / 300g", "notes": "whipped"},
        {"item": "GINGER JULIENNE", "quantity": "2-3 tablespoons"},
        {"item": "OIL/ GHEE", "quantity": "1 cup / 175 ml"},
        {"item": "SHAN KORMA MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"}
    ],
    "description": "Heat oil, fry onions until light golden, remove and crush. In the same oil, add meat, yogurt, and Shan Korma Mix. Cover and cook on low heat for 20-30 minutes. Add julienne ginger and ½-1 cup water for gravy. Cover and cook on low heat until meat is tender. Stir-in crushed onions. Cover and cook on low heat for 5-10 minutes."
}

insert_recipe(recipe12_info)

recipe13_info = {
    "name": "CHICKEN MASALA",
    "total_ingredients": [
        "Red Chili",
        "Salt",
        "Turmeric",
        "Star Aniseed",
        "Coriander",
        "Cinnamon",
        "Cumin",
        "Brown Cardamom",
        "Carom",
        "Black Pepper",
        "Fenugreek Seed",
        "Bay Leaf",
        "Clove",
        "Green Cardamom",
        "Ginger",
        "Garlic",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide (Anticaking Agent)"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "1 kg/2.2 lbs", "notes": "small portions"},
        {"item": "ONIONS", "quantity": "3 medium / 300g", "notes": "finely sliced or (Fried Onion 60g / ½ cup)"},
        {"item": "PLAIN YOGURT", "quantity": "1 ½ cups / 300g", "notes": "whipped"},
        {"item": "GINGER JULIENNE", "quantity": "2 tablespoons"},
        {"item": "OIL / GHEE", "quantity": "1 cup / 175 ml"},
        {"item": "SHAN CHICKEN MASALA MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"}
    ],
    "description": "Heat oil, fry onions until light golden, remove and crush. In the same oil, add chicken, yogurt, and Shan Chicken Masala Mix. Cover and cook on low heat for 20-30 minutes. Add julienne ginger and ½ -2 cups water for gravy. Cover and cook on low heat for 5 minutes. Stir-in crushed onions. Cover and cook on low heat for 5 minutes."
}

insert_recipe(recipe13_info)

recipe14_info = {
    "name": "NIHARI",
    "total_ingredients": [
        "Red Chili",
        "Salt",
        "Paprika",
        "Nigella",
        "Garlic",
        "Dehydrated Onion",
        "Cumin",
        "Bay Leaf",
        "Aniseed",
        "Green Cardamom",
        "Black Pepper",
        "Ginger",
        "Clove",
        "Fennel",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "1kg / 2.2lbs", "notes": "4-6 large portions"},
        {"item": "BONES", "quantity": "2kg / 4.4lbs", "notes": "knuckle & marrow"},
        {"item": "ONIONS", "quantity": "1 medium", "notes": "finely sliced"},
        {"item": "FLOUR", "quantity": "1 cup / 100g", "notes": "dissolve in 2 cups water"},
        {"item": "COOKING OIL", "quantity": "1 cup /175 ml"},
        {"item": "SHAN NIHARI MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"}
    ],
    "description": "Heat ½ cup oil, add meat and Shan Nihari Mix. Stir fry until oil separates from masala. Add 18 cups / 3 ½ liters water and bones. Stir and bring to boil. Cover and cook undisturbed on low heat (for: Beef 6 hours, Goat / Lamb 4 hours, Chicken 3 hours). Remove bones, collect marrow and discard bones. Add marrow to gravy. Gradually add dissolved flour in the gravy. Stir and mix. Bring to boil and cook for 15 minutes. Stir occasionally. Heat remaining oil and add sliced onion. Stir fry until golden and pour into Nihari. Cover and simmer for 10 minutes on low heat. Remove excessive oil before serving, if desired."
}

insert_recipe(recipe14_info)

recipe15_info = {
    "name": "MURGH CHOLAY",
    "total_ingredients": [
        "Coriander",
        "Paprika",
        "Salt",
        "Red Chili",
        "Black Pepper",
        "Clove",
        "Brown Cardamom",
        "Cinnamon",
        "Turmeric",
        "Muskmelon",
        "Cumin",
        "Bay Leaf",
        "Garlic",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide",
        "Raising Agent: Sodium Bicarbonate"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "750g large portions"},
        {"item": "CHICKPEAS", "quantity": "1 ½ cups / 300g", "notes": "soaked in water for 2 hours"},
        {"item": "ONIONS", "quantity": "2 medium/200g", "notes": "finely sliced"},
        {"item": "GARLIC PASTE", "quantity": "1 tablespoon"},
        {"item": "OIL / GHEE", "quantity": "1 cup"},
        {"item": "SHAN MURGH CHOLAY MIX", "quantity": "1 packet"}
    ],
    "description": "Heat half oil / ghee and fry onions until golden. Add garlic and chicken. Stir fry for a few minutes. Add 2 cups water. Cover and cook on low heat until chicken is tender. Separately: Add soaked chickpeas in 12 cups water and boil on low heat for 2 hours. Then add Shan Murgh Cholay Mix. Stir and boil for 1 hour or until chickpeas are tender. Combine cooked chicken with cooked chickpeas. Stir and cook for 30 minutes. Add heated half cup oil / ghee and cook until oil / ghee starts to separate from chickpeas curry."
}

insert_recipe(recipe15_info)

recipe16_info = {
    "name": "FISH BIRYANI",
    "total_ingredients": [
        "Salt",
        "Red Chili",
        "Paprika",
        "Turmeric",
        "Coriander",
        "Green Cardamom",
        "Carom",
        "Fenugreek Leaves",
        "Dried Mango Powder",
        "Black Pepper",
        "Clove",
        "Garlic",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "FISH", "quantity": "750g", "notes": "cubes/fillets (boneless)"},
        {"item": "RICE, BASMATI", "quantity": "750g/3 ½", "notes": "washed & soaked for 30 minutes"},
        {"item": "ONIONS", "quantity": "3 medium/300g", "notes": "finely sliced"},
        {"item": "GARLIC PASTE", "quantity": "2 tablespoons"},
        {"item": "PLAIN YOGURT", "quantity": "1¼ cups/250g", "notes": "whipped"},
        {"item": "SOYA LEAVES", "quantity": "½ cup", "notes": "chopped/1’’long"},
        {"item": "CILANTRO/FRESH CORIANDER", "quantity": "½ cup", "notes": "chopped"},
        {"item": "GREEN CHILIES", "quantity": "10-15 small whole", "notes": "slit from one side"},
        {"item": "LEMON JUICE", "quantity": "4 tablespoons"},
        {"item": "OIL / GHEE", "quantity": "1½ cups/250ml"},
        {"item": "SHAN FISH BIRYANI MIX", "quantity": "1 packet"}
    ],
    "description": "Mix lemon juice Shan Fish Biryani Mix and garlic. Apply the mixture to the fish and set it aside to marinate for half an hour. Heat half a cup of ghee/oil and fry 2 sliced onions for a few minutes. Then add marinated fish, green chilies and fresh coriander. Fry until oil separates from the masala. Stir in yogurt. Cover and cook on medium heat until the fish is tender. Avoid over stirring the fish. Separately: Take 2 tablespoons of ghee/oil and fry the soya leaves for about 2 minutes. Add 12 glasses of water and 2 tablespoons salt. Bring to boil and add the soaked rice. Cook until the rice is three-quarter tender. Then drain the liquid thoroughly. Spread half the rice in a pot and evenly pour the cooked fish and masala over it. Then spread and cover it with remaining rice. Heat the remaining 1 cup oil/ghee and fry the remaining 1 sliced onion until golden. Pour this evenly over the rice. Cover and cook on low heat until the rice is tender."
}

insert_recipe(recipe16_info)

recipe17_info = {
    "name": "SINDHI BIRYANI",
    "total_ingredients": [
        "Himalayan Pink Salt",
        "Red Chili",
        "Dried Plums with Pits",
        "Paprika",
        "Coriander",
        "Turmeric",
        "Cumin",
        "Cinnamon",
        "Clove",
        "Black Pepper",
        "Ginger",
        "Aniseed",
        "Carom",
        "Brown Cardamom",
        "Dried Papaya Powder",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Citric Acid",
        "Cane Sugar",
        "Canola Oil",
        "Natural and Artificial Food Flavor",
        "Silicon Dioxide (Anticaking Agent)"
    ],
    "ingredients_required": [
        {"item": "MEAT ON BONES", "quantity": "1 kg / 2.2 lbs", "notes": "small portions"},
        {"item": "RICE, BASMATI", "quantity": "750g/ 3 ½ cups", "notes": "washed & soaked"},
        {"item": "TOMATOES", "quantity": "200g / 2-3 medium", "notes": "thin round slices"},
        {"item": "POTATOES", "quantity": "250g / 2 medium", "notes": "peeled & quartered"},
        {"item": "PLAIN YOGURT", "quantity": "100g / ½ cup", "notes": "whipped"},
        {"item": "ONIONS", "quantity": "175g / 2 medium", "notes": "finely sliced"},
        {"item": "GARLIC PASTE", "quantity": "2 tablespoons"},
        {"item": "GINGER PASTE", "quantity": "2 tablespoons"},
        {"item": "SMALL GREEN CHILIES", "quantity": "10-20", "notes": "whole"},
        {"item": "CILANTRO/FRESH CORIANDER", "quantity": "1 cup", "notes": "chopped"},
        {"item": "MINT LEAVES", "quantity": "1 cup", "notes": "chopped"},
        {"item": "COOKING OIL", "quantity": "175ml /1cup"},
        {"item": "SHAN SINDHI BIRYANI MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"}
    ],
    "description": "Fry onions in hot oil until light golden. Add meat and garlic paste. Stir fry for 4-5 minutes on high heat. Add Shan Sindhi Biryani Mix, potatoes, yogurt, ginger paste and stir fry for 5 minutes. Add water (Beef/Lamb 4 cups, Chicken 2 cups). Cover and cook on low heat until meat is tender. When cooked there should be about two cups of gravy left (If less add water, if more increase heat). Place sliced tomatoes, green chilies, fresh coriander and mint leaves over the meat. Do not mix meat and green masala. Cover and cook on low heat for 5 minutes. Do not stir. Separately: In 15 cups / 3 liters of boiling water, stir in 3 tablespoons of Shan Salt and soaked rice. Boil rice until ¾ cooked. Remove and drain thoroughly. Spread cooked rice evenly over meat. Do not mix rice and meat. Cover and cook on low heat until rice is tender (5-10 minutes). Mix before serving."
}

insert_recipe(recipe17_info)

recipe18_info = {
    "name": "MEMONI BIRYANI",
    "total_ingredients": [
        "Salt",
        "Turmeric",
        "Paprika",
        "Red Chili",
        "Dill Seed",
        "Green Cardamom",
        "Black Pepper",
        "Clove",
        "Brown Cardamom",
        "Cumin",
        "Allspice",
        "Ginger",
        "Garlic",
        "Dried Papaya Powder",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide",
        "Natural And Artificial Food Flavor"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "750g", "notes": "meat on bone"},
        {"item": "RICE BASMATI", "quantity": "750g", "notes": "washed & soaked for 30 minutes"},
        {"item": "ONIONS", "quantity": "3-4 medium / 400g", "notes": "finely sliced"},
        {"item": "POTATOES", "quantity": "2 medium / 250g", "notes": "peeled & halved"},
        {"item": "TOMATOES", "quantity": "4 medium / 300g", "notes": "diced"},
        {"item": "PLAIN YOGURT", "quantity": "1¼ cups / 250g", "notes": "whipped"},
        {"item": "GARLIC PASTE", "quantity": "3 tablespoons"},
        {"item": "GINGER PASTE", "quantity": "2 tablespoons"},
        {"item": "GREEN CHILIES", "quantity": "10 medium / large", "notes": "whole"},
        {"item": "LEMON JUICE", "quantity": "3-4 tablespoons / 2 lemons"},
        {"item": "OIL/GHEE", "quantity": "1 ½ cup / 250ml"},
        {"item": "SHAN MEMONI BIRYANI", "quantity": "1 Packet"}
    ],
    "description": "Heat one cup ghee/oil and fry onions until light golden. Add meat, garlic, ginger and stir fry for a minute. Add Shan Memoni Mutton Biryani Mix and stir fry for 5-6 minutes. Add 3-4 cups water, yogurt and potatoes. Cover and cook on low heat until the meat is tender. Add tomatoes, green chilies and lemon juice. Stir and remove from heat. Separately: In 15 cups / 3 liters boiling water, stir in 3 tablespoons of Shan Salt and soaked rice. Boil rice until ¾ cooked. Remove and drain thoroughly. Spread three-quarter boiled rice in a pot and pour cooked meat curry over it. Then spread the remaining rice over the meat curry. Cover and cook on low heat for 10 minutes. Heat the remaining ½ cup oil/ghee and pour over the rice. Turn the rice from bottom to top to mix at few places. Cover and cook for 5 minutes."
}

insert_recipe(recipe18_info)

recipe19_info = {
    "name": "BIRYANI",
    "total_ingredients": [
        "Himalayan Pink Salt",
        "Garlic",
        "Ginger",
        "Cumin",
        "Bay Leaf",
        "Brown Cardamom",
        "Cinnamon",
        "Carom",
        "Green Cardamom",
        "Clove",
        "Red Chili",
        "Cane Sugar",
        "Coriander",
        "Turmeric",
        "Hydrolyzed Soy Protein",
        "Maltodextrin",
        "Canola Oil",
        "Natural and Artificial Food Flavor",
        "Silicon Dioxide (Anticaking Agent)"
    ],
    "ingredients_required": [
        {"item": "MEAT ON BONES", "quantity": "1 kg / 2.2 lbs", "notes": "small portions"},
        {"item": "RICE, BASMATI", "quantity": "3 ½ cups / 750g", "notes": "washed & soaked"},
        {"item": "ONIONS", "quantity": "3 medium", "notes": "250g, finely sliced"},
        {"item": "TOMATOES", "quantity": "3 medium", "notes": "250g, diced"},
        {"item": "CILANTRO/FRESH CORIANDER", "quantity": "½ cup", "notes": "chopped"},
        {"item": "MINT LEAVES", "quantity": "½ cup", "notes": "chopped"},
        {"item": "YOGURT, PLAIN", "quantity": "1 cup/ 200g", "notes": "whipped"},
        {"item": "COOKING OIL", "quantity": "1 cup / 175 ml"},
        {"item": "SHAN BIRYANI MIX", "quantity": "1 packet", "notes": "mix in ½ cup water"}
    ],
    "description": "Heat oil and fry onions until golden. Add meat, Shan Biryani Mix and stir fry for 5 minutes. Add yogurt and water (Beef/Lamb 4 cups, Chicken 2 cups). Cover and cook on low heat until meat is tender. Add tomatoes and stir fry on high heat until oil begins to separate from the gravy. Then keep aside. Separately: In 15 cups / 3 liters of boiling water, stir in 3 tablespoons of Shan Salt and soaked rice. Boil rice until ¾ cooked. Remove and drain thoroughly. Spread half rice in a pot and pour meat curry. Top with remaining rice. (Sprinkle a pinch of yellow food color if desired). Spread fresh coriander and mint leaves on the rice. Cover and cook on low heat until rice is tender (5-10 minutes). Mix before serving."
}

insert_recipe(recipe19_info)

recipe20_info = {
    "name": "CHICKEN HANDI",
    "total_ingredients": [
        "Salt",
        "Coriander",
        "Red Chili",
        "Black Pepper",
        "Ginger",
        "Garlic",
        "Paprika",
        "Aniseed",
        "Turmeric",
        "Cumin",
        "Acid: Citric Acid",
        "Green Cardamom",
        "Almond",
        "Coconut Powder",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "1kg", "notes": "Small boneless cubes"},
        {"item": "TOMATOES", "quantity": "6-8 medium / 500g", "notes": "Finely chopped"},
        {"item": "ONIONS", "quantity": "2 medium/ 200g", "notes": "Sliced, boil in water & grind"},
        {"item": "PLAIN YOGURT", "quantity": "½ cup", "notes": "Whipped"},
        {"item": "FRESH CILANTRO", "quantity": "2-3 tablespoons", "notes": "Chopped"},
        {"item": "SINGLE CREAM", "quantity": "½ cup"},
        {"item": "BUTTER", "quantity": "½ cup / 75g"},
        {"item": "COOKING OIL", "quantity": "¼ - ½ cup"},
        {"item": "SHAN CHICKEN HANDI MIX", "quantity": "1 packet"}
    ],
    "description": "Mix Shan Chicken Handi Mix in yoghurt and apply to chicken cubes. Marinate for 30 minutes. Boil finely diced tomatoes in 1-2 cups of water until soft and tender. Sieve to remove skin and seeds. Keep the tomato puree aside. Separately boil the onions in half cup of water and grind to a paste. Sieve and keep aside. In hot oil add the marinated chicken and stir-fry for 5 minutes. Add tomato puree and onion paste. Cover and cook on low heat for 10-15 minutes. Stir-in butter, chopped coriander leaves and single cream. Stir for 1 minute and remove from heat. Serve immediately with hot naans. Tips for Best Results: If using commercially packed “fresh cream”, add milk to make it thin before use. Wash chicken with 2 tablespoons white vinegar in half cup of water  before use. *Tomatoes can be replaced with 500g tomato puree/sauce."
}

insert_recipe(recipe20_info)

recipe21_info = {
    "name": "KARAHI",
    "total_ingredients": [
        "Red Chilli",
        "Paprika",
        "Salt",
        "Brown Cardamom",
        "Garlic",
        "Coriander",
        "Fenugreek Leaves",
        "Green Cardamom",
        "Cinnamon",
        "Clove",
        "Black Pepper",
        "Cumin",
        "Bay Leaf",
        "Onion",
        "Carom",
        "Dried Papaya Powder",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Acid: Citric Acid",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "MEAT", "quantity": "(1½ kg / 3.3 lbs) small cubes"},
        {"item": "TOMATO", "quantity": "6-7 medium / 500g", "notes": "Diced"},
        {"item": "GARLIC CRUSHED", "quantity": "2 tablespoons"},
        {"item": "GINGER PASTE", "quantity": "1 tablespoon"},
        {"item": "GREEN CHILLIES", "quantity": "6 medium", "notes": "Whole"},
        {"item": "CILANTRO/FRESH CORIANDER", "quantity": "Cilantro/Fresh Coriander, chopped"},
        {"item": "OIL", "quantity": "1½ cups / 275 ml"},
        {"item": "BUTTER", "quantity": "½ cup / 85g"},
        {"item": "SHAN KARHAI / FRY GOSHT", "quantity": "1 packet", "notes": "Mix in ½ cup water"}
    ],
    "description": "Mix garlic, ginger paste and Shan Karahi Mix. Apply to meat and marinate for (Chicken 15 minutes, Goat/ Lamb/ Beef 1-2 hours +). Heat one cup oil and stir fry meat on high heat for 5-6 minutes. Add julienne ginger. Cover and cook on low heat until meat is tender (Chicken 10 minutes, Goat / Lamb / Beef 45 minutes). Separately heat ½ cup oil and add tomatoes. Cook on low heat until soft (5-6 minutes). Stir periodically. Add cooked tomatoes and green chillies to the cooked meat. On medium heat stir-fry meat until oil separates from masala. Stir constantly. If desired remove excessive oil. Add fresh coriander and butter. Stir fry and serve with hot naans."
}

insert_recipe(recipe21_info)

recipe22_info = {
    "name": "ACHAR GOSHT",
    "total_ingredients": [
        "Red Chili",
        "Salt",
        "Turmeric",
        "Coriander",
        "Fennel",
        "Fenugreek Leaves",
        "Cumin",
        "Cinnamon",
        "Bay Leaf",
        "All Spice",
        "Nigella Seed",
        "Black Pepper",
        "Ginger",
        "Green Cardamom",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Citric Acid",
        "Cane Sugar",
        "Canola Oil",
        "Silicon Dioxide (Anticaking Agent)"
    ],
    "ingredients_required": [
        {"item": "MEAT ON BONES", "quantity": "1 kg / 2.2 lbs", "notes": "Small portions"},
        {"item": "GARLIC PASTE", "quantity": "1-2 tablespoons"},
        {"item": "GINGER PASTE", "quantity": "1-2 tablespoons"},
        {"item": "GREEN CHILIES", "quantity": "10 medium", "notes": "Slit lengthwise"},
        {"item": "LEMON JUICE", "quantity": "3-4 tablespoons"},
        {"item": "TOMATOES", "quantity": "6 medium / 500g", "notes": "Grind & sieve to make puree"},
        {"item": "PLAIN YOGURT", "quantity": "2 ½ cups / 500g", "notes": "Whipped"},
        {"item": "COOKING OIL", "quantity": "1 cup / 175ml"},
        {"item": "SHAN ACHAR GOSHT MIX", "quantity": "1 packet", "notes": "Mix in ½ cup water"}
    ],
    "description": "Mix 2 tablespoons of Shan Achar Gosht Mix with lemon juice and fill the green chilies. In hot oil add meat, garlic, ginger, yogurt and remaining Shan Achar Gosht Mix. Stir fry on high heat for 7-10 minutes. Add 2-3 cups of water. Cover and cook on low heat until meat is tender. Add tomato puree. Stir fry for 5-6 minutes on high heat and place green chilies over the meat. Cover and cook on low heat until oil separates from gravy. If desired remove excessive oil before serving. Tips: For meat, use cuts from shoulder and T-bone."
}

insert_recipe(recipe22_info)

recipe23_info = {
    "name": "CHICKEN BROAST",
    "total_ingredients": [
        "Extra Fine Wheat Flour",
        "Salt",
        "Red Chilli",
        "Dehydrated Onion",
        "Garlic",
        "Cumin",
        "Ginger",
        "Black Cumin",
        "Carom",
        "Bay Leaf",
        "Fenugreek Leaves",
        "Acid: Citric Acid",
        "Turmeric",
        "Green Cardamom",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Raising Agent: Sodium Bicarbonate",
        "Anticaking Agent: Silicone Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "1½ kg", "notes": "8 large portions, washed & drained"},
        {"item": "COOKING OIL", "quantity": "3 cups / 500g", "notes": "For deep frying"},
        {"item": "LEMON JUICE", "quantity": "2 tablespoons"},
        {"item": "SHAN CHICKEN BROAST MIX", "quantity": "1 packet"}
    ],
    "description": "Mix lemon juice and 1tsp of Shan salt and rub all over the chicken pieces. Cover and marinate for at least 3-4 hours. Coat chicken pieces in Shan Chicken Broast Mix and keep it in the fridge for 15 minutes. Before frying, coat the chicken pieces in the remaining broast mix. Heat oil and fry chicken pieces to a crisp golden color. Serving Suggestion: Serve hot with Shan Tamarind chutney/Tomato Ketchup. Hot & Spicy Broasted Chicken: Follow the directions given above for Chicken Broast and complete until Step No. 1. Then take additional ingredients: ½ cup crushed Potato Chips, ½ cup crushed Corn Flakes, mixed together. Add Shan Chicken Broast Mix in ½ cup of cold water to make a thin paste. Dip the chicken pieces in the batter and roll each in the Corn Flakes and Potato Chips mixture. Then deep fry until crisp and golden."
}

insert_recipe(recipe23_info)


recipe24_info = {
    "name": "LAHORI CHARGA",
    "total_ingredients": [
        "Red Chili",
        "Cumin",
        "Star Aniseed",
        "Salt",
        "Garlic",
        "Ginger",
        "Cinnamon",
        "Brown Cardamom",
        "Green Cardamom",
        "Turmeric",
        "Carom",
        "Acid: Citric Acid & Tartaric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "CHICKEN", "quantity": "1 -1 ½ kg", "notes": "1 skinless chicken weighing, make 4-5 deep slits on breast & thighs"},
        {"item": "GARLIC PASTE", "quantity": "1-2 tablespoons"},
        {"item": "GINGER PASTE", "quantity": "1-2 tablespoons"},
        {"item": "LEMON JUICE", "quantity": "8 tablespoons"},
        {"item": "COOKING OIL", "quantity": "5 cups/1 liter", "notes": "For deep frying"},
        {"item": "SHAN LAHORI CHARGA MIX", "quantity": "1 packet"}
    ],
    "description": "Mix garlic, ginger, lemon juice, and Shan Lahori Charga Mix. Apply it evenly over the chicken. Leave it aside to marinate overnight or for 3-4 hours. Steam the chicken in a steamer until tender. To STEAM without a steamer: Place a steel plate upside down in a deep Pour one cup of water. Put the chicken on the plate. Cover and cook on low heat for 20-30 minutes or until the chicken is fully tender. Heat oil in a deep wok and fry chicken until crisp golden from all sides. Remove and serve hot. Serving Suggestion: Sprinkle Shan Chaat Masala and squeeze a lemon over the Charga. Serve with chutney/tomato ketchup."
}

insert_recipe(recipe24_info)


recipe25_info = {
    "name": "DAAL MASALA",
    "total_ingredients": [
        "Salt",
        "Red Chili",
        "Turmeric",
        "Black Pepper",
        "Cumin",
        "Coriander",
        "Brown Cardamom",
        "Green Cardamom",
        "Garlic",
        "Ginger",
        "Dehydrated Dill Leaves",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "DAAL MUNG (SPLIT MUNG)", "quantity": "¾ cup / 175g", "notes": "Washed & soaked"},
        {"item": "DAAL MASOOR (SPLIT ORANGE PEA)", "quantity": "3 tablespoons", "notes": "Washed & soaked"},
        {"item": "ONION", "quantity": "1 large / 125g", "notes": "Sliced"},
        {"item": "GARLIC PASTE", "quantity": "10 cloves", "notes": "Coarsely chopped"},
        {"item": "TOMATO", "quantity": "1 small / 50g", "notes": "Diced"},
        {"item": "GREEN CHILIES", "quantity": "6-8 small /medium", "notes": "Whole"},
        {"item": "SOYA LEAVES", "quantity": "1 teaspoon", "notes": "Finely chopped"},
        {"item": "CURRY LEAVES", "quantity": "10 leaves"},
        {"item": "OIL / GHEE", "quantity": "¼ – ½ cup"},
        {"item": "SHAN DAAL MASALA MIX", "quantity": "1 ½ – 2 tablespoons"}
    ],
    "description": "Heat half oil and stir fry the onions for a few minutes. Add Shan Daal Masala Mix and garlic. Add lentils, tomato, soya leaves, green chilies, and 6 cups of water. Boil on low heat until the daal is tender and smooth (about 30 minutes). Heat the remaining ghee / oil and stir fry the curry leaves for a few seconds and pour over the cooked lentil curry. Cover and cook on low heat for 15-20 minutes. Serve with naan/roti/rice and onion rings."
}

insert_recipe(recipe25_info)

recipe26_info = {
    "name": "PAV BHAJI",
    "total_ingredients": [
        "Salt",
        "Red Chili",
        "Coriander",
        "Cumin",
        "Black Pepper",
        "Green Cardamom",
        "Dried Mango Powder",
        "Clove",
        "Fenugreek Seed",
        "Aniseed",
        "Acid: Citric Acid",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Sugar",
        "Canola Oil",
        "Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "POTATOES", "quantity": "4 medium/300g", "notes": "Peeled and cubed"},
        {"item": "GREEN PEAS", "quantity": "¾ cup (100g)"},
        {"item": "TOMATOES", "quantity": "2 medium / 100g", "notes": "¾ cup, chopped"},
        {"item": "ONION", "quantity": "1 large/100g", "notes": "¾ cup, finely chopped"},
        {"item": "CAULIFLOWER", "quantity": "1 cup / 100g", "notes": "Broken into flowerlets"},
        {"item": "CAPSICUM", "quantity": "½ cup (50g)"},
        {"item": "GARLIC", "quantity": "6-8 cloves"},
        {"item": "OIL / BUTTER", "quantity": "Butter (200g)"},
        {"item": "SHAN PAV BHAJI MIX", "quantity": "3 leveled tablespoons (30g)"}
    ],
    "description": "Boil potatoes, cauliflower, green peas, and garlic cloves in water until tender. Then coarsely mash and keep aside. On low heat melt butter and add onions. Fry until transparent. Add tomatoes and capsicum. Fry till the tomatoes are tender and done. Then add Shan Pav Bhaji Mix and fry for a few minutes or until butter / ghee begins to separate from the vegetables."
}

insert_recipe(recipe26_info)


recipe27_info = {
    "name": "VEGETABLE MASALA",
    "total_ingredients": [
        "Salt",
        "Red Chili",
        "Turmeric",
        "Fenugreek Seed",
        "Garlic",
        "Ginger",
        "Cumin",
        "Coriander",
        "Cinnamon",
        "Black Pepper",
        "Acid: Citric Acid",
        "Fenugreek Leaves",
        "Carom",
        "Clove",
        "Maltodextrin",
        "Hydrolyzed Soy Protein",
        "Cane Sugar",
        "Canola Oil",
        "Anticaking Agent: Silicon Dioxide"
    ],
    "ingredients_required": [
        {"item": "SINGLE / MIXED VEGETABLES", "quantity": "500g", "notes": "Washed & prepared accordingly"},
        {"item": "ONIONS", "quantity": "2 medium / 200g", "notes": "Finely sliced"},
        {"item": "TOMATOES", "quantity": "2-3 medium / 200g", "notes": "Finely chopped"},
        {"item": "COOKING OIL", "quantity": "½ cup / 85ml"},
        {"item": "SHAN VEGETABLE MASALA MIX", "quantity": "2-3 tablespoons"}
    ],
    "description": "In hot oil, fry the onions for a few minutes. Add tomatoes and fry for a few minutes. Add vegetables, Shan Vegetable Masala Mix, and fry for a few minutes. Stir and add the desired quantity of water if necessary. Cook on low heat until vegetables are tender."
}

insert_recipe(recipe27_info)





    # Visualize all recipes
    # visualize_data()
