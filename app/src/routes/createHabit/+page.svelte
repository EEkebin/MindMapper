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
    // Get habits from database http://localhost:5000/api/get_habits/username/password
    habits = await getHabits(username, password);
  });

  async function handleSubmit(event) {
    event.preventDefault();
    const response = await fetch(
      `http://localhost:5000/api/create_habit/${username}/${password}/${habit_name}/${metric_name}/${metric_value}/${goal_value}`,
      {
        method: "POST",
      }
    );
    if (response.ok) {
      alert("Habit Added Successfully");
      habit_name = "";
      metric_name = "";
      metric_value = "";
      goal_value = "";
      habits = await getHabits(username, password);
    }
  }

  async function getHabits(username, password) {
    const response = await fetch(
      "http://localhost:5000/api/get_user_habits/" + username + "/" + password,
      {
        method: "GET",
      }
    );
    const data = await response.json();
    const habits = [];
    for (let i = 0; i < data.length; i++) {
      const habit = data[i];
      habits.push([habit[2], habit[3], habit[4], habit[5]]);
    }
    return habits;
  }
</script>

<head>
  <title>Create Habit</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
</head>

<body>
  <div class="form-wrapper">
    <h1>Create Habit</h1>
    <form on:submit={handleSubmit}>
      <label for="habit-name">Habit Name:</label>
      <input type="text" id="habit-name" name="habit_name" required bind:value={habit_name} />
      <label for="metric-name">Metric Name:</label>
      <input type="text" id="metric-name" name="metric_name" required bind:value={metric_name} />
      <label for="metric-value">Metric Value:</label>
      <input type="number" id="metric-value" name="metric_value" step="1" required bind:value={metric_value} />
      <label for="goal-value">Goal Value:</label>
      <input type="number" id="goal-value" name="goal_value" step="1" required bind:value={goal_value} />
      <button type="submit">Create</button>
    </form>
    <table>
      <thead>
        <tr>
          <th>Habit Name</th>
          <th>Metric Name</th>
          <th>Metric Value</th>
          <th>Goal Value</th>
        </tr>
      </thead>
      <tbody>
        {#each habits as habit}
        <tr>
          {#each habit as value}
          <td>{value}</td>
          {/each}
        </tr>
        {/each}
      </tbody>
    </table>
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

button[type="submit"]:hover {
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
