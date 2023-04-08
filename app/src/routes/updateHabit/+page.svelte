<script>
    // Get habits from database and store in array
    import { onMount } from "svelte";
  
    let username = "";
    let password = "";
    let habit_name = "";
    let metric_name = "";
    let metric_value = "";
    let goal_value = "";
    let habits = [];
  
    // On mount, get habits from database
    onMount(async () => {
      // Get username from localstorage
      username = localStorage.getItem("username");
      password = localStorage.getItem("password");
      habit_name = localStorage.getItem("habit");
      console.log(habit_name)
      // Get habits from database http://localhost:5000/api/get_habits/username/password
      habits = await getHabit(username, password, habit_name);
      metric_name = habits[1];
      goal_value = habits[3];
    });

    //create function to update get habit /api/get_habit/<username>/<password>/<habit_name>',
    
  
    async function getHabit(username, password, habit_name) {
      const response = await fetch(
        "http://localhost:5000/api/get_habit/" + username + "/" + password + "/" + habit_name,
        {
          method: "GET",
        }
      );
      const data = await response.json();
      const habit = data[0];
      const metric_value = habit[4];
      const goal_value = habit[5];
      return [metric_value, habit[3], goal_value];
    }

    //update habit '/api/update_habit/<username>/<password>/<habit_name>/<metric_name>/<metric_value>'
    async function update_habit(metric_value) {
      const response = await fetch(
        `http://localhost:5000/api/update_habit/${username}/${password}/${habit_name}/${metric_name}/${metric_value}/${goal_value}`,
        {
          method: "PUT",
        }
      );
      if (response.ok) {
        alert("Habit Updated Successfully");
        metric_value = "";
        habits = await getHabit(username, password, habit_name);
      }
    }
  </script>
  
  <head>
    <title>Create Habit</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
  </head>
  
  <body>
    <div class="form-wrapper">
      <h1>Update Habit</h1>
      <form on:submit|preventDefault={getHabit}>
        <label for="habit-list">{habit_name}</label>
        <label for="metric-value">Metric Value</label>
        <input type="text" id="metric-value" name="metric-value" bind:value={metric_value} />
        <button type="submit" on:click={update_habit}>Update Habit</button>
      </form>
      <button on:click={() => window.location.href = "/landingPage"}>Return to Main Menu</button>
    </div>
  </body>

  <style>
  /* Set default styling for all elements */
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }
  
  /* Set body background and font */
  body {
    background-color: #f2f2f2;
    font-family: Arial, sans-serif;
  }
  
  /* Center and style the form wrapper */
  .form-wrapper {
    width: 90%;
    margin: 0 auto;
    margin-top: 50px;
    text-align: center;
  }
  
  /* Style the form elements */
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
  }
  
  label {
    margin-top: 20px;
    text-align: left;
    display: block;
  }
  
  input {
    padding: 10px;
    border-radius: 5px;
    border: 1px solid #ccc;
    margin-top: 5px;
    width: 100%;
    max-width: 300px;
  }
  
  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
    margin-top: 20px;
    width: 100%;
    max-width: 300px;
  }
  
  button:hover {
    background-color: #0069d9;
  }
  
  /* Style the table */
  table {
    margin-top: 30px;
    width: 100%;
    border-collapse: collapse;
  }
  
  th {
    text-align: left;
    font-weight: bold;
    padding: 10px;
    border-bottom: 2px solid #ddd;
  }
  
  td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
  }
  
  </style>
  