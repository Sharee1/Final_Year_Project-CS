import React from "react";
import { View, Text, TextInput, Button, TouchableOpacity } from "react-native";

const Login = ({ navigation }) => {
  return (
    <View style={styles.container}>
      <Text style={styles.Welcometext}>Welcome ! </Text>
      <Text style={styles.Signtext}>Sign into Continue</Text>
      <Text style={styles.usernamehead}>Username</Text>
      <TextInput style={styles.inputuser} placeholder="Enter Your Name">
        {" "}
      </TextInput>
      <Text style={styles.Passwordhead}>Password</Text>
      <TextInput style={styles.inputpassword} placeholder="Enter Your Password">
        {" "}
      </TextInput>
      {/* <Text style={styles.Forgot}>Forgot Password ? </Text> */}
      <View style={styles.buttonContainer}>
        <Button
          title="Login"
          color="#f5d90a"
          onPress={() => navigation.navigate("default")}
        />
      </View>
      <TouchableOpacity
        onPress={() => navigation.navigate("signup")}
        style={styles.SignUp}
      >
        <Text>Sign up </Text>
      </TouchableOpacity>
    </View>
  );
};

const styles = {
  // container: {
  //     flex: 1,
  //     backgroundColor: '#f0f0f0',
  //     padding: 20,
  //   },

  Welcometext: {
    color: "black",
    fontSize: 40,
    alignSelf: "flex-start",
    paddingLeft: 20,
    paddingTop: 80,
    fontWeight: "bold",
  },
  Signtext: {
    color: "black",
    fontSize: 30,
    alignSelf: "flex-start",
    paddingLeft: 20,
    paddingTop: 0,
    fontWeight: "bold",
  },
  usernamehead: {
    color: "grey",
    fontSize: 20,
    paddingTop: 50,
    paddingLeft: 20,
    fontWeight: "bold",
  },
  inputuser: {
    marginLeft: 20,
    paddingLeft: 10,
    borderWidth: 1.4,
    borderRadius: 4,
    height: 40,
    width: 350,
    marginTop: 5,
  },
  Passwordhead: {
    color: "grey",
    fontSize: 20,
    paddingTop: 20,
    paddingLeft: 20,
    fontWeight: "bold",
  },
  inputpassword: {
    marginLeft: 20,
    paddingLeft: 10,
    borderWidth: 1.4,
    borderRadius: 4,
    height: 40,
    width: 350,
    marginTop: 5,
  },
  Forgot: {
    color: "black",
    fontWeight: "bold",
    marginLeft: 250,
    paddingTop: 10,
  },
  buttonback: {
    alignSelf: "center",
    backgroundColor: "yellow",
    height: 50,
    width: 150,
    borderRadius: 45,
    borderRadius: 10,
    marginTop: 90,
  },
  Login: {
    color: "black",
    marginTop: -45,
    marginLeft: "200",
    fontWeight: "bold",
    fontSize: 30,
  },
  buttonContainer: {
    width: 370,
    height: 50,
    alignSelf: "center",
    marginTop: 40,
    fontWeight: "bold",
    fontSize: 40,
  },
  SignUp: {
    color: "black",
    fontWeight: "bold",
    marginLeft: 310,
    paddingTop: -5,
    fontSize: 20,
  },
};

export default Login;
