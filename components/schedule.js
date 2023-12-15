import React, { useState } from "react";
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
} from "react-native";
import DateTimePickerModal from "react-native-modal-datetime-picker";

export default function Schedule() {
  const [mealName, setMealName] = useState("");
  const [schedule, setSchedule] = useState([]);
  const [isDatePickerVisible, setDatePickerVisibility] = useState(false);
  const [selectedDate, setSelectedDate] = useState(null);

  const showDatePicker = () => {
    setDatePickerVisibility(true);
  };

  const hideDatePicker = () => {
    setDatePickerVisibility(false);
  };

  const handleConfirm = (date) => {
    hideDatePicker();
    setSelectedDate(date);
  };

  const addMeal = () => {
    if (mealName && selectedDate) {
      const newSchedule = [...schedule, { name: mealName, time: selectedDate }];
      setSchedule(newSchedule);
      setMealName("");
      setSelectedDate(null);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Schedule Your Meals</Text>

      <TextInput
        style={styles.input}
        placeholder="Enter Meal Name"
        value={mealName}
        onChangeText={(text) => setMealName(text)}
      />

      <TouchableOpacity style={styles.button} onPress={showDatePicker}>
        <Text style={styles.buttonText}>
          {selectedDate ? selectedDate.toLocaleTimeString() : "Select Time"}
        </Text>
      </TouchableOpacity>

      <TouchableOpacity style={styles.button} onPress={addMeal}>
        <Text style={styles.buttonText}>Add Meal</Text>
      </TouchableOpacity>

      <DateTimePickerModal
        isVisible={isDatePickerVisible}
        mode="time"
        onConfirm={handleConfirm}
        onCancel={hideDatePicker}
      />

      {schedule.length > 0 && (
        <View style={styles.scheduleContainer}>
          <Text style={styles.scheduleHeading}>Your Schedule:</Text>
          {schedule.map((item, index) => (
            <Text key={index} style={styles.scheduleItem}>
              {item.name} at {item.time.toLocaleTimeString()}
            </Text>
          ))}
        </View>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 16,
    justifyContent: "center",
    alignItems: "center",
  },
  heading: {
    fontSize: 24,
    fontWeight: "bold",
    marginBottom: 16,
  },
  input: {
    height: 40,
    borderColor: "gray",
    borderWidth: 1,
    marginBottom: 16,
    padding: 8,
    width: "100%",
  },
  button: {
    backgroundColor: "blue",
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    marginTop: 16,
  },
  buttonText: {
    color: "white",
    fontSize: 16,
    textAlign: "center",
  },
  scheduleContainer: {
    marginTop: 20,
  },
  scheduleHeading: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 10,
  },
  scheduleItem: {
    fontSize: 16,
    marginBottom: 5,
  },
});
